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

DeltaEtaCutBefore = True # False #

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

genleadjet_pt                  =   array.array('f', [-999.])
genleadjet_eta                 =   array.array('f', [-999.])
genleadjet_phi                 =   array.array('f', [-999.])
genleadjet_mass                =   array.array('f', [-999.])
genleadjet_partonFlavour       =   array.array('f', [-999.])

var_list.append(genleadjet_pt)
var_list.append(genleadjet_eta)
var_list.append(genleadjet_phi)
var_list.append(genleadjet_mass)
var_list.append(genleadjet_partonFlavour)

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

gensubleadjet_pt               =   array.array('f', [-999.])
gensubleadjet_eta              =   array.array('f', [-999.])
gensubleadjet_phi              =   array.array('f', [-999.])
gensubleadjet_mass             =   array.array('f', [-999.])
gensubleadjet_partonFlavour    =   array.array('f', [-999.])

var_list.append(gensubleadjet_pt)
var_list.append(gensubleadjet_eta)
var_list.append(gensubleadjet_phi)
var_list.append(gensubleadjet_mass)
var_list.append(gensubleadjet_partonFlavour)

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
deltaPhi_jj                 =   array.array('f', [-999.])#
deltaTheta_jj                 =   array.array('f', [-999.])#
ptRel_jj                 =   array.array('f', [-999.])#
deltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(m_jj)
var_list.append(deltaPhi_jj)#
var_list.append(deltaTheta_jj)#
var_list.append(ptRel_jj)#
var_list.append(deltaEta_jj)#

genm_jj                        =   array.array('f', [-999.])
gendeltaPhi_jj                 =   array.array('f', [-999.])#
gendeltaTheta_jj                 =   array.array('f', [-999.])#
genptRel_jj                 =   array.array('f', [-999.])#
gendeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(genm_jj)
var_list.append(gendeltaPhi_jj)#
var_list.append(gendeltaTheta_jj)#
var_list.append(genptRel_jj)#
var_list.append(gendeltaEta_jj)#

mm_jj                        =   array.array('f', [-999.])
mdeltaPhi_jj                 =   array.array('f', [-999.])#
mdeltaTheta_jj                 =   array.array('f', [-999.])#
mptRel_jj                 =   array.array('f', [-999.])#
mdeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(mm_jj)
var_list.append(mdeltaPhi_jj)#
var_list.append(mdeltaTheta_jj)#
var_list.append(mptRel_jj)#
var_list.append(mdeltaEta_jj)#

gmm_jj                        =   array.array('f', [-999.])
gmdeltaPhi_jj                 =   array.array('f', [-999.])#
gmdeltaTheta_jj                 =   array.array('f', [-999.])#
gmptRel_jj                 =   array.array('f', [-999.])#
gmdeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(gmdeltaPhi_jj)#
var_list.append(gmm_jj)
var_list.append(gmdeltaTheta_jj)#
var_list.append(gmptRel_jj)#
var_list.append(gmdeltaEta_jj)#m_jj                        =   array.array('f', [-999.])
deltaPhi_jj                 =   array.array('f', [-999.])#
deltaTheta_jj                 =   array.array('f', [-999.])#
ptRel_jj                 =   array.array('f', [-999.])#
deltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(m_jj)
var_list.append(deltaPhi_jj)#
var_list.append(deltaTheta_jj)#
var_list.append(ptRel_jj)#
var_list.append(deltaEta_jj)#

genm_jj                        =   array.array('f', [-999.])
gendeltaPhi_jj                 =   array.array('f', [-999.])#
gendeltaTheta_jj                 =   array.array('f', [-999.])#
genptRel_jj                 =   array.array('f', [-999.])#
gendeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(genm_jj)
var_list.append(gendeltaPhi_jj)#
var_list.append(gendeltaTheta_jj)#
var_list.append(genptRel_jj)#
var_list.append(gendeltaEta_jj)#

mm_jj                        =   array.array('f', [-999.])
mdeltaPhi_jj                 =   array.array('f', [-999.])#
mdeltaTheta_jj                 =   array.array('f', [-999.])#
mptRel_jj                 =   array.array('f', [-999.])#
mdeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(mm_jj)
var_list.append(mdeltaPhi_jj)#
var_list.append(mdeltaTheta_jj)#
var_list.append(mptRel_jj)#
var_list.append(mdeltaEta_jj)#

gmm_jj                        =   array.array('f', [-999.])
gmdeltaPhi_jj                 =   array.array('f', [-999.])#
gmdeltaTheta_jj                 =   array.array('f', [-999.])#
gmptRel_jj                 =   array.array('f', [-999.])#
gmdeltaEta_jj                 =   array.array('f', [-999.])#
var_list.append(gmdeltaPhi_jj)#
var_list.append(gmm_jj)
var_list.append(gmdeltaTheta_jj)#
var_list.append(gmptRel_jj)#
var_list.append(gmdeltaEta_jj)#

#lepton#
genlepton_pt               =   array.array('f', [-999.])
genlepton_eta              =   array.array('f', [-999.])
genlepton_phi              =   array.array('f', [-999.])
genlepton_mass             =   array.array('f', [-999.])
genlepton_pdgid            =   array.array('i', [-999])
genlepton_charge           =   array.array('i', [-999])
genlepton_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999.])
var_list.append(genlepton_pt)
var_list.append(genlepton_eta)
var_list.append(genlepton_phi)
var_list.append(genlepton_mass)
var_list.append(genlepton_pdgid)
var_list.append(genlepton_charge)
var_list.append(genlepton_Zeppenfeld_over_deltaEta_jj)

gmlepton_pt               =   array.array('f', [-999.])
gmlepton_eta              =   array.array('f', [-999.])
gmlepton_phi              =   array.array('f', [-999.])
gmlepton_mass             =   array.array('f', [-999.])
gmlepton_charge           =   array.array('i', [-999])
gmlepton_pdgid            =   array.array('i', [-999])
gmlepton_IsGenMatched     =   array.array('i', [-999])
gmlepton_TightRegion      =   array.array('i', [-999])
gmlepton_LnTRegion        =   array.array('i', [-999])
gmlepton_genPartFlav      =   array.array('i', [-999])
gmlepton_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999.])
var_list.append(gmlepton_pt)
var_list.append(gmlepton_eta)
var_list.append(gmlepton_phi)
var_list.append(gmlepton_mass)
var_list.append(gmlepton_charge)
var_list.append(gmlepton_pdgid)
var_list.append(gmlepton_IsGenMatched)
var_list.append(gmlepton_TightRegion)
var_list.append(gmlepton_LnTRegion)
var_list.append(gmlepton_genPartFlav)
var_list.append(gmlepton_Zeppenfeld_over_deltaEta_jj)

lepton_pt               =   array.array('f', [-999.])
lepton_eta              =   array.array('f', [-999.])
lepton_phi              =   array.array('f', [-999.])
lepton_mass             =   array.array('f', [-999.])
lepton_charge           =   array.array('i', [-999])
lepton_pdgid            =   array.array('i', [-999])
lepton_IsGenMatched     =   array.array('i', [-999])
lepton_TightRegion      =   array.array('i', [-999])
lepton_LnTRegion        =   array.array('i', [-999])
lepton_genPartFlav      =   array.array('i', [-999])
lepton_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999.])
var_list.append(lepton_pt)
var_list.append(lepton_eta)
var_list.append(lepton_phi)
var_list.append(lepton_mass)
var_list.append(lepton_charge)
var_list.append(lepton_pdgid)
var_list.append(lepton_IsGenMatched)
var_list.append(lepton_TightRegion)
var_list.append(lepton_LnTRegion)
var_list.append(lepton_genPartFlav)
var_list.append(lepton_Zeppenfeld_over_deltaEta_jj)

