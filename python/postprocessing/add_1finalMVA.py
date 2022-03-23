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
parser.add_option('-d', dest='dat', type=str, default = 'all', help='Default is all')
parser.add_option('--fake', dest='isfake', default = False, action = 'store_true', help='Default runs for analysis, true for fake ratio')
parser.add_option('--ct', dest='ct', type=str, default = '', help='Default is analysis, otherwise specified CT')
parser.add_option('--ch', dest='channel', type=str, default = 'ltau', help='Select final state, default is h_tau + lepton')
parser.add_option('--SMbdt', dest='smbdt', default = False, action = 'store_true', help='Add sm MVA')
parser.add_option('--DIM6bdt', dest='dim6bdt', default = False, action = 'store_true', help='Add dim6 MVA')
parser.add_option('--DIM8bdt', dest='dim8bdt', default = False, action = 'store_true', help='Add dim8 MVA')
parser.add_option('--SMdnn', dest='smdnn', default = False, action = 'store_true', help='Add sm MVA')
parser.add_option('--DIM6dnn', dest='dim6dnn', default = False, action = 'store_true', help='Add dim6 MVA')
parser.add_option('--DIM8dnn', dest='dim8dnn', default = False, action = 'store_true', help='Add dim8 MVA')
parser.add_option('--smBDTpath', dest='BDT_SM_path', type=str, help='sm BDT path')
parser.add_option('--dim6BDTpath', dest='BDT_dim6_path', type=str, help='dim6 BDT path')
parser.add_option('--dim8BDTpath', dest='BDT_dim8_path', type=str, help='dim8 BDT path')
parser.add_option('--smDNNpath', dest='DNN_SM_path', type=str, help='sm DNN path')
parser.add_option('--dim6DNNpath', dest='DNN_dim6_path', type=str, help='dim6 DNN path')
parser.add_option('--dim8DNNpath', dest='DNN_dim8_path', type=str, help='dim8 DNN path')
parser.add_option('--smSCALERpath', dest='scaler_SM_path', type=str, help='sm SCALER path')
parser.add_option('--dim6SCALERpath', dest='scaler_dim6_path', type=str, help='dim6 SCALER path')
parser.add_option('--dim8SCALERpath', dest='scaler_dim8_path', type=str, help='dim8 SCALER path')
parser.add_option('--smBDTbrname', dest='BDT_SM_brname', type=str, default = 'BDT_output_SM_opt', help='sm BDT branch name')
parser.add_option('--dim6BDTbrname', dest='BDT_dim6_brname', type=str, default = 'BDT_output_dim6_opt', help='dim6 BDT branch name')
parser.add_option('--dim8BDTbrname', dest='BDT_dim8_brname', type=str, default = 'BDT_output_dim8_opt', help='dim8 BDT branch name')
#parser.add_option('--smDNNbrname', dest='DNN_SM_brname', type=str, default = 'DNN_output_SM_opt', help='sm DNN branch name')
#parser.add_option('--dim6DNNbrname', dest='DNN_dim6_brname', type=str, default = 'DNN_output_dim6_opt', help='dim6 DNN branch name')
#parser.add_option('--dim8DNNbrname', dest='DNN_dim8_brname', type=str, default = 'DNN_output_dim8_opt', help='dim8 DNN branch name')
parser.add_option('--smDNNbrname', dest='DNN_SM_brname', type=str, default = 'dummy_sm', help='sm DNN branch name')
parser.add_option('--dim6DNNbrname', dest='DNN_dim6_brname', type=str, default = 'dummy_dim6', help='dim6 DNN branch name')
parser.add_option('--dim8DNNbrname', dest='DNN_dim8_brname', type=str, default = 'dummy_dim8', help='dim8 DNN branch name')

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

#print(path)
#dirlist = [dirs for dirs in os.listdir(path) if os.path.isdir(path+dirs) and opt.folder in dirs]
#datas = opt.dataset + "_" + opt.year

Debug = opt.check # True # False #
split = 50

