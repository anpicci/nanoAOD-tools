import os
import tensorflow
import optparse
import sys
from array import array
import pandas as pd
import uproot
import pickle
import numpy as np
import sklearn
import math
from xgboost import XGBClassifier

#os.environ['TF_CPP_MIN_LOG_LEVEL']

usage = 'python3 add_1finalMVA_test.py -y year -f folder'
parser = optparse.OptionParser(usage)
parser.add_option('-y', dest='year', type=str, default = '2017', help='Please enter a year, default is 2017')
parser.add_option('-f', dest='folder', type=str, default = 'v20', help='Please enter a folder, default is v4')
parser.add_option('-c', dest='check', default = False, action = 'store_true', help='Default runs makeplot')
parser.add_option('--rw', dest='rw', default = False, action = 'store_true', help='Default does not rewrite')
parser.add_option('--ov', dest='ovride', default = False, action = 'store_true', help='Override check for completed condorization')
parser.add_option('-d', dest='dat', type=str, default = 'all', help='Default is all')
parser.add_option('-v', dest='veto', type=str, default = 'none', help='Default is none')
parser.add_option('-s', dest='scenario', type=str, default = 'all', help='Default is all')
parser.add_option('--fake', dest='isfake', default = False, action = 'store_true', help='Default runs for analysis, true for fake ratio')
parser.add_option('--ct', dest='ct', type=str, default = '', help='Default is analysis, otherwise specified CT')
parser.add_option('--ch', dest='channel', type=str, default = 'ltau', help='Select final state, default is h_tau + lepton')
parser.add_option('--paths', dest='paths', type=str, help='Insert paths')
parser.add_option('--branches', dest='branches', type=str, help='Insert paths')
parser.add_option('--scalers', dest='scalers', default = "", type=str, help='Insert paths')

(opt, args) = parser.parse_args()

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])

crabpath = ''
if opt.ct == 'HT':
    crabpath = "../../crab/macros/files/Fake/HT/"
else:
    crabpath = "../../crab/macros/files/"

if "UL" in opt.year:
    from samples.samplesUL import *
else:
    from samples.samples import *
#username = 'mmagheri'
#inituser = 'm'

ofolder = ''

#if opt.ct != '':
    #ofolder += "CT" + opt.ct + "_"

ofolder += opt.folder# + "/"

#path = "/eos/home-" + inituser + "/" + username + "/VBS/nosynch/" + ofolder + "/"
path = "/eos/home-a/apiccine/VBS/nosynch/" + ofolder + "/"
#print(path, opt.isfake)
if not "btag" in opt.folder and not opt.isfake and (("mcreco" in opt.folder and int(opt.folder.split("mcreco")[-1].split("v")[-1]) >= 80) or not "mcreco" in opt.folder):
    path += opt.channel + "/"

modelpaths = opt.paths.split(",")
branches = opt.branches.split(",")
scalerpaths = opt.scalers.split(",")
print(branches, scalerpaths)

notAll = False
if opt.dat != "all":
    mergesamp = opt.dat.split(",")
    notAll = True
    print("Samples to do:", mergesamp)

toVeto = False
if opt.veto != "none":
    vetosamp = opt.veto.split(",")
    toVeto = True
    print("Samples to veto:", vetosamp)

for im, model in enumerate(modelpaths):
    print(im, model)
    print(im, branches[im])#

features = []
for ib, branch in enumerate(branches):
    features.append([])
    listfile = open("ML/" + branch + "_features.txt")
    for line in listfile.readlines():
        line = line.replace("\n", "")
        for word in line.split(","):
            features[ib].append(word)

models = []
scalers = []
for idm, modelpath in enumerate(modelpaths):
    if "BDT" in branches[idm]:
        models.append(XGBClassifier())
        models[idm].load_model(modelpath)
    elif "DNN" in branches[idm]:
        with open(scalerpaths[idm], 'rb') as file:
            scalers.append(pickle.load(file))
        models.append(tensorflow.keras.models.load_model(modelpath))

#print(len(modelpaths), len(branches))
Debug = opt.check # True # False #
split = 50

