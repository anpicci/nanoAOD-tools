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
from xgboost import XGBClassifier


usage = 'python3 PrepareToPlot.py -y year -f folder'
parser = optparse.OptionParser(usage)
parser.add_option('-y', dest='year', type=str, default = '2017', help='Please enter a year, default is 2017')
parser.add_option('-f', dest='folder', type=str, default = 'v20', help='Please enter a folder, default is v4')
parser.add_option('-c', dest='check', default = False, action = 'store_true', help='Default runs makeplot')
parser.add_option('--rw', dest='rw', default = False, action = 'store_true', help='Default does not rewrite')
parser.add_option('--ov', dest='ovride', default = False, action = 'store_true', help='Override check for completed condorization')
parser.add_option('-d', dest='dat', type=str, default = 'all', help='Default is all')
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

path = "/eos/home-" + inituser + "/" + username + "/VBS/nosynch/" + ofolder + "/"
#print(path, opt.isfake)
if not "btag" in opt.folder and not opt.isfake and (("mcreco" in opt.folder and int(opt.folder.split("mcreco")[-1].split("v")[-1]) >= 80) or not "mcreco" in opt.folder):
    path += opt.channel + "/"

modelpaths = opt.paths.split(",")
branches = opt.branches.split(",")
scalers = opt.scalers.split(",")

for im, model in enumerate(modelpaths):
    print(im, model)
    print(im, branches[im])#

features = []
for ib, branch in enumerate(branches):
    features.append([])
    listfile = open(branch + "_features.txt")
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
    elif "DNN" in branch[idm]:
        with open(scalers[idm], 'rb') as file:
            scalers.append(pickle.load(file))
        models.append(tensorflow.keras.models.load_model(modelpath))

print(len(modelpaths), len(branches))
Debug = opt.check # True # False #
split = 50

if "UL" in opt.folder and int(opt.folder.split("UL")[-1]) > 9:
    isWithSysts = True
    scenarios = ["nominal"]#, "jesUp", "jesDown", "jerUp", "jerDown", "TESUp", "TESDown", "FESUp", "FESDown"]
else:
    isWithSysts = False
    scenarios = ["all"]

def CondoredList(samplename):
    try:
        condlist = os.listdir(path+samplename)
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

def MLRun(k, kpath):
    if Debug:
        return("ML run...")
    file_path = kpath+k
    file_path += ".root"

    #check if there is at least one event in the tree
    if not os.path.exists(file_path):
        print(file_path, "does not exist!")
        return False

    file_path_cp = kpath+k+"_cp.root"

    tmpfile = ROOT.TFile.Open(file_path)

    for ids, scenario in enumerate(scenarios):
        if k.startswith("Data") and ids > 0:
            continue
        tmptree = tmpfile.Get("events_"+scenario)
        tmpentr = tmptree.GetEntries()
        #tmpfile.Close()
        #tmpfile.Delete()
        print("Processing events for scenario", scenario)
        #print("entries:", tmpentr)

        if tmpentr > 0:
            # insert BDT output value into merged file

            for idbr, branch in enumerate(branches):
                with uproot.open(file_path) as file:#_cp)
                    tree = file["events_" + scenario]
                    df = tree.arrays(library="pd", filter_branch=lambda b: b.name != "w_PDF")
                    df = df.fillna(0)

                    new_columns = []
                    for i in df.columns:
                        new_columns.append(i.split('[')[0])
                    df.columns = new_columns

                    if os.path.exists(file_path_cp):
                        os.system("rm " + file_path_cp)
                    os.system("cp " + file_path + " " + file_path_cp)

                    myfile = ROOT.TFile(file_path_cp, 'update')
                    #print("entries", scenario, myfile.Get("events_"+scenario).GetEntries())
                    mytree = myfile.Get("events_"+scenario)
                    numOfEvents = mytree.GetEntries()
                    if branch in mytree.GetListOfBranches():
                        print("branch", branch, "already exists. If you want to reprocess it, please first remerge the sample", k, "and then come back to us!")
                        myfile.Close()
                        continue
                    else:
                        print("branch", branch, "will be created for sample", k)


                    brancharray = array('d', [0.5])
                    newbranch = mytree.Branch(branch, brancharray, branch+"/D")

                    print("Creating branch for model", branch)
                    to_keep = features[idbr]

                    X = df[to_keep].to_numpy()
                    # update root file with BDT branch
                    if "BDT" in branch:
                        output_array = models[idbr].predict_proba(X)[:,1]
                    elif "DNN" in branch:
                        output_array = models[idbr].predict(scalers[idbr].transform(X_SM))
                                
                    for n in range(numOfEvents):
                        mytree.GetEntry(n)
                        sys.stdout.write("\rProcessing event {0}     complete {1:.3f} percent".format(n, 100*n/numOfEvents))
                        brancharray[0] = output_array[n]
                        newbranch.Fill()

                    print("\n", branch, "completed!")
                    myfile.cd()
                    mytree.Write("", ROOT.TFile.kOverwrite)
                    myfile.Close()

                    print("Saving tree with ML branches...")
                    os.system("mv " + file_path_cp + " " + file_path)

