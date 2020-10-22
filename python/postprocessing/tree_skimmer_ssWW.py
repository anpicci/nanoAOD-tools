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
from skimtree_utils import *

if sys.argv[4] == 'remote':
    from samples import *
    Debug = False
else:
    from samples.samples import *
    Debug = True
sample = sample_dict[sys.argv[1]]
part_idx = sys.argv[2]
file_list = list(map(str, sys.argv[3].strip('[]').split(',')))

MCReco = True
DeltaFilter = True
bjetSwitch = False # True #
startTime = datetime.datetime.now()
print("Starting running at " + str(startTime))

ROOT.gROOT.SetBatch()

leadingjet_ptcut = 150.

chain = ROOT.TChain('Events')
#print(chain)
for infile in file_list: 
    print("Adding %s to the chain" %(infile))
    chain.Add(infile)

print("Number of events in chain " + str(chain.GetEntries()))
print("Number of events in tree from chain " + str((chain.GetTree()).GetEntries()))
tree = InputTree(chain)
isMC = True
if ('Data' in sample.label):
    isMC = False

MCReco = MCReco * isMC

#++++++++++++++++++++++++++++++++++
#++   branching the new trees    ++
#++++++++++++++++++++++++++++++++++
outTreeFile = ROOT.TFile(sample.label+"_part"+str(part_idx)+".root", "RECREATE") # output file
trees = []
for i in range(10):
    trees.append(None)
#systZero = systWeights()
# defining the operations to be done with the systWeights class
maxSysts = 0
addPDF = True
addQ2 = False
addTopPt = False
addVHF = False
addTTSplit = False
addTopTagging = False
addWTagging = False
addTrigSF = False
nPDF = 0

systTree = systWeights()
systTree.prepareDefault(True, addQ2, addPDF, addTopPt, addVHF, addTTSplit)
systTree.addSelection("all")
systTree.initTreesSysts(trees, outTreeFile)

systTree.setWeightName("w_nominal",1.)
systTree.setWeightName("puSF",1.)
systTree.setWeightName("puUp",1.)
systTree.setWeightName("puDown",1.)
systTree.setWeightName("lepSF",1.)
systTree.setWeightName("lepUp",1.)
systTree.setWeightName("lepDown",1.)
systTree.setWeightName("PFSF",1.)
systTree.setWeightName("PFUp",1.)
systTree.setWeightName("PFDown",1.)


#++++++++++++++++++++++++++++++++++
#++     variables to branch      ++
#++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++++++++
#++         All category         ++
#++++++++++++++++++++++++++++++++++

#ssWW variables

#lepton variables
lepton_pt               =   array.array('f', [0.])
lepton_eta              =   array.array('f', [0.])
lepton_phi              =   array.array('f', [0.])
lepton_mass             =   array.array('f', [0.])
lepton_pdgid            =   array.array('i', [0])
lepton_pfRelIso03       =   array.array('f', [0.])

#tau variables
tau_pt                  =   array.array('f', [0.])
tau_eta                 =   array.array('f', [0.])
tau_phi                 =   array.array('f', [0.])
tau_charge              =   array.array('i', [0])
tau_mass                =   array.array('f', [0.])
tau_DeepTau_discr       =   array.array('f', [0.])
tau_HPS_discr           =   array.array('i', [0])

#jet variables
Leadjet_pt                  =   array.array('f', [0.])
Leadjet_eta                 =   array.array('f', [0.])
Leadjet_phi                 =   array.array('f', [0.])
Leadjet_mass                =   array.array('f', [0.])
Leadjet_CSVv2_b             =   array.array('f', [0.])
Leadjet_DeepFlv_b           =   array.array('f', [0.])
Leadjet_DeepCSVv2_b         =   array.array('f', [0.])

Subleadjet_pt               =   array.array('f', [0.])
Subleadjet_eta              =   array.array('f', [0.])
Subleadjet_phi              =   array.array('f', [0.])
Subleadjet_mass             =   array.array('f', [0.])
Subleadjet_CSVv2_b          =   array.array('f', [0.])
Subleadjet_DeepFlv_b        =   array.array('f', [0.])
Subleadjet_DeepCSVv2_b      =   array.array('f', [0.])

#MET
MET_pt                      =   array.array('f', [0.])
MET_eta                     =   array.array('f', [0.])
MET_phi                     =   array.array('f', [0.])
MET_mass                    =   array.array('f', [0.])


