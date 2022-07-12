import os
from ML.MLmodels import *
os.system("reset")

usage = 'python submit_condor.py -d dataset_name -f destination_folder --wp working_point'
parser = optparse.OptionParser(usage)
parser.add_option('-d', '--dat', dest='dataset', type=str, default = '', help='Please enter a dataset name')
parser.add_option('-v', '--veto', dest='veto', type=str, default = '', help='Please enter a dataset name to veto')
parser.add_option('-f', '--folder', dest='folder', type=str, default = '', help='Please enter a destination folder')
parser.add_option('-y', '--year', dest='years', type=str, default = '', help='Please enter year(s)')
(opt, args) = parser.parse_args()

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
if username == 'mmagheri':
    uid = 102889
elif username == 'apiccine':
    uid = 124949
elif username == 'ttedesch':
    uid = 103343

condorsub = "condorbranch"

def submitter(sample, argsin, folder):
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
    inputfiles = "transfer_input_files    = $(Proxy_path), ./samples, ./ML, PrepareToPlot.py, makeplot.py"
    f.write(inputfiles)
    f.write("+JobFlavour             = \"nextweek\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week                                           
    f.write("executable              = " + exe + "\n")
    f.write("arguments               = " + argsin + "\n")
    f.write("request_disk            = 50MB\n")
    f.write("output                  = condor_" + folder + "/output/"+ sample.label + ".out \n")
    f.write("error                   = condor_" + folder + "/error/"+ sample.label + ".err \n")
    f.write("log                     = condor_" + folder + "/log/"+ sample.label + ".log \n")
    f.write("queue\n")
    f.close()
    if os.path.exists("condor_" + folder + "/output/"+ sample.label + ".out"):
        os.system("rm condor_" + folder + "/output/"+ sample.label + ".out")
    if os.path.exists("condor_" + folder + "/error/"+ sample.label + ".err"):
        os.system("rm condor_" + folder + "/error/"+ sample.label + ".err")
    if os.path.exists("condor_" + folder + "/log/"+ sample.label + ".log"):
        os.system("rm condor_" + folder + "/log/"+ sample.label + ".log")

    os.system("condor_submit " + condorsubb)


years = opt.years.split(",")
toplot = opt.dataset.split(",")
toveto = opt.veto.split(",")

branches = [
    bdt_sm_branch_v2,
    bdt_cW_branch_v2,
    bdt_cHW_branch_v2,
    dnn_sm_branch_v2,
    dnn_cW_branch_v2,
    #bdt_pol_branch,
    #dnn_cHW_branch_bal,
    #dnn_pol_branch,
]

paths = [
    bdt_sm_path_v2,
    bdt_cW_path_v2,
    bdt_cHW_path_v2,
    dnn_sm_path_v2,
    dnn_cW_path_v2,
    #bdt_pol_path,
    #dnn_cHW_path_bal,
    #dnn_pol_path,
]

scalers = [
    bdt_sm_scaler_v2,
    bdt_cW_scaler_v2,
    bdt_cHW_scaler_v2,
    dnn_sm_scaler_v2,
    dnn_cW_scaler_v2,
    #bdt_pol_scaler,
    #dnn_cHW_scaler,
    #dnn_pol_scaler,
]

folder = opt.folder
exe = "add_1finalMVA_condor.py"

branchstr = "\""
pathstr = "\""
scalerstr = "\""

for idb, branch in enumerate(branches):
    if idb > 0:
        branchstr += ","
        pathstr += ","
        scalerstr += ","
    branchstr += branches[idb]
    pathstr += paths[idb]
    scalerstr += scalers[idb]

branchstr += "\""
pathstr += "\""
scalerstr += "\""

args = " -f " + folder + " --paths " + pathstr + " --branches " + branchstr + " --scalers " + scalerstr



 +  + " -d WZ_" + year + " --ov")

for year in years:
    args += " -y " + year 
    for dat in plot_list:
        
        if dat.year != year:
            continue

        if dal.label.startswith("Fake"):
            continue

        if len(toplot) > 0:
            for dtp in toplot:
                if dat.label != dtp:
                    continue
        
        if len(toveto) > 0:
            for dtp in toveto:
                if dat.label == dtp:
                    continue
        
        args += " -d " + sample.label

        submitter(dar, args, folder)