mlepton_pt               =   array.array('f', [-999.])
mlepton_eta              =   array.array('f', [-999.])
mlepton_phi              =   array.array('f', [-999.])
mlepton_mass             =   array.array('f', [-999.])
mlepton_charge           =   array.array('i', [-999])
mlepton_pdgid            =   array.array('i', [-999])
mlepton_IsGenMatched     =   array.array('i', [-999])
mlepton_TightRegion      =   array.array('i', [-999])
mlepton_LnTRegion        =   array.array('i', [-999])
mlepton_genPartFlav      =   array.array('i', [-999])
mlepton_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999.])
var_list.append(mlepton_pt)
var_list.append(mlepton_eta)
var_list.append(mlepton_phi)
var_list.append(mlepton_mass)
var_list.append(mlepton_charge)
var_list.append(mlepton_pdgid)
var_list.append(mlepton_IsGenMatched)
var_list.append(mlepton_TightRegion)
var_list.append(mlepton_LnTRegion)
var_list.append(mlepton_genPartFlav)
var_list.append(mlepton_Zeppenfeld_over_deltaEta_jj)

#tau#
tau_pt                  =   array.array('f', [-999.])
tau_eta                 =   array.array('f', [-999.])
tau_phi                 =   array.array('f', [-999.])
tau_charge              =   array.array('i', [-999])
tau_mass                =   array.array('f', [-999.])
tau_IsGenMatched        =   array.array('f', [-999.])
tau_DecayMode           =   array.array('f', [-999.])
tau_DeepTauVsEle_raw    =   array.array('f', [-999.])
tau_DeepTauVsMu_raw     =   array.array('f', [-999.])
tau_DeepTauVsJet_raw    =   array.array('f', [-999.])
tau_TightRegion         =   array.array('i', [-999])
tau_LnTRegion           =   array.array('i', [-999])
tau_genPartFlav         =   array.array('i', [-999])
tau_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999.])
var_list.append(tau_pt)
var_list.append(tau_eta)
var_list.append(tau_phi)
var_list.append(tau_charge)
var_list.append(tau_mass)
var_list.append(tau_IsGenMatched)
var_list.append(tau_DecayMode)
var_list.append(tau_DeepTauVsEle_raw)#
var_list.append(tau_DeepTauVsMu_raw)#
var_list.append(tau_DeepTauVsJet_raw)#
var_list.append(tau_TightRegion)#
var_list.append(tau_LnTRegion)#
var_list.append(tau_genPartFlav)#
var_list.append(tau_Zeppenfeld_over_deltaEta_jj)

mtau_pt                  =   array.array('f', [-999.])
mtau_eta                 =   array.array('f', [-999.])
mtau_phi                 =   array.array('f', [-999.])
mtau_charge              =   array.array('i', [-999])
mtau_mass                =   array.array('f', [-999.])
mtau_IsGenMatched        =   array.array('f', [-999.])
mtau_DecayMode           =   array.array('f', [-999.])
mtau_DeepTauVsEle_raw    =   array.array('f', [-999.])
mtau_DeepTauVsMu_raw     =   array.array('f', [-999.])
mtau_DeepTauVsJet_raw    =   array.array('f', [-999.])
mtau_TightRegion         =   array.array('i', [-999])
mtau_LnTRegion           =   array.array('i', [-999])
mtau_genPartFlav         =   array.array('i', [-999])
mtau_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999.])
var_list.append(mtau_pt)
var_list.append(mtau_eta)
var_list.append(mtau_phi)
var_list.append(mtau_charge)
var_list.append(mtau_mass)
var_list.append(mtau_IsGenMatched)
var_list.append(mtau_DecayMode)
var_list.append(mtau_DeepTauVsEle_raw)#
var_list.append(mtau_DeepTauVsMu_raw)#
var_list.append(mtau_DeepTauVsJet_raw)#
var_list.append(mtau_TightRegion)#
var_list.append(mtau_LnTRegion)#
var_list.append(mtau_genPartFlav)#
var_list.append(mtau_Zeppenfeld_over_deltaEta_jj)

gmtau_pt                  =   array.array('f', [-999.])
gmtau_eta                 =   array.array('f', [-999.])
gmtau_phi                 =   array.array('f', [-999.])
gmtau_charge              =   array.array('i', [-999])
gmtau_mass                =   array.array('f', [-999.])
#gmtau_IsGenMatched        =   array.array('f', [-999.])
gmtau_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999.])
var_list.append(gmtau_pt)
var_list.append(gmtau_eta)
var_list.append(gmtau_phi)
var_list.append(gmtau_charge)
var_list.append(gmtau_mass)
#var_list.append(gmtau_IsGenMatched)
var_list.append(gmtau_Zeppenfeld_over_deltaEta_jj)

gentau_pt                  =   array.array('f', [-999.])
gentau_eta                 =   array.array('f', [-999.])
gentau_phi                 =   array.array('f', [-999.])
gentau_charge              =   array.array('i', [-999])
gentau_mass                =   array.array('f', [-999.])
gentau_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999.])
var_list.append(gentau_pt)
var_list.append(gentau_eta)
var_list.append(gentau_phi)
var_list.append(gentau_charge)
var_list.append(gentau_mass)
var_list.append(gentau_Zeppenfeld_over_deltaEta_jj)

event_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999])
mevent_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999])
genevent_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999])
gmevent_Zeppenfeld_over_deltaEta_jj           =   array.array('f', [-999])

var_list.append(event_Zeppenfeld_over_deltaEta_jj)

genlnu_pt                  =   array.array('f', [-999.])
genlnu_eta                 =   array.array('f', [-999.])
genlnu_phi                 =   array.array('f', [-999.])
genlnu_mass                 =   array.array('f', [-999.])
var_list.append(genlnu_pt)
var_list.append(genlnu_eta)
var_list.append(genlnu_phi)
var_list.append(genlnu_mass)

gentnu_pt                  =   array.array('f', [-999.])
gentnu_eta                 =   array.array('f', [-999.])
gentnu_phi                 =   array.array('f', [-999.])
gentnu_mass                 =   array.array('f', [-999.])
var_list.append(gentnu_pt)
var_list.append(gentnu_eta)
var_list.append(gentnu_phi)
var_list.append(gentnu_mass)

geninv_pt                  =   array.array('f', [-999.])
geninv_eta                 =   array.array('f', [-999.])
geninv_phi                 =   array.array('f', [-999.])
geninv_mass                 =   array.array('f', [-999.])
var_list.append(geninv_pt)
var_list.append(geninv_eta)
var_list.append(geninv_phi)
var_list.append(geninv_mass)

met_pt                  =   array.array('f', [-999.])
met_sumEt                 =   array.array('f', [-999.])
met_phi                 =   array.array('f', [-999.])
var_list.append(met_pt)
var_list.append(met_sumEt)
var_list.append(met_phi)



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

