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
from skimtree_utils_ssWW_wFakes_bu import *
from TauIDSFTool import TauIDSFTool, TauESTool, TauFESTool, campaigns
from EFTOperator_dict import *

dim8_points = [
    "20",
    "10",
    "0",
]

vsJet = {"VVVL": 'VVVLoose',
         "VVL": 'VVLoose',
         "VL": 'VLoose',
         "L": 'Loose',
         "M": 'Medium',
         "T": 'Tight',
         "VT": 'VTight',
         "VVT": 'VVTight',
}

vsMu = {"VL": 'VLoose',
        "L": 'Loose',
        "M": 'Medium',
        "T": 'Tight'
}

vsEle = {"VVVL": 'VVVLoose',
         "VVL": 'VVLoose',
         "VL": 'VLoose',
         "L": 'Loose',
         "M": 'Medium',
         "T": 'Tight',
         "VT": 'VTight',
         "VVT": 'VVTight',
}

usage = "python tree_skimmer_ssWW_wFakes.py [nome_del_sample_in_samples.py] 0 [file_in_input] local wpvsjet wpvsele wpvsmu"

if sys.argv[4] == 'remote':
    from samples import *
    Debug = False
else:
    from samples.samples import *
    Debug = True
sample = sample_dict[sys.argv[1]]
part_idx = sys.argv[2]
file_list = list(map(str, sys.argv[3].strip('[]').split(',')))
print(file_list)

vsjetWP = vsJet[sys.argv[5]]
vseleWP = vsEle[sys.argv[6]]
vsmuWP = vsMu[sys.argv[7]]

act_camp = ''
for cam in campaigns:
    if str(sample.year) in cam:
        act_camp = copy.deepcopy(cam)
        break

#print(cam, vsjetWP, vseleWP, vsmuWP)
tauSFTool_vsjet = TauIDSFTool(act_camp, 'DeepTau2017v2p1VSjet', vsjetWP)
tauSFTool_vsele = TauIDSFTool(act_camp, 'DeepTau2017v2p1VSe', vseleWP)
tauSFTool_vsmu = TauIDSFTool(act_camp, 'DeepTau2017v2p1VSmu', vsmuWP)
tesTool = TauESTool(act_camp, 'DeepTau2017v2p1VSjet')
fesTool = TauFESTool(act_camp, 'DeepTau2017v2p1VSe')

MCReco = True
startTime = datetime.datetime.now()
print("Starting running at " + str(startTime))

ROOT.gROOT.SetBatch()

chain = ROOT.TChain('Events')
#print(chain)
for infile in file_list: 
    print("Adding %s to the chain" %(infile))
    chain.Add(infile)


print(chain)

print("Number of events in chain " + str(chain.GetEntries()))
print("Number of events in tree from chain " + str((chain.GetTree()).GetEntries()))
tree = InputTree(chain)
isMC = True
if ('Data' in sample.name):
    isMC = False

MCReco = MCReco * isMC

IsDim8 = False
if 'aQGC' in sample.name:
    IsDim8 = True

dataEle = False
dataMu = False
if 'DataMu' in sample.name:
    dataMu = True
if 'DataEle' in sample.name:
    dataEle = True


#Cut_dict = {}

#if Debug:
#Cut_dict = {1: ['Trigger             ', 0, 0.0, 0.0, 0.0, 0.0],
#2: ['Lepton selection    ', 0, 0.0, 0.0, 0.0, 0.0],
#            3: ['Lepton Veto         ', 0, 0.0, 0.0, 0.0, 0.0],
#            4: ['Tau selection       ', 0, 0.0, 0.0, 0.0, 0.0],
#            5: ['Same charge tau lep ', 0, 0.0, 0.0, 0.0, 0.0],
#            6: ['Jet Selection       ', 0, 0.0, 0.0, 0.0, 0.0],
#            7: ['BVeto               ', 0, 0.0, 0.0, 0.0, 0.0],
#            8: ['M_jj>500 GeV        ', 0, 0.0, 0.0, 0.0, 0.0],
#            9: ['MET>40 GeV          ', 0, 0.0, 0.0, 0.0, 0.0],
#}

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
systTree.setWeightName("tau_vsjet_SF",1.)
systTree.setWeightName("tau_vsjet_Up",1.)
systTree.setWeightName("tau_vsjet_Down",1.)
systTree.setWeightName("tau_vsele_SF",1.)
systTree.setWeightName("tau_vsele_Up",1.)
systTree.setWeightName("tau_vsele_Down",1.)
systTree.setWeightName("tau_vsmu_SF",1.)
systTree.setWeightName("tau_vsmu_Up",1.)
systTree.setWeightName("tau_vsmu_Down",1.)
systTree.setWeightName("tauSF",1.)
systTree.setWeightName("tauUp",1.)
systTree.setWeightName("tauDown",1.)
systTree.setWeightName("TESSF",1.)
systTree.setWeightName("TESUp",1.)
systTree.setWeightName("TESDown",1.)
systTree.setWeightName("FESSF",1.)
systTree.setWeightName("FESUp",1.)
systTree.setWeightName("FESDown",1.)
systTree.setWeightName("btagSF",1.)
systTree.setWeightName("btagUp",1.)
systTree.setWeightName("btagDown",1.)
systTree.setWeightName("mistagUp",1.)
systTree.setWeightName("mistagDown",1.)


