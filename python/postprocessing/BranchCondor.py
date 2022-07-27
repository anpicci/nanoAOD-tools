import os
from ML.MLmodels import *
import optparse
from samples.samplesUL import *

os.system("reset")

usage = 'python3 BranchCondor.py -d dataset_name -f destination_folder -y year'
parser = optparse.OptionParser(usage)
parser.add_option('-d', '--dat', dest='dataset', type=str, default = 'all', help='Please enter a dataset name')
parser.add_option('-v', '--veto', dest='veto', type=str, default = 'none', help='Please enter a dataset name to veto')
parser.add_option('-f', '--folder', dest='folder', type=str, default = '', help='Please enter a destination folder')
parser.add_option('-y', '--year', dest='years', type=str, default = 'UL2018,UL2017,UL2016APV,UL2016', help='Please enter year(s)')
(opt, args) = parser.parse_args()

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
if username == 'mmagheri':
    uid = 102889
elif username == 'apiccine':
    uid = 124949
elif username == 'ttedesch':
    uid = 103343

subfold = "branchcondor"
if not os.path.exists(subfold):
    os.system("mkdir " + subfold)

condorsub = "condorbranch"

outcore = "condorbranch_" + opt.folder + "/output/"
errcore = "condorbranch_" + opt.folder + "/error/"
logcore = "condorbranch_" + opt.folder + "/log/"

if not os.path.exists(outcore):
    os.system("mkdir -p " + outcore)
if not os.path.exists(errcore):
    os.system("mkdir -p " + errcore)
if not os.path.exists(logcore):
    os.system("mkdir -p " + logcore)

def submitter(sample, argsin, folder):
    exesh = subfold + "/" + exe + "_" + sample.label + ".sh"
    fsh = open(exesh, "w")
    fsh.write("#!/bin/bash\n")
    fsh.write("source /afs/cern.ch/work/a/apiccine/benv/bin/activate\n")
    fsh.write("python3 " + pymacro + " " + argsin + "\n")
    fsh.close()
    condorsubb = condorsub + "_" + str(sample.year) + ".sub"
    f = open(condorsubb, "w")
    f.write("Proxy_filename          = x509up\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/private/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    tagyear = str(sample.year)
    inputfiles = "transfer_input_files    = $(Proxy_path), ./samples, ./ML, PrepareToPlot.py, makeplot.py, " + pymacro+ "\n"
    f.write(inputfiles)
    f.write("+JobFlavour             = \"nextweek\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week                                           
    f.write("executable              = " + exesh + "\n")
    f.write("arguments               = \'\'\n") # + argsin + "\n")
    f.write("request_cpus            = 6\n")
    output = outcore + sample.label + ".out"
    log = logcore + sample.label + ".log"
    error = errcore + sample.label + ".err"
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

    print(condorsubb)
    os.system("condor_submit " + condorsubb)
    os.system("mv " + condorsubb + " " + subfold)

years = opt.years.split(",")
toplot = opt.dataset.split(",")
toveto = opt.veto.split(",")

branches = [
    bdt_sm_branch_T_DYL,
    bdt_cW_branch_novar,
    bdt_cW_branch_T_DYL_novar,
    dnn_sm_branch_T_DYL,
    dnn_cW_branch_novar,
    dnn_cW_branch_T_DYL_novar,
    dnn_sm_branch_v2,
    dnn_cW_branch_v2,
    dnn_cHW_branch_v2,
    dnn_aQGC_branch_v2,
    bdt_sm_branch_v2,
    bdt_cW_branch_v2,
    bdt_cHW_branch_v2,
    bdt_aQGC_branch_v2,
]

paths = [
    bdt_sm_path_T_DYL,
    bdt_cW_path_novar,
    bdt_cW_path_T_DYL_novar,
    dnn_sm_path_T_DYL,
    dnn_cW_path_novar,
    dnn_cW_path_T_DYL_novar,
    dnn_sm_path_v2,
    dnn_cW_path_v2,
    dnn_cHW_path_v2,
    dnn_aQGC_path_v2,
    bdt_sm_path_v2,
    bdt_cW_path_v2,
    bdt_cHW_path_v2,
    bdt_aQGC_path_v2,
]

scalers = [
    bdt_sm_scaler_T_DYL,
    bdt_cW_scaler_novar,
    bdt_cW_scaler_T_DYL_novar,
    dnn_sm_scaler_T_DYL,
    dnn_cW_scaler_novar,
    dnn_cW_scaler_T_DYL_novar,
    dnn_sm_scaler_v2,
    dnn_cW_scaler_v2,
    dnn_cHW_scaler_v2,
    dnn_aQGC_scaler_v2,
    bdt_sm_scaler_v2,
    bdt_cW_scaler_v2,
    bdt_cHW_scaler_v2,
    bdt_aQGC_scaler_v2,
]

folder = opt.folder
pymacro = "add_1finalMVA_condor.py"
exe = "branchcondor"
branchstr = "\'"
pathstr = "\'"
scalerstr = "\'"

print(branches, paths, scalers)

for idb, branch in enumerate(branches):
    if idb > 0:
        branchstr += ","
        pathstr += ","
        scalerstr += ","
    branchstr += branches[idb]
    pathstr += paths[idb]
    scalerstr += scalers[idb]

branchstr += "\'"
pathstr += "\'"
scalerstr += "\'"

arg0 = " -f " + folder + " --paths " + pathstr + " --branches " + branchstr + " --scalers " + scalerstr

print("toplot", toplot)
print("toveto", toveto)
#print(years)
for year in years:
    arg1 = " -y " + year 
    for dat in condor_list:
        
        if dat.label.startswith("TT_") or dat.label.startswith("WJets") or dat.label.startswith("DataHT"):
            continue
        
        args = arg0 + arg1
        if dat.year != year:
            continue
        
        if dat.label.startswith("Fake"):
            continue

        
        toPlot = False
        toVeto = False

        if opt.dataset != "all":
            for dtp in toplot:
                if dat.label.startswith(dtp):
                    toPlot = True
                    break
            
            if not toPlot:
                continue
        
        if opt.veto != "none":
            for dtp in toveto:
                if dat.label.startswith(dtp):
                    toVeto = True
                    break
            if toVeto:
                continue

        args += " -d " + dat.label
        submitter(dat, args, folder)
