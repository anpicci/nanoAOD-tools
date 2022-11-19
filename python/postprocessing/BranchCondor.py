import os
from ML.MLmodels import *
import optparse
from samples.samplesUL import *

#os.system("reset")

usage = 'python3 BranchCondor.py -d dataset_name -f destination_folder -y year'
parser = optparse.OptionParser(usage)
parser.add_option('-d', '--dat', dest='dataset', type=str, default = 'all', help='Please enter a dataset name')
parser.add_option('-v', '--veto', dest='veto', type=str, default = 'none', help='Please enter a dataset name to veto')
parser.add_option('-f', '--folder', dest='folder', type=str, default = '', help='Please enter a destination folder')
parser.add_option('-y', '--year', dest='years', type=str, default = 'UL2018,UL2017,UL2016APV,UL2016', help='Please enter year(s)')
parser.add_option('--rw', dest='rw', default = False, action = 'store_true', help='Default does not rewrite')
parser.add_option('--or', dest='override', default = False, action = 'store_true', help='Default does not override AreAllCondored')

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

os.popen("cp /tmp/x509up_u" + str(uid) + " /afs/cern.ch/user/" + inituser + "/" + username + "/private/x509up")

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
    f.write("+JobFlavour             = \"tomorrow\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week                                           
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
    dnn_sm_branch_1_lower_iter1,
    dnn_sm_branch_1_lower_iter4,
    dnn_sm_branch_bis_lower_iter2,
    dnn_sm_branch_bis_lower_iter4,
    dnn_dim8_branch_final_3_noQUAD_fix,
    dnn_dim8_branch_final_3_1to2,
    dnn_dim8_branch_final_3_again,
    dnn_sm_branch_1_NOMOREDY_test,
    dnn_sm_branch_1_NOMOREDY_test_2000,
    dnn_sm_branch_1_NOMOREDY_test_2001,
    dnn_sm_branch_1_NOMOREDY_test_2002,
    dnn_sm_branch_1_NOMOREDY_test_2003,
    dnn_dim8_branch_3_NOMOREDY_test,
    dnn_dim6_branch_2_NOMOREDY_test,
]

paths = [
    dnn_sm_path_1_lower_iter1,
    dnn_sm_path_1_lower_iter4,
    dnn_sm_path_bis_lower_iter2,
    dnn_sm_path_bis_lower_iter4,
    dnn_dim8_path_final_3_noQUAD_fix,
    dnn_dim8_path_final_3_1to2,
    dnn_dim8_path_final_3_again,
    dnn_sm_path_1_NOMOREDY_test,
    dnn_sm_path_1_NOMOREDY_test_2000,
    dnn_sm_path_1_NOMOREDY_test_2001,
    dnn_sm_path_1_NOMOREDY_test_2002,
    dnn_sm_path_1_NOMOREDY_test_2003,
    dnn_dim8_path_3_NOMOREDY_test,
    dnn_dim6_path_2_NOMOREDY_test,
]

scalers = [
    dnn_sm_scaler_1_lower_iter1,
    dnn_sm_scaler_1_lower_iter4,
    dnn_sm_scaler_bis_lower_iter2,
    dnn_sm_scaler_bis_lower_iter4,
    dnn_dim8_scaler_final_3_noQUAD_fix,
    dnn_dim8_scaler_final_3_1to2,
    dnn_dim8_scaler_final_3_again,
    dnn_sm_scaler_1_NOMOREDY_test,
    dnn_sm_scaler_1_NOMOREDY_test_2000,
    dnn_sm_scaler_1_NOMOREDY_test_2001,
    dnn_sm_scaler_1_NOMOREDY_test_2002,
    dnn_sm_scaler_1_NOMOREDY_test_2003,
    dnn_dim8_scaler_3_NOMOREDY_test,
    dnn_dim6_scaler_2_NOMOREDY_test,
]

folder = opt.folder
pymacro = "add_1finalMVA_condor.py"
exe = "branchcondor"
branchstr = "\'"
pathstr = "\'"
scalerstr = "\'"

#print(branches, paths, scalers)

MissAny = False
for idb, branch in enumerate(branches):
    if idb > 0:
        branchstr += ","
        pathstr += ","
        scalerstr += ","
    #try:
    if not os.path.exists(paths[idb]):
    #except:
        MissAny = True
        print("Missing " + paths[idb] + " for " + branches[idb])
    if scalers[idb] != "":
        if not os.path.exists(scalers[idb]):
            MissAny = True
            print("Missing " + scalers[idb] + " for " + branches[idb])
    pathfeat = "ML/" + branch + "_features.txt"
    if not os.path.exists(pathfeat):
        MissAny = True
        print("Missing " + pathfeat + " for " + branches[idb])

    branchstr += branches[idb]
    pathstr += paths[idb]
    scalerstr += scalers[idb]

if MissAny:
    raise ValueError("Check previous messages about missing models!")

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
        #print(dat.label)
        if dat.label.startswith("TT_") or dat.label.startswith("WJets") or "_Jbin_" in dat.label or dat.label.startswith("DataHT"):
            #print("hello1")
            continue
        
        args = arg0 + arg1
        if dat.year != year:
            #print("hello2")
            continue
        
        if dat.label.startswith("Fake"):
            #print("hello3")
            continue
        
        toPlot = False
        toVeto = False

        if opt.dataset != "all":
            for dtp in toplot:
                if dat.label.startswith(dtp):# or (hasattr(dat, "components") and True in [c.label.startswith(dtp) for c in dat.components]):
                    toPlot = True
                    break
            
            if not toPlot:
                #print("hello4")
                continue
        
        if opt.veto != "none":
            for dtp in toveto:
                if dat.label.startswith(dtp):
                    toVeto = True
                    break
            if toVeto:
                continue

        args += " -d " + dat.label
        if opt.rw:
            args += " --rw"
        if opt.override:
            args += " --or"

        submitter(dat, args, folder)