#++++++++++++++++++++++++++++++++++
#++     variables to branch      ++
#++++++++++++++++++++++++++++++++++
var_list = []
#++++++++++++++++++++++++++++++++++
#++        dim8 operator         ++
#++++++++++++++++++++++++++++++++++

if IsDim8:
    w_dim8             =   array.array('f', [-999.])
    w_neg              =   array.array('f', [-999.])
    w_pos              =   array.array('f', [-999.])
    var_list.append(w_dim8)
    var_list.append(w_neg)
    var_list.append(w_pos)
    
#++++++++++++++++++++++++++++++++++
#++         All category         ++
#++++++++++++++++++++++++++++++++++

nJets                       =   array.array('f', [-999.])#
nGenJets                    =   array.array('f', [-999.])#
nBJets                      =   array.array('f', [-999.])#
var_list.append(nJets)#
var_list.append(nGenJets)#
var_list.append(nBJets)#

#jet#
leadjet_pt                  =   array.array('f', [-999.])
leadjet_eta                 =   array.array('f', [-999.])
leadjet_phi                 =   array.array('f', [-999.])
leadjet_mass                =   array.array('f', [-999.])
leadjet_DeepFlv_b           =   array.array('f', [-999.])
leadjet_partonFlavour       =   array.array('f', [-999.])
leadjet_IsGenMatched       =   array.array('f', [-999.])

var_list.append(leadjet_pt)
var_list.append(leadjet_eta)
var_list.append(leadjet_phi)
var_list.append(leadjet_mass)
var_list.append(leadjet_DeepFlv_b)
var_list.append(leadjet_partonFlavour)
var_list.append(leadjet_IsGenMatched)

mleadjet_pt                  =   array.array('f', [-999.])
mleadjet_eta                 =   array.array('f', [-999.])
mleadjet_phi                 =   array.array('f', [-999.])
mleadjet_mass                =   array.array('f', [-999.])
mleadjet_DeepFlv_b           =   array.array('f', [-999.])
mleadjet_partonFlavour       =   array.array('f', [-999.])
mleadjet_IsGenMatched           =   array.array('f', [-999.])

var_list.append(mleadjet_pt)
var_list.append(mleadjet_eta)
var_list.append(mleadjet_phi)
var_list.append(mleadjet_mass)
var_list.append(mleadjet_DeepFlv_b)
var_list.append(mleadjet_partonFlavour)
var_list.append(mleadjet_IsGenMatched)

genjet1_pt                  =   array.array('f', [-999.])
genjet1_eta                 =   array.array('f', [-999.])
genjet1_phi                 =   array.array('f', [-999.])
genjet1_mass                =   array.array('f', [-999.])
genjet1_partonFlavour       =   array.array('f', [-999.])

var_list.append(genjet1_pt)
var_list.append(genjet1_eta)
var_list.append(genjet1_phi)
var_list.append(genjet1_mass)
var_list.append(genjet1_partonFlavour)

gmleadjet_pt                  =   array.array('f', [-999.])
gmleadjet_eta                 =   array.array('f', [-999.])
gmleadjet_phi                 =   array.array('f', [-999.])
gmleadjet_mass                =   array.array('f', [-999.])
gmleadjet_DeepFlv_b           =   array.array('f', [-999.])
gmleadjet_partonFlavour       =   array.array('f', [-999.])
gmleadjet_IsGenMatched           =   array.array('f', [-999.])

var_list.append(gmleadjet_pt)
var_list.append(gmleadjet_eta)
var_list.append(gmleadjet_phi)
var_list.append(gmleadjet_mass)
var_list.append(gmleadjet_DeepFlv_b)
var_list.append(gmleadjet_partonFlavour)
var_list.append(gmleadjet_IsGenMatched)

subleadjet_pt               =   array.array('f', [-999.])
subleadjet_eta              =   array.array('f', [-999.])
subleadjet_phi              =   array.array('f', [-999.])
subleadjet_mass             =   array.array('f', [-999.])
subleadjet_DeepFlv_b        =   array.array('f', [-999.])
subleadjet_partonFlavour        =   array.array('f', [-999.])
subleadjet_IsGenMatched        =   array.array('f', [-999.])

var_list.append(subleadjet_pt)
var_list.append(subleadjet_eta)
var_list.append(subleadjet_phi)
var_list.append(subleadjet_mass)
var_list.append(subleadjet_DeepFlv_b)
var_list.append(subleadjet_partonFlavour)
var_list.append(subleadjet_IsGenMatched)

msubleadjet_pt               =   array.array('f', [-999.])
msubleadjet_eta              =   array.array('f', [-999.])
msubleadjet_phi              =   array.array('f', [-999.])
msubleadjet_mass             =   array.array('f', [-999.])
msubleadjet_DeepFlv_b        =   array.array('f', [-999.])
msubleadjet_partonFlavour    =   array.array('f', [-999.])
msubleadjet_IsGenMatched    =   array.array('f', [-999.])

