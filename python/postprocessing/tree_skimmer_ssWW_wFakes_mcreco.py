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
from skimtree_utils_ssWW_wFakes import *
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

HLT_effLumi                 =   array.array('f', [-999.])
var_list.append(HLT_effLumi)

m_jj                        =   array.array('f', [-999.])
var_list.append(m_jj)
deltaPhi_jj                 =   array.array('f', [-999.])#
var_list.append(deltaPhi_jj)#
deltaTheta_jj                 =   array.array('f', [-999.])#
var_list.append(deltaTheta_jj)#
ptRel_jj                 =   array.array('f', [-999.])#
var_list.append(ptRel_jj)#
deltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(deltaEta_jj)#

genm_jj                        =   array.array('f', [-999.])
var_list.append(genm_jj)
gendeltaPhi_jj                 =   array.array('f', [-999.])#
var_list.append(gendeltaPhi_jj)#
gendeltaTheta_jj                 =   array.array('f', [-999.])#
var_list.append(gendeltaTheta_jj)#
genptRel_jj                 =   array.array('f', [-999.])#
var_list.append(genptRel_jj)#
gendeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(gendeltaEta_jj)#

mm_jj                        =   array.array('f', [-999.])
var_list.append(mm_jj)
mdeltaPhi_jj                 =   array.array('f', [-999.])#
var_list.append(mdeltaPhi_jj)#
mdeltaTheta_jj                 =   array.array('f', [-999.])#
var_list.append(mdeltaTheta_jj)#
mptRel_jj                 =   array.array('f', [-999.])#
var_list.append(mptRel_jj)#
mdeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(mdeltaEta_jj)#

gmm_jj                        =   array.array('f', [-999.])
var_list.append(gmm_jj)
gmdeltaPhi_jj                 =   array.array('f', [-999.])#
var_list.append(gmdeltaPhi_jj)#
gmdeltaTheta_jj                 =   array.array('f', [-999.])#
var_list.append(gmdeltaTheta_jj)#
gmptRel_jj                 =   array.array('f', [-999.])#
var_list.append(gmptRel_jj)#
gmdeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(gmdeltaEta_jj)#

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
systTree.branchTreesSysts(trees, "all", "leadjet_partonFlavour",    outTreeFile, leadjet_partonFlavour)
systTree.branchTreesSysts(trees, "all", "leadjet_IsGenMatched",    outTreeFile, leadjet_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "subleadjet_pt",           outTreeFile, subleadjet_pt)
systTree.branchTreesSysts(trees, "all", "subleadjet_eta",          outTreeFile, subleadjet_eta)
systTree.branchTreesSysts(trees, "all", "subleadjet_phi",          outTreeFile, subleadjet_phi)
systTree.branchTreesSysts(trees, "all", "subleadjet_mass",         outTreeFile, subleadjet_mass)
systTree.branchTreesSysts(trees, "all", "subleadjet_DeepFlv_b",    outTreeFile, subleadjet_DeepFlv_b)
systTree.branchTreesSysts(trees, "all", "subleadjet_partonFlavour",    outTreeFile, subleadjet_partonFlavour)
systTree.branchTreesSysts(trees, "all", "subleadjet_IsGenMatched",    outTreeFile, subleadjet_IsGenMatched)

systTree.branchTreesSysts(trees, "all", "mleadjet_pt",           outTreeFile, mleadjet_pt)
systTree.branchTreesSysts(trees, "all", "mleadjet_eta",          outTreeFile, mleadjet_eta)
systTree.branchTreesSysts(trees, "all", "mleadjet_phi",          outTreeFile, mleadjet_phi)
systTree.branchTreesSysts(trees, "all", "mleadjet_mass",         outTreeFile, mleadjet_mass)
systTree.branchTreesSysts(trees, "all", "mleadjet_DeepFlv_b",    outTreeFile, mleadjet_DeepFlv_b)
systTree.branchTreesSysts(trees, "all", "mleadjet_partonFlavour",    outTreeFile, mleadjet_partonFlavour)
systTree.branchTreesSysts(trees, "all", "mleadjet_IsGenMatched",    outTreeFile, mleadjet_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "msubleadjet_pt",           outTreeFile, msubleadjet_pt)
systTree.branchTreesSysts(trees, "all", "msubleadjet_eta",          outTreeFile, msubleadjet_eta)
systTree.branchTreesSysts(trees, "all", "msubleadjet_phi",          outTreeFile, msubleadjet_phi)
systTree.branchTreesSysts(trees, "all", "msubleadjet_mass",         outTreeFile, msubleadjet_mass)
systTree.branchTreesSysts(trees, "all", "msubleadjet_DeepFlv_b",    outTreeFile, msubleadjet_DeepFlv_b)
systTree.branchTreesSysts(trees, "all", "msubleadjet_partonFlavour",    outTreeFile, msubleadjet_partonFlavour)
systTree.branchTreesSysts(trees, "all", "msubleadjet_IsGenMatched",    outTreeFile, msubleadjet_IsGenMatched)