if "UL" in opt.folder and int(opt.folder.split("UL")[-1]) > 9:
    isWithSysts = True
    if opt.scenario == "all":
        scenarios = [
            "nominal",
            "jesUp",
            "jesDown",
            "jerUp",
            "jerDown",
            "TESUp",
            "TESDown",
            "FESUp",
            "FESDown",
        ]
    else:
        scenarios = opt.scenario.split(",")
else:
    isWithSysts = False
    scenarios = ["all"]

def CondoredList(samplename):
    try:
        condlist = [f for f in os.listdir(path+samplename) if "_part" in f]
    except:
        condlist = []

    if len(condlist) > 0:
        toRel = False
        wrongex = False
        for condfile in condlist:
            if os.stat(path+samplename+"/"+condfile).st_size == 0.:
                print("Condoring still not ended so far")
                condlist.remove(condfile)
            elif os.stat(path+samplename+"/"+condfile).st_size < 1024.:
                toRel = True
                condlist.remove(condfile)
                if not opt.check:
                    os.system("rm -r "+ path + samplename + "/" + condfile)
                else:
                    print("rm -r "+ path + samplename + "/" + condfile)
            else:
                try:
                    tempf = ROOT.TFile.Open(path+samplename+"/"+condfile, "READ")
                except(RuntimeWarning):
                    condlist.remove(condfile)
                    wrongex = True
                    if not opt.check:
                        print("Removing damaged files...")
                        os.system("rm "+ path + samplename + "/" + condfile)
                    else:
                        print("rm "+ path + samplename + "/" + condfile)
                    
                else:
                    pass

                for ids, scenario in enumerate(scenarios):
                    if (samplename.startswith("Data") or samplename.startswith("Fake")) and ids > 0:
                        continue
                    try:
                        tempentr = tempf.Get(str("events_" + scenario)).GetEntries()
                    except(AttributeError, ReferenceError):#, RuntimeWarning):
                        try:
                            condlist.remove(condfile)
                        except:
                            pass
                        wrongex = True
                        if not opt.check:
                            print("Removing files with damaged " + scenario + " tree...")
                            os.system("rm "+ path + samplename + "/" + condfile)
                        else:
                            print("rm "+ path + samplename + "/" + condfile)
                    else:
                        pass

                    if ids == 0 and (not isWithSysts or "Data" in samplename):
                        break

        if toRel:
            print("Something went wrong during condoring", samplename, "fix it and relaunch")
            return CondoredList(samplename)
        elif wrongex:
            print("Something went wrong when remapping rootfiles for", samplename, "fix it and relaunch")

    return condlist

def DoesSampleExist(samplename):
    if samplename+".txt" not in os.listdir(crabpath):
        return False
    else:
        return True

def AreAllCondored(crabname, condorname):
    storelist = [line for line in open(crabpath+crabname+".txt")]
    condoredlist = CondoredList(condorname)

    if condorname+"_merged.root" in condoredlist:
        condoredlist.remove(condorname+"_merged.root")
    if condorname+".root" in condoredlist:
        condoredlist.remove(condorname+".root")

    lenstore = len(storelist)
    
    if 'Data' in crabname:
        remainder = int(lenstore%split)
        lenstore = int(lenstore/split)
        if remainder > 0:
            lenstore += 1

    if len(condoredlist) < (lenstore):
        print("condored: ", len(condoredlist), "\tlenstore: ", lenstore)
        return False
    elif lenstore==0 and len(condoredlist)==0:
        print("Warning for", condorname, "False flag for crabbed files! need to recrab them")
        return False
    else:
        return True

def MLRun(st, stpath):
    if Debug:
        return("ML run...")
    #file_path = stpath+k
    #file_path += ".root"
    filelist = [f for f in CondoredList(st) if "part" in f]
    finalpath = stpath + st + ".root"
    
    if os.path.exists(finalpath):
        IsThere = []
        finalfile = ROOT.TFile.Open(finalpath, "READ")

        for scen in scenarios:
            if "Data" in st and scen != "nominal":
                continue
            try:
                finaltree = finalfile.Get("events_" + scen)
            except:
                print("Something went wrong when trying to open " + finalpath +", redoing this...")
                IsThere.append(False)
                break
            else:
                pass

            for bran in branches:
                if bran in finaltree.GetListOfBranches():
                    print(bran + " already there in " + st + " for scenario " + scen)
                    IsThere.append(True)
                else:
                    IsThere.append(False)

        if True in IsThere:
            print("\n")
            return False
        else:
            pass
                    
    totMLed = []
    for fpath in filelist:
        totfpath = stpath+fpath
        fMLed = OpenAndRun(st, totfpath)
        totMLed.append(fMLed)

    if True in totMLed:
        return True
    else:
        return False