var_list.append(msubleadjet_pt)
var_list.append(msubleadjet_eta)
var_list.append(msubleadjet_phi)
var_list.append(msubleadjet_mass)
var_list.append(msubleadjet_DeepFlv_b)
var_list.append(msubleadjet_partonFlavour)
var_list.append(msubleadjet_IsGenMatched)

genjet2_pt               =   array.array('f', [-999.])
genjet2_eta              =   array.array('f', [-999.])
genjet2_phi              =   array.array('f', [-999.])
genjet2_mass             =   array.array('f', [-999.])
genjet2_partonFlavour    =   array.array('f', [-999.])

var_list.append(genjet2_pt)
var_list.append(genjet2_eta)
var_list.append(genjet2_phi)
var_list.append(genjet2_mass)
var_list.append(genjet2_partonFlavour)

gmsubleadjet_pt               =   array.array('f', [-999.])
gmsubleadjet_eta              =   array.array('f', [-999.])
gmsubleadjet_phi              =   array.array('f', [-999.])
gmsubleadjet_mass             =   array.array('f', [-999.])
gmsubleadjet_partonFlavour    =   array.array('f', [-999.])
gmsubleadjet_DeepFlv_b    =   array.array('f', [-999.])
gmsubleadjet_IsGenMatched    =   array.array('f', [-999.])

var_list.append(gmsubleadjet_pt)
var_list.append(gmsubleadjet_eta)
var_list.append(gmsubleadjet_phi)
var_list.append(gmsubleadjet_mass)
var_list.append(gmsubleadjet_partonFlavour)
var_list.append(gmsubleadjet_DeepFlv_b)
var_list.append(gmsubleadjet_IsGenMatched)

#inv and transv masses
m_jj                        =   array.array('f', [-999.])
var_list.append(m_jj)

#deltaPhi#                                                                      
deltaPhi_jj                 =   array.array('f', [-999.])#
var_list.append(deltaPhi_jj)#

#deltaTheta
deltaTheta_jj                 =   array.array('f', [-999.])#
var_list.append(deltaTheta_jj)#

#ptRel
ptRel_jj                 =   array.array('f', [-999.])#
var_list.append(ptRel_jj)#

HLT_effLumi                 =   array.array('f', [-999.])
var_list.append(HLT_effLumi)

#deltaEta#                                                                      
deltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(deltaEta_jj)#

#cut variables
pass_lepton_selection       =   array.array('i', [0])
pass_lepton_iso             =   array.array('i', [0])
pass_lepton_veto            =   array.array('i', [0])
pass_tau_selection          =   array.array('i', [0])
pass_tau_vsJetWP            =   array.array('i', [0])
pass_charge_selection       =   array.array('i', [0])
pass_jet_selection          =   array.array('i', [0])
pass_b_veto                 =   array.array('i', [0])
pass_mjj_cut                =   array.array('i', [0])
pass_MET_cut                =   array.array('i', [0])
pass_upToBVeto              =   array.array('i', [0])
#pass_upToBVeto_ML           =   array.array('i', [0])#
#pass_tau_selection_ML       =   array.array('i', [0])#
pass_everyCut               =   array.array('i', [0])
var_list.append(pass_lepton_selection)
var_list.append(pass_lepton_veto)
var_list.append(pass_lepton_iso)
var_list.append(pass_tau_selection)
#var_list.append(pass_tau_selection_ML)#
var_list.append(pass_tau_vsJetWP)
var_list.append(pass_charge_selection)
var_list.append(pass_jet_selection)
var_list.append(pass_b_veto)
var_list.append(pass_mjj_cut)
var_list.append(pass_MET_cut)
var_list.append(pass_upToBVeto)
#var_list.append(pass_upToBVeto_ML)#
var_list.append(pass_everyCut)

#weights#
w_PDF_all = array.array('f', [0.]*110)#
w_nominal_all = array.array('f', [0.])

#w_dim8
if IsDim8:
    systTree.branchTreesSysts(trees, "all", "w_dim8",            outTreeFile, w_dim8)
    systTree.branchTreesSysts(trees, "all", "w_pos",            outTreeFile, w_pos)
    systTree.branchTreesSysts(trees, "all", "w_neg",            outTreeFile, w_neg)
    
#branches added for ssWW analysis

#jet variables
systTree.branchTreesSysts(trees, "all", "leadjet_pt",           outTreeFile, leadjet_pt)
systTree.branchTreesSysts(trees, "all", "leadjet_eta",          outTreeFile, leadjet_eta)
systTree.branchTreesSysts(trees, "all", "leadjet_phi",          outTreeFile, leadjet_phi)
systTree.branchTreesSysts(trees, "all", "leadjet_mass",         outTreeFile, leadjet_mass)
systTree.branchTreesSysts(trees, "all", "leadjet_DeepFlv_b",    outTreeFile, leadjet_DeepFlv_b)
systTree.branchTreesSysts(trees, "all", "subleadjet_pt",           outTreeFile, subleadjet_pt)
systTree.branchTreesSysts(trees, "all", "subleadjet_eta",          outTreeFile, subleadjet_eta)
systTree.branchTreesSysts(trees, "all", "subleadjet_phi",          outTreeFile, subleadjet_phi)
systTree.branchTreesSysts(trees, "all", "subleadjet_mass",         outTreeFile, subleadjet_mass)
systTree.branchTreesSysts(trees, "all", "subleadjet_DeepFlv_b",    outTreeFile, subleadjet_DeepFlv_b)

