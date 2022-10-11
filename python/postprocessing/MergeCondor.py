import os
from ML.MLmodels import *
import optparse
from samples.samplesUL import *

#os.system("reset")

usage = 'python3 PlotCondor.py -d dataset_name -f destination_folder -y year'
parser = optparse.OptionParser(usage)
parser.add_option('-d', '--dat', dest='dataset', type=str, default = 'all', help='Please enter a dataset name')
parser.add_option('--veto', dest='veto', type=str, default = 'none', help='Please enter a dataset name to veto')
parser.add_option('-f', '--folder', dest='folder', type=str, default = '', help='Please enter a destination folder')
parser.add_option('-y', '--year', dest='years', type=str, default = 'UL2016APV,UL2016,UL2017,UL2018', help='Please enter year(s)')
parser.add_option('--rw', dest='rw', default = False, action = 'store_true', help='Default does not rewrite')
parser.add_option('--or', dest='override', default = False, action = 'store_true', help='Default does not override AreAllCondored')

(opt, args) = parser.parse_args()

if opt.folder == '':
    raise ValueError("Specify a folder!")

def cutToTag(cut):
    newstring = cut.replace("-", "neg").replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("!=","_NEQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
    return newstring

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
if username == 'mmagheri':
    uid = 102889
elif username == 'apiccine':
    uid = 124949
elif username == 'ttedesch':
    uid = 103343

subfold = "mergecondor"
if not os.path.exists(subfold):
    os.system("mkdir " + subfold)

condorsub = "condormerge"

outcore = "condormerge_" + opt.folder + "/output/"
errcore = "condormerge_" + opt.folder + "/error/"
logcore = "condormerge_" + opt.folder + "/log/"

if not os.path.exists(outcore):
    os.system("mkdir -p " + outcore)
if not os.path.exists(errcore):
    os.system("mkdir -p " + errcore)
if not os.path.exists(logcore):
    os.system("mkdir -p " + logcore)

os.popen("cp /tmp/x509up_u" + str(uid) + " /afs/cern.ch/user/" + inituser + "/" + username + "/private/x509up")

def submitter(sample, argsins, folder):
    exesh = subfold + "/" + exe + "_" + sample.label + "_" + folder + ".sh"
    fsh = open(exesh, "w")
    fsh.write("#!/bin/bash\n")
    fsh.write("cd /afs/cern.ch/user/" + inituser + "/" + username + "\n")
    fsh.write("source setenv_VBS_113.sh\n")
    fsh.write("cd PhysicsTools/NanoAODTools/python/postprocessing/\n")
    for argsin in argsins:
        fsh.write("python3 " + pymacro + " " + argsin + "\n")
    fsh.close()
    
    condorsubb = condorsub + "_" + str(sample.year) + "_" + folder + ".sub"
    f = open(condorsubb, "w")
    f.write("Proxy_filename          = x509up\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/private/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    tagyear = str(sample.year)
    inputfiles = "transfer_input_files    = $(Proxy_path),\n" # ./rwgcards, ./samples, CMS_lumi.py, variabile.py, makeplot.py, " + pymacro+ "\n"
    f.write(inputfiles)
    f.write("+JobFlavour             = \"nextweek\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week                                           
    f.write("executable              = " + exesh + "\n")
    f.write("arguments               = \'\'\n") # + argsin + "\n")
    f.write("request_cpus            = 8\n")
    
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

    os.system("condor_submit " + condorsubb)
    os.system("mv " + condorsubb + " " + subfold)

years = opt.years.split(",")
tomerge = opt.dataset.split(",")
toveto = opt.veto.split(",")

condorstatus = [l.replace("\n", "") for l in os.popen("condor_q").readlines() if "apiccine" in l and not "Total" in l]
for line in condorstatus:
    idjob = line.split(" 1 ")[-1]
    sample = ""
    try:
        sample = os.popen("condor_ssh_to_job " + idjob + " \"head snfile.txt\" ").readlines()[0]
    except:
        continue

    if sample != "" and (True in [sample.endswith(year) for year in years]):
        if not sample in toveto:
            toveto.append(sample)

folder = opt.folder
pymacro = "PrepareToPlot.py"
exe = "branchmerge"

arg0 = " -f " + folder

print("tomerge", tomerge)
print("toveto", toveto)

'''
for dat in merge_list:
    if dat.year == years[0]:
        print(dat.label)
'''

for year in years:
    arg1 = " -y " + year 
    for dat in merge_list:
        argss = []
        if dat.label.startswith("TT_") or dat.label.startswith("WJets_") or dat.label.startswith("DataHT"):
            continue

        if dat.year != year:
            continue

        toMerge = False
        toVeto = False
        
        if opt.dataset != "all":
            for dtp in tomerge:
                if dat.label.startswith(dtp):
                    toMerge = True
                    break
            
            if not toMerge:
                continue
        
        if opt.veto != "none":
            for dtp in toveto:
                if dat.label.startswith(dtp):
                    toVeto = True
                    break
            if toVeto:
                continue

        arg2 = arg0 + arg1 + " -d " + dat.label

        if opt.rw:
            arg2 += " --rw"
        if opt.override:
            arg2 += " --or"

        argss.append(arg2)

        submitter(dat, argss, folder)
