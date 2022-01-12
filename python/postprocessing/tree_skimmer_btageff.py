#!/bin/env python3
import os
##print(os.environ)
##print("**********************************************************************")
##print("**********************************************************************")
##print("**********************************************************************")
##print(str(os.environ.get('PYTHONPATH')))
##print(str(os.environ.get('PYTHON3PATH')))
import sys
##print("*************** This is system version info ***************************")
##print(sys.version_info)
#import platform
##print("*************** This is python version info ***************************")
##print(platform.python_version())
import ROOT
##print("Succesfully imported ROOT")
import math
import datetime
import copy
from array import array
from skimtree_utils_ssWW_wFakes_old import *

if not "_UL" in sys.argv[1]:
    if sys.argv[4] == 'remote':
        from samples import *
        Debug = False
    else:
        from samples.samples import *
        Debug = True
else:
    if sys.argv[4] == 'remote':
        from samplesUL import *
        Debug = False
    else:
        from samples.samplesUL import *
        Debug = True

sample = sample_dict[sys.argv[1]]
part_idx = sys.argv[2]
file_list = list(map(str, sys.argv[3].strip('[]').split(',')))
#print("file_list: ", file_list, "\nloop #1 over it")
#for infile in file_list:
    #print(infile)

def AddOverflow(h):
    nxbins = h.GetXaxis().GetNbins()
    nybins = h.GetYaxis().GetNbins()

    idxx = 0.
    idxy = nybins + 1 
    for ix in range(nxbins):
        idxx = ix + 1 
        ovf_bincont = h.GetBinContent(idxx, idxy)
        last_bincont = h.GetBinContent(idxx, nybins)
        new_last_bincont = ovf_bincont + last_bincont
        h.SetBinContent(idxx, nybins, new_last_bincont)

    idxx = nxbins + 1 
    idxy = 0. 
    for iy in range(nybins):
        idxy = iy + 1 
        ovf_bincont = h.GetBinContent(idxx, idxy)
        last_bincont = h.GetBinContent(nxbins, idxy)
        new_last_bincont = ovf_bincont + last_bincont
        h.SetBinContent(nxbins, idxy, new_last_bincont)


startTime = datetime.datetime.now()
print("Starting running at " + str(startTime))

ROOT.gROOT.SetBatch()

leadingjet_ptcut = 150.

chain = ROOT.TChain('Events')
#print(chain)
#print("loop #2 over file_list")
for infile in file_list: 
    #print("Adding %s to the chain" %(infile))
    chain.Add(infile)

print("Number of events in chain " + str(chain.GetEntries()))
#print("Number of events in tree from chain " + str((chain.GetTree()).GetEntries()))
#print("Type of tree from chain " + str(type(chain.GetTree())))
#treechain = (ROOT.TTree)(chain.GetTree())
tree = InputTree(chain)
print("Number of entries: " +str(tree.GetEntries()))
#print("tree: ", tree)

isMC = True
if ('Data' in sample.name):
    isMC = False

#MCReco = MCReco * isMC

IsDim8 = False
if 'aQGC' in sample.name:
    IsDim8 = True

dataEle = False
dataMu = False
if 'DataMu' in sample.name:
    dataMu = True
if 'DataEle' in sample.name:
    dataEle = True

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])
#folder = 'vbtag'
#if not os.path.exists("/eos/user/" + inituser + "/" + username + "/VBS/nosynch/" + folder + "/" + sample.label):
    #os.makedirs("/eos/user/" + inituser + "/" + username +"/VBS/nosynch/" + folder + "/" + sample.label)
#outpath = "/eos/user/" + inituser + "/" + username +"/VBS/nosynch/" + folder + "/" + sample.label + "/"
#++++++++++++++++++++++++++++++++++
#++   branching the new trees    ++
#++++++++++++++++++++++++++++++++++
#print(outpath + sample.label+"_part"+str(part_idx)+".root")
outTreeFile = ROOT.TFile(sample.label+"_part"+str(part_idx)+".root", "RECREATE") #some name of the output file