systTree.branchTreesSysts(trees, "all", "genjet1_pt",           outTreeFile, genjet1_pt)
systTree.branchTreesSysts(trees, "all", "genjet1_eta",          outTreeFile, genjet1_eta)
systTree.branchTreesSysts(trees, "all", "genjet1_phi",          outTreeFile, genjet1_phi)
systTree.branchTreesSysts(trees, "all", "genjet1_mass",         outTreeFile, genjet1_mass)
systTree.branchTreesSysts(trees, "all", "genjet1_partonFlavour",      outTreeFile, genjet1_partonFlavour)
systTree.branchTreesSysts(trees, "all", "genjet2_pt",           outTreeFile, genjet2_pt)
systTree.branchTreesSysts(trees, "all", "genjet2_eta",          outTreeFile, genjet2_eta)
systTree.branchTreesSysts(trees, "all", "genjet2_phi",          outTreeFile, genjet2_phi)
systTree.branchTreesSysts(trees, "all", "genjet2_mass",         outTreeFile, genjet2_mass)
systTree.branchTreesSysts(trees, "all", "genjet2_partonFlavour",      outTreeFile, genjet2_partonFlavour)

systTree.branchTreesSysts(trees, "all", "nJets",  outTreeFile, nJets)
systTree.branchTreesSysts(trees, "all", "nGenJets",  outTreeFile, nGenJets)
systTree.branchTreesSysts(trees, "all", "nBJets", outTreeFile, nBJets)#

#masses
systTree.branchTreesSysts(trees, "all", "m_jj",                  outTreeFile, m_jj)
#deltaPhi#
systTree.branchTreesSysts(trees, "all", "deltaPhi_jj",              outTreeFile, deltaPhi_jj)#
#deltaEta#
systTree.branchTreesSysts(trees, "all", "deltaEta_jj",              outTreeFile, deltaEta_jj)#
#deltaTheta#
systTree.branchTreesSysts(trees, "all", "deltaTheta_jj",              outTreeFile, deltaTheta_jj)#
#ptRel#
systTree.branchTreesSysts(trees, "all", "ptRel_jj",              outTreeFile, ptRel_jj)#
#other                                                                                    
systTree.branchTreesSysts(trees, "all", "HLT_effLumi",              outTreeFile, HLT_effLumi)#
#zeppenfeld

#cut variables
systTree.branchTreesSysts(trees, "all", "pass_lepton_selection",    outTreeFile, pass_lepton_selection)
systTree.branchTreesSysts(trees, "all", "pass_lepton_iso",          outTreeFile, pass_lepton_iso)
systTree.branchTreesSysts(trees, "all", "pass_lepton_veto",         outTreeFile, pass_lepton_veto)
systTree.branchTreesSysts(trees, "all", "pass_tau_selection",       outTreeFile, pass_tau_selection)
systTree.branchTreesSysts(trees, "all", "pass_tau_vsJetWP",         outTreeFile, pass_tau_vsJetWP)
systTree.branchTreesSysts(trees, "all", "pass_charge_selection",    outTreeFile, pass_charge_selection)
systTree.branchTreesSysts(trees, "all", "pass_jet_selection",       outTreeFile, pass_jet_selection)
systTree.branchTreesSysts(trees, "all", "pass_b_veto",              outTreeFile, pass_b_veto)
systTree.branchTreesSysts(trees, "all", "pass_mjj_cut",             outTreeFile, pass_mjj_cut)
systTree.branchTreesSysts(trees, "all", "pass_MET_cut",             outTreeFile, pass_MET_cut)
systTree.branchTreesSysts(trees, "all", "pass_upToBVeto",           outTreeFile, pass_upToBVeto)

systTree.branchTreesSysts(trees, "all", "pass_everyCut",            outTreeFile, pass_everyCut)

if(isMC and addPDF):
    systTree.branchTreesSysts(trees, "all", "w_PDF", outTreeFile, w_PDF_all)
####################################################################################################################################################################################################################################

#++++++++++++++++++++++++++++++++++
#++      taking MC weights       ++
#++++++++++++++++++++++++++++++++++
print("isMC: ", isMC)
if(isMC):
    newfile = ROOT.TFile.Open(file_list[0])
    dirc = ROOT.TDirectory()
    dirc = newfile.Get("plots")
    isthere_gen = bool(dirc.GetListOfKeys().Contains("h_genweight"))
    isthere_pdf = bool(dirc.GetListOfKeys().Contains("h_PDFweight"))
    print("gen?: ", isthere_gen, " pdf?: ", isthere_pdf)

    if isthere_gen or isthere_pdf:
        if isthere_gen:
            h_genweight = ROOT.TH1F()
            h_genweight.SetNameTitle('h_genweight', 'h_genweight')
            h_genw_tmp = ROOT.TH1F(dirc.Get("h_genweight"))
            if(ROOT.TH1F(h_genweight).Integral() < 1.):
                h_genweight.SetBins(h_genw_tmp.GetXaxis().GetNbins(), h_genw_tmp.GetXaxis().GetXmin(), h_genw_tmp.GetXaxis().GetXmax())
            h_genweight.Add(h_genw_tmp)
    
        if isthere_pdf:
            h_PDFweight = ROOT.TH1F()
            h_PDFweight.SetNameTitle("h_PDFweight","h_PDFweight")
            h_pdfw_tmp = ROOT.TH1F(dirc.Get("h_PDFweight"))
            if(ROOT.TH1F(h_PDFweight).Integral() < 1.):
                h_PDFweight.SetBins(h_pdfw_tmp.GetXaxis().GetNbins(), h_pdfw_tmp.GetXaxis().GetXmin(), h_pdfw_tmp.GetXaxis().GetXmax())
            h_PDFweight.Add(h_pdfw_tmp)
        else:
            addPDF = False
    newfile.Close()

