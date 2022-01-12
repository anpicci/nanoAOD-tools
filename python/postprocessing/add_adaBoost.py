import os
import optparse
import sys
from samples.samples import *
from array import array
import pandas as pd
import uproot
import pickle
import numpy as np
import sklearn
import xgboost


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
parser.add_option('--sm', dest='sm', default = False, action = 'store_true', help='sm ada')
parser.add_option('--dim6', dest='dim6', default = False, action = 'store_true', help='dim6 ada')
parser.add_option('--dim8', dest='dim8', default = False, action = 'store_true', help='dim8 ada')

(opt, args) = parser.parse_args()

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])

crabpath = ''
if opt.ct == 'HT':
    crabpath = "../../crab/macros/files/Fake/HT/"
else:
    crabpath = "../../crab/macros/files/"

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

def CondoredList(samplename):
    try:
        condlist = os.listdir(path+samplename)
    except:
        condlist = []

    if len(condlist) > 0:
        toRel = False
        wrongex = False
        for condfile in condlist:
            if os.stat(path+samplename+"/"+condfile).st_size < 1024.:#not samplename.startswith('DY')
                toRel =True
                condlist.remove(condfile)
                if not opt.check:
                    os.system("rm -r "+ path + samplename + "/" + condfile)
            else:
                tempf = ROOT.TFile.Open(path+samplename+"/"+condfile, "READ")
                try:
                    tempentr = tempf.Get("events_all").GetEntries()
                except (AttributeError, ReferenceError, RuntimeWarning) as e:
                    condlist.remove(condfile)
                    wrongex = True
                    if not opt.check:
                        os.system("rm "+ path + samplename + "/" + condfile)
                    
        if toRel:
            print("Something went wrong during condoring", samplename, "fix it and relaunch")
            return CondoredList(samplename)
        elif wrongex:
            print("Something when remapping rootfiles for ", samplename, "fix it and relaunch")

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

#print dirlist

#for dirn in dirlist:
#exsamples = [d for d in os.listdir(path+dirn) if os.path.isdir(path+dirn+"/"+d)]
#print exsamples

'''
print("samples")
for k, v in merge_dict.items():
    print(k, v)
'''