if "UL" in opt.folder and int(opt.folder.split("UL")[-1]) > 9:
    isWithSysts = True
    scenarios = ["nominal", "jesUp", "jesDown", "jerUp", "jerDown", "TESUp", "TESDown", "FESUp", "FESDown"]
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
                    try:
                        tempentr = tempf.Get(str("events_" + scenario)).GetEntries()
                    except(AttributeError, ReferenceError, RuntimeWarning):
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
    print(k + " already merged and lumied")
    file_path = kpath+k
    file_path += ".root"
    #check if there is at least one event in the tree
    print(os.path.exists(file_path))
    tmpfile = ROOT.TFile.Open(file_path)
    #tmpfile.ls()

    for ids, scenario in enumerate(scenarios):
        tmptree = tmpfile.Get("events_"+scenario)
        tmpentr = tmptree.GetEntries()
        tmptree.Delete()
        tmpfile.Close()
        tmpfile.Delete()
        print("entries:", tmpentr)

        if tmpentr > 0:
            # insert BDT output value into merged file
            file_path_cp = kpath+k+"_cp.root"
            os.system("cp " + file_path + " " + file_path_cp)

            #print(file_path)

            # open root file
            file = uproot.open(file_path_cp)
            tree = file["events_" + scenario]
            df = tree.arrays(library="pd", filter_branch=lambda b: b.name != "w_PDF")
            df = df.fillna(0)
        
            new_columns = []
            for i in df.columns:
                new_columns.append(i.split('[')[0])
            df.columns = new_columns

            to_keep_SM = [
                'm_jj',
                'subleadjet_pt',
                'leadjet_pt',
                'nBJets',
                'm_jjtaulep',
                'm_o1',
                'nJets',
                'event_Zeppenfeld_over_deltaEta_jj',
                'taujet_deltaEta',
                'mT_lep_MET',
                'tau_DecayMode',
                'm_1T',
                'taujet_EmGamma',
                'leadjet_DeepFlv_b',
                'MET_pt',
                'subleadjet_DeepFlv_b',
                'taujet_relpt',
                'm_taulep',
                'taujet_deltaPhi',
                'taujet_HadGamma',
                'taujet_HEGamma',  
                'm_jjtau', #new
                'tau_pt',
                'tau_mass',
                'event_RT',
                'mT_leptau_MET',
                'ptRel_lepj1',
                'ptRel_lepj2',
                'tau_isolation',
                'mT_tau_MET',
            ]
            
            #to_keep_SM = ['leadjet_DeepFlv_b', 'subleadjet_DeepFlv_b', 'event_Zeppenfeld_over_deltaEta_jj', 'taujet_relpt', 'm_o1', 'event_RT', 'taujet_deltaPhi', 'nJets', 'mT_lep_MET', 'm_jjtau', 'm_1T', 'nBJets', 'subleadjet_pt', 'm_jjtaulep', 'm_jj', 'leadjet_pt'] ###ReReco
            
            to_keep_dim6 = [
                'm_1T',
                'MET_pt',
                'm_jjtaulep',
                'm_o1',
                'leadjet_pt',
                'tau_pt',
                'lepton_pt',
                'm_taulep',
                'nJets',
                'deltaEta_taulep',
                'subleadjet_pt',
                'nBJets'
            ]

            #to_keep_dim6 = ['subleadjet_DeepFlv_b', 'leadjet_DeepFlv_b', 'event_Zeppenfeld', 'event_RT', 'm_jjtau', 'm_taulep', 'm_jj', 'nJets', 'mT_lep_MET', 'nBJets', 'm_o1', 'MET_pt', 'subleadjet_pt', 'm_1T', 'leadjet_pt', 'm_jjtaulep']###ReReco
            to_keep_dim8 = ['subleadjet_DeepCSVv2_b', 'leadjet_DeepCSVv2_b', 'm_taulep', 'event_RT', 'nBJets', 'mT_lep_MET', 'leadjet_pt', 'MET_pt', 'subleadjet_pt', 'm_jjtaulep', 'm_1T', 'm_o1']
        
            X_SM = df[to_keep_SM].to_numpy()
            X_dim6 = df[to_keep_dim6].to_numpy()
            X_dim8 = df[to_keep_dim8].to_numpy()

            # update root file with BDT branch
            if opt.smbdt == True:
                BDT_output_SM_array = BDT_SM.predict_proba(X_SM)[:,1]
            if opt.smdnn == True:
                DNN_output_SM_array = DNN_SM.predict(scaler_SM.transform(X_SM))
            if opt.dim6bdt == True:
                BDT_output_dim6_array = BDT_dim6.predict_proba(X_dim6)[:,1]
            if opt.dim6dnn == True:
                DNN_output_dim6_array = DNN_dim6.predict(scaler_dim6.transform(X_dim6))
            if opt.dim8bdt == True:
                BDT_output_dim8_array = BDT_dim8.predict_proba(X_dim8)[:,1]
            if opt.dim8dnn == True:
                DNN_output_dim8_array = DNN_dim8.predict(scaler_dim8.transform(X_dim8))

            myfile = ROOT.TFile(file_path_cp, 'update')
            mytree = myfile.Get("events_"+scenario)
            listOfNewBranches = []
            if opt.smbdt == True:
                BDT_output_SM   = array('d', [0.5] )
                listOfNewBranches.append(mytree.Branch(name_bdtbranch_SM, BDT_output_SM, name_bdtbranch_SM+"/D") )
            if opt.smdnn == True:
                DNN_output_SM   = array('d', [0.5] )
                listOfNewBranches.append(mytree.Branch(name_dnnbranch_SM, DNN_output_SM, name_dnnbranch_SM+"/D") )
            if opt.dim6bdt == True:
                BDT_output_dim6   = array('d', [0.5] )
                listOfNewBranches.append(mytree.Branch(name_bdtbranch_dim6, BDT_output_dim6, name_bdtbranch_dim6+"/D") )
            if opt.dim6dnn == True:
                DNN_output_dim6   = array('d', [0.5] )
                listOfNewBranches.append(mytree.Branch(name_dnnbranch_dim6, DNN_output_dim6, name_dnnbranch_dim6+"/D") )
            if opt.dim8bdt == True:
                BDT_output_dim8   = array('d', [0.5] )
                listOfNewBranches.append(mytree.Branch(name_bdtbranch_dim8, BDT_output_dim8, name_bdtbranch_dim8+"/D") )
            if opt.dim8dnn == True:
                DNN_output_dim8   = array('d', [0.5] )
                listOfNewBranches.append(mytree.Branch(name_dnnbranch_dim8, DNN_output_dim8, name_dnnbranch_dim8+"/D") )
            
            numOfEvents = mytree.GetEntries()
            for n in range(numOfEvents):
                if opt.smbdt == True:
                    BDT_output_SM[0] = BDT_output_SM_array[n]
                if opt.smdnn == True:
                    DNN_output_SM[0] = DNN_output_SM_array[n]
                if opt.dim6bdt == True:
                    BDT_output_dim6[0] = BDT_output_dim6_array[n]
                if opt.dim6dnn == True:
                    DNN_output_dim6[0] = DNN_output_dim6_array[n]
                if opt.dim8bdt == True:
                    BDT_output_dim8[0] = BDT_output_dim8_array[n]
                if opt.dim8dnn == True:
                    DNN_output_dim8[0] = DNN_output_dim8_array[n]
                    
                mytree.GetEntry(n)
                for newBranch in sorted(listOfNewBranches):
                    newBranch.Fill()

            mytree.Write("", ROOT.TFile.kOverwrite)
            myfile.Close()   
            os.system("mv " + file_path_cp + " " + file_path)
            #### if ends here