#cut variables
pass_lepton_selection       =   array.array('b', [False])
pass_lepton_veto            =   array.array('b', [False])
pass_tau_selection          =   array.array('b', [False])
pass_charge_selection       =   array.array('b', [False])
pass_jet_selection          =   array.array('b', [False])
pass_b_veto                 =   array.array('b', [False])
pass_mjj_cut                =   array.array('b', [False])
pass_MET_cut                =   array.array('b', [False])


w_PDF_all = array.array('f', [0.]*110) #capisci a cosa serve
w_nominal_all = array.array('f', [0.])



#branches added for ssWW analysis
#lepton
systTree.branchTreesSysts(trees, "all", "lepton_pt",            outTreeFile, lepton_pt)
systTree.branchTreesSysts(trees, "all", "lepton_eta",           outTreeFile, lepton_eta)
systTree.branchTreesSysts(trees, "all", "lepton_phi",           outTreeFile, lepton_phi)
systTree.branchTreesSysts(trees, "all", "lepton_mass",          outTreeFile, lepton_mass)
systTree.branchTreesSysts(trees, "all", "lepton_pdgid",         outTreeFile, lepton_pdgid)
systTree.branchTreesSysts(trees, "all", "lepton_pfRelIso03",    outTreeFile, lepton_pfRelIso03)
#tau variables
systTree.branchTreesSysts(trees, "all", "tau_pt",               outTreeFile, tau_pt)
systTree.branchTreesSysts(trees, "all", "tau_eta",              outTreeFile, tau_eta)
systTree.branchTreesSysts(trees, "all", "tau_phi",              outTreeFile, tau_phi)
systTree.branchTreesSysts(trees, "all", "tau_mass",             outTreeFile, tau_mass)
#jet variables
systTree.branchTreesSysts(trees, "all", "Leadjet_pt",           outTreeFile, Leadjet_pt)
systTree.branchTreesSysts(trees, "all", "Leadjet_eta",          outTreeFile, Leadjet_eta)
systTree.branchTreesSysts(trees, "all", "Leadjet_phi",          outTreeFile, Leadjet_phi)
systTree.branchTreesSysts(trees, "all", "Leadjet_mass",         outTreeFile, Leadjet_mass)
systTree.branchTreesSysts(trees, "all", "Leadjet_CSVv2_b",      outTreeFile, Leadjet_CSVv2_b)
systTree.branchTreesSysts(trees, "all", "Leadjet_DeepFlv_b",    outTreeFile, Leadjet_DeepFlv_b)
systTree.branchTreesSysts(trees, "all", "Leadjet_DeepCSVv2_b",  outTreeFile, Leadjet_DeepCSVv2_b)

systTree.branchTreesSysts(trees, "all", "Subleadjet_pt",           outTreeFile, Subleadjet_pt)
systTree.branchTreesSysts(trees, "all", "Subleadjet_eta",          outTreeFile, Subleadjet_eta)
systTree.branchTreesSysts(trees, "all", "Subleadjet_phi",          outTreeFile, Subleadjet_phi)
systTree.branchTreesSysts(trees, "all", "Subleadjet_mass",         outTreeFile, Subleadjet_mass)
systTree.branchTreesSysts(trees, "all", "Subleadjet_CSVv2_b",      outTreeFile, Subleadjet_CSVv2_b)
systTree.branchTreesSysts(trees, "all", "Subleadjet_DeepFlv_b",    outTreeFile, Subleadjet_DeepFlv_b)
systTree.branchTreesSysts(trees, "all", "Subleadjet_DeepCSVv2_b",  outTreeFile, Subleadjet_DeepCSVv2_b)

#MET

systTree.branchTreesSysts(trees, "all", "MET_pt",               outTreeFile, MET_pt)
systTree.branchTreesSysts(trees, "all", "MET_eta",              outTreeFile, MET_eta)
systTree.branchTreesSysts(trees, "all", "MET_phi",              outTreeFile, MET_phi)
systTree.branchTreesSysts(trees, "all", "MET_mass",             outTreeFile, MET_mass)