#++++++++++++++++++++++++++++++++++
#++         All category         ++
#++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++
#++      Efficiency studies      ++
#++++++++++++++++++++++++++++++++++
ptNBins = 100
ptMin = 0
ptMax = 1000.
etaNBins = 60
etaMin = -3.
etaMax = 3.
ptbins = array.array('d', [30, 50, 80, 140, 200, 300, 600, 1000])
etabins = array.array('d', [0.0, 0.8, 1.6, 2.4])
nptbins = len(ptbins)-1
netabins = len(etabins)-1
h2_BTaggingEff_Denom_b    = ROOT.TH2D("h2_BTaggingEff_Denom_b", "MC bjet;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)
h2_BTaggingEff_Denom_c    = ROOT.TH2D("h2_BTaggingEff_Denom_c", "MC cjet;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)
h2_BTaggingEff_Denom_udsg = ROOT.TH2D("h2_BTaggingEff_Denom_udsg", "MC ljet;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)
h2_BTaggingEff_Num_b    = ROOT.TH2D("h2_BTaggingEff_Num_b", "Tagged bjet;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)
h2_BTaggingEff_Num_c    = ROOT.TH2D("h2_BTaggingEff_Num_c", "Tagged cjet;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)
h2_BTaggingEff_Num_udsg = ROOT.TH2D("h2_BTaggingEff_Num_udsg", "Tagged ljet;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)

h2_BTaggingEff_Denom_b.Sumw2()
h2_BTaggingEff_Denom_c.Sumw2()
h2_BTaggingEff_Denom_udsg.Sumw2()
h2_BTaggingEff_Num_b.Sumw2()
h2_BTaggingEff_Num_c.Sumw2()
h2_BTaggingEff_Num_udsg.Sumw2()

#++++++++++++++++++++++++++++++++++
#++   looping over the events    ++
#++++++++++++++++++++++++++++++++++
for i in range(tree.GetEntries()):
    #++++++++++++++++++++++++++++++++++
    #++        taking objects        ++
    #++++++++++++++++++++++++++++++++++
    if Debug:
        if i > 100:
            break
    if not Debug and i%5000 == 0:
        print("Event #", i+1, " out of ", tree.GetEntries())
    event = Event(tree,i)
    electrons = Collection(event, "Electron")
    muons = Collection(event, "Muon")
    jets = Collection(event, "Jet")
    njets = len(jets)
    fatjets = Collection(event, "FatJet")
    HLT = Object(event, "HLT")
    PV = Object(event, "PV")
    Flag = Object(event, 'Flag')

    #++++++++++++++++++++++++++++++++++
    #++      defining variables      ++
    #++++++++++++++++++++++++++++++++++
    tightlep = None
    tightlep_p4 = None
    tightlep_p4t = None
    tightlep_SF = None
    tightlep_SFUp = None
    tightlep_SFDown = None
    recomet_p4t = None
    PF_SF = None
    PF_SFUp = None
    PF_SFDown = None
    PU_SF = None
    PU_SFUp = None
    PU_SFDown = None
    #++++++++++++++++++++++++++++++++++
    #++    starting the analysis     ++
    #++++++++++++++++++++++++++++++++++
    #VetoMu = get_LooseMu(muons)
    #goodMu = get_Mu(muons)
    #VetoEle = get_LooseEle(electrons)
    #goodEle = get_Ele(electrons)
    year = sample.year
    if(isMC):
        runPeriod = ''
    else:
        runPeriod = sample.runP

    if not isMC:
        if not Flag.eeBadScFilter:
            continue

    #print "------ ", i
    passMu, passEle, passHT, noTrigger = trig_map(HLT, PV, year, runPeriod, Flag)

    if noTrigger:
        continue

    '''
    GoodEle, ele_TightRegion = SelectLepton(electrons, False) 
    GoodMu, mu_TightRegion = SelectLepton(muons, True) 
 
    if GoodEle is None and GoodMu is None:
        continue

    ele_lepton_veto = -1
    mu_lepton_veto = -1

    if GoodEle != None:
        ele_lepton_veto = LepVeto(GoodEle, electrons, muons)
    if GoodMu != None:
        mu_lepton_veto = LepVeto(GoodMu, electrons, muons)

    SingleEle=False
    SingleMu=False
    ElMu=False

    LeadLepFamily="not selected"
    
    GoodLep = None
    leptons = None

    lepton_TightRegion = 0

    if 'DataHT' not in sample.label:
        if passEle and not passMu:
            if GoodEle != None and ele_lepton_veto:
                GoodLep = GoodEle
                lepton_TightRegion = copy.deepcopy(ele_TightRegion)
                SingleEle = True
                SingleMu = False
            else:
                continue

        elif passMu and not passEle:
            if GoodMu != None and mu_lepton_veto:
                GoodLep = GoodMu
                lepton_TightRegion = copy.deepcopy(mu_TightRegion)
                SingleEle = False
                SingleMu = True
            else:
                continue

        elif passMu and passEle:
            ElMu=True
        
        else:
            continue


    else:
        if passHT:
            ElMu = True
        else:
            continue

    if ElMu:
        if GoodMu==None and GoodEle!=None and ele_lepton_veto:
            GoodLep = GoodEle
            lepton_TightRegion = copy.deepcopy(ele_TightRegion)
            SingleEle = True
            SingleMu = False

        elif GoodMu!=None and mu_lepton_veto and GoodEle==None:
            GoodLep = GoodMu
            lepton_TightRegion = copy.deepcopy(mu_TightRegion)
            SingleMu = True
            SingleEle = False
                
        elif GoodMu!=None and GoodEle!=None:
            if ele_lepton_veto and not mu_lepton_veto:
                GoodLep = GoodEle
                lepton_TightRegion = copy.deepcopy(ele_TightRegion)
                SingleEle = True
                SingleMu = False
            elif not ele_lepton_veto and mu_lepton_veto:            
                GoodLep = GoodMu
                lepton_TightRegion = copy.deepcopy(mu_TightRegion)
                SingleMu = True
                SingleEle = False

            elif ele_lepton_veto and mu_lepton_veto:
                if GoodEle.pt > GoodMu.pt:
                    GoodLep = GoodEle
                    lepton_TightRegion = copy.deepcopy(ele_TightRegion)
                    SingleEle = True
                    SingleMu = False
                else:
                    GoodLep = GoodMu
                    lepton_TightRegion = copy.deepcopy(mu_TightRegion)
                    SingleMu = True
                    SingleEle = False
         
            else:
                continue

        else:
            continue

    vTrigEle, vTrigMu, vTrigHT = trig_finder(HLT, sample.year, sample.label)
    
    if SingleEle==True:
        if isMC: 
            HLT_effLumi = lumiFinder("Ele", vTrigEle, sample.year)
        leptons = electrons
    elif SingleMu==True:
        if isMC:
            HLT_effLumi = lumiFinder("Mu", vTrigMu, sample.year)
        leptons = muons

    elif not (SingleMu or SingleEle):
        continue

    if SingleEle and dataMu:
        continue
    if SingleMu and dataEle:
        continue
   
    if GoodLep==None or (lepton_TightRegion < 1):
        if Debug:
            print("exiting at lepton selection (without saving)")
        continue
    '''

    ######################################
    ## Selecting only jets with pt>30  ##
    ######################################
    goodJets = get_Jet(jets, 30)
    bjets, nobjets = bjet_filter(goodJets, 'DeepFlv', 'M')

    if (len(goodJets) < 2 or len(fatjets) < 2):
        continue

    for jet in goodJets:
        if(abs(jet.partonFlavour) == 5):
            h2_BTaggingEff_Denom_b.Fill(jet.pt, abs(jet.eta))
            if(len(bjet_filter([jet], 'DeepFlv', 'M')[0])==1):
                h2_BTaggingEff_Num_b.Fill(jet.pt, abs(jet.eta))
        elif(abs(jet.partonFlavour) == 4):
            h2_BTaggingEff_Denom_c.Fill(jet.pt, abs(jet.eta))
            if(len(bjet_filter([jet], 'DeepFlv', 'M')[0])==1):
                h2_BTaggingEff_Num_c.Fill(jet.pt, abs(jet.eta))
        else:
            h2_BTaggingEff_Denom_udsg.Fill(jet.pt, abs(jet.eta))
            if(len(bjet_filter([jet], 'DeepFlv', 'M')[0])==1):
                h2_BTaggingEff_Num_udsg.Fill(jet.pt, abs(jet.eta))

outTreeFile.cd()
h2_BTaggingEff_Denom_b.Write()
h2_BTaggingEff_Denom_c.Write()
h2_BTaggingEff_Denom_udsg.Write()
h2_BTaggingEff_Num_b.Write()
h2_BTaggingEff_Num_c.Write()
h2_BTaggingEff_Num_udsg.Write()

h2_Eff_b = ROOT.TEfficiency("h2_BTaggingEff_b", "bjet efficiency;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)
h2_Eff_b.SetTotalHistogram(h2_BTaggingEff_Denom_b, "")
h2_Eff_b.SetPassedHistogram(h2_BTaggingEff_Num_b, "")

h2_Eff_c = ROOT.TEfficiency("h2_BTaggingEff_c", "cjet efficiency;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)
h2_Eff_c.SetTotalHistogram(h2_BTaggingEff_Denom_c, "")
h2_Eff_c.SetPassedHistogram(h2_BTaggingEff_Num_c, "")

h2_Eff_udsg = ROOT.TEfficiency("h2_BTaggingEff_udsg", "light jet efficiency;p_{T} [GeV];#eta", nptbins, ptbins, netabins, etabins)
h2_Eff_udsg.SetTotalHistogram(h2_BTaggingEff_Denom_udsg, "")
h2_Eff_udsg.SetPassedHistogram(h2_BTaggingEff_Num_udsg, "")

h2_Eff_b.Write()
h2_Eff_c.Write()
h2_Eff_udsg.Write()

endTime = datetime.datetime.now()
print("Ending running at " + str(endTime))