systTree.branchTreesSysts(trees, "all", "genleadjet_pt",           outTreeFile, genleadjet_pt)
systTree.branchTreesSysts(trees, "all", "genleadjet_eta",          outTreeFile, genleadjet_eta)
systTree.branchTreesSysts(trees, "all", "genleadjet_phi",          outTreeFile, genleadjet_phi)
systTree.branchTreesSysts(trees, "all", "genleadjet_mass",         outTreeFile, genleadjet_mass)
systTree.branchTreesSysts(trees, "all", "genleadjet_partonFlavour",      outTreeFile, genleadjet_partonFlavour)
systTree.branchTreesSysts(trees, "all", "gensubleadjet_pt",           outTreeFile, gensubleadjet_pt)
systTree.branchTreesSysts(trees, "all", "gensubleadjet_eta",          outTreeFile, gensubleadjet_eta)
systTree.branchTreesSysts(trees, "all", "gensubleadjet_phi",          outTreeFile, gensubleadjet_phi)
systTree.branchTreesSysts(trees, "all", "gensubleadjet_mass",         outTreeFile, gensubleadjet_mass)
systTree.branchTreesSysts(trees, "all", "gensubleadjet_partonFlavour",      outTreeFile, gensubleadjet_partonFlavour)

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

systTree.branchTreesSysts(trees, "all", "lepton_pt",           outTreeFile, lepton_pt)
systTree.branchTreesSysts(trees, "all", "lepton_eta",           outTreeFile, lepton_eta)
systTree.branchTreesSysts(trees, "all", "lepton_phi",           outTreeFile, lepton_phi)
systTree.branchTreesSysts(trees, "all", "lepton_mass",           outTreeFile, lepton_mass)
systTree.branchTreesSysts(trees, "all", "lepton_charge",           outTreeFile, lepton_charge)
systTree.branchTreesSysts(trees, "all", "lepton_pdgid",           outTreeFile, lepton_pdgid)
systTree.branchTreesSysts(trees, "all", "lepton_IsGenMatched",           outTreeFile, lepton_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "lepton_TightRegion",           outTreeFile, lepton_TightRegion)
systTree.branchTreesSysts(trees, "all", "lepton_LnTRegion",           outTreeFile, lepton_LnTRegion)
systTree.branchTreesSysts(trees, "all", "lepton_genPartFlav",           outTreeFile, lepton_genPartFlav)
systTree.branchTreesSysts(trees, "all", "lepton_Zeppenfeld_over_deltaEta_jj",           outTreeFile, lepton_Zeppenfeld_over_deltaEta_jj)

systTree.branchTreesSysts(trees, "all", "gmlepton_pt",           outTreeFile, lepton_pt)
systTree.branchTreesSysts(trees, "all", "gmlepton_eta",           outTreeFile, lepton_eta)
systTree.branchTreesSysts(trees, "all", "gmlepton_phi",           outTreeFile, lepton_phi)
systTree.branchTreesSysts(trees, "all", "gmlepton_mass",           outTreeFile, lepton_mass)
systTree.branchTreesSysts(trees, "all", "gmlepton_charge",           outTreeFile, lepton_charge)
systTree.branchTreesSysts(trees, "all", "gmlepton_pdgid",           outTreeFile, lepton_pdgid)
systTree.branchTreesSysts(trees, "all", "gmlepton_IsGenMatched",           outTreeFile, lepton_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "gmlepton_genPartFlav",           outTreeFile, lepton_genPartFlav)
systTree.branchTreesSysts(trees, "all", "gmlepton_Zeppenfeld_over_deltaEta_jj",           outTreeFile, lepton_Zeppenfeld_over_deltaEta_jj)

systTree.branchTreesSysts(trees, "all", "mlepton_pt",           outTreeFile, mlepton_pt)
systTree.branchTreesSysts(trees, "all", "mlepton_eta",           outTreeFile, mlepton_eta)
systTree.branchTreesSysts(trees, "all", "mlepton_phi",           outTreeFile, mlepton_phi)
systTree.branchTreesSysts(trees, "all", "mlepton_mass",           outTreeFile, mlepton_mass)
systTree.branchTreesSysts(trees, "all", "mlepton_charge",           outTreeFile, mlepton_charge)
systTree.branchTreesSysts(trees, "all", "mlepton_pdgid",           outTreeFile, mlepton_pdgid)
systTree.branchTreesSysts(trees, "all", "mlepton_IsGenMatched",           outTreeFile, mlepton_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "mlepton_TightRegion",           outTreeFile, mlepton_TightRegion)
systTree.branchTreesSysts(trees, "all", "mlepton_LnTRegion",           outTreeFile, mlepton_LnTRegion)
systTree.branchTreesSysts(trees, "all", "mlepton_genPartFlav",           outTreeFile, mlepton_genPartFlav)
systTree.branchTreesSysts(trees, "all", "mlepton_Zeppenfeld_over_deltaEta_jj",           outTreeFile, mlepton_Zeppenfeld_over_deltaEta_jj)

systTree.branchTreesSysts(trees, "all", "genlepton_pt",           outTreeFile, genlepton_pt)
systTree.branchTreesSysts(trees, "all", "genlepton_eta",           outTreeFile, genlepton_eta)
systTree.branchTreesSysts(trees, "all", "genlepton_phi",           outTreeFile, genlepton_phi)
systTree.branchTreesSysts(trees, "all", "genlepton_mass",           outTreeFile, genlepton_mass)
systTree.branchTreesSysts(trees, "all", "genlepton_charge",           outTreeFile, genlepton_charge)
systTree.branchTreesSysts(trees, "all", "genlepton_pdgid",           outTreeFile, genlepton_pdgid)
systTree.branchTreesSysts(trees, "all", "genlepton_Zeppenfeld_over_deltaEta_jj",           outTreeFile, genlepton_Zeppenfeld_over_deltaEta_jj)

systTree.branchTreesSysts(trees, "all", "tau_pt",           outTreeFile, tau_pt)
systTree.branchTreesSysts(trees, "all", "tau_eta",           outTreeFile, tau_eta)
systTree.branchTreesSysts(trees, "all", "tau_phi",           outTreeFile, tau_phi)
systTree.branchTreesSysts(trees, "all", "tau_mass",           outTreeFile, tau_mass)
systTree.branchTreesSysts(trees, "all", "tau_charge",           outTreeFile, tau_charge)
systTree.branchTreesSysts(trees, "all", "tau_IsGenMatched",           outTreeFile, tau_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "tau_DecayMode",           outTreeFile, tau_DecayMode)
systTree.branchTreesSysts(trees, "all", "tau_DeepTauVsEle_raw",           outTreeFile, tau_DeepTauVsEle_raw)
systTree.branchTreesSysts(trees, "all", "tau_DeepTauVsMu_raw",           outTreeFile, tau_DeepTauVsMu_raw)
systTree.branchTreesSysts(trees, "all", "tau_DeepTauVsJet_raw",           outTreeFile, tau_DeepTauVsJet_raw)
systTree.branchTreesSysts(trees, "all", "tau_TightRegion",           outTreeFile, tau_TightRegion)
systTree.branchTreesSysts(trees, "all", "tau_LnTRegion",           outTreeFile, tau_LnTRegion)
systTree.branchTreesSysts(trees, "all", "tau_genPartFlav",           outTreeFile, tau_genPartFlav)
systTree.branchTreesSysts(trees, "all", "tau_Zeppenfeld_over_deltaEta_jj",           outTreeFile, tau_Zeppenfeld_over_deltaEta_jj)

