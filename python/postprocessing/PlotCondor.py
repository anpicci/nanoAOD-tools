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
parser.add_option('-c', '--cuts', dest='cut', type=str, default = 'not', help='Please enter a cut')
parser.add_option('-y', '--year', dest='years', type=str, default = 'UL2016M,UL2017,UL2018,ULRunII', help='Please enter year(s)')
#parser.add_option('-y', '--year', dest='years', type=str, default = 'UL2016M,UL2016APV,UL2016,UL2017,UL2018', help='Please enter year(s)')
parser.add_option('--var', dest='vars', type=str, default = 'all', help='Please enter variable(s)')
parser.add_option('--nosyst', dest='nosyst', default = False, action='store_true', help='no syst applied')
parser.add_option('--systs', dest='systs', type=str, default = 'all', help='Systs to plot')
parser.add_option('--count', dest='count', default = False, action='store_true', help='enable writing countings')
parser.add_option('--tDMcut', dest='tDMcut', default = False, action='store_true', help='Enable tau DecayMode cut')
parser.add_option('--test', dest='test', default = False, action='store_true', help='Enable test saving')
(opt, args) = parser.parse_args()

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

subfold = "plotcondor"
if not os.path.exists(subfold):
    os.system("mkdir " + subfold)

condorsub = "condorplot"

regions = [
    "sr",
    "ttbar",
    "fakes",
    "wsdy --bvetoL",
    #"presel",
]

tagf = ""
if opt.tDMcut:
    tagf += "_tdmcut"
elif opt.test:
    tagf += "_test"

outcore = "condorplot_" + opt.folder + tagf + "/output/"
errcore = "condorplot_" + opt.folder + tagf + "/error/"
logcore = "condorplot_" + opt.folder + tagf + "/log/"

if not os.path.exists(outcore):
    os.system("mkdir -p " + outcore)
if not os.path.exists(errcore):
    os.system("mkdir -p " + errcore)
if not os.path.exists(logcore):
    os.system("mkdir -p " + logcore)

os.popen("cp /tmp/x509up_u" + str(uid) + " /afs/cern.ch/user/" + inituser + "/" + username + "/private/x509up")

def submitter(sample, argsins, folder, cut):
    cuttag = ""
    if cut != "not":
        cuttag = "_" + cutToTag(cut)
    exesh = subfold + "/" + exe + "_" + sample.label + "_" + folder + cuttag + ".sh"
    fsh = open(exesh, "w")
    fsh.write("#!/bin/bash\n")
    for argsin in argsins:
        fsh.write("python3 " + pymacro + " " + argsin + "\n")
    fsh.close()
    
    condorsubb = condorsub + "_" + str(sample.year) + "_" + folder + cuttag + ".sub"
    f = open(condorsubb, "w")
    f.write("Proxy_filename          = x509up\n")
    f.write("Proxy_path              = /afs/cern.ch/user/" + inituser + "/" + username + "/private/$(Proxy_filename)\n")
    f.write("universe                = vanilla\n")
    f.write("x509userproxy           = $(Proxy_path)\n")
    f.write("use_x509userproxy       = true\n")
    f.write("should_transfer_files   = YES\n")
    f.write("when_to_transfer_output = ON_EXIT\n")
    tagyear = str(sample.year)
    inputfiles = "transfer_input_files    = $(Proxy_path), ./rwgcards, ./samples, CMS_lumi.py, variabile.py, " + pymacro+ "\n"
    f.write(inputfiles)
    f.write("+JobFlavour             = \"nextweek\"\n") # options are espresso = 20 minutes, microcentury = 1 hour, longlunch = 2 hours, workday = 8 hours, tomorrow = 1 day, testmatch = 3 days, nextweek     = 1 week                                           
    f.write("executable              = " + exesh + "\n")
    f.write("arguments               = \'\'\n") # + argsin + "\n")
    f.write("request_cpus            = 8\n")
    #f.write("+AccountingGroup        = \"group_u_BE.ABP.SLAP\"\n")
    output = outcore + sample.label + cuttag + ".out"
    log = logcore + sample.label + cuttag + ".log"
    error = errcore + sample.label + cuttag + ".err"
    f.write("output                  = " + output + "\n")
    f.write("error                   = " + error + "\n")
    f.write("log                     = " + log + "\n")
    f.write("queue\n")
    f.close()
    #if os.path.exists(output):     
    os.system("rm " + output)
    #if os.path.exists(log):
    os.system("rm " + log)
    #if os.path.exists(error):
    os.system("rm " + error)

    os.system("condor_submit " + condorsubb)
    os.system("mv " + condorsubb + " " + subfold)

years = opt.years.split(",")
toplot = opt.dataset.split(",")
toveto = opt.veto.split(",")
variables = []
if opt.vars != "all":
    variables = opt.vars.split(",")

cuts = []
if opt.cut != "not":
    cuts = opt.cut.split(",")

folder = opt.folder
pymacro = "makeplot.py"
exe = "branchplot" + tagf

arg0 = " -p -f " + folder

print("toplot", toplot)
print("toveto", toveto)

for year in years:
    arg1 = " -y " + year 
    for dat in plot_list:
        argss = []
        if dat.label.startswith("TT_") or dat.label.startswith("WJets") or dat.label.startswith("DataHT"):
            continue

        if dat.year != year:
            continue

        toPlot = False
        toVeto = False

        lepss = []    
        if dat.label.startswith("DataEle_") or dat.label.startswith("FakeEle_"):
            lepss = ["electron"]
        elif dat.label.startswith("DataMu_") or dat.label.startswith("FakeMu_"):
            lepss = ["muon"]
        else:
            lepss = [
                "muon",
                "electron",
            ]

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

        #arg2 = arg0 + arg1 + " --ch ltau --count -d " + dat.label
        arg2 = arg0 + arg1 + " --ch ltau -d " + dat.label
        
        for region in regions:
            arg3 = arg2 + " --" + region
            if len(variables) > 0:
                arg3 += " -v "
                for idv, variab in enumerate(variables):
                    if idv > 0:
                        arg3 += ","
                    arg3 += variab

            if opt.count:
                arg3 += " --count"

            if opt.tDMcut:
                arg3 += " --tDMcut"
            elif opt.test:
                arg3 += " --test"

            for lepn in lepss:
                arg4 = arg3 + " --lep " + lepn
                if opt.nosyst:
                    arg4 += " --syst noSyst"
                elif opt.systs != "all":
                    arg4 += " --syst " + str(opt.systs)
                if opt.cut != "not":
                    arg5 = ""
                    for cut in cuts: 
                        arg5 = arg4 + " --cut \"" + cut + "\""
                        argss.append(arg5)
                else:
                    argss.append(arg4)
                
        submitter(dat, argss, folder, opt.cut)
        