#cut variables
systTree.branchTreesSysts(trees, "all", "pass_lepton_selection",    outTreeFile, pass_lepton_selection)
systTree.branchTreesSysts(trees, "all", "pass_lepton_veto",         outTreeFile, pass_lepton_veto)
systTree.branchTreesSysts(trees, "all", "pass_tau_selection",       outTreeFile, pass_tau_selection)
systTree.branchTreesSysts(trees, "all", "pass_charge_selection",    outTreeFile, pass_charge_selection)
systTree.branchTreesSysts(trees, "all", "pass_jet_selection",       outTreeFile, pass_jet_selection)
systTree.branchTreesSysts(trees, "all", "pass_b_veto",              outTreeFile, pass_b_veto)
systTree.branchTreesSysts(trees, "all", "pass_mjj_cut",             outTreeFile, pass_mjj_cut)
systTree.branchTreesSysts(trees, "all", "pass_MET_cut",             outTreeFile, pass_MET_cut)


#print("Is MC: " + str(isMC) + "      option addPDF: " + str(addPDF))
if(isMC and addPDF):
    systTree.branchTreesSysts(trees, "all", "w_PDF", outTreeFile, w_PDF_all)
if('TT_' in sample.label): 
    systTree.branchTreesSysts(trees, "all", "nlep", outTreeFile, nlep_all)
####################################################################################################################################################################################################################################

#++++++++++++++++++++++++++++++++++
#++      taking MC weights       ++
#++++++++++++++++++++++++++++++++++
print("isMC: ", isMC)
if(isMC):
    h_genweight = ROOT.TH1F()
    h_genweight.SetNameTitle('h_genweight', 'h_genweight')
    h_PDFweight = ROOT.TH1F()
    h_PDFweight.SetNameTitle("h_PDFweight","h_PDFweight")
    for infile in file_list: 
        #if Debug:
            #print(infile)
            #print("entered file_list loop #3")    
            #print("Getting the histos from %s" %(infile))
        newfile = ROOT.TFile.Open(infile)
        dirc = ROOT.TDirectory()
        dirc = newfile.Get("plots")
        #h_genw_tmp = ROOT.TH1F(dirc.Get("h_genweight"))
        #if Debug:
            #print("in newfile: ")
            #dirc.Get("h_genweight").Print()
            #print("in macro: ")
            #h_genw_tmp.Print()
        
        #if(dirc.GetListOfKeys().Contains("h_PDFweight")):
        #    h_pdfw_tmp = ROOT.TH1F(dirc.Get("h_PDFweight"))

       #     if(ROOT.TH1F(h_PDFweight).Integral() < 1.):
        #        h_PDFweight.SetBins(h_pdfw_tmp.GetXaxis().GetNbins(), h_pdfw_tmp.GetXaxis().GetXmin(), h_pdfw_tmp.GetXaxis().GetXmax())
        #        print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(ROOT.TH1F(dirc.Get("h_genweight")).GetBinContent(1), ROOT.TH1F(dirc.Get("h_PDFweight")).GetNbinsX()))
        #    h_PDFweight.Add(h_pdfw_tmp)
        #else:
        #    addPDF = False
        #if(ROOT.TH1F(h_genweight).Integral() < 1.):
        #    h_genweight.SetBins(h_genw_tmp.GetXaxis().GetNbins(), h_genw_tmp.GetXaxis().GetXmin(), h_genw_tmp.GetXaxis().GetXmax())
        #h_genweight.Add(h_genw_tmp)
    #print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(h_genweight.GetBinContent(1), h_PDFweight.GetNbinsX()))