print("year", opt.year)

mergefakes = {
    str("FakeMu_"+str(opt.year)): {comp.label:False for comp in merge_dict["FakeMu_"+str(opt.year)].components},
    str("FakeEle_"+str(opt.year)): {comp.label:False for comp in merge_dict["FakeEle_"+str(opt.year)].components},
}

for k, v in merge_dict.items():
    if not k.endswith(str(opt.year)):
        continue

    if k.startswith("Fake"):
        continue

    ismerged = False
    doesexist = []
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
    if hascomp:
        if opt.dat != 'all':
            if not str(k).startswith(opt.dat):
                if not k.startswith(opt.dat):
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
            
            doesexist.append(True)

            #print(cpath)
            partmerge = False
            #print(cpath+k+".root")
            if not os.path.exists(cpath+c.label+".root") or opt.rw:
                partmerge = True
                #if (hasattr(v, "components") and os.path.exists(cpath+k+"_merged.root")) or opt.rw:
                if os.path.exists(cpath+c.label+"_merged.root") or opt.rw:
                    if Debug:
                        print("rm -f " + cpath + c + "_merged.root")
                    else:
                        os.system("rm -f " + cpath + c + "_merged.root")
            print("Merging parts?", partmerge)
            if partmerge:
                print(c.label + " not merged so far")

                if os.path.exists(cpath+c.label+".root"):
                    if Debug:
                        print("rm -f " + cpath + c.label + ".root")
                    else:
                        os.system("rm -f " + cpath + c.label + ".root")

                print("Merging and luming " + c.label + "...")
                merging.append(True)
                if Debug:
                    print("python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + c.label + " --folder " + ofolder + " --ch " + opt.channel )
                else:
                    os.system("python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + c.label + " --folder " + ofolder + " --ch " + opt.channel )
                print("Merged and lumied!")
            else:
                print(c.label + " already merged and lumied")
            #partmerge = False
            
            MLRun(c.label, cpath)

        samplemerge = False
        if len(doesexist) == len(v.components):
            samplemerge = True

        if samplemerge:
            if os.path.exists(kpath+k+".root"):
                if Debug:
                    print("rm -f "+kpath+k+".root")
                else:
                    os.system("rm -f "+kpath+k+".root")
            if Debug:
                print("python3 makeplot.py -y ", opt.year, " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel )
            else:
                os.system("python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel )

        else:
            print(k + "not ready to be merged")
            
    else:
        if opt.dat != 'all':
            if not k.startswith(opt.dat):
                continue
        if not os.path.exists(kpath+k+".root") or opt.rw:
            if not DoesSampleExist(v.name) and not opt.ovride:
                print(k + " not crabbed yet")
                continue
            if not AreAllCondored(v.name, k) and not opt.ovride:
                print(k + " not condored at all yet")
                continue

        doesexist.append(True)
        samplemerge = False
        if not os.path.exists(kpath+k+".root") or opt.rw:
            samplemerge = True
            if os.path.exists(kpath+k+"_merged.root") or opt.rw:
                if Debug:
                    print("rm -f " + kpath + k + "_merged.root")
                else:
                    os.system("rm -f " + kpath + k + "_merged.root")

        if samplemerge:
            if os.path.exists(kpath+k+".root"):
                if Debug:
                    print("rm -f " + kpath + k + ".root")
                else:
                    os.system("rm -f " + kpath + k + ".root")
            print(k + " neither merged nor lumied so far")
            print("Merging and luming " + k + "...")
            if Debug:
                print("python3 makeplot.py -y ", opt.year, " --merpart --lumi --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel )
            else:
                os.system("python3 makeplot.py -y " + opt.year + " --merpart --lumi --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel )
            print("Merged and lumied!")
        else:
            print(k + " already merged and lumied")
        MLRun(k, kpath)

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
