import os
from ML.MLmodels import *
import optparse
from samples.samplesUL import *
import copy

os.system("reset")

usage = 'python3 CombineCondor.py -d dataset_name -f destination_folder -y year'
parser = optparse.OptionParser(usage)
parser.add_option('--folder', dest='folder', type='string', default = 'vUL025', help = 'Analysis folder')
parser.add_option('--user', dest='user', type='string', default = 'apiccine', help = 'Username')
parser.add_option('--notImpacts', dest='impacts', default = True, action='store_false', help = 'Default does impacts')
parser.add_option('--notUncBreak', dest='uncbreak', default = True, action='store_false', help = 'Default does unc. breaking')
parser.add_option('--plot', dest='plotvar', type='string', default = 'all', help = 'Specify variables to plot in postfit')
parser.add_option('--year', dest='year', type='string', default = 'RunII', help = 'Specify year, default is RunII')
parser.add_option('--cut', dest='cut', type='string', default = 'not', help = 'Specify cut, if needed')
parser.add_option('--sm', dest='sm', default = False, action='store_true', help = 'Default does not run SM significance')
parser.add_option('--noFit', dest='dofit', default = True, action='store_false', help = 'Default does not run SM significance')
parser.add_option('--doPost', dest='postfit', default = False, action='store_true', help = 'Default does not run postfit plots')
parser.add_option('-m', '--models', dest='models', type=str, default = 'vbs', help='Please enter a dataset name')
parser.add_option('--srvar', dest='srvar', type=str, default = 'm_o1', help='var in sr')
parser.add_option('--crvar', dest='crvar', type=str, default = 'same', help='var in cr')
parser.add_option('--notCI', dest='doCI', default = True, action='store_false', help = 'Default does not run postfit plots')
parser.add_option('--tDMcut', dest='tDMcut', default = False, action='store_true', help='Enable tau DecayMode cut')
parser.add_option('--test', dest='test', default = False, action='store_true', help='Enable test')

(opt, args) = parser.parse_args()

models = opt.models.split(",")
srvars = opt.srvar.split(":")
if opt.crvar == "same":
    crvars = copy.deepcopy(srvars)
else:
    crvars = opt.crvar.split(":")

if len(srvars) != len(crvars):
    raise ValueError("number of srvars has to be equal to number of crvars")

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
if username == 'mmagheri':
    uid = 102889
elif username == 'apiccine':
    uid = 124949
elif username == 'ttedesch':
    uid = 103343

subfold = "combinecondor"
if not os.path.exists(subfold):
    os.system("mkdir " + subfold)

condorsub = "condorcombine"

outcore = "condorcombine_" + opt.folder + "/output/"
errcore = "condorcombine_" + opt.folder + "/error/"
logcore = "condorcombine_" + opt.folder + "/log/"

if not os.path.exists(outcore):
    os.system("mkdir -p " + outcore)
if not os.path.exists(errcore):
    os.system("mkdir -p " + errcore)
if not os.path.exists(logcore):
    os.system("mkdir -p " + logcore)

def submitter(model, srvar, crvar, argsins, folder):
    exesh = subfold + "/" + exe + "_" + folder + "_" + model + "_" + srvar + "_" + crvar + ".sh"
    fsh = open(exesh, "w")
    fsh.write("#!/bin/bash\n")
    fsh.write("cd /afs/cern.ch/user/a/apiccine\n")
    fsh.write("source setenv_combine.sh\n")
    fsh.write("cd Stat/Limits/test\n")
    for argsin in argsins:
        fsh.write("python " + pymacro + " " + argsin + "\n")
    fsh.close()
    
    condorsubb = condorsub + "_" + folder + "_" + model + "_" + srvar + "_" + crvar + ".sub"
    f = open(condorsubb, "w")
    f.write("Proxy_filename          = x509up\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/private/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    inputfiles = "transfer_input_files    = $(Proxy_path)\n"
    f.write(inputfiles)
    f.write("+JobFlavour             = \"nextweek\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week                                           
    f.write("executable              = " + exesh + "\n")
    f.write("arguments               = \'\'\n") # + argsin + "\n")
    f.write("request_cpus            = 12\n")
    output = outcore + folder + "_" + model + "_" + srvar + "_" + crvar + ".out"
    log = logcore + folder + "_" + model + "_" + srvar + "_" + crvar + ".log"
    error = errcore + folder + "_" + model + "_" + srvar + "_" + crvar + ".err"
    f.write("output                  = " + output + "\n")
    f.write("error                   = " + error + "\n")
    f.write("log                     = " + log + "\n")
    f.write("queue\n")
    f.close()
    if os.path.exists(output):
        os.system("rm " + output)
    if os.path.exists(log):
        os.system("rm " + log)
    if os.path.exists(error):
        os.system("rm " + error)

    os.system("condor_submit " + condorsubb)
    os.system("mv " + condorsubb + " " + subfold)

folder = opt.folder
#pymacro = "FitAndPlot.py"
pymacro = "FitAndPlot_dev.py"
exe = "branchcombine"

arg0 = " --folder " + folder 
if not opt.impacts:
    arg0 += " --notImpacts"
if not opt.uncbreak:
    arg0 += " --notUncBreak"
if not opt.dofit:
    arg0 += " --noFit"


if opt.postfit:
    arg0 += " --doPost"
if opt.plotvar != "all":
    arg0 += " --plot " + opt.plotvar
arg0 += " --year " + opt.year

for model in models:
    arg1 = ""
    if model.startswith("vbs"):
        arg1 += " --sm --vbs"
        if model != "vbs":
            arg1 += " --pol " + model.replace("vbs", "")
    elif model.startswith("wpwp"):
        arg1 += " --sm --" + model
    elif model == "EWvsQCD":
        arg1 += " --" + model
    else:
        arg1 += " --eft " + model
        if not opt.doCI:
            arg1 += " --notCI"

    for idsr, srvar in enumerate(srvars):
        arg2 = ""
        argss = []
        arg2 = arg0 + arg1 + " --fit " + srvar

        if not opt.crvar == "same":
            arg2 += " --cr " + crvars[idsr]
            crvar = crvars[idsr]
        else:
            crvar = srvar

        if opt.tDMcut:
            arg2 += " --tDMcut"
        elif opt.test:
            arg2 += " --test"

        argss.append(arg2)
        submitter(model, srvar, crvar, argss, folder)
        