for k, v in merge_dict.items():
    #print(v.label)
    #print("hello", k)
    if opt.year not in k:
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

    if k.startswith('Fake'):
        mergable = False
        for c in v.components:
            if os.path.exists(path + c.label + "/" + c.label + ".root"):
                mergable = True
            else:
                mergable = False
        
        if mergable:
            if Debug:
                print("python3 makeplot.py -y ", opt.year, " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel)
            else:
                os.system("python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel)
        else:
            print(k, "not mergable")
        continue

    if True:#hasattr(v, 'components'):
        if opt.dat != 'all':
            if not str(v.label).startswith(opt.dat):
                if not k.startswith(opt.dat):
                    continue
        
        print("Sample: ", v.label)
        ncomps = 0
        cpath = ""
        if hasattr(v, 'components'):
            ncomps = len(v.components)
            for c in v.components:
                if not DoesSampleExist(c.name):
                    print(c.label, "not crabbed yet")
                    continue
                cpath = kpath # + v.label + "/"
                if not AreAllCondored(c.name, c.label):
                    print(v.label + " not condorly produced yet")
                    continue
                doesexist.append(True)


        else:
            ncomps = 1
            if not DoesSampleExist(v.name):
                print(v.label, "not crabbed yet")
                continue
            cpath = kpath # + v.label + "/"
            if not AreAllCondored(v.name, v.label):
                print(v.label + " not condorly produced yet")
                continue
            doesexist.append(True)

        #print(cpath)
        partmerge = False
        #print(cpath+v.label+".root")
        if not os.path.exists(cpath+v.label+".root") or opt.rw:
            partmerge = True
            if (hasattr(v, "components") and os.path.exists(cpath+v.label+"_merged.root")) or opt.rw:
                if Debug:
                    print("rm -f " + cpath + v.label + "_merged.root")
                else:
                    os.system("rm -f " + cpath + v.label + "_merged.root")

        if partmerge:
            print(v.label + " not merged so far")

            if os.path.exists(cpath+v.label+".root"):
                if Debug:
                    print("rm -f " + cpath + v.label + ".root")
                else:
                    os.system("rm -f " + cpath + v.label + ".root")

            print("Merging and luming " + v.label + "...")
            merging.append(True)
            if Debug:
                print("python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + v.label + " --folder " + ofolder + " --ch " + opt.channel)
            else:
                os.system("python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + v.label + " --folder " + ofolder + " --ch " + opt.channel)
            print("Merged and lumied!")
            partmerge = False

        if not partmerge:
            if opt.sm:
                model_SM_path = "/afs/cern.ch/user/t/ttedesch/public/adaBDT_SM_v100.p"
                name_bdtbranch = "BDT_output_SM_ada"
            elif opt.dim6:
                model_SM_path = "/afs/cern.ch/user/t/ttedesch/public/adaBDT_cH-chW-SM_v100.p"
                name_bdtbranch = "BDT_output_dim6_ada"
            elif opt.dim8:
                model_SM_path = "/afs/cern.ch/user/t/ttedesch/public/adaBDT_aQGC_v100.p"
                name_bdtbranch = "BDT_output_dim8_ada"
            else:
                print("Indicate model!")

            print("model: ", model_SM_path, "\tname branch: ", name_bdtbranch)

            if Debug:
                print("AdaBoost run...")
                continue
            print(v.label + " already merged and lumied")
            file_path = cpath+v.label+".root"
            #check if there is at least one event in the tree
            tmpfile = ROOT.TFile.Open(file_path)
            tmptree = tmpfile.Get("events_all")
            tmpentr = tmptree.GetEntries()
            tmptree.Delete()
            tmpfile.Close()
            tmpfile.Delete()
            print("entries:", tmpentr)

            if tmpentr > 0:
                # insert BDT output value into merged file
                file_path_cp = cpath+v.label+"_cp.root"
                os.system("cp " + file_path + " " + file_path_cp)
                #print(file_path)

                #model_SM_path = opt.model_SM
                #model_dim6_path = opt.model_dim6
                #model_dim8_path = opt.model_dim8
                #model_mu_path = opt.model_mu
                #model_ele_path = opt.model_ele
                #model_mu_path = opt.model_mu
                #print(model_path)
                #print(model_ele_path)
                #print(model_mu_path)
                # load sklearn models 
                file = open(model_SM_path,'rb')
                clf_SM = pickle.load(file)
                file.close()
                #file = open(model_dim6_path,'rb')
                #clf_dim6 = pickle.load(file)
                #file.close()
                #file = open(model_dim8_path,'rb')
                #clf_dim8 = pickle.load(file)
                #file.close()
            
                #load xgboost model
                #clf_SM = xgboost.XGBClassifier()
                #clf_SM.load_model(model_SM_path)

                #clf_dim6 = xgboost.XGBClassifier()
                #clf_dim6.load_model(model_dim6_path)

                #clf_dim8 = xgboost.XGBClassifier()
                #clf_dim8.load_model(model_dim8_path)
                
                # load model 
                #file = open(model_path,'rb')
                #clf = pickle.load(file)
                #file.close()
            
                #file = open(model_ele_path,'rb')
                #clf_ele = pickle.load(file)
                #file.close()
            
                #file = open(model_mu_path,'rb')
                #clf_mu = pickle.load(file)
                #file.close()

                # open root file
                file = uproot.open(file_path_cp)
                tree = file["events_all"]
                df = tree.arrays(library="pd", filter_branch=lambda b: b.name != "w_PDF")
                df = df.fillna(0)
            
                '''
                to_drop = ['w_nominal','lepSF[0]', 'lepUp[0]', 'lepDown[0]', 'puSF[0]', 'puUp[0]',
                'puDown[0]', 'PFSF[0]', 'PFUp[0]', 'PFDown[0]', 'q2Up[0]', 'q2Down[0]','w_PDF[0]',
                'SF_Fake[0]', 'tau_vsjet_SF[0]', 'tau_vsele_SF[0]', 'tau_vsmu_SF[0]', 'tau_vsjet_Up[0]', 'tau_vsjet_Down[0]', 'tau_vsele_Up[0]', 'tau_vsele_Down[0]', 'tau_vsmu_Up[0]', 'tau_vsmu_Down[0]',
                'tauSF[0]','tauUp[0]','tauDown[0]','TESSF[0]','TESUp[0]','TESDown[0]','FESSF[0]','FESUp[0]','FESDown[0]',
                'event_SFFake_vsjet2[0]', 'event_SFFake_vsjet4[0]','lepton_SFFake_vsjet2[0]', 'lepton_SFFake_vsjet4[0]', 'tau_SFFake_vsjet2[0]', 'tau_SFFake_vsjet4[0]',
                'tau_DeepTau_WP[0]','tau_DeepTauVsJet_WP[0]', 'tau_DeepTauVsMu_WP[0]','tau_DeepTauVsEle_WP[0]', 
                'HLT_effLumi[0]', 'pass_lepton_selection[0]','pass_tau_selection[0]', 'pass_tau_vsJetWP[0]','pass_jet_selection[0]', 'pass_upToBVeto[0]', 'pass_lepton_iso[0]','pass_lepton_veto[0]', 
                'pass_charge_selection[0]', 'pass_b_veto[0]', 'pass_mjj_cut[0]','pass_MET_cut[0]', 'pass_everyCut[0]', 'nBJets[0]',
                'event_Zeppenfeld[0]','tau_Zeppenfeld[0]','lepton_Zeppenfeld[0]', 
                'lepton_LnTRegion[0]', 'tau_LnTRegion[0]',  'tau_isolation[0]', 'lepton_TightRegion[0]','tau_TightRegion[0]','tau_isPrompt[0]','lepton_isPrompt[0]', 
                'tau_GenMatch[0]',
                'leadjet_CSVv2_b[0]', 'subleadjet_CSVv2_b[0]',] 
                '''



                #X = df.drop(columns=to_drop)
            
                new_columns = []
                for i in df.columns:
                    new_columns.append(i.split('[')[0])
                df.columns = new_columns

                '''            
                to_keep = ['lepton_pt',
                        'lepton_eta',
                        'lepton_phi',
                        'lepton_mass',
                        'lepton_pdgid',
                        'lepton_pfRelIso04',
                        'tau_pt',
                        'tau_eta',
                        'tau_phi',
                        'tau_mass',
                        'tau_DecayMode',
                        'tau_DeepTauVsEle_raw',
                        'tau_DeepTauVsMu_raw',
                        'tauleadTk_ptOverTau',
                        'tauleadTk_deltaPhi',
                        'tauleadTk_deltaEta',
                        'tauleadTk_Gamma',
                        'taujet_relpt',
                        'taujet_deltaPhi',
                        'taujet_deltaEta',
                        'taujet_HadGamma',
                        'taujet_EmGamma',
                        'taujet_HEGamma',
                        'leadjet_pt',
                        'leadjet_eta',
                        'leadjet_phi',
                        'leadjet_mass',
                        'leadjet_DeepFlv_b',
                        'leadjet_DeepCSVv2_b',
                        'AK8leadjet_pt',
                        'AK8leadjet_eta',
                        'AK8leadjet_phi',
                        'AK8leadjet_mass',
                        'AK8leadjet_tau21',
                        'AK8leadjet_tau32',
                        'AK8leadjet_tau43',
                        'leadjet_dRAK48',
                        'subleadjet_pt',
                        'subleadjet_eta',
                        'subleadjet_phi',
                        'subleadjet_mass',
                        'subleadjet_DeepFlv_b',
                        'subleadjet_DeepCSVv2_b',
                        'AK8subleadjet_pt',
                        'AK8subleadjet_eta',
                        'AK8subleadjet_phi',
                        'AK8subleadjet_mass',
                        'AK8subleadjet_tau21',
                        'AK8subleadjet_tau32',
                        'AK8subleadjet_tau43',
                        'subleadjet_dRAK48',
                        'nJets',
                        'MET_pt',
                        'MET_phi',
                        'm_jj',
                        'mT_lep_MET',
                        'mT_tau_MET',
                        'mT_leptau_MET',
                        'm_taulep',
                        'm_jjtau',
                        'm_jjtaulep',
                        'deltaPhi_jj',
                        'deltaPhi_taulep',
                        'deltaPhi_tauj1',
                        'deltaPhi_tauj2',
                        'deltaPhi_lepj1',
                        'deltaPhi_lepj2',
                        'deltaEta_jj',
                        'deltaEta_taulep',
                        'deltaEta_tauj1',
                        'deltaEta_tauj2',
                        'deltaEta_lepj1',
                        'deltaEta_lepj2',
                        'deltaTheta_jj',
                        'deltaTheta_taulep',
                        'deltaTheta_tauj1',
                        'deltaTheta_tauj2',
                        'deltaTheta_lepj1',
                        'deltaTheta_lepj2',
                        'ptRel_jj',
                        'ptRel_taulep',
                        'ptRel_tauj1',
                        'ptRel_tauj2',
                        'ptRel_lepj1',
                        'ptRel_lepj2',
                        'lepton_Zeppenfeld_over_deltaEta_jj',
                        'tau_Zeppenfeld_over_deltaEta_jj',
                        'event_Zeppenfeld_over_deltaEta_jj',
                        'event_RT',
                    ]
                '''
        
                to_keep = ['m_jj', 'm_jjtaulep', 'm_taulep', 'mT_lep_MET', 'leadjet_pt', 'subleadjet_pt', 'tau_mass', 'MET_pt']
            
                X = df[to_keep].to_numpy()
                
                '''
                X = df[['lepton_pt', 'lepton_eta', 'lepton_phi', 'lepton_mass', 'lepton_pdgid',
                'lepton_pfRelIso04', 'tau_pt', 'tau_eta', 'tau_phi', 'tau_mass',
                'tau_DeepTauVsEle_raw', 'tau_DeepTauVsMu_raw', 'leadjet_pt',
                'leadjet_eta', 'leadjet_phi', 'leadjet_mass', 'leadjet_CSVv2_b',
                'leadjet_DeepFlv_b', 'leadjet_DeepCSVv2_b', 'AK8leadjet_pt',
                'AK8leadjet_eta', 'AK8leadjet_phi', 'AK8leadjet_mass',
                'AK8leadjet_tau21', 'AK8leadjet_tau32', 'AK8leadjet_tau43',
                'leadjet_dRAK48', 'subleadjet_pt', 'subleadjet_eta', 'subleadjet_phi',
                'subleadjet_mass', 'subleadjet_CSVv2_b', 'subleadjet_DeepFlv_b',
                'subleadjet_DeepCSVv2_b', 'AK8subleadjet_pt', 'AK8subleadjet_eta',
                'AK8subleadjet_phi', 'AK8subleadjet_mass', 'AK8subleadjet_tau21',
                'AK8subleadjet_tau32', 'AK8subleadjet_tau43', 'subleadjet_dRAK48',
                'nJets', 'MET_pt', 'MET_phi', 'm_jj', 'mT_lep_MET', 'mT_tau_MET',
                'mT_leptau_MET', 'deltaPhi_jj', 'deltaPhi_taulep', 'deltaPhi_tauj1',
                'deltaPhi_tauj2', 'deltaPhi_lepj1', 'deltaPhi_lepj2', 'deltaEta_jj',
                'lepton_Zeppenfeld', 'tau_Zeppenfeld', 'event_Zeppenfeld',
                'pass_mjj_cut', 'pass_MET_cut', 'pass_everyCut']].to_numpy() 
                '''

                # update root file with BDT branch
                BDT_output_SM_ada_array = clf_SM.predict_proba(X)[:,1]
                #BDT_output_dim6_array = clf_dim6.predict_proba(X)[:,1]
                #BDT_output_dim8_array = clf_dim8.predict_proba(X)[:,1]
                
                #print(BDT_output_SM_array)
                #print(BDT_output_dim6_array)
                #print(BDT_output_dim8_array)
                #print()
                #BDT_output_SM_array = clf_SM.decision_function(X)
                #BDT_output_dim6_array = clf_dim6.decision_function(X)
                #BDT_output_dim8_array = clf_dim8.decision_function(X)

                myfile = ROOT.TFile(file_path_cp, 'update')
                mytree = myfile.Get("events_all")
                listOfNewBranches = []
                BDT_output_SM_ada   = array('d', [0.5] )
                #BDT_output_dim6   = array('d', [0.5] )
                #BDT_output_dim8   = array('d', [0.5] )
                #BDT_output   = array('d', [0.5] )
                #BDT_output_ele   = array('d', [0.5] )
                #BDT_output_mu   = array('d', [0.5] )
                #if opt.sm:
                listOfNewBranches.append(mytree.Branch(name_bdtbranch, BDT_output_SM_ada, name_bdtbranch+"/D") )
                    #listOfNewBranches.append(mytree.Branch("BDT_output_SM", BDT_output_SM, "BDT_output_SM/D") )
                #elif opt.dim6:
                    #listOfNewBranches.append(mytree.Branch(name_bdtbranch, BDT_output_SM_ada, name_bdtbranch+"/D") )
                #elif opt.dim8:
                    #listOfNewBranches.append(mytree.Branch(name_bdtbranch, BDT_output_SM_ada, name_bdtbranch+"/D") )
                #listOfNewBranches.append(mytree.Branch("BDT_output_dim8", BDT_output_dim8, "BDT_output_dim8/D") )
                #listOfNewBranches.append(mytree.Branch("BDT_output", BDT_output, "BDT_output/D") )
                #listOfNewBranches.append(mytree.Branch("BDT_output_ele", BDT_output_ele, "BDT_output_ele/D") )
                #listOfNewBranches.append(mytree.Branch("BDT_output_mu", BDT_output_mu, "BDT_output_mu/D") )
                numOfEvents = mytree.GetEntries()
                for n in range(numOfEvents):
                    BDT_output_SM_ada[0] = BDT_output_SM_ada_array[n]
                    #BDT_output_dim6[0] = 1.
                    #BDT_output_dim8[0] = 1.
                    #BDT_output_dim6[0] = BDT_output_dim6_array[n]
                    #BDT_output_dim8[0] = BDT_output_dim8_array[n]
                    
                    #BDT_output[0] = BDT_output_array[n]
                    #BDT_output_ele[0] = BDT_output_ele_array[n]
                    #BDT_output_mu[0] = BDT_output_mu_array[n]
                    #if n%1000 == 0:
                        #print(BDT_output[0])
                    mytree.GetEntry(n)
                    for newBranch in sorted(listOfNewBranches):
                        newBranch.Fill()

                mytree.Write("", ROOT.TFile.kOverwrite)
                myfile.Close()       
                os.system("mv " + file_path_cp + " " + file_path)

        samplemerge = False

        '''
        #print len(doesexist), len(v.components)
        if len(doesexist) == ncomps:
            if len(merging) == 0:
                if os.path.exists(kpath+k+".root") and not opt.rw:
                    print(k + " already merged")
                    samplemerge = False
                else:
                    samplemerge = True
            else:
                samplemerge = True

            if samplemerge:
                if os.path.exists(kpath+k+".root"):
                    if Debug:
                        print("rm -f "+kpath+k+".root")
                    else:
                        os.system("rm -f "+kpath+k+".root")
                if Debug:
                    print("python3 makeplot.py -y ", opt.year, " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel)
                else:
                    os.system("python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel)
        '''
        #else:
        #print k + "not ready to be merged"
