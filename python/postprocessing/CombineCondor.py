import os
from ML.MLmodels import *
import optparse
from samples.samplesUL import *
import copy
from datetime import datetime

#os.system("reset")

usage = 'python3 CombineCondor.py -d dataset_name -f destination_folder -y year'
parser = optparse.OptionParser(usage)
parser.add_option('--folder', dest='folder', type='string', default = 'vUL025', help = 'Analysis folder')
parser.add_option('--user', dest='user', type='string', default = 'apiccine', help = 'Username')
parser.add_option('--notImpacts', dest='impacts', default = True, action='store_false', help = 'Default does impacts')
parser.add_option('--notUncBreak', dest='uncbreak', default = True, action='store_false', help = 'Default does unc. breaking')
parser.add_option('--plot', dest='plotvar', type='string', default = 'fitvar', help = 'Specify variables to plot in postfit')
parser.add_option('--year', dest='year', type='string', default = 'RunII', help = 'Specify year, default is RunII')
parser.add_option('--cut', dest='cut', type='string', default = 'not', help = 'Specify cut, if needed')
parser.add_option('--sm', dest='sm', default = False, action='store_true', help = 'Default does not run SM significance')
parser.add_option('--noFit', dest='dofit', default = True, action='store_false', help = 'Default does not run SM significance')
parser.add_option('--doPost', dest='postfit', default = False, action='store_true', help = 'Default does not run postfit plots')
parser.add_option('-m', '--models', dest='models', type=str, default = 'vbs', help='Please enter a dataset name')
parser.add_option('--Lambda8', dest='Lambda8', default = False, action='store_true', help='add dim8 quad in 2D fits')
parser.add_option('--srvar', dest='srvar', type=str, default = 'm_o1', help='var in sr')
parser.add_option('--crvar', dest='crvar', type=str, default = 'same', help='var in cr')
parser.add_option('--notCI', dest='doCI', default = True, action='store_false', help = 'Default does not run postfit plots')
parser.add_option('--tDMcut', dest='tDMcut', default = False, action='store_true', help='Enable tau DecayMode cut')
parser.add_option('--test', dest='test', default = False, action='store_true', help='Enable test')
parser.add_option('--vbroad', dest='vbroad', default = False, action='store_true', help='Enable vbroad')
parser.add_option('--vvbroad', dest='vvbroad', default = False, action='store_true', help='Enable vvery broad')
parser.add_option('--vvvbroad', dest='vvvbroad', default = False, action='store_true', help='Enable vvvery broad')
parser.add_option('--noflat', dest='flat', default = True, action='store_false', help='Disable flattening bin')
parser.add_option('-u', '--unblind', dest = 'unblind', default = False, action = 'store_true', help = 'unblinding SR, default not')
parser.add_option('--PDFWithTTDY', dest='pdfttdy', default = False, action='store_true', help = 'apply pdf to ttbar and dy')
parser.add_option('--DYrp', dest='DYrp', default = False, action='store_true', help = 'apply rateParam to dy')
parser.add_option('--pdf', dest='pdf', type='string', default = 'total', help = 'Specify type of pdf')
parser.add_option('--flnN', dest='flnN', default = False, action='store_true', help = 'apply lognormal to fakes')
parser.add_option('--frp', dest='frp', default = False, action='store_true', help = 'apply rateParam to fakes')
parser.add_option('--profile', dest='profile', default = False, action='store_true', help = 'apply profiling to 2D fits eft')
parser.add_option('--regions', dest='regions', type='string', default = 'SR,CRTT,CROS,CRF', help = 'Regions to fit')
parser.add_option('--leptons', dest='leptons', type='string', default = 'muon,electron', help = 'Channels to include')
parser.add_option('--HN', dest='HN', default = False, action='store_true', help = 'fit with HybridNew instead of AsymptoticLimits')

(opt, args) = parser.parse_args()

models = opt.models.split(",")
srvars = opt.srvar.split(":")
regions = opt.regions.split(":")
leptons = opt.leptons.split(":")

if opt.crvar == "same":
    crvars = copy.deepcopy(srvars)
else:
    crvars = opt.crvar.split(":")

plotvars = []
if opt.postfit:
    if opt.plotvar == "fitvar":
        plotvars = copy.deepcopy(srvars)
    else:
        plotvars = opt.plotvar.split(":")
        if len(plotvars) != len(srvars):
            raise ValueError("number of plotvars has to be equal to number of srvars")

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

now = datetime.now().time().strftime("%H%M%S%f")

subfold = "combinecondor_" + opt.pdf
condorsub = "condorcombine_" + opt.pdf
exe = "branchcombine_" + opt.pdf

if opt.unblind:
    condorsub += "_DF"
    subfold += "_DF"
    exe += "_DF"
else:
    condorsub += "_TF"
    subfold += "_TF"
    exe += "_TF"

#condorsub += opt.regions.replace(",", "-") + "_" + opt.leptons.replace(",", "-")
#subfold += opt.regions.replace(",", "-") + "_" + opt.leptons.replace(",", "-")
#exe += opt.regions.replace(",", "-") + "_" + opt.leptons.replace(",", "-")

if opt.DYrp:
    condorsub += "_OSrp"
    subfold += "_OSrp"
    exe += "_OSyrp"
if opt.flnN:
    condorsub += "_flnN"
    subfold += "_flnN"
    exe += "_flnN"
if opt.frp:
    condorsub += "_frp"
    subfold += "_frp"
    exe += "_frp"
if opt.pdfttdy:
    condorsub += "_PDFwithTTDY"
    subfold += "_PDFwithTTDY"    
    exe += "_PDFwithTTDY"    
if opt.Lambda8:
    condorsub += "_Lambda8"
    subfold += "_Lambda8"
    exe += "_Lambda8"