def OpenAndRun(st, file_path):
    #check if there is at least one event in the tree
    if not os.path.exists(file_path):
        print(file_path, "does not exist!")
        return False
    print("\n\nProcessing " + file_path)
    tmpdir = "tmpML_" + opt.folder
    #file_path_cp = stpath+st+"_cp.root"
    if os.path.exists(tmpdir):
        pass
        #os.system("rm -rf " + tmpdir + "/*")
    else:
        os.system("mkdir " + tmpdir)
    fname = file_path.split("/")[-1].replace(".root", "")
    #file_path_cp = tmpdir + "/"+st+"_cp.root"
    file_path_cp = tmpdir + "/"+fname+"_cp.root"
    #tmpfile = ROOT.TFile.Open(file_path)
    ids = 0
    MLed = []
    while ids < len(scenarios):
    #for ids, scenario in enumerate(scenarios):
        scenario = scenarios[ids]
        if st.startswith("Data") and ids > 0:
            ids += 1
            continue

        #print("Processing events for scenario", scenario)
        try:
            tmpfile = ROOT.TFile.Open(file_path)
            tmptree = tmpfile.Get("events_"+scenario)
            tmpentr = tmptree.GetEntries()
        except:
            print("Problems with opening " + file_path + ", retrying...")
            continue
        else:
            pass
        ids += 1
        tmpfile.Close()

        if tmpentr > 0:
            print("\nStarting with " + scenario)
            idbr = 0
            #for idbr, branch in enumerate(branches):
            while idbr < len(branches):
                branch = branches[idbr]
                isDamaged1 = False
                isDamaged2 = False
                isDamaged3 = False
                os.system("cp " + file_path + " " + file_path_cp)
                myfile = ROOT.TFile(file_path_cp, 'update')
                try:
                    myfile.Get("events_"+scenario).GetListOfBranches()
                except:
                    print("Problems with copying " + file_path + ", retrying...")
                    myfile.Close()
                    os.system("rm " + file_path_cp)
                    continue
                else:
                    pass
                if branch in myfile.Get("events_"+scenario).GetListOfBranches():
                    print("branch", branch, "already exists. If you want to reprocess it, please first remerge the sample", st, "and then come back to us!")
                    myfile.Close()
                    MLed.append(False)
                    idbr += 1
                    continue
                else:
                    print("branch", branch, "will be created for sample", st)
                    pass

                mytree = myfile.Get("events_"+scenario)
                to_keep = features[idbr]
         
                with uproot.open(file_path) as file:#_cp)
                    df = pd.DataFrame(columns = to_keep)
                    stepsize = 1000
                    tree = file["events_" + scenario]
                    steps = math.floor(tmpentr/stepsize) + 1
                    #print("steps", steps)
                    for step in range(0,steps):
                        #print("step", step)
                        #print("entry_start", stepsize * step, "entry_stop", min(tmpentr, stepsize * (step + 1)))
                        df_step = tree.arrays(library="pd", filter_branch=lambda b: b.name in to_keep, entry_start = stepsize * step, entry_stop = min(tmpentr, stepsize * (step + 1)))
                        df_step = df_step.fillna(0)
                        new_columns = []
                        for i in df_step.columns:
                            new_columns.append(i.split('[')[0])
                        df_step.columns = new_columns
                        df_step = df_step[to_keep]
                        df = pd.concat([df,df_step])
                        for i in df.columns:
                            if 'taujet' in i:
                                df.loc[df[i]==-999,i] = -2. 
                        
                    numOfEvents = mytree.GetEntries()

                    brancharray = array('d', [0.5])
                    newbranch = mytree.Branch(branch, brancharray, branch+"/D")

                    print("Creating branch for model", branch)
                    to_keep = features[idbr]
                    X = df[to_keep].to_numpy()
                    # update root file with BDT branch
                    if "BDT" in branch:
                        output_array = models[idbr].predict_proba(X)[:,1]
                    elif "DNN" in branch:
                        output_array = models[idbr].predict(scalers[idbr].transform(X))
                                
                    for n in range(numOfEvents):
                        mytree.GetEntry(n)

                        try:
                            remainder = (n+1)%int(numOfEvents/100)
                        except ZeroDivisionError:
                            remainder = 0

                        if remainder == 0 or (n+1) == numOfEvents:
                            sys.stdout.write("\rProcessing event {0}     complete {1:.0f} percent".format(n, round(100*(n+1)/numOfEvents), 0))
                        brancharray[0] = output_array[n]
                        newbranch.Fill()

                    print("\n", branch, "completed!")
                
                myfile.cd()
                mytree.Write("", ROOT.TFile.kOverwrite)
                myfile.Close()

                file_path_bu = file_path.replace(".root", "_bu.root")
                os.system("mv " + file_path + " " + file_path_bu)
                os.system("mv " + file_path_cp + " " + file_path)
                #os.system("rm " + file_path_cp)
                
                try:
                    checkfile = ROOT.TFile(file_path, 'update')
                except:
                    print("Warning! " + file_path + " corrupted afer copy, retrying the branching " + branch)
                    os.system("mv " + file_path_bu + " " + file_path)
                    isDamaged1 = True
                else:
                    pass
                
                for idcs, chscen in enumerate(scenarios):
                    if st.startswith("Data") and (idcs > 0 or chscen != "nominal"):
                        continue#break
                    try:
                        checknum = checkfile.Get("events_"+chscen).GetEntries()
                    except:
                        print("Warning! " + file_path + " " + chscen + " corrupted after copy, retrying the branching " + branch)
                        os.system("mv " + file_path_bu + " " + file_path)
                        isDamaged2 = True
                        break
                    else:
                        if chscen == scenario:
                            try:
                                IsBranched = branch in checkfile.Get("events_"+scenario).GetListOfBranches()
                            except:
                                print("Warning! " + file_path + " " + chscen + " corrupted after copy, retrying the branching " + branch)
                                os.system("mv " + file_path_bu + " " + file_path)
                                isDamaged3 = True
                                break
                            else:
                                if not IsBranched:
                                    print("Warning! " + file_path + " " + chscen + " corrupted after copy, retrying the branching " + branch)
                                    os.system("mv " + file_path_bu + " " + file_path)
                                    isDamaged3 = True
                                    break
                                else:
                                    pass
                        pass
                    pass
                
                print("isDamaged?", (isDamaged1 or isDamaged2))

                if isDamaged1 or isDamaged2 or isDamaged3:
                    print("Branching damaged file! Avoid to save and relaunching "  + branch + "...")
                    if isDamaged2:
                        checkfile.Close()
                    continue
                else:
                    checkfile.Close()
                    os.system("rm " + file_path_bu)
                    MLed.append(True)
                    idbr += 1
        
        else:
            os.system("cp " + file_path + " " + file_path_cp)
            myfile = ROOT.TFile(file_path_cp, 'update')
            mytree = myfile.Get("events_"+scenario)
            print("File has 0 entries, managing with this...")
            for branch in branches:
                if branch in mytree.GetListOfBranches():
                    print("branch", branch, "already exists. If you want to reprocess it, please first remerge the sample", st, "and then come back to us!")
                    myfile.Close()
                    MLed.append(False)
                    continue
                
                brancharray = array('d', [0])
                newbranch = mytree.Branch(branch, brancharray, branch+"/D")
                MLed.append(True)

                myfile.cd()
                mytree.Write("", ROOT.TFile.kOverwrite)

            myfile.Close()
            os.system("mv " + file_path_cp + " " + file_path)
                
    if True in MLed:
        return True
    else:
        return False