#++++++++++++++++++++++++++++++++++
#++      Efficiency studies      ++
#++++++++++++++++++++++++++++++++++
neutrino_failed = 0
nrecochi = 0
nrecoclosest = 0
nrecosublead = 0
nrecobest = 0
nbinseff = 10
h_eff_mu = ROOT.TH1D("h_eff_mu", "h_eff_mu", nbinseff, 0, nbinseff)
h_eff_ele = ROOT.TH1D("h_eff_ele", "h_eff_ele", nbinseff, 0, nbinseff)
#++++++++++++++++++++++++++++++++++
#++   looping over the events    ++
#++++++++++++++++++++++++++++++++++
for i in range(tree.GetEntries()):
    w_nominal_all[0] = 1.
    #++++++++++++++++++++++++++++++++++
    #++        taking objects        ++
    #++++++++++++++++++++++++++++++++++
    if Debug:
        #print("evento n. " + str(i))
        if i > 2000:
            break
    
    if not Debug and i%5000 == 0:
        print("Event #", i+1, " out of ", tree.GetEntries())
    event = Event(tree,i)
    electrons = Collection(event, "Electron")
    muons = Collection(event, "Muon")
    jets = Collection(event, "Jet")
    njets = len(jets)
    fatjets = Collection(event, "FatJet")
    HT = Object(event, "HT")
    PV = Object(event, "PV")
    HLT = Object(event, "HLT")
    Flag = Object(event, 'Flag')
    met = Object(event, "MET")
    MET = {'metPx': met.pt*ROOT.TMath.Cos(met.phi), 'metPy': met.pt*ROOT.TMath.Sin(met.phi)}
    genpart = None
    
    h_eff_mu.Fill('Total', 1)
    h_eff_ele.Fill('Total', 1)
    if isMC:
        genpart = Collection(event, "GenPart")
        LHE = Collection(event, "LHEPart")
    chain.GetEntry(i)
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
    VetoMu = get_LooseMu(muons)
    goodMu = get_Mu(muons)
    VetoEle = get_LooseEle(electrons)
    goodEle = get_Ele(electrons)
    year = sample.year
    if(isMC):
        runPeriod = None
    else:
        runPeriod = sample.runP
    passMu, passEle, noTrigger = trig_map(HLT, year, runPeriod)
    isDilepton = False
    isMuon = (len(goodMu) == 1) and (len(goodEle) == 0) and len(VetoMu) == 0 and len(VetoEle) == 0 and (passMu)
    isElectron = (len(goodMu) == 0) and (len(goodEle) == 1) and len(VetoMu) == 0 and len(VetoEle) == 0 and (passEle)

    doublecounting = True
    if(isMC):
        doublecounting = False
    #Double counting removal
    if('DataMu' in sample.label and passMu):
        doublecounting = False
    if('DataEle' in sample.label and (not passMu and passEle)):
        doublecounting = False

    if doublecounting:
        continue

    SingleEle=False
    SingleMu=False
    ElMu=False

    HighestLepPt=-999
    LeadLepFamily="not selected"
    
    if passEle and not HLT.Ele32_WPTight_Gsf_L1DoubleEG: print "Errore"
    if passEle and not passMu:  
        print i
        print passEle, passMu, len(electrons)
        SingleEle=True
        LeadLepFamily="electrons"
        HighestLepPt=electrons[0].pt

    if passMu and not passEle:
        SingleMu=True
        LeadLepFamilu="muons"
        HighestLepPt=muons[0].pt

    if passMu and passEle:
        ElMu=True


    if ElMu:
        for mu in muons:
            if mu.pt>HighestLepPt:
                HighestLepPt=mu.pt
        for ele in electrons:
            if ele.pt>HighestLepPt:
                SingleEle=True
                break
        if SingleEle==False and HighestLepPt>0: SingleMu=True

    
    if SingleEle==True: leptons=electrons
    if SingleMu==True:  leptons=muons




    #######################################
    ## Removing events with HEM problem  ##
    #######################################
    passesMETHEMVeto = HEMveto(jets, electrons)
    if(sample.year == 2018 and not passesMETHEMVeto):
        if(not isMC and chain.run > 319077.):
            continue
        elif(isMC):
            w_nominal_all[0] *= 0.354

    if len(goodMu) == 1:
        h_eff_mu.Fill('Good Mu', 1)
        if len(goodEle) == 0:
            h_eff_mu.Fill('Good Ele', 1)
        if len(VetoMu) == 0:
            h_eff_mu.Fill('Veto Mu', 1)
        if len(VetoEle) == 0:
            h_eff_mu.Fill('Veto Ele', 1)
    if len(goodEle) == 1:
        h_eff_ele.Fill('Good Ele', 1)
        if len(goodMu) == 0:
            h_eff_ele.Fill('Good Mu', 1)
        if len(VetoMu) == 0:
            h_eff_ele.Fill('Veto Mu', 1)
        if len(VetoEle) == 0:
            h_eff_ele.Fill('Veto Ele', 1)


    systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
    systTree.fillTreesSysts(trees, "all")

#if Debug:
    #print("Event with neutrino failed: ", neutrino_failed, " out of ", str(50000))
#else:
    #print("Event with neutrino failed: ", neutrino_failed, " out of ", tree.GetEntries())

#trees[0].Print()
outTreeFile.cd()
if(isMC):
    #print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(h_genweight.GetBinContent(1), h_PDFweight.GetNbinsX()))
    h_genweight.Write()
    h_PDFweight.Write()
    h_eff_mu.Write()
    h_eff_ele.Write()
systTree.writeTreesSysts(trees, outTreeFile)
print("Number of events in output tree " + str(trees[0].GetEntries()))

endTime = datetime.datetime.now()
print("Ending running at " + str(endTime))