#print dirlist

#for dirn in dirlist:
#exsamples = [d for d in os.listdir(path+dirn) if os.path.isdir(path+dirn+"/"+d)]
#print exsamples

'''
print("samples")
for k, v in merge_dict.items():
    print(k, v)
'''

BDT_SM_path = opt.BDT_SM_path
BDT_dim6_path = opt.BDT_dim6_path
BDT_dim8_path = opt.BDT_dim8_path
DNN_SM_path = opt.DNN_SM_path
DNN_dim6_path = opt.DNN_dim6_path
DNN_dim8_path = opt.DNN_dim8_path
            
name_bdtbranch_SM = opt.BDT_SM_brname
name_bdtbranch_dim6 = opt.BDT_dim6_brname
name_bdtbranch_dim8 = opt.BDT_dim8_brname
name_dnnbranch_SM = opt.DNN_SM_brname
name_dnnbranch_dim6 = opt.DNN_dim6_brname
name_dnnbranch_dim8 = opt.DNN_dim8_brname


scaler_SM_path = opt.scaler_SM_path
scaler_dim6_path = opt.scaler_dim6_path
scaler_dim8_path = opt.scaler_dim8_path


# load models
if opt.smbdt == True:
    BDT_SM = XGBClassifier()
    BDT_SM.load_model(BDT_SM_path)
if opt.smdnn == True:
    with open(scaler_SM_path, 'rb') as file:
        scaler_SM = pickle.load(file)
    DNN_SM = tensorflow.keras.models.load_model(DNN_SM_path)