systTree.branchTreesSysts(trees, "all", "mtau_pt",           outTreeFile, mtau_pt)
systTree.branchTreesSysts(trees, "all", "mtau_eta",           outTreeFile, mtau_eta)
systTree.branchTreesSysts(trees, "all", "mtau_phi",           outTreeFile, mtau_phi)
systTree.branchTreesSysts(trees, "all", "mtau_mass",           outTreeFile, mtau_mass)
systTree.branchTreesSysts(trees, "all", "mtau_charge",           outTreeFile, mtau_charge)
systTree.branchTreesSysts(trees, "all", "mtau_IsGenMatched",           outTreeFile, mtau_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "mtau_DecayMode",           outTreeFile, mtau_DecayMode)
systTree.branchTreesSysts(trees, "all", "mtau_DeepTauVsEle_raw",           outTreeFile, mtau_DeepTauVsEle_raw)
systTree.branchTreesSysts(trees, "all", "mtau_DeepTauVsMu_raw",           outTreeFile, mtau_DeepTauVsMu_raw)
systTree.branchTreesSysts(trees, "all", "mtau_DeepTauVsJet_raw",           outTreeFile, mtau_DeepTauVsJet_raw)
systTree.branchTreesSysts(trees, "all", "mtau_TightRegion",           outTreeFile, mtau_TightRegion)
systTree.branchTreesSysts(trees, "all", "mtau_LnTRegion",           outTreeFile, mtau_LnTRegion)
systTree.branchTreesSysts(trees, "all", "mtau_genPartFlav",           outTreeFile, mtau_genPartFlav)
systTree.branchTreesSysts(trees, "all", "mtau_Zeppenfeld_over_deltaEta_jj",           outTreeFile, mtau_Zeppenfeld_over_deltaEta_jj)

systTree.branchTreesSysts(trees, "all", "gmtau_pt",           outTreeFile, gmtau_pt)
systTree.branchTreesSysts(trees, "all", "gmtau_eta",           outTreeFile, gmtau_eta)
systTree.branchTreesSysts(trees, "all", "gmtau_phi",           outTreeFile, gmtau_phi)
systTree.branchTreesSysts(trees, "all", "gmtau_mass",           outTreeFile, gmtau_mass)
systTree.branchTreesSysts(trees, "all", "gmtau_charge",           outTreeFile, gmtau_charge)
#systTree.branchTreesSysts(trees, "all", "gmtau_IsGenMatched",           outTreeFile, gmtau_IsGenMatched)
systTree.branchTreesSysts(trees, "all", "gmtau_Zeppenfeld_over_deltaEta_jj",           outTreeFile, gmtau_Zeppenfeld_over_deltaEta_jj)

systTree.branchTreesSysts(trees, "all", "gentau_pt",           outTreeFile, gentau_pt)
systTree.branchTreesSysts(trees, "all", "gentau_eta",           outTreeFile, gentau_eta)
systTree.branchTreesSysts(trees, "all", "gentau_phi",           outTreeFile, gentau_phi)
systTree.branchTreesSysts(trees, "all", "gentau_mass",           outTreeFile, gentau_mass)
systTree.branchTreesSysts(trees, "all", "gentau_charge",           outTreeFile, gentau_charge)
systTree.branchTreesSysts(trees, "all", "gentau_Zeppenfeld_over_deltaEta_jj",           outTreeFile, gentau_Zeppenfeld_over_deltaEta_jj)

systTree.branchTreesSysts(trees, "all", "event_Zeppenfeld_over_deltaEta_jj",              outTreeFile, event_Zeppenfeld_over_deltaEta_jj)#
systTree.branchTreesSysts(trees, "all", "mevent_Zeppenfeld_over_deltaEta_jj",              outTreeFile, mevent_Zeppenfeld_over_deltaEta_jj)#
systTree.branchTreesSysts(trees, "all", "genevent_Zeppenfeld_over_deltaEta_jj",              outTreeFile, event_Zeppenfeld_over_deltaEta_jj)#
systTree.branchTreesSysts(trees, "all", "gmevent_Zeppenfeld_over_deltaEta_jj",              outTreeFile, event_Zeppenfeld_over_deltaEta_jj)#

systTree.branchTreesSysts(trees, "all", "genlnu_pt",           outTreeFile, genlnu_pt)
systTree.branchTreesSysts(trees, "all", "genlnu_eta",           outTreeFile, genlnu_eta)
systTree.branchTreesSysts(trees, "all", "genlnu_phi",           outTreeFile, genlnu_phi)
systTree.branchTreesSysts(trees, "all", "genlnu_mass",           outTreeFile, genlnu_mass)
systTree.branchTreesSysts(trees, "all", "gentnu_pt",           outTreeFile, gentnu_pt)
systTree.branchTreesSysts(trees, "all", "gentnu_eta",           outTreeFile, gentnu_eta)
systTree.branchTreesSysts(trees, "all", "gentnu_phi",           outTreeFile, gentnu_phi)
systTree.branchTreesSysts(trees, "all", "gentnu_mass",           outTreeFile, gentnu_mass)
systTree.branchTreesSysts(trees, "all", "geninv_pt",           outTreeFile, geninv_pt)
systTree.branchTreesSysts(trees, "all", "geninv_eta",           outTreeFile, geninv_eta)
systTree.branchTreesSysts(trees, "all", "geninv_phi",           outTreeFile, geninv_phi)
systTree.branchTreesSysts(trees, "all", "geninv_mass",           outTreeFile, geninv_mass)