contagood=0
#++++++++++++++++++++++++++++++++++
#++   looping over the events    ++
#++++++++++++++++++++++++++++++++++

for i in range(tree.GetEntries()):
    #reinizializza tutte le variabili a 0, per sicurezza
    for j, var in enumerate(var_list):
        if j<len(var_list)-12:#
            var_list[j][0] = -999
        else:
            var_list[j][0] = 0
    SF_Fake[0]=1

    w_nominal_all[0] = 1.
    #++++++++++++++++++++++++++++++++++
    #++        taking objects        ++
    #++++++++++++++++++++++++++++++++++
    
    if Debug:
        print("\nevento n. " + str(i))
        if i > tree.GetEntries():#1000:
            break
    
    else:
        if (i+1)%1000 == 0 and i!=0:
            print("Event #", i+1, " out of ", tree.GetEntries())

    if i%(tree.GetEntries()) == 0:
        print("Last event being processed (#" + str(i+1))

    event       = Event(tree,i)
    electrons   = Collection(event, "Electron")
    muons       = Collection(event, "Muon")
    jets        = Collection(event, "Jet")
    njets       = len(jets)
    fatjets     = Collection(event, "FatJet")
    taus        = Collection(event, "Tau")
    HT          = Object(event, "HT")
    PV          = Object(event, "PV")
    HLT         = Object(event, "HLT")
    Flag        = Object(event, 'Flag')
    met         = Object(event, "PuppiMET")
    genjets     = Collection(event, "GenJet")
    genpart     = None
    
    if isMC:
        genpart = Collection(event, "GenPart")
        if not ("WZ" in sample.label or "WWTo2L2Nu_DoubleScattering"):
            LHE = Collection(event, "LHEPart")
        if IsDim8:
            LHEDim8 = Collection(event, "LHEReweightingWeight")

    chain.GetEntry(i)
    #++++++++++++++++++++++++++++++++++
    #++      defining variables      ++
    #++++++++++++++++++++++++++++++++++
    tightlep = None
    tightlep_p4 = None
    tightlep_p4t = None
    recomet_p4t = None
    #++++++++++++++++++++++++++++++++++
    #++    starting the analysis     ++
    #++++++++++++++++++++++++++++++++++

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

    if noTrigger: continue

    genjet1, genjet2 = SelectVBSQGenJet(genjets)

    genjet1_pt[0]               =   jet1.pt
    genjet1_eta[0]              =   jet1.eta
    genjet1_phi[0]              =   jet1.phi
    genjet1_mass[0]             =   jet1.mass
    genjet1_partonFlavour[0]    =   jet1.partonFlavour
    genjet2_pt[0]            =   jet2.pt
    genjet2_eta[0]           =   jet2.eta
    genjet2_phi[0]           =   jet2.phi
    genjet2_mass[0]          =   jet2.mass
    genjet2_partonFlavour[0]     =   jet2.partonFlavour
    
    indexGoodEle, ele_TightRegion = SelectLepton(electrons, False) 
    indexGoodMu, mu_TightRegion = SelectLepton(muons, True) 
 
    if indexGoodEle < 0 and indexGoodMu < 0:
        continue

    ele_lepton_veto = -1
    mu_lepton_veto = -1

    if indexGoodEle >= 0:
        ele_lepton_veto = LepVeto(electrons[indexGoodEle], electrons, muons)
    if indexGoodMu >= 0:
        mu_lepton_veto = LepVeto(muons[indexGoodMu], electrons, muons)

    SingleEle=False
    SingleMu=False
    ElMu=False

    LeadLepFamily="not selected"
    
    indexGoodLep = -1
    leptons = None

    if 'DataHT' not in sample.label:
        if passEle and not passMu:
            if indexGoodEle>=0 and ele_lepton_veto:
                indexGoodLep = copy.deepcopy(indexGoodEle)
                lepton_TightRegion[0] = copy.deepcopy(ele_TightRegion)
                SingleEle = True
                SingleMu = False
            else:
                continue

        elif passMu and not passEle:
            if indexGoodMu>=0 and mu_lepton_veto:
                indexGoodLep = copy.deepcopy(indexGoodMu)
                lepton_TightRegion[0] = copy.deepcopy(mu_TightRegion)
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
        if indexGoodMu<0 and indexGoodEle>=0 and ele_lepton_veto:
            indexGoodLep = copy.deepcopy(indexGoodEle)
            lepton_TightRegion[0] = copy.deepcopy(ele_TightRegion)
            SingleEle = True
            SingleMu = False

        elif indexGoodMu>=0 and mu_lepton_veto and indexGoodEle<0:
            indexGoodLep = copy.deepcopy(indexGoodMu)
            lepton_TightRegion[0] = copy.deepcopy(mu_TightRegion)
            SingleMu = True
            SingleEle = False
                
        elif indexGoodMu>=0 and indexGoodEle>=0:
            if ele_lepton_veto and not mu_lepton_veto:
                indexGoodLep = copy.deepcopy(indexGoodEle)
                lepton_TightRegion[0] = copy.deepcopy(ele_TightRegion)
                SingleEle = True
                SingleMu = False
            elif not ele_lepton_veto and mu_lepton_veto:            
                indexGoodLep = copy.deepcopy(indexGoodMu)
                lepton_TightRegion[0] = copy.deepcopy(mu_TightRegion)
                SingleMu = True
                SingleEle = False

            elif ele_lepton_veto and mu_lepton_veto:
                if electrons[indexGoodEle].pt > muons[indexGoodMu].pt:
                    indexGoodLep = copy.deepcopy(indexGoodEle)
                    lepton_TightRegion[0] = copy.deepcopy(ele_TightRegion)
                    SingleEle = True
                    SingleMu = False
                else:
                    indexGoodLep = copy.deepcopy(indexGoodMu)
                    lepton_TightRegion[0] = copy.deepcopy(mu_TightRegion)
                    SingleMu = True
                    SingleEle = False
         
            else:
                continue

        else:
            continue

    vTrigEle, vTrigMu, vTrigHT = trig_finder(HLT, sample.year, sample.label)
    
    if SingleEle==True:
        if isMC: 
            HLT_effLumi[0] = lumiFinder("Ele", vTrigEle)
        leptons = electrons
    elif SingleMu==True:
        if isMC:
            HLT_effLumi[0] = lumiFinder("Mu", vTrigMu)
        leptons = muons

    elif not (SingleMu or SingleEle):
        continue

    if SingleEle and dataMu:
        continue
    if SingleMu and dataEle:
        continue

    if lepton_TightRegion[0]==1:
        lepton_LnTRegion[0] = 0
    elif lepton_TightRegion[0]==0:
        lepton_LnTRegion[0] = 1
    else:
        lepton_LnTRegion[0] = -999
    
    if indexGoodLep<0 or indexGoodLep>=len(leptons) or (lepton_TightRegion[0]<0 and lepton_LnTRegion[0]<0): 
        #if Debug:
            #print("exiting at lepton selection (without saving)")
        continue

    if lepton_TightRegion[0]==1 or lepton_LnTRegion[0]==1:
        pass_lepton_selection[0] = 1
    else:
        pass_lepton_selection[0] = 0

    pass_lepton_veto[0] = 1

    GoodLep = leptons[indexGoodLep]

    ThereIsOneTau, ltau_list = SelectAndVetoTaus(list(taus), GoodLep)

    if ThereIsOneTau:
        indexGoodTau = ltau_list[0][0]
        if ltau_list[0][1] == 'T':
            tau_TightRegion[0] = 1
            tau_LnTRegion[0] = 0
        elif ltau_list[0][1] == 'L':
            tau_TightRegion[0] = 0
            tau_LnTRegion[0] = 1            
    else:
        continue

    GoodTau=taus[indexGoodTau]

    if tau_TightRegion[0]==1 or tau_LnTRegion[0]==1:
        pass_tau_selection[0] = 1
    else:
        pass_tau_selection[0] = 0
    
    if GoodTau.charge==GoodLep.charge:
        pass_charge_selection[0]=1

    nJets[0] = len(jets)
    nBJets[0] = CountBJets(jets)#
    nGenJets[0] = len(genjets)

    outputJetSel=SelectJet(list(jets), GoodTau, GoodLep)
    
    if outputJetSel==-999:
        #systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        #systTree.fillTreesSysts(trees, "all")
        #if Debug:
            #print("exiting at jet selection (without saving)")
        continue  

    jet1, jet2 = outputJetSel
    
    leadjet_pt[0]               =   jet1.pt
    leadjet_eta[0]              =   jet1.eta
    leadjet_phi[0]              =   jet1.phi
    leadjet_mass[0]             =   jet1.mass
    leadjet_DeepFlv_b[0]        =   jet1.btagDeepFlavB
    leadjet_DeepCSVv2_b[0]      =   jet1.btagDeepB
    leadjet_CSVv2_b[0]          =   jet1.btagCSVV2
    subleadjet_pt[0]            =   jet2.pt
    subleadjet_eta[0]           =   jet2.eta
    subleadjet_phi[0]           =   jet2.phi
    subleadjet_mass[0]          =   jet2.mass
    subleadjet_DeepFlv_b[0]     =   jet2.btagDeepFlavB
    subleadjet_DeepCSVv2_b[0]   =   jet2.btagDeepB
    subleadjet_CSVv2_b[0]       =   jet2.btagCSVV2
    
    pass_jet_selection[0]=1

    #calculating deltaPhi                                                                                                      
    deltaPhi_jj[0]      =   deltaPhi(jet1, jet2)#
    deltaPhi_taulep[0]  =   deltaPhi(GoodTau, GoodLep)#
    deltaPhi_tauj1[0]   =   deltaPhi(GoodTau, jet1)#
    deltaPhi_tauj2[0]   =   deltaPhi(GoodTau, jet2)#
    deltaPhi_lepj1[0]   =   deltaPhi(GoodLep, jet1)#
    deltaPhi_lepj2[0]   =   deltaPhi(GoodLep, jet2)#

    #calculating deltaEta                                                                                                      
    deltaEta_jj[0]      =   jet1.eta - jet2.eta#
    deltaEta_taulep[0]  =   GoodTau.eta - GoodLep.eta#
    deltaEta_tauj1[0]   =   GoodTau.eta - jet1.eta#
    deltaEta_tauj2[0]   =   GoodTau.eta - jet2.eta#
    deltaEta_lepj1[0]   =   GoodLep.eta - jet1.eta#
    deltaEta_lepj2[0]   =   GoodLep.eta - jet2.eta#

    #calculating deltaTheta                                                                                                      
    deltaTheta_jj[0]      =   (jet1.p4() - jet2.p4()).CosTheta()
    deltaTheta_taulep[0]  =   (GoodTau_p4 - GoodLep.p4()).CosTheta()
    deltaTheta_tauj1[0]   =   (GoodTau_p4 - jet1.p4()).CosTheta()
    deltaTheta_tauj2[0]   =   (GoodTau_p4 - jet2.p4()).CosTheta()
    deltaTheta_lepj1[0]   =   (GoodLep.p4() - jet1.p4()).CosTheta()
    deltaTheta_lepj2[0]   =   (GoodLep.p4() - jet2.p4()).CosTheta()


    #calculating ptRel                                                                                                      
    ptRel_jj[0]      =   get_ptrel(jet1, jet2, 1.)
    if isMC:
        ptRel_taulep[0]  =   get_ptrel(GoodTau, GoodLep, (fes*tes))
        ptRel_tauj1[0]   =   get_ptrel(GoodTau, jet1, (fes*tes))
        ptRel_tauj2[0]   =   get_ptrel(GoodTau, jet2, (fes*tes))
    else:
        ptRel_taulep[0]  =   get_ptrel(GoodTau, GoodLep, 1.)
        ptRel_tauj1[0]   =   get_ptrel(GoodTau, jet1, 1.)
        ptRel_tauj2[0]   =   get_ptrel(GoodTau, jet2, 1.)
    ptRel_lepj1[0]   =   get_ptrel(GoodLep, jet1, 1.)
    ptRel_lepj2[0]   =   get_ptrel(GoodLep, jet2, 1.)

    lepton_Zeppenfeld[0], tau_Zeppenfeld[0], event_Zeppenfeld[0] = Zeppenfeld(lepton_eta[0], tau_eta[0], leadjet_eta[0], subleadjet_eta[0])

    AK8jet1, dR_jet1AK48 = closest(jet1, fatjets)
    AK8jet2, dR_jet2AK48 = closest(jet1, fatjets)
    
    if dR_jet1AK48 < 0.8:
        AK8leadjet_pt[0]               =   AK8jet1.pt
        AK8leadjet_eta[0]              =   AK8jet1.eta
        AK8leadjet_phi[0]              =   AK8jet1.phi
        AK8leadjet_mass[0]             =   AK8jet1.msoftdrop
    
        AK8leadjet_tau21[0]             =   AK8jet1.tau2/((AK8jet1.tau1==0.)*1 + (AK8jet1.tau1!=0.)*AK8jet1.tau1)
        AK8leadjet_tau32[0]             =   AK8jet1.tau3/((AK8jet1.tau2==0.)*1 + (AK8jet1.tau2!=0.)*AK8jet1.tau2)
        AK8leadjet_tau43[0]             =   AK8jet1.tau4/((AK8jet1.tau3==0.)*1 + (AK8jet1.tau3!=0.)*AK8jet1.tau3)
        leadjet_dRAK48[0] = copy.deepcopy(dR_jet1AK48)

    if dR_jet2AK48 < 0.8:
        AK8subleadjet_pt[0]               =   AK8jet2.pt
        AK8subleadjet_eta[0]              =   AK8jet2.eta
        AK8subleadjet_phi[0]              =   AK8jet2.phi
        AK8subleadjet_mass[0]             =   AK8jet2.msoftdrop
        
        AK8subleadjet_tau21[0]             =   AK8jet2.tau2/((AK8jet2.tau1==0.)*1 + (AK8jet2.tau1!=0.)*AK8jet2.tau1)
        AK8subleadjet_tau32[0]             =   AK8jet2.tau3/((AK8jet2.tau2==0.)*1 + (AK8jet2.tau2!=0.)*AK8jet2.tau2)
        AK8subleadjet_tau43[0]             =   AK8jet2.tau4/((AK8jet2.tau3==0.)*1 + (AK8jet2.tau3!=0.)*AK8jet2.tau3)
        subleadjet_dRAK48[0] = copy.deepcopy(dR_jet2AK48)


    if not BVeto(jets): pass_b_veto[0]=1

    if (SingleEle or SingleMu) and pass_lepton_selection[0]==1 and pass_lepton_veto[0]==1 and pass_tau_selection[0]==1 and pass_charge_selection[0]==1 and pass_jet_selection[0]==1 and pass_b_veto[0]==1: pass_upToBVeto[0]=1#

    leadJet=ROOT.TLorentzVector()
    subleadJet=ROOT.TLorentzVector()
    leadJet.SetPtEtaPhiM(jet1.pt, jet1.eta, jet1.phi, jet1.mass)
    subleadJet.SetPtEtaPhiM(jet2.pt, jet2.eta, jet2.phi, jet2.mass) 
    
    if not JetCut(leadJet, subleadJet): pass_mjj_cut[0]=1

    m_jj[0]=(leadJet + subleadJet).M()
    m_jjtau[0]=(leadJet + subleadJet + GoodTau_p4).M()
    m_jjtaulep[0]=(leadJet + subleadJet + GoodTau_p4 + GoodLep.p4()).M()

    lepton_Zeppenfeld_over_deltaEta_jj[0] = lepton_Zeppenfeld[0]/deltaEta_jj[0]
    tau_Zeppenfeld_over_deltaEta_jj[0] = tau_Zeppenfeld[0]/deltaEta_jj[0]
    lepton_Zeppenfeld_over_deltaEta_jj[0] = event_Zeppenfeld[0]/deltaEta_jj[0]

    if isMC:
        event_RT[0] = (GoodLep.pt * GoodTau.pt*(fes*tes)) / (jet1.pt * jet2.pt)
    else:
        event_RT[0] = (GoodLep.pt * GoodTau.pt) / (jet1.pt * jet2.pt)

    if not metCut(met): pass_MET_cut[0]=1

    if (SingleEle or SingleMu) and pass_lepton_selection[0]==1 and pass_lepton_veto[0]==1 and pass_tau_selection[0]==1 and pass_charge_selection[0]==1 and pass_jet_selection[0]==1 and pass_b_veto[0]==1 and pass_mjj_cut[0]==1 and pass_MET_cut[0]==1:
        pass_everyCut[0]=1


    #######################################
    ## Removing events with HEM problem  ##
    #######################################
    passesMETHEMVeto = HEMveto(jets, electrons)
    if(sample.year == 2018 and not passesMETHEMVeto):
        if(not isMC and chain.run > 319077.):
            continue
        elif(isMC):
            w_nominal_all[0] *= 0.354

    '''
    
    if IsDim8:
        opname = ""
        opmag = 0
        for opi, opn in enumerate(EFT_operator_names):
            if ("_" + opn + "_") in sample.label:
                opmax = EFT_operator[opn]["max"]
                step = opmax/5.

                for eidx in range(11):
                    epoint = opmax - step * eidx
                    IsZero = (epoint == 0.)
                    str_epoint = "_" + str(epoint).replace(".0", "").replace(".", "p") + "_"

                    if str_epoint in sample.label:
                        idxpos = int((EFT_operator[opn]["idx"])*11 - (eidx + 1))
                        idxneg = int((EFT_operator[opn]["idx"] - 1)*11 + eidx)
                        if IsZero and idxneg != idxpos:
                            print("Something went wrong with dim8 weights assignment")
                            #break
                        wpos = LHEitem(LHEDim8[idxpos])
                        wneg = LHEitem(LHEDim8[idxneg])
                        #print('idxneg:', idxneg, 'wneg:', wneg)
                        #print('idxpos:', idxpos, 'wpos:', wpos)

                        w_pos[0] = copy.deepcopy(wpos)
                        w_neg[0] = copy.deepcopy(wneg)

                        wsign = 0
                        kpow = 0
                        #print(sample.label, "_BSM_" in sample.label, "_0_" in sample.label, "_INT_" in sample.label)
                        if "_BSM_" in sample.label:#
                            if Debug:
                                print("BSM")
                            wsign = +1.
                            kpow = 2.*(epoint**2.)
                        elif "_0_" in sample.label:
                            if Debug:
                                print("0")
                            wsign = +1.
                            kpow = +2.
                        elif "_INT_" in sample.label:
                            if Debug:
                                print("INT")
                            wsign = -1.
                            kpow = 2.*epoint
                            
                        #print("wsign:", wsign, "kpow:", kpow)

                        w_coeff = (wpos + wsign * wneg) / kpow
                        #print("w_coeff:", w_coeff)
                        w_dim8[0] = copy.deepcopy(w_coeff)
        

                        break
                break
        #print("w_dim8:", w_dim8[0])
    
    systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
    systTree.fillTreesSysts(trees, "all")

outTreeFile.cd()
if(isMC):
    #print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(h_genweight.GetBinContent(1), h_PDFweight.GetNbinsX()))
    h_genweight.Write()
    if isthere_pdf:
        h_PDFweight.Write()

systTree.writeTreesSysts(trees, outTreeFile)
print("Number of events in output tree " + str(trees[0].GetEntries()))

endTime = datetime.datetime.now()
print("Ending running at " + str(endTime) + "\n Goodbye")