if opt.dim6bdt == True:
    BDT_dim6 = XGBClassifier()
    BDT_dim6.load_model(BDT_dim6_path)
if opt.dim6dnn == True:
    with open(scaler_dim6_path, 'rb') as file:
        scaler_dim6 = pickle.load(file)
    DNN_dim6 = tensorflow.keras.models.load_model(DNN_dim6_path)
if opt.dim8bdt == True:
    BDT_dim8 = XGBClassifier()
    BDT_dim8.load_model(BDT_dim8_path)
if opt.dim8dnn == True:
    with open(scaler_dim8_path, 'rb') as file:
        scaler_dim8 = pickle.load(file)
    DNN_dim8 = tensorflow.keras.models.load_model(DNN_dim8_path)

print("year", opt.year)
for k, v in merge_dict.items():
#for v in class_list:
    #print(v.label)
    #k = v.label
    #print("hello", k)
    if not k.endswith(str(opt.year)):
        continue

    if k.startswith("Fake"):
        continue

    ismerged = False
    doesexist = []
    merging = []

    kpath = path+k+"/"
    #print(kpath)
    if not opt.isfake:# or opt.ct == '':
        pass
        #if k.startswith('DY'):# or k.startswith('DataHT'):
            #pass #continue

    elif opt.isfake:
        if not (k.startswith('TT_') or k.startswith('DataHT') or k.startswith('DY') or k.startswith('WJets') or k.startswith('GluGluToContin') or k.startswith('ZZ')):
            continue
        
    '''
    if k.startswith('Fake'):
        mergable = False
        for c in v.components:
            if os.path.exists(path + c.label + "/" + c.label + ".root"):
                mergable = True
            else:
                mergable = False
        
        if mergable:
            if Debug:
                print("python3 makeplot.py -y ", opt.year, " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel + " --skipML")
            else:
                os.system("python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel + " --skipML")
        else:
            print(k, "not mergable")
        continue
    '''

    hascomp = False
    if "UL" in opt.year:
        hascomp = hasattr(v, "components")
    else:
        hascomp = v.components is not None
    if hascomp:#hasattr(v, 'components'):
        if opt.dat != 'all':
            if not str(k).startswith(opt.dat):
                if not k.startswith(opt.dat):
                    continue
        print("with components")
        print("Sample: ", k)

        for c in v.components:
            if not DoesSampleExist(c.name):
                print(c.label, "not crabbed yet")
                continue
            cpath = path + c.label +"/"
            if not AreAllCondored(c.name, c.label):
                print(c + " not condorly produced yet")
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
                    print("python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + c.label + " --folder " + ofolder + " --ch " + opt.channel + " --skipML")
                else:
                    os.system("python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + c.label + " --folder " + ofolder + " --ch " + opt.channel + " --skipML")
                print("Merged and lumied!")
            else:
                print(c.label + " already merged and lumied")
            #partmerge = False
            
            MLRun(c.label, cpath)
        #samplemerge = False

        #print len(doesexist), len(v.components)
        if len(doesexist) == len(v.components):

            '''
            if len(merging) == 0:
                if os.path.exists(kpath+k+".root") and not opt.rw:
                    print(k + " already merged")
                    samplemerge = False
                else:
                    samplemerge = True
            else:
            '''

            samplemerge = True

            if samplemerge:
                if os.path.exists(kpath+k+".root"):
                    if Debug:
                        print("rm -f "+kpath+k+".root")
                    else:
                        os.system("rm -f "+kpath+k+".root")
                if Debug:
                    print("python3 makeplot.py -y ", opt.year, " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel + " --skipML")
                else:
                    os.system("python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel + " --skipML")
        #else:
            #print k + "not ready to be merged"
            
    else:
        if opt.dat != 'all':
            if not k.startswith(opt.dat):
                continue
        if not DoesSampleExist(v.name):
            print(k + " not crabbed yet")
            continue
        if not AreAllCondored(v.name, k):
        #if not os.path.exists(kpath+k):
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
                print("python3 makeplot.py -y ", opt.year, " --merpart --lumi --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel + " --skipML")
            else:
                os.system("python3 makeplot.py -y " + opt.year + " --merpart --lumi --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel + " --skipML")
            print("Merged and lumied!")
        else:
            print(k + " already merged and lumied")
        MLRun(k, kpath)