print("year", opt.year)

#mergefakes = {
    #str("FakeMu_"+str(opt.year)): {comp.label:False for comp in merge_dict["FakeMu_"+str(opt.year)].components},
    #str("FakeEle_"+str(opt.year)): {comp.label:False for comp in merge_dict["FakeEle_"+str(opt.year)].components},
#}

for k, v in merge_dict.items():
    if not k.endswith(str(opt.year)):
        continue

    if toVeto and k in vetosamp:
        continue

    if notAll and k not in mergesamp:
        continue
    #else:
        #print(notAll, k)

    if k.startswith("Fake"):
        continue

    isMLed = False

    merging = []

    kpath = path+k+"/"

    if not opt.isfake:# or opt.ct == '':
        pass
        #if k.startswith('DY'):# or k.startswith('DataHT'):
            #pass #continue

    elif opt.isfake:
        if not (k.startswith('TT_') or k.startswith('DataHT') or k.startswith('DY') or k.startswith('WJets') or k.startswith('GluGluToContin') or k.startswith('ZZ')):
            continue

    #print("\n")
    hascomp = False
    if "UL" in opt.year:
        hascomp = hasattr(v, "components")
    else:
        hascomp = v.components is not None

    doesexist = []
    if hascomp:
        if opt.dat != 'all':
            IsIncluded = False
            for dat in mergesamp:
                if str(k).startswith(dat):
                    IsIncluded = True
                    break
                
            if not IsIncluded:
                    continue

        print("with components")
        print("Sample: ", k)

        for c in v.components:
            cpath = path + c.label +"/"
            if not os.path.exists(cpath+c.label+".root") or opt.rw:
                if not DoesSampleExist(c.name) and not opt.ovride:
                    print(c.label, "not crabbed yet")
                    continue
                if not AreAllCondored(c.name, c.label) and not opt.ovride:
                    print(c.label + " not condorly produced yet")
                    continue

            result = MLRun(c.label, cpath)
            doesexist.append(result)

        samplemerge = False
        if len(doesexist) == len(v.components) and True in doesexist:
            samplemerge = True

        if samplemerge:
            if os.path.exists(kpath+k+".root"):
                if Debug:
                    print("rm -f "+kpath+k+".root")
                else:
                    os.system("rm -f "+kpath+k+".root")
            if Debug:
                print("python3 PrepareToPlot.py -f " + ofolder + " -y " + opt.year +" -d " + k + " --rw --or")
            else:
                print("python3 PrepareToPlot.py -f " + ofolder + " -y " + opt.year +" -d " + k + " --rw --or")
                os.system("python3 PrepareToPlot.py -f " + ofolder + " -y " + opt.year +" -d " + k + " --rw --or")

            
        else:
            print(k + " not to be merged")
            
    else:
        if opt.dat != 'all':
            IsIncluded = False
            for dat in mergesamp:
                if k.startswith(dat):
                    IsIncluded = True
                    break
            if not IsInclued:
                continue

        if not os.path.exists(kpath+k+".root") or opt.rw:
            if not DoesSampleExist(v.name) and not opt.ovride:
                print(k + " not crabbed yet")
                continue
            if not AreAllCondored(v.name, k) and not opt.ovride:
                print(k + " not condored at all yet")
                continue

        result = MLRun(k, kpath)

        samplemerge = True#result
        if not samplemerge:
            continue

        if os.path.exists(kpath+k+".root"):
            if Debug:
                print("rm -f "+kpath+k+".root")
            else:
                os.system("rm -f "+kpath+k+".root")
        if Debug:
            print("python3 PrepareToPlot.py -f " + ofolder + " -y " + opt.year +" -d " + k + " --rw --or")
        else:
            print("python3 PrepareToPlot.py -f " + ofolder + " -y " + opt.year +" -d " + k + " --rw --or")
            os.system("python3 PrepareToPlot.py -f " + ofolder + " -y " + opt.year +" -d " + k + " --rw --or")


'''
if opt.dat=="all" or opt.dat.startswith("Fake"):
        for kf, vf in mergefakes.items():
            if k in vf.keys():
                vf[k] = True

if opt.dat=="all" or opt.dat.startswith("Fake"):
    for kf, vf in mergefakes.items():
        if False in vf.values():
            continue

        kfpath = path + kf + "/"
        if os.path.exists(kfpath+k+".root"):
            if Debug:
                print("rm -f "+kfpath+kf+".root")
            else:
                os.system("rm -f "+kfpath+kf+".root")
        if Debug:
            print("python3 makeplot.py -y ", opt.year, " --mertree -d " + kf + " --folder "+ ofolder + " --ch " + opt.channel )
        else:
            os.system("python3 makeplot.py -y " + opt.year + " --mertree -d " + kf + " --folder " + ofolder + " --ch " + opt.channel )

print(mergefakes)
'''