systTree.branchTreesSysts(trees, "all", "gmleadjet_pt",           outTreeFile, gmleadjet_pt)
systTree.branchTreesSysts(trees, "all", "gmleadjet_eta",          outTreeFile, gmleadjet_eta)
systTree.branchTreesSysts(trees, "all", "gmleadjet_phi",          outTreeFile, gmleadjet_phi)
systTree.branchTreesSysts(trees, "all", "gmleadjet_mass",         outTreeFile, gmleadjet_mass)
systTree.branchTreesSysts(trees, "all", "gmleadjet_DeepFlv_b",    outTreeFile, gmleadjet_DeepFlv_b)
systTree.branchTreesSysts(trees, "all", "gmleadjet_partonFlavour",    outTreeFile, gmleadjet_partonFlavour)
systTree.branchTreesSysts(trees, "all", "gmleadjet_IsGenMatched",    outTreeFile, gmleadjet_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "gmsubleadjet_pt",           outTreeFile, gmsubleadjet_pt)
systTree.branchTreesSysts(trees, "all", "gmsubleadjet_eta",          outTreeFile, gmsubleadjet_eta)
systTree.branchTreesSysts(trees, "all", "gmsubleadjet_phi",          outTreeFile, gmsubleadjet_phi)
systTree.branchTreesSysts(trees, "all", "gmsubleadjet_mass",         outTreeFile, gmsubleadjet_mass)
systTree.branchTreesSysts(trees, "all", "gmsubleadjet_DeepFlv_b",    outTreeFile, gmsubleadjet_DeepFlv_b)
systTree.branchTreesSysts(trees, "all", "gmsubleadjet_partonFlavour",    outTreeFile, gmsubleadjet_partonFlavour)
systTree.branchTreesSysts(trees, "all", "gmsubleadjet_IsGenMatched",    outTreeFile, gmsubleadjet_IsGenMatched)

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

systTree.branchTreesSysts(trees, "all", "m_jj",                  outTreeFile, m_jj)
systTree.branchTreesSysts(trees, "all", "deltaPhi_jj",              outTreeFile, deltaPhi_jj)#
systTree.branchTreesSysts(trees, "all", "deltaEta_jj",              outTreeFile, deltaEta_jj)#
systTree.branchTreesSysts(trees, "all", "deltaTheta_jj",              outTreeFile, deltaTheta_jj)#
systTree.branchTreesSysts(trees, "all", "ptRel_jj",              outTreeFile, ptRel_jj)#

systTree.branchTreesSysts(trees, "all", "mm_jj",                  outTreeFile, mm_jj)
systTree.branchTreesSysts(trees, "all", "mdeltaPhi_jj",              outTreeFile, mdeltaPhi_jj)#
systTree.branchTreesSysts(trees, "all", "mdeltaEta_jj",              outTreeFile, mdeltaEta_jj)#
systTree.branchTreesSysts(trees, "all", "mdeltaTheta_jj",              outTreeFile, mdeltaTheta_jj)#
systTree.branchTreesSysts(trees, "all", "mptRel_jj",              outTreeFile, mptRel_jj)#

systTree.branchTreesSysts(trees, "all", "genm_jj",                  outTreeFile, genm_jj)
systTree.branchTreesSysts(trees, "all", "gendeltaPhi_jj",              outTreeFile, gendeltaPhi_jj)#
systTree.branchTreesSysts(trees, "all", "gendeltaEta_jj",              outTreeFile, gendeltaEta_jj)#
systTree.branchTreesSysts(trees, "all", "gendeltaTheta_jj",              outTreeFile, gendeltaTheta_jj)#
systTree.branchTreesSysts(trees, "all", "genptRel_jj",              outTreeFile, genptRel_jj)#