if opt.tDMcut:
    condorsub += "_tDM"
    subfold += "_tDM"
    exe += "_tDM"
elif opt.test:
    condorsub += "_test"
    subfold += "_test"
    exe += "_test"
elif opt.vbroad:
    condorsub += "_vbroad"
    subfold += "_vbroad"
    exe += "_vbroad"
elif opt.vvbroad:
    condorsub += "_vvbroad"
    subfold += "_vvbroad"
    exe += "_vvbroad"
elif opt.vvvbroad:
    condorsub += "_vvvbroad"
    subfold += "_vvvbroad"
    exe += "_vvvbroad"
if not opt.flat:
    condorsub += "_noflat"
    subfold += "_noflat"
    exe += "_noflat"
#if opt.flat:
    #condorsub += "_flat"
    #subfold += "_flat"
    #exe += "_flat"
if opt.profile:
    condorsub += "_profile"
    subfold += "_profile"
    exe += "_profile"
if opt.HN:
    condorsub += "_HN"
    subfold += "_HN"
    exe += "_HN"

condorsub += "_"
subfold += "_" + opt.folder
    
if not os.path.exists(subfold):
    os.system("mkdir " + subfold)

outcore = condorsub + opt.folder + "/output/"
errcore = condorsub + opt.folder + "/error/"
logcore = condorsub + opt.folder + "/log/"

if not os.path.exists(outcore):
    os.system("mkdir -p " + outcore)
if not os.path.exists(errcore):
    os.system("mkdir -p " + errcore)
if not os.path.exists(logcore):
    os.system("mkdir -p " + logcore)

def submitter(model, srvar, crvar, argsins, folder, lepton, region):
    exesh = subfold + "/" + exe + "_" + folder + "_" + model + "_" + srvar + "_" + crvar + "_" + lepton.replace(",", "-") + "_" + region.replace(",", "-") + ".sh"
    fsh = open(exesh, "w")
    fsh.write("#!/bin/bash\n")
    fsh.write("cd /afs/cern.ch/user/a/apiccine\n")
    fsh.write("source setenv_combine.sh\n")
    fsh.write("cd Stat/Limits/test\n")
    for argsin in argsins:
        fsh.write("python " + pymacro + " " + argsin + "\n")
    fsh.close()
    
    condorsubb = condorsub + folder + "_" + model + "_" + srvar + "_" + crvar + "_" + lepton.replace(",", "-") + "_" + region.replace(",", "-") + ".sub"
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
    if (model.startswith("c") and ":" in model):
        f.write("+JobFlavour             = \"nextweek\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week
    else:    
        f.write("+JobFlavour             = \"testmatch\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week
    f.write("executable              = " + exesh + "\n")
    f.write("arguments               = \'\'\n") # + argsin + "\n")
    if (model.startswith("c") and ":" in model) or model == "EWvsQCD":
        f.write("request_cpus            = 10\n")
    elif model.startswith("c") or model.startswith("F"):
        f.write("request_cpus            = 6\n")
    else:
        f.write("request_cpus            = 4\n")
    output = outcore + folder + "_" + model + "_" + srvar + "_" + crvar + "_" + lepton.replace(",", "-") + "_" + region.replace(",", "-") + ".out"
    log = logcore + folder + "_" + model + "_" + srvar + "_" + crvar + "_" + lepton.replace(",", "-") + "_" + region.replace(",", "-") + ".log"
    error = errcore + folder + "_" + model + "_" + srvar + "_" + crvar + "_" + lepton.replace(",", "-") + "_" + region.replace(",", "-") + ".err"
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
        
    #os.system("condor_submit " + condorsubb)
    os.system("mv " + condorsubb + " " + subfold)

folder = opt.folder
pymacro = "FitAndPlot"
pymacro += ".py"

arg0 = " --folder " + folder 
arg0 += " --year " + opt.year

if opt.unblind:
    arg0 += " -u"
if not opt.impacts:
    arg0 += " --notImpacts"
if not opt.uncbreak:
    arg0 += " --notUncBreak"
if not opt.dofit:
    arg0 += " --noFit"

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
        if opt.Lambda8:
            arg1 += " --Lambda8"
        if opt.profile:
            arg1 += " --profile"
    if opt.HN:
        arg1 += " --HN"    
    for idsr, srvar in enumerate(srvars):
        arg2 = ""
        arg2 = arg0 + arg1 + " --fit " + srvar

        if not opt.crvar == "same":
            arg2 += " --cr " + crvars[idsr]
            crvar = crvars[idsr]
        else:
            crvar = srvar

        if opt.postfit:
            arg2 += " --doPost --plot " + plotvars[idsr]

        if opt.tDMcut:
            arg2 += " --tDMcut"
        elif opt.test:
            arg2 += " --test"
        elif opt.vbroad:
            arg2 += " --vbroad"
        elif opt.vvbroad:
            arg2 += " --vvbroad"
        elif opt.vvvbroad:
            arg2 += " --vvvbroad"
        if not opt.flat:
            arg2 += " --noflat"
        #if opt.flat:
            #arg2 += " --flat"

        if opt.pdfttdy:
            arg2 += " --PDFWithTTDY"
        if opt.DYrp:
            arg2 += " --DYrp"
        if opt.flnN:
            arg2 += " --flnN"
        if opt.frp:
            arg2 += " --frp"

        arg2 += " --pdf " + opt.pdf
        
        for lepton in leptons:
            for region in regions:
                argss = []
                arg3 = arg2 + " --regions " + region + " --leptons " + lepton
                arg3 += " > /dev/null "

                argss.append(arg3)
                submitter(model, srvar, crvar, argss, folder, lepton, region)
        
        