systTree.branchTreesSysts(trees, "all", "met_pt",           outTreeFile, met_pt)
systTree.branchTreesSysts(trees, "all", "met_phi",           outTreeFile, met_phi)
systTree.branchTreesSysts(trees, "all", "met_sumEt",           outTreeFile, met_sumEt)

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
    
    if True:#Debug:
        print("\nevento n. " + str(i))
    if i > 500 and Debug:#1000:
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
    genhtaus     = Collection(event, "GenVisTau")
    genparts     = None
    
    if isMC:
        genparts = Collection(event, "GenPart")
        if not ("WZ" in sample.label or "WWTo2L2Nu_DoubleScattering"):
            LHE = Collection(event, "LHEPart")
        if IsDim8:
            LHEDim8 = Collection(event, "LHEReweightingWeight")

    chain.GetEntry(i)
    #++++++++++++++++++++++++++++++++++
    #++      defining variables      ++
    #++++++++++++++++++++++++++++++++++

    GoodLep = None
    GoodTau = None
    mGoodLep = None
    mGoodTau = None
    genlepton = None
    gentau = None
    gmlepton = None
    gmtau = None
    geninv = None

    genlnu = None
    gentnu = None

    genleadjet = None
    gensubleadjet = None
    gmleadjet = None
    gmsubleadjet = None
    leadjet = None
    subleadjet = None
    mleadjet = None
    msubleadjet = None
    sgenjets = []
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

    sgenjets = SelectVBSQGenJet(genparts, genjets)

    if len(sgenjets) < 2 or None in sgenjets:
        continue

    genleadjet = sgenjets[0]
    gensubleadjet = sgenjets[1]

    print("in tree_skimmer:", genleadjet, genleadjet.eta, genleadjet.pt, gensubleadjet, gensubleadjet.eta, gensubleadjet.pt)
    genlepton, gentau = SelectGenLeptons(genparts)

    genlnu, gentnu = SelectGenNus(genparts)

    if (genlepton == None or gentau == None or genlnu == None or gentnu == None):
        continue

    if Debug:
        print(genlnu, gentnu)
    geninv = genlnu.p4() + gentnu.p4()

    genlnu_pt[0] = genlnu.pt
    genlnu_eta[0] = genlnu.eta
    genlnu_phi[0] = genlnu.phi
    genlnu_mass[0] = genlnu.mass

    gentnu_pt[0] = gentnu.pt
    gentnu_eta[0] = gentnu.eta
    gentnu_phi[0] = gentnu.phi
    gentnu_mass[0] = gentnu.mass

    geninv_pt[0] = geninv.Pt()
    geninv_eta[0] = geninv.Eta()
    geninv_phi[0] = geninv.Phi()
    geninv_mass[0] = geninv.M()

    met_pt[0] = met.pt
    met_phi[0] = met.phi
    met_sumEt[0] = met.sumEt

    genleadjet_pt[0]               =   genleadjet.pt
    genleadjet_eta[0]              =   genleadjet.eta
    genleadjet_phi[0]              =   genleadjet.phi
    genleadjet_mass[0]             =   genleadjet.mass
    genleadjet_partonFlavour[0]    =   genleadjet.partonFlavour
    gensubleadjet_pt[0]                =   gensubleadjet.pt
    gensubleadjet_eta[0]               =   gensubleadjet.eta
    gensubleadjet_phi[0]               =   gensubleadjet.phi
    gensubleadjet_mass[0]              =   gensubleadjet.mass
    gensubleadjet_partonFlavour[0]     =   gensubleadjet.partonFlavour
    gendeltaPhi_jj[0]   =   deltaPhi(genleadjet, gensubleadjet)
    gendeltaEta_jj[0]   =   genleadjet.eta - gensubleadjet.eta
    gendeltaTheta_jj[0] =   (genleadjet.p4() - gensubleadjet.p4()).CosTheta()
    genptRel_jj[0]      =   get_ptrel(genleadjet, gensubleadjet, 1.)
    genm_jj[0]          =   (genleadjet.p4() + gensubleadjet.p4()).M()

    genlepton_pt[0] = genlepton.pt
    genlepton_eta[0] = genlepton.eta
    genlepton_phi[0] = genlepton.phi
    genlepton_mass[0] = genlepton.mass
    genlepton_pdgid[0] = genlepton.pdgId
    genlepton_charge[0] = -int(genlepton.pdgId/abs(genlepton.pdgId))

    gentau_pt[0] = gentau.pt   
    gentau_eta[0] = gentau.eta
    gentau_phi[0] = gentau.phi 
    gentau_charge[0] = -int(gentau.pdgId/abs(gentau.pdgId))
    gentau_mass[0] = gentau.mass

    genlepton_Zeppenfeld, gentau_Zeppenfeld, genevent_Zeppenfeld = Zeppenfeld(genlepton.eta, gentau.eta, genleadjet.eta, gensubleadjet.eta)

    if gendeltaEta_jj[0] != 0.:
        genlepton_Zeppenfeld_over_deltaEta_jj[0] = genlepton_Zeppenfeld/gendeltaEta_jj[0]
        gentau_Zeppenfeld_over_deltaEta_jj[0] = gentau_Zeppenfeld/gendeltaEta_jj[0]
        genevent_Zeppenfeld_over_deltaEta_jj[0] = genevent_Zeppenfeld/gendeltaEta_jj[0]
    '''
    else:
        genlepton_Zeppenfeld_over_deltaEta_jj[0] = 0.#genlepton_Zeppenfeld/gendeltaEta_jj[0]
        gentau_Zeppenfeld_over_deltaEta_jj[0] = 0.#gentau_Zeppenfeld/gendeltaEta_jj[0]
        genevent_Zeppenfeld_over_deltaEta_jj[0] = 0.#genevent_Zeppenfeld/gendeltaEta_jj[0]
    '''

    gmleadjet = None
    gmsubleadjet = None

    for jet in jets:
        if not (jet.genJetIdx>-1 and jet.genJetIdx < len(genjets)):
            continue
        if genjets[jet.genJetIdx] == genleadjet:
            gmleadjet = jet
        elif genjets[jet.genJetIdx] == gensubleadjet:
            gmsubleadjet = jet

    if not (gmleadjet == None or gmsubleadjet == None):
        gmleadjet_pt[0]              =   gmleadjet.pt
        gmleadjet_eta[0]              =   gmleadjet.eta
        gmleadjet_phi[0]              =   gmleadjet.phi
        gmleadjet_mass[0]             =   gmleadjet.mass
        gmleadjet_DeepFlv_b[0]        =   gmleadjet.btagDeepFlavB
        gmleadjet_partonFlavour[0]    =   gmleadjet.btagDeepFlavB
        if gmleadjet.genJetIdx > -1 and gmleadjet.genJetIdx < len(genjets):
            if genjets[gmleadjet.genJetIdx] == genleadjet:
                gmleadjet_IsGenMatched[0] = 1
            else:
                gmleadjet_IsGenMatched[0] = 0
        else:
            gmleadjet_IsGenMatched[0] = 0

        gmsubleadjet_pt[0]            =   gmsubleadjet.pt
        gmsubleadjet_eta[0]           =   gmsubleadjet.eta
        gmsubleadjet_phi[0]           =   gmsubleadjet.phi
        gmsubleadjet_mass[0]          =   gmsubleadjet.mass
        gmsubleadjet_DeepFlv_b[0]     =   gmsubleadjet.btagDeepFlavB
        gmsubleadjet_partonFlavour[0] =   gmsubleadjet.btagDeepFlavB
        if gmsubleadjet.genJetIdx > -1 and gmsubleadjet.genJetIdx < len(genjets):
            if genjets[gmsubleadjet.genJetIdx] == gensubleadjet:
                gmsubleadjet_IsGenMatched[0] = 1
            else:
                gmsubleadjet_IsGenMatched[0] = 0
        else:
            gmsubleadjet_IsGenMatched[0] = 0

        gmdeltaPhi_jj[0]   =   deltaPhi(gmleadjet, gmsubleadjet)
        gmdeltaEta_jj[0]   =   gmleadjet.eta - gmsubleadjet.eta
        gmdeltaTheta_jj[0] =   (gmleadjet.p4() - gmsubleadjet.p4()).CosTheta()
        gmptRel_jj[0]      =   get_ptrel(gmleadjet, gmsubleadjet, 1.)
        gmm_jj[0]          =   (gmleadjet.p4() + gmsubleadjet.p4()).M()

    leptons = []
    for i, m in enumerate(muons):
        leptons.append(muons[i])
    for i, el in enumerate(electrons):
        leptons.append(electrons[i])

    gmlepton = SelectGenMatchedLep(leptons, genlepton, genparts)

    if gmlepton != None:
        gmlepton_pt[0] = gmlepton.pt
        gmlepton_eta[0] = gmlepton.eta
        gmlepton_phi[0] = gmlepton.phi
        gmlepton_mass[0] = gmlepton.mass
        gmlepton_charge[0] = gmlepton.charge
        gmlepton_pdgid[0] = gmlepton.pdgId
        gmlepton_IsGenMatched[0] = int(IsLepGenMatched(gmlepton, genlepton, genparts))
        gmlepton_genPartFlav[0] = gmlepton.genPartFlav

    gmtau = SelectGenVisTau(genhtaus)

    if gmtau != None:
        gmtau_pt[0] = gmtau.pt
        gmtau_eta[0] = gmtau.eta
        gmtau_phi[0] = gmtau.phi
        gmtau_charge[0] = gmtau.charge
        gmtau_mass[0] = gmtau.mass

    if not(gmleadjet == None or gmsubleadjet == None or gmlepton == None or gmtau == None):
        gmlepton_Zeppenfeld, gmtau_Zeppenfeld, gmevent_Zeppenfeld = Zeppenfeld(gmlepton.eta, gmtau.eta, gmleadjet.eta, gmsubleadjet.eta)
    
        gmlepton_Zeppenfeld_over_deltaEta_jj[0] = gmlepton_Zeppenfeld/gmdeltaEta_jj[0]
        gmtau_Zeppenfeld_over_deltaEta_jj[0] = gmtau_Zeppenfeld/gmdeltaEta_jj[0]
        gmevent_Zeppenfeld_over_deltaEta_jj[0] = gmevent_Zeppenfeld/gmdeltaEta_jj[0]
        

    nJets[0] = len(jets)
    nBJets[0] = CountBJets(jets)#
    nGenJets[0] = len(genjets)

    leadjet, subleadjet = SelectVBSJets(jets = list(jets), applyDeltaEtaCut = DeltaEtaCutBefore, lep1 = GoodLep, lep2 = GoodTau)
    mleadjet, msubleadjet = SelectVBSJets(jets = list(jets), useMassCrit = True, applyDeltaEtaCut = DeltaEtaCutBefore, lep1 = mGoodLep, lep2 = mGoodTau)

    if (leadjet == None or subleadjet == None) and (mleadjet == None or msubleadjet == None):
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        systTree.fillTreesSysts(trees, "all")
        continue  

    pass_jet_selection[0]=1

    if not (leadjet == None or subleadjet == None):
        leadjet_pt[0]               =   leadjet.pt
        leadjet_eta[0]              =   leadjet.eta
        leadjet_phi[0]              =   leadjet.phi
        leadjet_mass[0]             =   leadjet.mass
        leadjet_DeepFlv_b[0]        =   leadjet.btagDeepFlavB
        leadjet_partonFlavour[0]    =   leadjet.btagDeepFlavB

        if leadjet.genJetIdx > -1 and leadjet.genJetIdx < len(genjets):
            if genjets[leadjet.genJetIdx] == genleadjet:
                leadjet_IsGenMatched[0] = 1
            else:
                leadjet_IsGenMatched[0] = 0
        else:
            leadjet_IsGenMatched[0] = 0

        subleadjet_pt[0]            =   subleadjet.pt
        subleadjet_eta[0]           =   subleadjet.eta
        subleadjet_phi[0]           =   subleadjet.phi
        subleadjet_mass[0]          =   subleadjet.mass
        subleadjet_DeepFlv_b[0]     =   subleadjet.btagDeepFlavB
        subleadjet_partonFlavour[0] =   subleadjet.btagDeepFlavB

        if subleadjet.genJetIdx > -1 and subleadjet.genJetIdx < len(genjets):
            if genjets[subleadjet.genJetIdx] == gensubleadjet:
                subleadjet_IsGenMatched[0] = 1
            else:
                subleadjet_IsGenMatched[0] = 0
        else:
            subleadjet_IsGenMatched[0] = 0

        deltaPhi_jj[0]   =   deltaPhi(leadjet, subleadjet)
        deltaEta_jj[0]   =   leadjet.eta - subleadjet.eta
        deltaTheta_jj[0] =   (leadjet.p4() - subleadjet.p4()).CosTheta()
        ptRel_jj[0]      =   get_ptrel(leadjet, subleadjet, 1.)
        m_jj[0]          =   (leadjet.p4() + subleadjet.p4()).M()

    if not (mleadjet == None or msubleadjet == None):
        mleadjet_pt[0]               =   mleadjet.pt
        mleadjet_eta[0]              =   mleadjet.eta
        mleadjet_phi[0]              =   mleadjet.phi
        mleadjet_mass[0]             =   mleadjet.mass
        mleadjet_DeepFlv_b[0]        =   mleadjet.btagDeepFlavB
        mleadjet_partonFlavour[0]    =   mleadjet.btagDeepFlavB
        if mleadjet.genJetIdx > -1 and mleadjet.genJetIdx < len(genjets):
            if genjets[mleadjet.genJetIdx] == genleadjet:
                mleadjet_IsGenMatched[0] = 1
            else:
                mleadjet_IsGenMatched[0] = 0
        else:
            mleadjet_IsGenMatched[0] = 0

        msubleadjet_pt[0]            =   msubleadjet.pt
        msubleadjet_eta[0]           =   msubleadjet.eta
        msubleadjet_phi[0]           =   msubleadjet.phi
        msubleadjet_mass[0]          =   msubleadjet.mass
        msubleadjet_DeepFlv_b[0]     =   msubleadjet.btagDeepFlavB
        msubleadjet_partonFlavour[0] =   msubleadjet.btagDeepFlavB
        if msubleadjet.genJetIdx > -1 and msubleadjet.genJetIdx < len(genjets):
            if genjets[msubleadjet.genJetIdx] == gensubleadjet:
                msubleadjet_IsGenMatched[0] = 1
            else:
                msubleadjet_IsGenMatched[0] = 0
        else:
            msubleadjet_IsGenMatched[0] = 0

        mdeltaPhi_jj[0]   =   deltaPhi(leadjet, subleadjet)
        mdeltaEta_jj[0]   =   mleadjet.eta - msubleadjet.eta
        mdeltaTheta_jj[0] =   (mleadjet.p4() - msubleadjet.p4()).CosTheta()
        mptRel_jj[0]      =   get_ptrel(leadjet, msubleadjet, 1.)
        mm_jj[0]          =   (mleadjet.p4() + msubleadjet.p4()).M()

    #leading jet reco
    GoodLep = None
    leptons = None
    GoodTau = None
        
    SingleEle=False
    SingleMu=False
    ElMu=False

    if True:#not (leadjet == None or subleadjet == None):
        GoodEle, ele_TightRegion = SelectLepton(electrons, leadjet, subleadjet) 
        GoodMu, mu_TightRegion = SelectLepton(muons, leadjet, subleadjet) 
    
        ele_lepton_veto = False
        mu_lepton_veto = False

        if not (GoodEle == None and GoodMu == None):
            if GoodEle != None:
                ele_lepton_veto = LepVeto(GoodEle, electrons, muons)
            if GoodMu != None:
                mu_lepton_veto = LepVeto(GoodMu, electrons, muons)   
   
            if passEle and not passMu:
                if GoodEle != None and ele_lepton_veto:
                    GoodLep = GoodEle
                    lepton_TightRegion[0] = copy.deepcopy(ele_TightRegion)
                    SingleEle = True
                    SingleMu = False
                else:
                    pass

            elif passMu and not passEle:
                if GoodMu != None and mu_lepton_veto:
                    GoodLep = GoodMu
                    lepton_TightRegion[0] = copy.deepcopy(mu_TightRegion)
                    SingleEle = False
                    SingleMu = True
                else:
                    pass

            elif passMu and passEle:
                ElMu=True
        

            if ElMu:
                if GoodMu == None and GoodEle != None and ele_lepton_veto:
                    GoodLep = GoodEle
                    lepton_TightRegion[0] = copy.deepcopy(ele_TightRegion)
                    SingleEle = True
                    SingleMu = False

                elif GoodMu != None and mu_lepton_veto and GoodEle == None:
                    GoodLep = GoodMu
                    lepton_TightRegion[0] = copy.deepcopy(mu_TightRegion)
                    SingleMu = True
                    SingleEle = False
                
                elif GoodMu != None and GoodEle != None:
                    if ele_lepton_veto and not mu_lepton_veto:
                        GoodLep = GoodEle
                        lepton_TightRegion[0] = copy.deepcopy(ele_TightRegion)
                        SingleEle = True
                        SingleMu = False
                    elif not ele_lepton_veto and mu_lepton_veto:            
                        GoodLep = GoodMu
                        lepton_TightRegion[0] = copy.deepcopy(mu_TightRegion)
                        SingleMu = True
                        SingleEle = False

                    elif ele_lepton_veto and mu_lepton_veto:
                        if GoodEle.pt > GoodMu.pt:
                            GoodLep = GoodEle
                            lepton_TightRegion[0] = copy.deepcopy(ele_TightRegion)
                            SingleEle = True
                            SingleMu = False
                        else:
                            GoodLep = GoodMu
                            lepton_TightRegion[0] = copy.deepcopy(mu_TightRegion)
                            SingleMu = True
                            SingleEle = False
         
    #mass jet reco
    mGoodLep = None
    mleptons = None
    mGoodTau = None
        
    mSingleEle=False
    mSingleMu=False
    mElMu=False

    if True:#not (mleadjet == None or msubleadjet == None):
        mGoodEle, mele_TightRegion = SelectLepton(electrons, leadjet, subleadjet) 
        mGoodMu, mmu_TightRegion = SelectLepton(muons, leadjet, subleadjet) 
    
        mele_lepton_veto = False
        mmu_lepton_veto = False

        if not (mGoodEle == None and mGoodMu == None):
            if mGoodEle != None:
                mele_lepton_veto = LepVeto(mGoodEle, electrons, muons)
            if mGoodMu != None:
                mmu_lepton_veto = LepVeto(mGoodMu, electrons, muons)   
   
            if passEle and not passMu:
                if mGoodEle != None and mele_lepton_veto:
                    mGoodLep = mGoodEle
                    mlepton_TightRegion[0] = copy.deepcopy(mele_TightRegion)
                    mSingleEle = True
                    mSingleMu = False
                else:
                    pass

            elif passMu and not passEle:
                if mGoodMu != None and mmu_lepton_veto:
                    mGoodLep = mGoodMu
                    mlepton_TightRegion[0] = copy.deepcopy(mmu_TightRegion)
                    mSingleEle = False
                    mSingleMu = True
                else:
                    pass

            elif passMu and passEle:
                mElMu=True
        

            if mElMu:
                if mGoodMu == None and mGoodEle != None and mele_lepton_veto:
                    mGoodLep = mGoodEle
                    mlepton_TightRegion[0] = copy.deepcopy(mele_TightRegion)
                    mSingleEle = True
                    mSingleMu = False

                elif mGoodMu != None and mmu_lepton_veto and mGoodEle == None:
                    mGoodLep = mGoodMu
                    mlepton_TightRegion[0] = copy.deepcopy(mmu_TightRegion)
                    mSingleMu = True
                    mSingleEle = False
                
                elif mGoodMu != None and mGoodEle != None:
                    if mele_lepton_veto and not mmu_lepton_veto:
                        mGoodLep = mGoodEle
                        mlepton_TightRegion[0] = copy.deepcopy(mele_TightRegion)
                        mSingleEle = True
                        mSingleMu = False
                    elif not mele_lepton_veto and mmu_lepton_veto:            
                        mGoodLep = mGoodMu
                        mlepton_TightRegion[0] = copy.deepcopy(mmu_TightRegion)
                        mSingleMu = True
                        mSingleEle = False

                    elif mele_lepton_veto and mmu_lepton_veto:
                        if mGoodEle.pt > mGoodMu.pt:
                            mGoodLep = mGoodEle
                            mlepton_TightRegion[0] = copy.deepcopy(mele_TightRegion)
                            mSingleEle = True
                            mSingleMu = False
                        else:
                            mGoodLep = mGoodMu
                            mlepton_TightRegion[0] = copy.deepcopy(mmu_TightRegion)
                            mSingleMu = True
                            mSingleEle = False

    vTrigEle, vTrigMu, vTrigHT = trig_finder(HLT, sample.year, sample.label)
    
    if (SingleEle==True or mSingleEle==True):
        if isMC: 
            HLT_effLumi[0] = lumiFinder("Ele", vTrigEle)
    elif (SingleMu==True or mSingleMu==True):
        if isMC:
            HLT_effLumi[0] = lumiFinder("Mu", vTrigMu)

    elif not ((SingleMu or mSingleMu) or (SingleEle or mSingleEle)):
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        systTree.fillTreesSysts(trees, "all")
        continue

    if (SingleEle or SingleMu):
        if lepton_TightRegion[0]==1:
            lepton_LnTRegion[0] = 0
        elif lepton_TightRegion[0]==0:
            lepton_LnTRegion[0] = 1
        else:
            lepton_LnTRegion[0] = -999

    if (mSingleEle or mSingleMu):
        if mlepton_TightRegion[0]==1:
            mlepton_LnTRegion[0] = 0
        elif mlepton_TightRegion[0]==0:
            mlepton_LnTRegion[0] = 1
        else:
            mlepton_LnTRegion[0] = -999
    
    if (lepton_TightRegion[0] == 1 or lepton_LnTRegion[0] == 1 or mlepton_TightRegion[0] == 1 or mlepton_LnTRegion[0] == 1):
        pass_lepton_selection[0] = 1
        pass_lepton_veto[0] = 1
    else:
        pass_lepton_selection[0] = 0
        pass_lepton_veto[0] = 0

    if (GoodLep == None or (lepton_TightRegion[0]<0 and lepton_LnTRegion[0]<0)) and (mGoodLep == None or (mlepton_TightRegion[0]<0 and mlepton_LnTRegion[0]<0)): 
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        systTree.fillTreesSysts(trees, "all")
        continue

    if GoodLep != None:
        if abs(GoodLep.pdgId)==13:
            lepton_pt[0]                =   GoodLep.corrected_pt
        elif abs(GoodLep.pdgId)==11:
            lepton_pt[0]                =   GoodLep.pt
        lepton_eta[0]               =   GoodLep.eta
        lepton_phi[0]               =   GoodLep.phi
        lepton_mass[0]              =   GoodLep.mass
        lepton_pdgid[0]             =   GoodLep.pdgId
        lepton_charge[0] = -int(GoodLep.pdgId/abs(GoodLep.pdgId))
        lepton_genPartFlav[0] = GoodLep.genPartFlav
        lepton_IsGenMatched[0]  =   int(IsLepGenMatched(GoodLep, genlepton, genparts))


    if mGoodLep != None:
        if abs(mGoodLep.pdgId)==13:
            mlepton_pt[0]                =   mGoodLep.corrected_pt
        elif abs(GoodLep.pdgId)==11:
            lepton_pt[0]                =   mGoodLep.pt
        mlepton_eta[0]               =   mGoodLep.eta
        mlepton_phi[0]               =   mGoodLep.phi
        mlepton_mass[0]              =   mGoodLep.mass
        mlepton_pdgid[0]             =   mGoodLep.pdgId
        lepton_charge[0] = -int(mGoodLep.pdgId/abs(mGoodLep.pdgId))
        lepton_genPartFlav[0] = mGoodLep.genPartFlav
        lepton_IsGenMatched[0]  =   int(IsLepGenMatched(mGoodLep, genlepton, genparts))


    ThereIsOneTau = False
    tau_TightRegion = 0
    tau_LnTRegion = 0

    #lead jet reco
    if not (leadjet == None or subleadjet == None or GoodLep == None):
        ThereIsOneTau, ltau_list = SelectAndVetoTaus(list(taus), GoodLep, leadjet, subleadjet)
        if ThereIsOneTau:
            indexGoodTau = ltau_list[0][0]
            if ltau_list[0][1] == 'T':
                tau_TightRegion = 1
                tau_LnTRegion = 0
            elif ltau_list[0][1] == 'L':
                tau_TightRegion = 0
                tau_LnTRegion = 1            
                
            GoodTau = taus[indexGoodTau]

    #mass jet reco
    mThereIsOneTau = False
    mtau_TightRegion = -1
    mtau_LnTRegion = -1

    if not (mleadjet == None or msubleadjet == None or mGoodLep == None):
        mThereIsOneTau, mltau_list = SelectAndVetoTaus(list(taus), mGoodLep, mleadjet, msubleadjet)

        if mThereIsOneTau:
            mindexGoodTau = mltau_list[0][0]
            if mltau_list[0][1] == 'T':
                mtau_TightRegion = 1
                mtau_LnTRegion = 0
            elif mltau_list[0][1] == 'L':
                mtau_TightRegion = 0
                mtau_LnTRegion = 1            
                
            mGoodTau = taus[mindexGoodTau]

    if (tau_TightRegion==1 or tau_LnTRegion==1) or (mtau_TightRegion==1 or mtau_LnTRegion==1):
        pass_tau_selection[0] = 1
    else:
        pass_tau_selection[0] = 0

    if not (ThereIsOneTau or mThereIsOneTau):
        systTree.setWeightName("w_nominal",copy.deepcopy(w_nominal_all[0]))
        systTree.fillTreesSysts(trees, "all")
        continue

    if(ThereIsOneTau):
        tau_pt[0] = GoodTau.pt
        tau_phi[0] = GoodTau.phi
        tau_eta[0] = GoodTau.eta
        tau_charge[0] = GoodTau.charge
        tau_mass[0] = GoodTau.mass
        tau_IsGenMatched[0] =  float(GoodTau.genPartFlav==5)
        tau_DecayMode[0] = GoodTau.decayMode
        tau_DeepTauVsEle_raw[0] =  GoodTau.rawDeepTau2017v2p1VSe
        tau_DeepTauVsMu_raw[0] =  GoodTau.rawDeepTau2017v2p1VSmu
        tau_DeepTauVsJet_raw[0] =  GoodTau.rawDeepTau2017v2p1VSjet
        tau_genPartFlav[0] = GoodTau.genPartFlav

    if(mThereIsOneTau):
        mtau_pt[0] = mGoodTau.pt
        mtau_phi[0] = mGoodTau.phi
        mtau_eta[0] = mGoodTau.eta
        mtau_charge[0] = mGoodTau.charge
        mtau_mass[0] = mGoodTau.mass
        mtau_IsGenMatched[0] =  float(mGoodTau.genPartFlav==5)
        mtau_DecayMode[0] = mGoodTau.decayMode
        mtau_DeepTauVsEle_raw[0] =  mGoodTau.rawDeepTau2017v2p1VSe
        mtau_DeepTauVsMu_raw[0] =  mGoodTau.rawDeepTau2017v2p1VSmu
        mtau_DeepTauVsJet_raw[0] =  mGoodTau.rawDeepTau2017v2p1VSjet
        mtau_genPartFlav[0] = mGoodTau.genPartFlav


    if (GoodTau != None and GoodLep != None and GoodTau.charge==GoodLep.charge) or (mGoodTau != None and mGoodLep != None and mGoodTau.charge==mGoodLep.charge):
        pass_charge_selection[0]=1

    if not(leadjet == None or subleadjet == None or GoodLep == None or GoodTau == None):
        lepton_Zeppenfeld, tau_Zeppenfeld, event_Zeppenfeld = Zeppenfeld(GoodLep.eta, GoodTau.eta, leadjet.eta, subleadjet.eta)
    
        lepton_Zeppenfeld_over_deltaEta_jj[0] = lepton_Zeppenfeld/deltaEta_jj[0]
        tau_Zeppenfeld_over_deltaEta_jj[0] = tau_Zeppenfeld/deltaEta_jj[0]
        event_Zeppenfeld_over_deltaEta_jj[0] = event_Zeppenfeld/deltaEta_jj[0]

    if not(mleadjet == None or msubleadjet == None or mGoodLep == None or mGoodTau == None):
        mlepton_Zeppenfeld, mtau_Zeppenfeld, mevent_Zeppenfeld = Zeppenfeld(mGoodLep.eta, mGoodTau.eta, mleadjet.eta, msubleadjet.eta)
    
        mlepton_Zeppenfeld_over_deltaEta_jj[0] = mlepton_Zeppenfeld/mdeltaEta_jj[0]
        mtau_Zeppenfeld_over_deltaEta_jj[0] = mtau_Zeppenfeld/mdeltaEta_jj[0]
        mevent_Zeppenfeld_over_deltaEta_jj[0] = mevent_Zeppenfeld/mdeltaEta_jj[0]


    if not BVeto(jets):
        pass_b_veto[0]=1

    if (SingleEle or SingleMu or mSingleEle or mSingleMu) and pass_lepton_selection[0]==1 and pass_lepton_veto[0]==1 and pass_tau_selection[0]==1 and pass_charge_selection[0]==1 and pass_jet_selection[0]==1 and pass_b_veto[0]==1:
        pass_upToBVeto[0]=1#


    
    if not metCut(met): pass_MET_cut[0]=1

    if (SingleEle or SingleMu or mSingleEle or mSingleMu) and pass_lepton_selection[0]==1 and pass_lepton_veto[0]==1 and pass_tau_selection[0]==1 and pass_charge_selection[0]==1 and pass_jet_selection[0]==1 and pass_b_veto[0]==1 and pass_MET_cut[0]==1:
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