systTree.branchTreesSysts(trees, "all", "gmm_jj",                  outTreeFile, gmm_jj)
systTree.branchTreesSysts(trees, "all", "gmdeltaPhi_jj",              outTreeFile, gmdeltaPhi_jj)#
systTree.branchTreesSysts(trees, "all", "gmdeltaEta_jj",              outTreeFile, gmdeltaEta_jj)#
systTree.branchTreesSysts(trees, "all", "gmdeltaTheta_jj",              outTreeFile, gmdeltaTheta_jj)#
systTree.branchTreesSysts(trees, "all", "gmptRel_jj",              outTreeFile, gmptRel_jj)#

systTree.branchTreesSysts(trees, "all", "HLT_effLumi",              outTreeFile, HLT_effLumi)#


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

    w_nominal_all[0] = 1.
    #++++++++++++++++++++++++++++++++++
    #++        taking objects        ++
    #++++++++++++++++++++++++++++++++++
    
    if Debug:
        print("\nevento n. " + str(i))
        if i > 500:#1000:
            break
    
    else:
        if (i+1)%1000 == 0 and i!=0:
            print("Event #", i+1, " out of ", tree.GetEntries())

    if i%(tree.GetEntries()) == 0 and i!=0:
        print("Last event being processed (#" + str(i+1) + ")")

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

    sgenjets = SelectVBSQGenJet(genjets)

    if len(sgenjets) < 2:
        continue

    genjet1 = sgenjets[0]
    genjet2 = sgenjets[1]

    genjet1_pt[0]               =   genjet1.pt
    genjet1_eta[0]              =   genjet1.eta
    genjet1_phi[0]              =   genjet1.phi
    genjet1_mass[0]             =   genjet1.mass
    genjet1_partonFlavour[0]    =   genjet1.partonFlavour
    genjet2_pt[0]                =   genjet2.pt
    genjet2_eta[0]               =   genjet2.eta
    genjet2_phi[0]               =   genjet2.phi
    genjet2_mass[0]              =   genjet2.mass
    genjet2_partonFlavour[0]     =   genjet2.partonFlavour

    gmjet1 = None
    gmjet2 = None

    for jet in jets:
        if not (jet.genJetIdx>-1 and jet.genJetIdx < len(genjets)):
            continue
        if genjets[jet.genJetIdx] == genjet1:
            gmjet1 = jet
        elif genjets[jet.genJetIdx] == genjet2:
            gmjet2 = jet

    if not (gmjet1 == None or gmjet2 == None):
        gmleadjet_pt[0]              =   gmjet1.pt
        gmleadjet_eta[0]              =   gmjet1.eta
        gmleadjet_phi[0]              =   gmjet1.phi
        gmleadjet_mass[0]             =   gmjet1.mass
        gmleadjet_DeepFlv_b[0]        =   gmjet1.btagDeepFlavB
        gmleadjet_partonFlavour[0]    =   gmjet1.btagDeepFlavB
        if gmjet1.genJetIdx > -1 and gmjet1.genJetIdx < len(genjets):
            if genjets[gmjet1.genJetIdx] == genjet1:
                gmleadjet_IsGenMatched[0] = 1
            else:
                gmleadjet_IsGenMatched[0] = 0
        else:
            gmleadjet_IsGenMatched[0] = 0

        gmsubleadjet_pt[0]            =   gmjet2.pt
        gmsubleadjet_eta[0]           =   gmjet2.eta
        gmsubleadjet_phi[0]           =   gmjet2.phi
        gmsubleadjet_mass[0]          =   gmjet2.mass
        gmsubleadjet_DeepFlv_b[0]     =   gmjet2.btagDeepFlavB
        gmsubleadjet_partonFlavour[0] =   gmjet2.btagDeepFlavB
        if gmjet2.genJetIdx > -1 and gmjet2.genJetIdx < len(genjets):
            if genjets[gmjet2.genJetIdx] == genjet2:
                gmsubleadjet_IsGenMatched[0] = 1
            else:
                gmsubleadjet_IsGenMatched[0] = 0
        else:
            gmsubleadjet_IsGenMatched[0] = 0

        gmdeltaPhi_jj[0]   =   deltaPhi(gmjet1, gmjet2)
        gmdeltaEta_jj[0]   =   gmjet1.eta - gmjet2.eta
        gmdeltaTheta_jj[0] =   (gmjet1.p4() - gmjet2.p4()).CosTheta()
        gmptRel_jj[0]      =   get_ptrel(gmjet1, gmjet2, 1.)
        gmm_jj[0]          =   (gmjet1.p4() + gmjet2.p4()).M()

    
    gendeltaPhi_jj[0]   =   deltaPhi(genjet1, genjet2)
    gendeltaEta_jj[0]   =   genjet1.eta - genjet2.eta
    gendeltaTheta_jj[0] =   (genjet1.p4() - genjet2.p4()).CosTheta()
    genptRel_jj[0]      =   get_ptrel(genjet1, genjet2, 1.)
    genm_jj[0]          =   (genjet1.p4() + genjet2.p4()).M()


    GoodEle, ele_TightRegion = SelectLepton(electrons)#, jet1, jet2) 
    GoodMu, mu_TightRegion = SelectLepton(muons)#, jet1, jet2) 
    
    if GoodEle == None and GoodMu == None:
        continue

    ele_lepton_veto = False
    mu_lepton_veto = False

    if GoodEle != None:
        ele_lepton_veto = LepVeto(GoodEle, electrons, muons)
    if GoodMu != None:
        mu_lepton_veto = LepVeto(GoodMu, electrons, muons)   
 
    SingleEle=False
    SingleMu=False
    ElMu=False
   
    GoodLep = None
    leptons = None
    lepton_TightRegion = 0
    lepton_LnTRegion = 0

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
        if GoodMu == None and GoodEle != None and ele_lepton_veto:
            GoodLep = GoodEle
            lepton_TightRegion = copy.deepcopy(ele_TightRegion)
            SingleEle = True
            SingleMu = False

        elif GoodMu != None and mu_lepton_veto and GoodEle == None:
            GoodLep = GoodMu
            lepton_TightRegion = copy.deepcopy(mu_TightRegion)
            SingleMu = True
            SingleEle = False
                
        elif GoodMu != None and GoodEle != None:
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
            HLT_effLumi[0] = lumiFinder("Ele", vTrigEle)
    elif SingleMu==True:
        if isMC:
            HLT_effLumi[0] = lumiFinder("Mu", vTrigMu)

    elif not (SingleMu or SingleEle):
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        systTree.fillTreesSysts(trees, "all")
        continue

    if SingleEle and dataMu:
        continue
    if SingleMu and dataEle:
        continue

    if lepton_TightRegion==1:
        lepton_LnTRegion = 0
    elif lepton_TightRegion==0:
        lepton_LnTRegion = 1
    else:
        lepton_LnTRegion = -999
    
    if GoodLep == None or (lepton_TightRegion<0 and lepton_LnTRegion<0): 
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        systTree.fillTreesSysts(trees, "all")
        continue

    if lepton_TightRegion==1:# or lepton_LnTRegion==1:
        pass_lepton_selection[0] = 1
    else:
        pass_lepton_selection[0] = 0

    pass_lepton_veto[0] = 1

    ThereIsOneTau, ltau_list = SelectAndVetoTaus(list(taus), GoodLep)

    tau_TightRegion = 0
    tau_LnTRegion = 0

    if ThereIsOneTau:
        indexGoodTau = ltau_list[0][0]
        if ltau_list[0][1] == 'T':
            tau_TightRegion = 1
            tau_LnTRegion = 0
        elif ltau_list[0][1] == 'L':
            tau_TightRegion = 0
            tau_LnTRegion = 1            
    else:
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        systTree.fillTreesSysts(trees, "all")
        continue

    GoodTau = taus[indexGoodTau]

    if tau_TightRegion==1 or tau_LnTRegion==1:
        pass_tau_selection[0] = 1
    else:
        pass_tau_selection[0] = 0
    
    if GoodTau.charge==GoodLep.charge:
        pass_charge_selection[0]=1

    nJets[0] = len(jets)
    nBJets[0] = CountBJets(jets)#
    nGenJets[0] = len(genjets)

    jet1, jet2 = SelectVBSJets(jets = list(jets), lep1 = GoodTau, lep2 = GoodLep)
    mjet1, mjet2 = SelectVBSJets(jets = list(jets), useMassCrit = True, lep1 = GoodTau, lep2 = GoodLep)

    if (jet1 == None or jet2 == None) and (mjet1 == None or mjet2 == None):
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        systTree.fillTreesSysts(trees, "all")
        continue  

    pass_jet_selection[0]=1

    if not (jet1 == None or jet2 == None):
        leadjet_pt[0]               =   jet1.pt
        leadjet_eta[0]              =   jet1.eta
        leadjet_phi[0]              =   jet1.phi
        leadjet_mass[0]             =   jet1.mass
        leadjet_DeepFlv_b[0]        =   jet1.btagDeepFlavB
        leadjet_partonFlavour[0]    =   jet1.btagDeepFlavB

        if jet1.genJetIdx > -1 and jet1.genJetIdx < len(genjets):
            if genjets[jet1.genJetIdx] == genjet1:
                leadjet_IsGenMatched[0] = 1
            else:
                leadjet_IsGenMatched[0] = 0
        else:
            leadjet_IsGenMatched[0] = 0

        subleadjet_pt[0]            =   jet2.pt
        subleadjet_eta[0]           =   jet2.eta
        subleadjet_phi[0]           =   jet2.phi
        subleadjet_mass[0]          =   jet2.mass
        subleadjet_DeepFlv_b[0]     =   jet2.btagDeepFlavB
        subleadjet_partonFlavour[0] =   jet2.btagDeepFlavB

        if jet2.genJetIdx > -1 and jet2.genJetIdx < len(genjets):
            if genjets[jet2.genJetIdx] == genjet2:
                subleadjet_IsGenMatched[0] = 1
            else:
                subleadjet_IsGenMatched[0] = 0
        else:
            subleadjet_IsGenMatched[0] = 0

        deltaPhi_jj[0]   =   deltaPhi(jet1, jet2)
        deltaEta_jj[0]   =   jet1.eta - jet2.eta
        deltaTheta_jj[0] =   (jet1.p4() - jet2.p4()).CosTheta()
        ptRel_jj[0]      =   get_ptrel(jet1, jet2, 1.)
        m_jj[0]          =   (jet1.p4() + jet2.p4()).M()

    if not (mjet1 == None or mjet2 == None):
        mleadjet_pt[0]               =   mjet1.pt
        mleadjet_eta[0]              =   mjet1.eta
        mleadjet_phi[0]              =   mjet1.phi
        mleadjet_mass[0]             =   mjet1.mass
        mleadjet_DeepFlv_b[0]        =   mjet1.btagDeepFlavB
        mleadjet_partonFlavour[0]    =   mjet1.btagDeepFlavB
        if mjet1.genJetIdx > -1 and mjet1.genJetIdx < len(genjets):
            if genjets[mjet1.genJetIdx] == genjet1:
                mleadjet_IsGenMatched[0] = 1
            else:
                mleadjet_IsGenMatched[0] = 0
        else:
            mleadjet_IsGenMatched[0] = 0

        msubleadjet_pt[0]            =   mjet2.pt
        msubleadjet_eta[0]           =   mjet2.eta
        msubleadjet_phi[0]           =   mjet2.phi
        msubleadjet_mass[0]          =   mjet2.mass
        msubleadjet_DeepFlv_b[0]     =   mjet2.btagDeepFlavB
        msubleadjet_partonFlavour[0] =   mjet2.btagDeepFlavB
        if mjet2.genJetIdx > -1 and mjet2.genJetIdx < len(genjets):
            if genjets[mjet2.genJetIdx] == genjet2:
                msubleadjet_IsGenMatched[0] = 1
            else:
                msubleadjet_IsGenMatched[0] = 0
        else:
            msubleadjet_IsGenMatched[0] = 0
    

        mdeltaPhi_jj[0]   =   deltaPhi(jet1, jet2)
        mdeltaEta_jj[0]   =   mjet1.eta - jet2.eta
        mdeltaTheta_jj[0] =   (mjet1.p4() - jet2.p4()).CosTheta()
        mptRel_jj[0]      =   get_ptrel(jet1, jet2, 1.)
        mm_jj[0]          =   (mjet1.p4() + mjet2.p4()).M()

    if not BVeto(jets):
        pass_b_veto[0]=1

    if (SingleEle or SingleMu) and pass_lepton_selection[0]==1 and pass_lepton_veto[0]==1 and pass_tau_selection[0]==1 and pass_charge_selection[0]==1 and pass_jet_selection[0]==1 and pass_b_veto[0]==1:
        pass_upToBVeto[0]=1#


    
    if not metCut(met): pass_MET_cut[0]=1

    if (SingleEle or SingleMu) and pass_lepton_selection[0]==1 and pass_lepton_veto[0]==1 and pass_tau_selection[0]==1 and pass_charge_selection[0]==1 and pass_jet_selection[0]==1 and pass_b_veto[0]==1 and pass_MET_cut[0]==1:
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
    '''
 
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
