import ROOT
import os 
#import json_reader as jr

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label, name=""):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label
        if name == "":
            self.name = label
        else:
            self.name = name

### color labels ###
ZZcolor = ROOT.kViolet-9
TTcolor = ROOT.kRed+2
TTdilepcolor = ROOT.kAzure-9
TVXcolor = ROOT.kCyan-7
VGcolor = ROOT.kSpring+7
WScolor = ROOT.kGreen-10

######### UL2016APV ##########

### ZZtoLep ###

ZZTo2L2Nu_UL2016APV = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_UL2016APV")
ZZTo2L2Nu_UL2016APV.year = "UL2016APV"
ZZTo2L2Nu_UL2016APV.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo2L2Nu_UL2016APV.sigma = 0.9738 #pb NLO

ZZTo4L_UL2016APV = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_UL2016APV") ### not sure is the right background
ZZTo4L_UL2016APV.year = "UL2016APV"
ZZTo4L_UL2016APV.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo4L_UL2016APV.sigma = 13.74 #pb NLO

#### to be produced ####
GluGluToContinToZZTo2e2nu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_UL2016APV")
GluGluToContinToZZTo2e2nu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2e2nu_UL2016APV.dataset = ""
GluGluToContinToZZTo2e2nu_UL2016APV.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_UL2016APV")
GluGluToContinToZZTo4e_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo4e_UL2016APV.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo4e_UL2016APV.sigma = 1.619 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2mu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_UL2016APV")
GluGluToContinToZZTo2e2mu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2e2mu_UL2016APV.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_UL2016APV.sigma = 3.292 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_UL2016APV")
GluGluToContinToZZTo2e2tau_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2e2tau_UL2016APV.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_UL2016APV.sigma = 3.294 # * 0.001 #pb to be checked

#### in production stage ######
GluGluToContinToZZTo2mu2nu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_UL2016APV")
GluGluToContinToZZTo2mu2nu_UL2016APV.year = "UL2016APV"
#GluGluToContinToZZTo2mu2nu_UL2016APV.dataset = ""
GluGluToContinToZZTo2mu2nu_UL2016APV.sigma = 17.73 # * 0.001 #pb to be checked

#### to be replaced with v9 when available ####
GluGluToContinToZZTo4mu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_UL2016APV")
GluGluToContinToZZTo4mu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo4mu_UL2016APV.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_UL2016APV.sigma = 1.608 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_UL2016APV")
GluGluToContinToZZTo2mu2tau_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2mu2tau_UL2016APV.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_UL2016APV.sigma = 3.294 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_UL2016APV")
GluGluToContinToZZTo2tau2nu_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo2tau2nu_UL2016APV.dataset = ""
GluGluToContinToZZTo2tau2nu_UL2016APV.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_UL2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_UL2016APV")
GluGluToContinToZZTo4tau_UL2016APV.year = "UL2016APV"
GluGluToContinToZZTo4tau_UL2016APV.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_UL2016APV.sigma = 1.626 # * 0.001 #pb to be checked

ZZtoLep_UL2016APV = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2016APV")
ZZtoLep_UL2016APV.year = "UL2016APV"
ZZtoLep_UL2016APV.components = [
    ZZTo2L2Nu_UL2016APV,
    ZZTo4L_UL2016APV,
    #GluGluToContinToZZTo2e2nu_UL2016APV,
    GluGluToContinToZZTo4e_UL2016APV,
    GluGluToContinToZZTo2e2mu_UL2016APV,
    GluGluToContinToZZTo2e2tau_UL2016APV,
    #GluGluToContinToZZTo2mu2nu_UL2016APV,
    GluGluToContinToZZTo4mu_UL2016APV,
    GluGluToContinToZZTo2mu2tau_UL2016APV,
    #GluGluToContinToZZTo2tau2nu_UL2016APV,
    GluGluToContinToZZTo4tau_UL2016APV,
]

### TT with quark ###

TT_SemiLep_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_UL2016APV")
TT_SemiLep_UL2016APV.year = "UL2016APV"
TT_SemiLep_UL2016APV.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TT_SemiLep_UL2016APV.sigma = 365.3 #pb to check

TT_Had_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_UL2016APV")
TT_Had_UL2016APV.year = "UL2016APV"
TT_Had_UL2016APV.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TT_Had_UL2016APV.sigma = 377.96 #pb to check

TT_UL2016APV = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2016APV")
TT_UL2016APV.year = "UL2016APV"
TT_UL2016APV.components = [
    TT_SemiLep_UL2016APV,
    TT_Had_UL2016APV,
]

TTTo2L2Nu_UL2016APV = sample(TTdilepcolor, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_UL2016APV")
TTTo2L2Nu_UL2016APV.year = "UL2016APV"
TTTo2L2Nu_UL2016APV.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TTTo2L2Nu_UL2016APV.sigma = 88.29 #pb

### TVX ###

TTGJets_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> qq", "TTGJets_UL2016APV")
TTGJets_UL2016APV.year = "UL2016APV"
TTGJets_UL2016APV.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
TTGJets_UL2016APV.sigma = 3.757

TTZToQQ_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_UL2016APV")
TTZToQQ_UL2016APV.year = "UL2016APV"
TTZToQQ_UL2016APV.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
TTZToQQ_UL2016APV.sigma = 0.5104

TTZToLLNuNu_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_UL2016APV")
TTZToLLNuNu_UL2016APV.year = "UL2016APV"
TTZToLLNuNu_UL2016APV.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTZToLLNuNu_UL2016APV.sigma = 0.2439

#### to be replaced with v9 when available ####
TTWJetsToQQ_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_UL2016APV")
TTWJetsToQQ_UL2016APV.year = "UL2016APV"
TTWJetsToQQ_UL2016APV.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToQQ_UL2016APV.sigma = 0.4377

#### to be replaced with v9 when available ####
TTWJetsToLNu_UL2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_UL2016APV")
TTWJetsToLNu_UL2016APV.year = "UL2016APV"
TTWJetsToLNu_UL2016APV.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToLNu_UL2016APV.sigma = 0.216

tZq_ll_4f_UL2016APV = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_UL2016APV")
tZq_ll_4f_UL2016APV.year = "UL2016APV"
tZq_ll_4f_UL2016APV.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
tZq_ll_4f_UL2016APV.sigma = 0.07561

TVX_UL2016APV = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2016APV")
TVX_UL2016APV.year = "UL2016APV"
TVX_UL2016APV.components = [
    TTGJets_UL2016APV,
    TTZToQQ_UL2016APV,
    TTZToLLNuNu_UL2016APV,
    TTWJetsToQQ_UL2016APV,
    TTWJetsToLNu_UL2016APV,
    tZq_ll_4f_UL2016APV,
]

### VG ###

#### to be replaced with v9 when available ####
ZG_UL2016APV = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_UL2016APV")
ZG_UL2016APV.year = "UL2016APV"
ZG_UL2016APV.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
ZG_UL2016APV.sigma = 51.1 # to check

WG_UL2016APV = sample(VGcolor, 1, 1001, "W #gamma", "WG_UL2016APV")
WG_UL2016APV.year = "UL2016APV"
WG_UL2016APV.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WG_UL2016APV.sigma = 191.3 # to check

VG_UL2016APV = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2016APV")
VG_UL2016APV.year = "UL2016APV"
VG_UL2016APV.components = [
    ZG_UL2016APV,
    WG_UL2016APV,
]

### WrongSign ###

WWto2L2Nu_UL2016APV = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "WWto2L2Nu_UL2016APV")
WWto2L2Nu_UL2016APV.year = "UL2016APV"
WWto2L2Nu_UL2016APV.dataset = "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WWto2L2Nu_UL2016APV.sigma = 11.09

GluGluToWWToENEN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> 2e2#nu", "GluGluToWWToENEN_UL2016APV")
GluGluToWWToENEN_UL2016APV.year = "UL2016APV"
GluGluToWWToENEN_UL2016APV.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToENEN_UL2016APV.sigma = 36.8 * 1./9. * 1.4

GluGluToWWToENMN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#mu2#nu", "GluGluToWWToENMN_UL2016APV")
GluGluToWWToENMN_UL2016APV.year = "UL2016APV"
GluGluToWWToENMN_UL2016APV.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToENMN_UL2016APV.sigma = 36.8 * 1./9. * 1.4

GluGluToWWToENTN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToENTN_UL2016APV")
GluGluToWWToENTN_UL2016APV.year = "UL2016APV"
GluGluToWWToENTN_UL2016APV.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToENTN_UL2016APV.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNEN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNEN_UL2016APV")
GluGluToWWToMNEN_UL2016APV.year = "UL2016APV"
GluGluToWWToMNEN_UL2016APV.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToMNEN_UL2016APV.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNMN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNMN_UL2016APV")
GluGluToWWToMNMN_UL2016APV.year = "UL2016APV"
GluGluToWWToMNMN_UL2016APV.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToMNMN_UL2016APV.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNTN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNTN_UL2016APV")
GluGluToWWToMNTN_UL2016APV.year = "UL2016APV"
GluGluToWWToMNTN_UL2016APV.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToMNTN_UL2016APV.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNEN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNEN_UL2016APV")
GluGluToWWToTNEN_UL2016APV.year = "UL2016APV"
GluGluToWWToTNEN_UL2016APV.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToTNEN_UL2016APV.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNMN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNMN_UL2016APV")
GluGluToWWToTNMN_UL2016APV.year = "UL2016APV"
GluGluToWWToTNMN_UL2016APV.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToTNMN_UL2016APV.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNTN_UL2016APV = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNTN_UL2016APV")
GluGluToWWToTNTN_UL2016APV.year = "UL2016APV"
GluGluToWWToTNTN_UL2016APV.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
GluGluToWWToTNTN_UL2016APV.sigma = 36.81 * 1./9. * 1.4

ST_tW_top_UL2016APV = sample(WScolor, 1, 1001, "Single top", "ST_tW_top_UL2016APV")
ST_tW_top_UL2016APV.year = "UL2016APV"
ST_tW_top_UL2016APV.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ST_tW_top_UL2016APV.sigma =  34.91

ST_tW_antitop_UL2016APV = sample(WScolor, 1, 1001, "Single top", "ST_tW_antitop_UL2016APV")
ST_tW_antitop_UL2016APV.year = "UL2016APV"
ST_tW_antitop_UL2016APV.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ST_tW_antitop_UL2016APV.sigma =  34.97

GluGluHToWWTo2L2Nu_UL2016APV = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWTo2L2Nu_UL2016APV")
GluGluHToWWTo2L2Nu_UL2016APV.year = "UL2016APV"
GluGluHToWWTo2L2Nu_UL2016APV.dataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluHToWWTo2L2Nu_UL2016APV.sigma = 28.86

#### to be produced ####
GluGluHToWWToLNuQQ_UL2016APV = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWToLNuQQ_UL2016APV")
GluGluHToWWToLNuQQ_UL2016APV.year = "UL2016APV"
GluGluHToWWToLNuQQ_UL2016APV.dataset = ""
GluGluHToWWToLNuQQ_UL2016APV.sigma = 0.# check nowe

#### in production stage ####
GluGluHToZZTo4L_UL2016APV = sample(WScolor, 1, 1001, "Single top", "GluGluHToZZTo4L_UL2016APV")
GluGluHToZZTo4L_UL2016APV.year = "UL2016APV"
GluGluHToZZTo4L_UL2016APV.dataset = ""
GluGluHToZZTo4L_UL2016APV.sigma = 28.84# check nowe

#### in production stage ####
GluGluHToTauTau_UL2016APV = sample(WScolor, 1, 1001, "Single top", "GluGluHToTauTau_UL2016APV")
GluGluHToTauTau_UL2016APV.year = "UL2016APV"
GluGluHToTauTau_UL2016APV.dataset = ""
GluGluHToTauTau_UL2016APV.sigma = 21.46# check nowe

VBFHToWWTo2L2Nu_UL2016APV = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2016APV")
VBFHToWWTo2L2Nu_UL2016APV.year = "UL2016APV"
VBFHToWWTo2L2Nu_UL2016APV.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2016APV.sigma = 3.892 # check nowe

VBFHToWWTo2L2Nu_UL2016APV = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2016APV")
VBFHToWWTo2L2Nu_UL2016APV.year = "UL2016APV"
VBFHToWWTo2L2Nu_UL2016APV.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2016APV.sigma = 3.892 # check nowe

#### in production stage ####
VBFHToTauTau_UL2016APV = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToTauTau_UL2016APV")
VBFHToTauTau_UL2016APV.year = "UL2016APV"
VBFHToTauTau_UL2016APV.dataset = ""
VBFHToTauTau_UL2016APV.sigma = 3.861 # check nowe

ttHToNonbb_UL2016APV = sample(WScolor, 1, 1001, "ttH", "ttHToNonbb_UL2016APV")
ttHToNonbb_UL2016APV.year = "UL2016APV"
ttHToNonbb_UL2016APV.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
ttHToNonbb_UL2016APV.sigma = 0.5638 # check nowe

VHToNonbb_UL2016APV = sample(WScolor, 1, 1001, "VH", "VHToNonbb_UL2016APV")
VHToNonbb_UL2016APV.year = "UL2016APV"
VHToNonbb_UL2016APV.dataset = "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
VHToNonbb_UL2016APV.sigma = 2.528 # check nowe

WrongSign_UL2016APV = sample(WScolor, 1, 1001, "V#gamma", "WrongSign_UL2016APV")
WrongSign_UL2016APV.year = "UL2016APV"
WrongSign_UL2016APV.components = [
    WWto2L2Nu_UL2016APV,
    GluGluToWWToENEN_UL2016APV,
    GluGluToWWToENMN_UL2016APV,
    GluGluToWWToENTN_UL2016APV,
    GluGluToWWToMNEN_UL2016APV,
    GluGluToWWToMNMN_UL2016APV,
    GluGluToWWToMNTN_UL2016APV,
    GluGluToWWToTNEN_UL2016APV,
    GluGluToWWToTNMN_UL2016APV,
    GluGluToWWToTNTN_UL2016APV,
    ST_tW_top_UL2016APV,
    ST_tW_antitop_UL2016APV,
    GluGluHToWWTo2L2Nu_UL2016APV,
    #GluGluHToWWToLNuQQ_UL2016APV,
    GluGluHToZZTo4L_UL2016APV,
    GluGluHToTauTau_UL2016APV,
    VBFHToWWTo2L2Nu_UL2016APV,
    #VBFHToTauTau_UL2016APV,
    ttHToNonbb_UL2016APV,
    VHToNonbb_UL2016APV,
]


######### UL2016 ##########

### ZZtoLep ###

ZZTo2L2Nu_UL2016 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_UL2016")
ZZTo2L2Nu_UL2016.year = "UL2016"
ZZTo2L2Nu_UL2016.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo2L2Nu_UL2016.sigma = 0.9738 #pb NLO

ZZTo4L_UL2016 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_UL2016") ### not sure is the right background
ZZTo4L_UL2016.year = "UL2016"
ZZTo4L_UL2016.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
ZZTo4L_UL2016.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_UL2016")
GluGluToContinToZZTo2e2nu_UL2016.year = "UL2016"
GluGluToContinToZZTo2e2nu_UL2016.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2nu_UL2016.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_UL2016")
GluGluToContinToZZTo4e_UL2016.year = "UL2016"
GluGluToContinToZZTo4e_UL2016.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
GluGluToContinToZZTo4e_UL2016.sigma = 1.619 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_UL2016")
GluGluToContinToZZTo2e2mu_UL2016.year = "UL2016"
GluGluToContinToZZTo2e2mu_UL2016.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2mu_UL2016.sigma = 3.292 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_UL2016")
GluGluToContinToZZTo2e2tau_UL2016.year = "UL2016"
GluGluToContinToZZTo2e2tau_UL2016.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2tau_UL2016.sigma = 3.294 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_UL2016")
GluGluToContinToZZTo2mu2nu_UL2016.year = "UL2016"
GluGluToContinToZZTo2mu2nu_UL2016.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_UL2016.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4mu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_UL2016")
GluGluToContinToZZTo4mu_UL2016.year = "UL2016"
GluGluToContinToZZTo4mu_UL2016.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
GluGluToContinToZZTo4mu_UL2016.sigma = 1.608 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_UL2016")
GluGluToContinToZZTo2mu2tau_UL2016.year = "UL2016"
GluGluToContinToZZTo2mu2tau_UL2016.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_UL2016.sigma = 3.294 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_UL2016")
GluGluToContinToZZTo2tau2nu_UL2016.year = "UL2016"
GluGluToContinToZZTo2tau2nu_UL2016.dataset = ""
GluGluToContinToZZTo2tau2nu_UL2016.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_UL2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_UL2016")
GluGluToContinToZZTo4tau_UL2016.year = "UL2016"
GluGluToContinToZZTo4tau_UL2016.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo4tau_UL2016.sigma = 1.626 # * 0.001 #pb to be checked

ZZtoLep_UL2016 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2016")
ZZtoLep_UL2016.year = "UL2016"
ZZtoLep_UL2016.components = [
    ZZTo2L2Nu_UL2016,
    ZZTo4L_UL2016,
    GluGluToContinToZZTo2e2nu_UL2016,
    GluGluToContinToZZTo4e_UL2016,
    GluGluToContinToZZTo2e2mu_UL2016,
    GluGluToContinToZZTo2e2tau_UL2016,
    GluGluToContinToZZTo2mu2nu_UL2016,
    GluGluToContinToZZTo4mu_UL2016,
    GluGluToContinToZZTo2mu2tau_UL2016,
    #GluGluToContinToZZTo2tau2nu_UL2016,
    GluGluToContinToZZTo4tau_UL2016,
]

### TT with quark ###

TT_SemiLep_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_UL2016")
TT_SemiLep_UL2016.year = "UL2016"
TT_SemiLep_UL2016.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TT_SemiLep_UL2016.sigma = 365.3 #pb to check

TT_Had_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_UL2016")
TT_Had_UL2016.year = "UL2016"
TT_Had_UL2016.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TT_Had_UL2016.sigma = 377.96 #pb to check

TT_UL2016 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2016")
TT_UL2016.year = "UL2016"
TT_UL2016.components = [
    TT_SemiLep_UL2016,
    TT_Had_UL2016,
]

TTTo2L2Nu_UL2016 = sample(TTdilepcolor, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_UL2016")
TTTo2L2Nu_UL2016.year = "UL2016"
TTTo2L2Nu_UL2016.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTTo2L2Nu_UL2016.sigma =  88.29 #pb

### TVX ###

TTGJets_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_UL2016")
TTGJets_UL2016.year = "UL2016"
TTGJets_UL2016.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTGJets_UL2016.sigma = 3.757

TTZToQQ_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_UL2016")
TTZToQQ_UL2016.year = "UL2016"
TTZToQQ_UL2016.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTZToQQ_UL2016.sigma = 0.5104

TTZToLLNuNu_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_UL2016")
TTZToLLNuNu_UL2016.year = "UL2016"
TTZToLLNuNu_UL2016.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTZToLLNuNu_UL2016.sigma = 0.2439

TTWJetsToQQ_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_UL2016")
TTWJetsToQQ_UL2016.year = "UL2016"
TTWJetsToQQ_UL2016.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTWJetsToQQ_UL2016.sigma = 0.4377

TTWJetsToLNu_UL2016 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_UL2016")
TTWJetsToLNu_UL2016.year = "UL2016"
TTWJetsToLNu_UL2016.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToLNu_UL2016.sigma = 0.216

tZq_ll_4f_UL2016 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_UL2016")
tZq_ll_4f_UL2016.year = "UL2016"
tZq_ll_4f_UL2016.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
tZq_ll_4f_UL2016.sigma = 0.07561

TVX_UL2016 = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2016")
TVX_UL2016.year = "UL2016"
TVX_UL2016.components = [
    TTGJets_UL2016,
    TTZToQQ_UL2016,
    TTZToLLNuNu_UL2016,
    TTWJetsToQQ_UL2016,
    TTWJetsToLNu_UL2016,
    tZq_ll_4f_UL2016,
]

### VG ###

ZG_UL2016 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_UL2016")
ZG_UL2016.year = "UL2016"
ZG_UL2016.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
ZG_UL2016.sigma = 51.1 # to check

WG_UL2016 = sample(VGcolor, 1, 1001, "W #gamma", "WG_UL2016")
WG_UL2016.year = "UL2016"
WG_UL2016.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WG_UL2016.sigma = 191.3 # to check

VG_UL2016 = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2016")
VG_UL2016.year = "UL2016"
VG_UL2016.components = [
    ZG_UL2016,
    WG_UL2016,
]

### WrongSign ###

WWto2L2Nu_UL2016 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "WWto2L2Nu_UL2016")
WWto2L2Nu_UL2016.year = "UL2016"
WWto2L2Nu_UL2016.dataset = "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WWto2L2Nu_UL2016.sigma = 11.09

GluGluToWWToENEN_UL2016 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENEN_UL2016")
GluGluToWWToENEN_UL2016.year = "UL2016"
GluGluToWWToENEN_UL2016.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToENEN_UL2016.sigma = 36.8

GluGluToWWToENMN_UL2016 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENMN_UL2016")
GluGluToWWToENMN_UL2016.year = "UL2016"
GluGluToWWToENMN_UL2016.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToENMN_UL2016.sigma = 36.8

GluGluToWWToENTN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToENTN_UL2016")
GluGluToWWToENTN_UL2016.year = "UL2016"
GluGluToWWToENTN_UL2016.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToENTN_UL2016.sigma = 36.81

GluGluToWWToMNEN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNEN_UL2016")
GluGluToWWToMNEN_UL2016.year = "UL2016"
GluGluToWWToMNEN_UL2016.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToMNEN_UL2016.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNMN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNMN_UL2016")
GluGluToWWToMNMN_UL2016.year = "UL2016"
GluGluToWWToMNMN_UL2016.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToMNMN_UL2016.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNTN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNTN_UL2016")
GluGluToWWToMNTN_UL2016.year = "UL2016"
GluGluToWWToMNTN_UL2016.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToMNTN_UL2016.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNEN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNEN_UL2016")
GluGluToWWToTNEN_UL2016.year = "UL2016"
GluGluToWWToTNEN_UL2016.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToTNEN_UL2016.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNMN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNMN_UL2016")
GluGluToWWToTNMN_UL2016.year = "UL2016"
GluGluToWWToTNMN_UL2016.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToTNMN_UL2016.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNTN_UL2016 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNTN_UL2016")
GluGluToWWToTNTN_UL2016.year = "UL2016"
GluGluToWWToTNTN_UL2016.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToWWToTNTN_UL2016.sigma = 36.81 * 1./9. * 1.4

ST_tW_top_UL2016 = sample(WScolor, 1, 1001, "Single top", "ST_tW_top_UL2016")
ST_tW_top_UL2016.year = "UL2016"
ST_tW_top_UL2016.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
ST_tW_top_UL2016.sigma = 34.91

ST_tW_antitop_UL2016 = sample(WScolor, 1, 1001, "Single top", "ST_tW_antitop_UL2016")
ST_tW_antitop_UL2016.year = "UL2016"
ST_tW_antitop_UL2016.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
ST_tW_antitop_UL2016.sigma =  34.97

GluGluHToWWTo2L2Nu_UL2016 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWTo2L2Nu_UL2016")
GluGluHToWWTo2L2Nu_UL2016.year = "UL2016"
GluGluHToWWTo2L2Nu_UL2016.dataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluHToWWTo2L2Nu_UL2016.sigma = 28.86

#### to be produced ####
GluGluHToWWToLNuQQ_UL2016 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWToLNuQQ_UL2016")
GluGluHToWWToLNuQQ_UL2016.year = "UL2016"
GluGluHToWWToLNuQQ_UL2016.dataset = ""
GluGluHToWWToLNuQQ_UL2016.sigma = 0.# check nowe

GluGluHToZZTo4L_UL2016 = sample(WScolor, 1, 1001, "Single top", "GluGluHToZZTo4L_UL2016")
GluGluHToZZTo4L_UL2016.year = "UL2016"
GluGluHToZZTo4L_UL2016.dataset = "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
GluGluHToZZTo4L_UL2016.sigma = 28.84 # check nowe

#### to be replaced with v9 when available ####
GluGluHToTauTau_UL2016 = sample(WScolor, 1, 1001, "Single top", "GluGluHToTauTau_UL2016")
GluGluHToTauTau_UL2016.year = "UL2016"
GluGluHToTauTau_UL2016.dataset = "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv2-106X_mcRun2_asymptotic_v15-v1/NANOAODSIM"
GluGluHToTauTau_UL2016.sigma = 21.46# check nowe

VBFHToWWTo2L2Nu_UL2016 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2016")
VBFHToWWTo2L2Nu_UL2016.year = "UL2016"
VBFHToWWTo2L2Nu_UL2016.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2016.sigma = 3.892 # check nowe

VBFHToTauTau_UL2016 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToTauTau_UL2016")
VBFHToTauTau_UL2016.year = "UL2016"
VBFHToTauTau_UL2016.dataset = "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
VBFHToTauTau_UL2016.sigma = 3.861 # check nowe

ttHToNonbb_UL2016 = sample(WScolor, 1, 1001, "ttH", "ttHToNonbb_UL2016")
ttHToNonbb_UL2016.year = "UL2016"
ttHToNonbb_UL2016.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
ttHToNonbb_UL2016.sigma = 0.5638 # check nowe

VHToNonbb_UL2016 = sample(WScolor, 1, 1001, "VH", "VHToNonbb_UL2016")
VHToNonbb_UL2016.year = "UL2016"
VHToNonbb_UL2016.dataset = "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
VHToNonbb_UL2016.sigma = 2.528 # check nowe

WrongSign_UL2016 = sample(WScolor, 1, 1001, "V#gamma", "WrongSign_UL2016")
WrongSign_UL2016.year = "UL2016"
WrongSign_UL2016.components = [
    WWto2L2Nu_UL2016,
    GluGluToWWToENEN_UL2016,
    GluGluToWWToENMN_UL2016,
    GluGluToWWToENTN_UL2016,
    GluGluToWWToMNEN_UL2016,
    GluGluToWWToMNMN_UL2016,
    GluGluToWWToMNTN_UL2016,
    GluGluToWWToTNEN_UL2016,
    GluGluToWWToTNMN_UL2016,
    GluGluToWWToTNTN_UL2016,
    ST_tW_top_UL2016,
    ST_tW_antitop_UL2016,
    GluGluHToWWTo2L2Nu_UL2016,
    #GluGluHToWWToLNuQQ_UL2016,
    GluGluHToZZTo4L_UL2016,
    GluGluHToTauTau_UL2016,
    VBFHToWWTo2L2Nu_UL2016,
    VBFHToTauTau_UL2016,
    ttHToNonbb_UL2016,
    VHToNonbb_UL2016,
]

######### UL2017 ##########

### ZZtoLep ###

ZZTo2L2Nu_UL2017 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_UL2017")
ZZTo2L2Nu_UL2017.year = "UL2017"
ZZTo2L2Nu_UL2017.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZZTo2L2Nu_UL2017.sigma = 0.9738 #pb NLO

ZZTo4L_UL2017 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_UL2017") ### not sure is the right background
ZZTo4L_UL2017.year = "UL2017"
ZZTo4L_UL2017.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZZTo4L_UL2017.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_UL2017")
GluGluToContinToZZTo2e2nu_UL2017.year = "UL2017"
GluGluToContinToZZTo2e2nu_UL2017.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2nu_UL2017.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_UL2017")
GluGluToContinToZZTo4e_UL2017.year = "UL2017"
GluGluToContinToZZTo4e_UL2017.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4e_UL2017.sigma = 1.619 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_UL2017")
GluGluToContinToZZTo2e2mu_UL2017.year = "UL2017"
GluGluToContinToZZTo2e2mu_UL2017.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_UL2017.sigma = 3.292 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_UL2017")
GluGluToContinToZZTo2e2tau_UL2017.year = "UL2017"
GluGluToContinToZZTo2e2tau_UL2017.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_UL2017.sigma = 3.294 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_UL2017")
GluGluToContinToZZTo2mu2nu_UL2017.year = "UL2017"
GluGluToContinToZZTo2mu2nu_UL2017.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_UL2017.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4mu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_UL2017")
GluGluToContinToZZTo4mu_UL2017.year = "UL2017"
GluGluToContinToZZTo4mu_UL2017.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4mu_UL2017.sigma = 1.608 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_UL2017")
GluGluToContinToZZTo2mu2tau_UL2017.year = "UL2017"
GluGluToContinToZZTo2mu2tau_UL2017.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_UL2017.sigma = 3.294 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_UL2017")
GluGluToContinToZZTo2tau2nu_UL2017.year = "UL2017"
GluGluToContinToZZTo2tau2nu_UL2017.dataset = ""
GluGluToContinToZZTo2tau2nu_UL2017.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_UL2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_UL2017")
GluGluToContinToZZTo4tau_UL2017.year = "UL2017"
GluGluToContinToZZTo4tau_UL2017.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_UL2017.sigma = 1.626 # * 0.001 #pb to be checked

ZZtoLep_UL2017 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2017")
ZZtoLep_UL2017.year = "UL2017"
ZZtoLep_UL2017.components = [
    ZZTo2L2Nu_UL2017,
    ZZTo4L_UL2017,
    GluGluToContinToZZTo2e2nu_UL2017,
    GluGluToContinToZZTo4e_UL2017,
    GluGluToContinToZZTo2e2mu_UL2017,
    GluGluToContinToZZTo2e2tau_UL2017,
    GluGluToContinToZZTo2mu2nu_UL2017,
    GluGluToContinToZZTo4mu_UL2017,
    GluGluToContinToZZTo2mu2tau_UL2017,
    #GluGluToContinToZZTo2tau2nu_UL2017,
    GluGluToContinToZZTo4tau_UL2017,
]

### TT with quark ###

TT_SemiLep_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_UL2017")
TT_SemiLep_UL2017.year = "UL2017"
TT_SemiLep_UL2017.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM"
TT_SemiLep_UL2017.sigma = 365.3 #pb to check

#### in production stage ####
TT_Had_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_UL2017")
TT_Had_UL2017.year = "UL2017"
TT_Had_UL2017.dataset = ""
TT_Had_UL2017.sigma = 377.96 #pb to check

TT_UL2017 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2017")
TT_UL2017.year = "UL2017"
TT_UL2017.components = [
    TT_SemiLep_UL2017,
    #TT_Had_UL2017,
]

TTTo2L2Nu_UL2017 = sample(TTdilepcolor, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_UL2017")
TTTo2L2Nu_UL2017.year = "UL2017"
TTTo2L2Nu_UL2017.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTTo2L2Nu_UL2017.sigma =  88.29 #pb

### TVX ###

TTGJets_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_UL2017")
TTGJets_UL2017.year = "UL2017"
TTGJets_UL2017.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTGJets_UL2017.sigma = 3.757

TTZToQQ_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_UL2017")
TTZToQQ_UL2017.year = "UL2017"
TTZToQQ_UL2017.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTZToQQ_UL2017.sigma = 0.5104

TTZToLLNuNu_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_UL2017")
TTZToLLNuNu_UL2017.year = "UL2017"
TTZToLLNuNu_UL2017.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTZToLLNuNu_UL2017.sigma = 0.2439

TTWJetsToQQ_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_UL2017")
TTWJetsToQQ_UL2017.year = "UL2017"
TTWJetsToQQ_UL2017.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTWJetsToQQ_UL2017.sigma = 0.4377

TTWJetsToLNu_UL2017 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_UL2017")
TTWJetsToLNu_UL2017.year = "UL2017"
TTWJetsToLNu_UL2017.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
TTWJetsToLNu_UL2017.sigma = 0.216

tZq_ll_4f_UL2017 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_UL2017")
tZq_ll_4f_UL2017.year = "UL2017"
tZq_ll_4f_UL2017.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
tZq_ll_4f_UL2017.sigma = 0.07561

TVX_UL2017 = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2017")
TVX_UL2017.year = "UL2017"
TVX_UL2017.components = [
    TTGJets_UL2017,
    TTZToQQ_UL2017,
    TTZToLLNuNu_UL2017,
    TTWJetsToQQ_UL2017,
    TTWJetsToLNu_UL2017,
    tZq_ll_4f_UL2017,
]

### VG ###

ZG_UL2017 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_UL2017")
ZG_UL2017.year = "UL2017"
ZG_UL2017.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZG_UL2017.sigma = 51.1 # to check

WG_UL2017 = sample(VGcolor, 1, 1001, "W #gamma", "WG_UL2017")
WG_UL2017.year = "UL2017"
WG_UL2017.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WG_UL2017.sigma = 191.3 # to check

VG_UL2017 = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2017")
VG_UL2017.year = "UL2017"
VG_UL2017.components = [
    ZG_UL2017,
    WG_UL2017,
]

### WrongSign ###

WWto2L2Nu_UL2017 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "WWto2L2Nu_UL2017")
WWto2L2Nu_UL2017.year = "UL2017"
WWto2L2Nu_UL2017.dataset = "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
WWto2L2Nu_UL2017.sigma = 11.09

GluGluToWWToENEN_UL2017 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENEN_UL2017")
GluGluToWWToENEN_UL2017.year = "UL2017"
GluGluToWWToENEN_UL2017.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToENEN_UL2017.sigma = 36.8

GluGluToWWToENMN_UL2017 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENMN_UL2017")
GluGluToWWToENMN_UL2017.year = "UL2017"
GluGluToWWToENMN_UL2017.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToENMN_UL2017.sigma = 36.8

GluGluToWWToENTN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToENTN_UL2017")
GluGluToWWToENTN_UL2017.year = "UL2017"
GluGluToWWToENTN_UL2017.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToENTN_UL2017.sigma = 36.81

GluGluToWWToMNEN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNEN_UL2017")
GluGluToWWToMNEN_UL2017.year = "UL2017"
GluGluToWWToMNEN_UL2017.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToMNEN_UL2017.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNMN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNMN_UL2017")
GluGluToWWToMNMN_UL2017.year = "UL2017"
GluGluToWWToMNMN_UL2017.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToMNMN_UL2017.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNTN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNTN_UL2017")
GluGluToWWToMNTN_UL2017.year = "UL2017"
GluGluToWWToMNTN_UL2017.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToMNTN_UL2017.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNEN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNEN_UL2017")
GluGluToWWToTNEN_UL2017.year = "UL2017"
GluGluToWWToTNEN_UL2017.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToTNEN_UL2017.sigma = 36.81 * 1./9. * 1.4

#### to be replaced with v9 when available ####
GluGluToWWToTNMN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNMN_UL2017")
GluGluToWWToTNMN_UL2017.year = "UL2017"
GluGluToWWToTNMN_UL2017.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM"
GluGluToWWToTNMN_UL2017.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNTN_UL2017 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNTN_UL2017")
GluGluToWWToTNTN_UL2017.year = "UL2017"
GluGluToWWToTNTN_UL2017.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluToWWToTNTN_UL2017.sigma = 36.81 * 1./9. * 1.4

ST_tW_top_UL2017 = sample(WScolor, 1, 1001, "Single top", "ST_tW_top_UL2017")
ST_tW_top_UL2017.year = "UL2017"
ST_tW_top_UL2017.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
ST_tW_top_UL2017.sigma = 34.91

ST_tW_antitop_UL2017 = sample(WScolor, 1, 1001, "Single top", "ST_tW_antitop_UL2017")
ST_tW_antitop_UL2017.year = "UL2017"
ST_tW_antitop_UL2017.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
ST_tW_antitop_UL2017.sigma =  34.97

#### to be replaced with v9 when available ####
GluGluHToWWTo2L2Nu_UL2017 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWTo2L2Nu_UL2017")
GluGluHToWWTo2L2Nu_UL2017.year = "UL2017"
GluGluHToWWTo2L2Nu_UL2017.dataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/RunIISummer20UL17NanoAODv2-106X_mc2017_realistic_v8-v1/NANOAODSIM"
GluGluHToWWTo2L2Nu_UL2017.sigma = 28.86

#### to be produced ####
GluGluHToWWToLNuQQ_UL2017 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWToLNuQQ_UL2017")
GluGluHToWWToLNuQQ_UL2017.year = "UL2017"
GluGluHToWWToLNuQQ_UL2017.dataset = ""
GluGluHToWWToLNuQQ_UL2017.sigma = 0.# check nowe

GluGluHToZZTo4L_UL2017 = sample(WScolor, 1, 1001, "Single top", "GluGluHToZZTo4L_UL2017")
GluGluHToZZTo4L_UL2017.year = "UL2017"
GluGluHToZZTo4L_UL2017.dataset = "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluHToZZTo4L_UL2017.sigma = 28.84# check nowe

GluGluHToTauTau_UL2017 = sample(WScolor, 1, 1001, "Single top", "GluGluHToTauTau_UL2017")
GluGluHToTauTau_UL2017.year = "UL2017"
GluGluHToTauTau_UL2017.dataset = "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
GluGluHToTauTau_UL2017.sigma = 21.46# check nowe

VBFHToWWTo2L2Nu_UL2017 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2017")
VBFHToWWTo2L2Nu_UL2017.year = "UL2017"
VBFHToWWTo2L2Nu_UL2017.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2017.sigma = 3.892 # check nowe

VBFHToTauTau_UL2017 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToTauTau_UL2017")
VBFHToTauTau_UL2017.year = "UL2017"
VBFHToTauTau_UL2017.dataset = "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
VBFHToTauTau_UL2017.sigma = 3.861 # check nowe

ttHToNonbb_UL2017 = sample(WScolor, 1, 1001, "ttH", "ttHToNonbb_UL2017")
ttHToNonbb_UL2017.year = "UL2017"
ttHToNonbb_UL2017.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
ttHToNonbb_UL2017.sigma = 0.5638 # check nowe

VHToNonbb_UL2017 = sample(WScolor, 1, 1001, "VH", "VHToNonbb_UL2017")
VHToNonbb_UL2017.year = "UL2017"
VHToNonbb_UL2017.dataset = "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
VHToNonbb_UL2017.sigma = 2.528 # check nowe

WrongSign_UL2017 = sample(WScolor, 1, 1001, "V#gamma", "WrongSign_UL2017")
WrongSign_UL2017.year = "UL2017"
WrongSign_UL2017.components = [
    WWto2L2Nu_UL2017,
    GluGluToWWToENEN_UL2017,
    GluGluToWWToENMN_UL2017,
    GluGluToWWToENTN_UL2017,
    GluGluToWWToMNEN_UL2017,
    GluGluToWWToMNMN_UL2017,
    GluGluToWWToMNTN_UL2017,
    GluGluToWWToTNEN_UL2017,
    GluGluToWWToTNMN_UL2017,
    GluGluToWWToTNTN_UL2017,
    ST_tW_top_UL2017,
    ST_tW_antitop_UL2017,
    GluGluHToWWTo2L2Nu_UL2017,
    #GluGluHToWWToLNuQQ_UL2017,
    GluGluHToZZTo4L_UL2017,
    GluGluHToTauTau_UL2017,
    VBFHToWWTo2L2Nu_UL2017,
    VBFHToTauTau_UL2017,
    ttHToNonbb_UL2017,
    VHToNonbb_UL2017,
]


######### UL2018 ##########

### ZZtoLep ###

ZZTo2L2Nu_UL2018 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_UL2018")
ZZTo2L2Nu_UL2018.year = "UL2018"
ZZTo2L2Nu_UL2018.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZZTo2L2Nu_UL2018.sigma = 0.9738 #pb NLO

ZZTo4L_UL2018 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_UL2018") ### not sure is the right background
ZZTo4L_UL2018.year = "UL2018"
ZZTo4L_UL2018.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZZTo4L_UL2018.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_UL2018")
GluGluToContinToZZTo2e2nu_UL2018.year = "UL2018"
GluGluToContinToZZTo2e2nu_UL2018.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2nu_UL2018.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_UL2018")
GluGluToContinToZZTo4e_UL2018.year = "UL2018"
GluGluToContinToZZTo4e_UL2018.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo4e_UL2018.sigma = 1.619 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_UL2018")
GluGluToContinToZZTo2e2mu_UL2018.year = "UL2018"
GluGluToContinToZZTo2e2mu_UL2018.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_UL2018.sigma = 3.292 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_UL2018")
GluGluToContinToZZTo2e2tau_UL2018.year = "UL2018"
GluGluToContinToZZTo2e2tau_UL2018.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_UL2018.sigma = 3.294 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_UL2018")
GluGluToContinToZZTo2mu2nu_UL2018.year = "UL2018"
GluGluToContinToZZTo2mu2nu_UL2018.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_UL2018.sigma = 17.73 # * 0.001 #pb to be checked

#### to be replaced with v9 when available ####
GluGluToContinToZZTo4mu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_UL2018")
GluGluToContinToZZTo4mu_UL2018.year = "UL2018"
GluGluToContinToZZTo4mu_UL2018.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_UL2018.sigma = 1.608 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_UL2018")
GluGluToContinToZZTo2mu2tau_UL2018.year = "UL2018"
GluGluToContinToZZTo2mu2tau_UL2018.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_UL2018.sigma = 3.294 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_UL2018")
GluGluToContinToZZTo2tau2nu_UL2018.year = "UL2018"
GluGluToContinToZZTo2tau2nu_UL2018.dataset = ""
GluGluToContinToZZTo2tau2nu_UL2018.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_UL2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_UL2018")
GluGluToContinToZZTo4tau_UL2018.year = "UL2018"
GluGluToContinToZZTo4tau_UL2018.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_UL2018.sigma = 1.626 # * 0.001 #pb to be checked

ZZtoLep_UL2018 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_UL2018")
ZZtoLep_UL2018.year = "UL2018"
ZZtoLep_UL2018.components = [
    ZZTo2L2Nu_UL2018,
    ZZTo4L_UL2018,
    GluGluToContinToZZTo2e2nu_UL2018,
    GluGluToContinToZZTo4e_UL2018,
    GluGluToContinToZZTo2e2mu_UL2018,
    GluGluToContinToZZTo2e2tau_UL2018,
    GluGluToContinToZZTo2mu2nu_UL2018,
    GluGluToContinToZZTo4mu_UL2018,
    GluGluToContinToZZTo2mu2tau_UL2018,
    #GluGluToContinToZZTo2tau2nu_UL2018,
    GluGluToContinToZZTo4tau_UL2018,
]

TT_SemiLep_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_UL2018")
TT_SemiLep_UL2018.year = "UL2018"
TT_SemiLep_UL2018.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TT_SemiLep_UL2018.sigma = 687.1 #pb to check

TT_Had_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_UL2018")
TT_Had_UL2018.year = "UL2018"
TT_Had_UL2018.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TT_Had_UL2018.sigma = 687.1 #pb to check

TT_UL2018 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_UL2018")
TT_UL2018.year = "UL2018"
TT_UL2018.components = [
    TT_SemiLep_UL2018,
    TT_Had_UL2018,
]

TTTo2L2Nu_UL2018 = sample(TTdilepcolor, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_UL2018")
TTTo2L2Nu_UL2018.year = "UL2018"
TTTo2L2Nu_UL2018.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTTo2L2Nu_UL2018.sigma =  88.29 #pb

### TVX ###

TTGJets_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_UL2018")
TTGJets_UL2018.year = "UL2018"
TTGJets_UL2018.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTGJets_UL2018.sigma = 3.757

TTZToQQ_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_UL2018")
TTZToQQ_UL2018.year = "UL2018"
TTZToQQ_UL2018.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTZToQQ_UL2018.sigma = 0.5104

TTZToLLNuNu_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_UL2018")
TTZToLLNuNu_UL2018.year = "UL2018"
TTZToLLNuNu_UL2018.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTZToLLNuNu_UL2018.sigma = 0.2439

TTWJetsToQQ_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_UL2018")
TTWJetsToQQ_UL2018.year = "UL2018"
TTWJetsToQQ_UL2018.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTWJetsToQQ_UL2018.sigma = 0.4377

#### to be replaced with v9 when available ####
TTWJetsToLNu_UL2018 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_UL2018")
TTWJetsToLNu_UL2018.year = "UL2018"
TTWJetsToLNu_UL2018.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
TTWJetsToLNu_UL2018.sigma = 0.216

#### to be replaced with v9 when available ####
tZq_ll_4f_UL2018 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_UL2018")
tZq_ll_4f_UL2018.year = "UL2018"
tZq_ll_4f_UL2018.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
tZq_ll_4f_UL2018.sigma = 0.07561

TVX_UL2018 = sample(TVXcolor, 1, 1001, "tVX", "TVX_UL2018")
TVX_UL2018.year = "UL2018"
TVX_UL2018.components = [
    TTGJets_UL2018,
    TTZToQQ_UL2018,
    TTZToLLNuNu_UL2018,
    TTWJetsToQQ_UL2018,
    TTWJetsToLNu_UL2018,
    tZq_ll_4f_UL2018,
]

### VG ###

ZG_UL2018 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_UL2018")
ZG_UL2018.year = "UL2018"
ZG_UL2018.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZG_UL2018.sigma = 51.1 # to check

WG_UL2018 = sample(VGcolor, 1, 1001, "W #gamma", "WG_UL2018")
WG_UL2018.year = "UL2018"
WG_UL2018.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WG_UL2018.sigma = 191.3 # to check

VG_UL2018 = sample(VGcolor, 1, 1001, "V#gamma", "VG_UL2018")
VG_UL2018.year = "UL2018"
VG_UL2018.components = [
    ZG_UL2018,
    WG_UL2018,
]

### WrongSign ###

WWto2L2Nu_UL2018 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "WWto2L2Nu_UL2018")
WWto2L2Nu_UL2018.year = "UL2018"
WWto2L2Nu_UL2018.dataset = "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WWto2L2Nu_UL2018.sigma = 11.09

GluGluToWWToENEN_UL2018 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENEN_UL2018")
GluGluToWWToENEN_UL2018.year = "UL2018"
GluGluToWWToENEN_UL2018.dataset = "/GluGluToWWToENEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToENEN_UL2018.sigma = 36.8

GluGluToWWToENMN_UL2018 = sample(WScolor, 1, 1001, "WW --> 2l2#nu", "GluGluToWWToENMN_UL2018")
GluGluToWWToENMN_UL2018.year = "UL2018"
GluGluToWWToENMN_UL2018.dataset = "/GluGluToWWToENMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToENMN_UL2018.sigma = 36.8

GluGluToWWToENTN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToENTN_UL2018")
GluGluToWWToENTN_UL2018.year = "UL2018"
GluGluToWWToENTN_UL2018.dataset = "/GluGluToWWToENTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluToWWToENTN_UL2018.sigma = 36.81

GluGluToWWToMNEN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNEN_UL2018")
GluGluToWWToMNEN_UL2018.year = "UL2018"
GluGluToWWToMNEN_UL2018.dataset = "/GluGluToWWToMNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToMNEN_UL2018.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNMN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNMN_UL2018")
GluGluToWWToMNMN_UL2018.year = "UL2018"
GluGluToWWToMNMN_UL2018.dataset = "/GluGluToWWToMNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToMNMN_UL2018.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToMNTN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToMNTN_UL2018")
GluGluToWWToMNTN_UL2018.year = "UL2018"
GluGluToWWToMNTN_UL2018.dataset = "/GluGluToWWToMNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluToWWToMNTN_UL2018.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNEN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNEN_UL2018")
GluGluToWWToTNEN_UL2018.year = "UL2018"
GluGluToWWToTNEN_UL2018.dataset = "/GluGluToWWToTNEN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluToWWToTNEN_UL2018.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNMN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNMN_UL2018")
GluGluToWWToTNMN_UL2018.year = "UL2018"
GluGluToWWToTNMN_UL2018.dataset = "/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluToWWToTNMN_UL2018.sigma = 36.81 * 1./9. * 1.4

GluGluToWWToTNTN_UL2018 = sample(WScolor, 1, 1001, "gg --> WW --> e#tau2#nu", "GluGluToWWToTNTN_UL2018")
GluGluToWWToTNTN_UL2018.year = "UL2018"
GluGluToWWToTNTN_UL2018.dataset = "/GluGluToWWToTNTN_TuneCP5_13TeV_MCFM701_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToWWToTNTN_UL2018.sigma = 36.81 * 1./9. * 1.4

ST_tW_top_UL2018 = sample(WScolor, 1, 1001, "Single top", "ST_tW_top_UL2018")
ST_tW_top_UL2018.year = "UL2018"
ST_tW_top_UL2018.dataset = "/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
ST_tW_top_UL2018.sigma = 34.91

ST_tW_antitop_UL2018 = sample(WScolor, 1, 1001, "Single top", "ST_tW_antitop_UL2018")
ST_tW_antitop_UL2018.year = "UL2018"
ST_tW_antitop_UL2018.dataset = "/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
ST_tW_antitop_UL2018.sigma =  34.97

#### to be replaced with v9 when available ####
GluGluHToWWTo2L2Nu_UL2018 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWTo2L2Nu_UL2018")
GluGluHToWWTo2L2Nu_UL2018.year = "UL2018"
GluGluHToWWTo2L2Nu_UL2018.dataset = "/GluGluHToWWTo2L2Nu_M125_TuneCP5_PSw_13TeV-powheg2-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
GluGluHToWWTo2L2Nu_UL2018.sigma = 28.86

#### to be produced ####
GluGluHToWWToLNuQQ_UL2018 = sample(WScolor, 1, 1001, "Single top", "GluGluHToWWToLNuQQ_UL2018")
GluGluHToWWToLNuQQ_UL2018.year = "UL2018"
GluGluHToWWToLNuQQ_UL2018.dataset = ""
GluGluHToWWToLNuQQ_UL2018.sigma = 0.# check nowe

GluGluHToZZTo4L_UL2018 = sample(WScolor, 1, 1001, "Single top", "GluGluHToZZTo4L_UL2018")
GluGluHToZZTo4L_UL2018.year = "UL2018"
GluGluHToZZTo4L_UL2018.dataset = "/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluHToZZTo4L_UL2018.sigma = 28.84# check nowe

GluGluHToTauTau_UL2018 = sample(WScolor, 1, 1001, "Single top", "GluGluHToTauTau_UL2018")
GluGluHToTauTau_UL2018.year = "UL2018"
GluGluHToTauTau_UL2018.dataset = "/GluGluHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
GluGluHToTauTau_UL2018.sigma = 21.46# check nowe

VBFHToWWTo2L2Nu_UL2018 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToWWTo2L2Nu_UL2018")
VBFHToWWTo2L2Nu_UL2018.year = "UL2018"
VBFHToWWTo2L2Nu_UL2018.dataset = "/VBFHToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
VBFHToWWTo2L2Nu_UL2018.sigma = 3.892 # check nowe

VBFHToTauTau_UL2018 = sample(WScolor, 1, 1001, "VBF H --> 2l2#nu", "VBFHToTauTau_UL2018")
VBFHToTauTau_UL2018.year = "UL2018"
VBFHToTauTau_UL2018.dataset = "/VBFHToTauTau_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
VBFHToTauTau_UL2018.sigma = 3.861 # check nowe

ttHToNonbb_UL2018 = sample(WScolor, 1, 1001, "ttH", "ttHToNonbb_UL2018")
ttHToNonbb_UL2018.year = "UL2018"
ttHToNonbb_UL2018.dataset = "/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
ttHToNonbb_UL2018.sigma = 0.5638 # check nowe

VHToNonbb_UL2018 = sample(WScolor, 1, 1001, "VH", "VHToNonbb_UL2018")
VHToNonbb_UL2018.year = "UL2018"
VHToNonbb_UL2018.dataset = "/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
VHToNonbb_UL2018.sigma = 2.528 # check nowe

WrongSign_UL2018 = sample(WScolor, 1, 1001, "V#gamma", "WrongSign_UL2018")
WrongSign_UL2018.year = "UL2018"
WrongSign_UL2018.components = [
    WWto2L2Nu_UL2018,
    GluGluToWWToENEN_UL2018,
    GluGluToWWToENMN_UL2018,
    GluGluToWWToENTN_UL2018,
    GluGluToWWToMNEN_UL2018,
    GluGluToWWToMNMN_UL2018,
    GluGluToWWToMNTN_UL2018,
    GluGluToWWToTNEN_UL2018,
    GluGluToWWToTNMN_UL2018,
    GluGluToWWToTNTN_UL2018,
    ST_tW_top_UL2018,
    ST_tW_antitop_UL2018,
    GluGluHToWWTo2L2Nu_UL2018,
    #GluGluHToWWToLNuQQ_UL2018,
    GluGluHToZZTo4L_UL2018,
    GluGluHToTauTau_UL2018,
    VBFHToWWTo2L2Nu_UL2018,
    VBFHToTauTau_UL2018,
    ttHToNonbb_UL2018,
    VHToNonbb_UL2018,
]


########################################################

sample_dict={
    "ZZtoLep_UL2016APV":ZZtoLep_UL2016APV,
    "ZZTo2L2Nu_UL2016APV":ZZTo2L2Nu_UL2016APV, "ZZTo4L_UL2016APV":ZZTo4L_UL2016APV, "GluGluToContinToZZTo4e_UL2016APV":GluGluToContinToZZTo4e_UL2016APV, "GluGluToContinToZZTo2e2mu_UL2016APV":GluGluToContinToZZTo2e2mu_UL2016APV, "GluGluToContinToZZTo2e2tau_UL2016APV":GluGluToContinToZZTo2e2tau_UL2016APV,"GluGluToContinToZZTo2mu2nu_UL2016APV":GluGluToContinToZZTo2mu2nu_UL2016APV, "GluGluToContinToZZTo4mu_UL2016APV":GluGluToContinToZZTo4mu_UL2016APV, "GluGluToContinToZZTo2mu2tau_UL2016APV":GluGluToContinToZZTo2mu2tau_UL2016APV, "GluGluToContinToZZTo2tau2nu_UL2016APV":GluGluToContinToZZTo2tau2nu_UL2016APV, "GluGluToContinToZZTo4tau_UL2016APV":GluGluToContinToZZTo4tau_UL2016APV, "GluGluToContinToZZTo2e2nu_UL2016APV":GluGluToContinToZZTo2e2nu_UL2016APV,
    "TT_UL2016APV":TT_UL2016APV,
    "TT_SemiLep_UL2016APV":TT_SemiLep_UL2016APV, "TT_Had_UL2016APV":TT_Had_UL2016APV,
    "TTTo2L2Nu_UL2016APV":TTTo2L2Nu_UL2016APV,
    "TVX_UL2016APV":TVX_UL2016APV,
    "TTGJets_UL2016APV":TTGJets_UL2016APV, "TTZToQQ_UL2016APV":TTZToQQ_UL2016APV, "TTZToLLNuNu_UL2016APV":TTZToLLNuNu_UL2016APV, "TTWJetsToQQ_UL2016APV":TTWJetsToQQ_UL2016APV, "TTWJetsToLNu_UL2016APV":TTWJetsToLNu_UL2016APV, "tZq_ll_4f_UL2016APV":tZq_ll_4f_UL2016APV,
    "VG_UL2016APV":VG_UL2016APV,
    "ZG_UL2016APV":ZG_UL2016APV, "WG_UL2016APV":WG_UL2016APV,
    "WrongSign_UL2016APV":WrongSign_UL2016APV,
    "WWto2L2Nu_UL2016APV":WWto2L2Nu_UL2016APV, "GluGluToWWToENEN_UL2016APV":GluGluToWWToENEN_UL2016APV, "GluGluToWWToENMN_UL2016APV":GluGluToWWToENMN_UL2016APV, "GluGluToWWToENTN_UL2016APV":GluGluToWWToENTN_UL2016APV, "GluGluToWWToMNEN_UL2016APV":GluGluToWWToMNEN_UL2016APV, "GluGluToWWToMNMN_UL2016APV":GluGluToWWToMNMN_UL2016APV, "GluGluToWWToMNTN_UL2016APV":GluGluToWWToMNTN_UL2016APV, "GluGluToWWToTNEN_UL2016APV":GluGluToWWToTNEN_UL2016APV, "GluGluToWWToTNMN_UL2016APV":GluGluToWWToTNMN_UL2016APV, "GluGluToWWToTNTN_UL2016APV":GluGluToWWToTNTN_UL2016APV, "ST_tW_top_UL2016APV":ST_tW_top_UL2016APV, "ST_tW_antitop_UL2016APV":ST_tW_antitop_UL2016APV, "GluGluHToWWTo2L2Nu_UL2016APV":GluGluHToWWTo2L2Nu_UL2016APV, "GluGluHToWWToLNuQQ_UL2016APV":GluGluHToWWToLNuQQ_UL2016APV, "GluGluHToZZTo4L_UL2016APV":GluGluHToZZTo4L_UL2016APV, "GluGluHToTauTau_UL2016APV":GluGluHToTauTau_UL2016APV, "VBFHToWWTo2L2Nu_UL2016APV": VBFHToWWTo2L2Nu_UL2016APV, "VBFHToTauTau_UL2016APV":VBFHToTauTau_UL2016APV, "ttHToNonbb_UL2016APV":ttHToNonbb_UL2016APV, "VHToNonbb_UL2016APV":VHToNonbb_UL2016APV,

    "ZZtoLep_UL2016":ZZtoLep_UL2016,
    "ZZTo2L2Nu_UL2016":ZZTo2L2Nu_UL2016, "ZZTo4L_UL2016":ZZTo4L_UL2016, "GluGluToContinToZZTo4e_UL2016":GluGluToContinToZZTo4e_UL2016, "GluGluToContinToZZTo2e2mu_UL2016":GluGluToContinToZZTo2e2mu_UL2016, "GluGluToContinToZZTo2e2tau_UL2016":GluGluToContinToZZTo2e2tau_UL2016, "GluGluToContinToZZTo2mu2nu_UL2016":GluGluToContinToZZTo2mu2nu_UL2016, "GluGluToContinToZZTo4mu_UL2016":GluGluToContinToZZTo4mu_UL2016, "GluGluToContinToZZTo2mu2tau_UL2016":GluGluToContinToZZTo2mu2tau_UL2016, "GluGluToContinToZZTo2tau2nu_UL2016":GluGluToContinToZZTo2tau2nu_UL2016, "GluGluToContinToZZTo4tau_UL2016":GluGluToContinToZZTo4tau_UL2016, "GluGluToContinToZZTo2e2nu_UL2016":GluGluToContinToZZTo2e2nu_UL2016,
    "TT_UL2016":TT_UL2016,
    "TT_SemiLep_UL2016":TT_SemiLep_UL2016, "TT_Had_UL2016":TT_Had_UL2016,
    "TTTo2L2Nu_UL2016":TTTo2L2Nu_UL2016,
    "TVX_UL2016":TVX_UL2016,
    "TTGJets_UL2016":TTGJets_UL2016, "TTZToQQ_UL2016":TTZToQQ_UL2016, "TTZToLLNuNu_UL2016":TTZToLLNuNu_UL2016, "TTWJetsToQQ_UL2016":TTWJetsToQQ_UL2016, "TTWJetsToLNu_UL2016":TTWJetsToLNu_UL2016, "tZq_ll_4f_UL2016":tZq_ll_4f_UL2016,
    "VG_UL2016":VG_UL2016,
    "ZG_UL2016":ZG_UL2016, "WG_UL2016":WG_UL2016,
    "WrongSign_UL2016":WrongSign_UL2016,
    "WWto2L2Nu_UL2016":WWto2L2Nu_UL2016, "GluGluToWWToENEN_UL2016":GluGluToWWToENEN_UL2016, "GluGluToWWToENMN_UL2016":GluGluToWWToENMN_UL2016, "GluGluToWWToENTN_UL2016":GluGluToWWToENTN_UL2016, "GluGluToWWToMNEN_UL2016":GluGluToWWToMNEN_UL2016, "GluGluToWWToMNMN_UL2016":GluGluToWWToMNMN_UL2016, "GluGluToWWToMNTN_UL2016":GluGluToWWToMNTN_UL2016, "GluGluToWWToTNEN_UL2016":GluGluToWWToTNEN_UL2016, "GluGluToWWToTNMN_UL2016":GluGluToWWToTNMN_UL2016, "GluGluToWWToTNTN_UL2016":GluGluToWWToTNTN_UL2016, "ST_tW_top_UL2016":ST_tW_top_UL2016, "ST_tW_antitop_UL2016":ST_tW_antitop_UL2016, "GluGluHToWWTo2L2Nu_UL2016":GluGluHToWWTo2L2Nu_UL2016, "GluGluHToWWToLNuQQ_UL2016":GluGluHToWWToLNuQQ_UL2016, "GluGluHToZZTo4L_UL2016":GluGluHToZZTo4L_UL2016, "GluGluHToTauTau_UL2016":GluGluHToTauTau_UL2016, "VBFHToWWTo2L2Nu_UL2016": VBFHToWWTo2L2Nu_UL2016, "VBFHToTauTau_UL2016":VBFHToTauTau_UL2016, "ttHToNonbb_UL2016":ttHToNonbb_UL2016, "VHToNonbb_UL2016":VHToNonbb_UL2016,

    "ZZtoLep_UL2017":ZZtoLep_UL2017,
    "ZZTo2L2Nu_UL2017":ZZTo2L2Nu_UL2017, "ZZTo4L_UL2017":ZZTo4L_UL2017, "GluGluToContinToZZTo4e_UL2017":GluGluToContinToZZTo4e_UL2017, "GluGluToContinToZZTo2e2mu_UL2017":GluGluToContinToZZTo2e2mu_UL2017, "GluGluToContinToZZTo2e2tau_UL2017":GluGluToContinToZZTo2e2tau_UL2017, "GluGluToContinToZZTo2mu2nu_UL2017":GluGluToContinToZZTo2mu2nu_UL2017, "GluGluToContinToZZTo4mu_UL2017":GluGluToContinToZZTo4mu_UL2017, "GluGluToContinToZZTo2mu2tau_UL2017":GluGluToContinToZZTo2mu2tau_UL2017, "GluGluToContinToZZTo2tau2nu_UL2017":GluGluToContinToZZTo2tau2nu_UL2017, "GluGluToContinToZZTo4tau_UL2017":GluGluToContinToZZTo4tau_UL2017, "GluGluToContinToZZTo2e2nu_UL2017":GluGluToContinToZZTo2e2nu_UL2017,
    "TT_UL2017":TT_UL2017,
    "TT_SemiLep_UL2017":TT_SemiLep_UL2017, "TT_Had_UL2017":TT_Had_UL2017,
    "TTTo2L2Nu_UL2017":TTTo2L2Nu_UL2017,
    "TVX_UL2017":TVX_UL2017,
    "TTGJets_UL2017":TTGJets_UL2017, "TTZToQQ_UL2017":TTZToQQ_UL2017, "TTZToLLNuNu_UL2017":TTZToLLNuNu_UL2017, "TTWJetsToQQ_UL2017":TTWJetsToQQ_UL2017, "TTWJetsToLNu_UL2017":TTWJetsToLNu_UL2017, "tZq_ll_4f_UL2017":tZq_ll_4f_UL2017,
    "VG_UL2017":VG_UL2017,
    "ZG_UL2017":ZG_UL2017, "WG_UL2017":WG_UL2017,
    "WrongSign_UL2017":WrongSign_UL2017,
    "WWto2L2Nu_UL2017":WWto2L2Nu_UL2017, "GluGluToWWToENEN_UL2017":GluGluToWWToENEN_UL2017, "GluGluToWWToENMN_UL2017":GluGluToWWToENMN_UL2017, "GluGluToWWToENTN_UL2017":GluGluToWWToENTN_UL2017, "GluGluToWWToMNEN_UL2017":GluGluToWWToMNEN_UL2017, "GluGluToWWToMNMN_UL2017":GluGluToWWToMNMN_UL2017, "GluGluToWWToMNTN_UL2017":GluGluToWWToMNTN_UL2017, "GluGluToWWToTNEN_UL2017":GluGluToWWToTNEN_UL2017, "GluGluToWWToTNMN_UL2017":GluGluToWWToTNMN_UL2017, "GluGluToWWToTNTN_UL2017":GluGluToWWToTNTN_UL2017, "ST_tW_top_UL2017":ST_tW_top_UL2017, "ST_tW_antitop_UL2017":ST_tW_antitop_UL2017, "GluGluHToWWTo2L2Nu_UL2017":GluGluHToWWTo2L2Nu_UL2017, "GluGluHToWWToLNuQQ_UL2017":GluGluHToWWToLNuQQ_UL2017, "GluGluHToZZTo4L_UL2017":GluGluHToZZTo4L_UL2017, "GluGluHToTauTau_UL2017":GluGluHToTauTau_UL2017, "VBFHToWWTo2L2Nu_UL2017": VBFHToWWTo2L2Nu_UL2017, "VBFHToTauTau_UL2017":VBFHToTauTau_UL2017, "ttHToNonbb_UL2017":ttHToNonbb_UL2017, "VHToNonbb_UL2017":VHToNonbb_UL2017,

    "ZZtoLep_UL2018":ZZtoLep_UL2018,
    "ZZTo2L2Nu_UL2018":ZZTo2L2Nu_UL2018, "ZZTo4L_UL2018":ZZTo4L_UL2018, "GluGluToContinToZZTo4e_UL2018":GluGluToContinToZZTo4e_UL2018, "GluGluToContinToZZTo2e2mu_UL2018":GluGluToContinToZZTo2e2mu_UL2018, "GluGluToContinToZZTo2e2tau_UL2018":GluGluToContinToZZTo2e2tau_UL2018, "GluGluToContinToZZTo2mu2nu_UL2018":GluGluToContinToZZTo2mu2nu_UL2018, "GluGluToContinToZZTo4mu_UL2018":GluGluToContinToZZTo4mu_UL2018, "GluGluToContinToZZTo2mu2tau_UL2018":GluGluToContinToZZTo2mu2tau_UL2018, "GluGluToContinToZZTo2tau2nu_UL2018":GluGluToContinToZZTo2tau2nu_UL2018, "GluGluToContinToZZTo4tau_UL2018":GluGluToContinToZZTo4tau_UL2018, "GluGluToContinToZZTo2e2nu_UL2018":GluGluToContinToZZTo2e2nu_UL2018,
    "TT_UL2018":TT_UL2018,
    "TT_SemiLep_UL2018":TT_SemiLep_UL2018, "TT_Had_UL2018":TT_Had_UL2018,
    "TTTo2L2Nu_UL2018":TTTo2L2Nu_UL2018,
    "TVX_UL2018":TVX_UL2018,
    "TTGJets_UL2018":TTGJets_UL2018, "TTZToQQ_UL2018":TTZToQQ_UL2018, "TTZToLLNuNu_UL2018":TTZToLLNuNu_UL2018, "TTWJetsToQQ_UL2018":TTWJetsToQQ_UL2018, "TTWJetsToLNu_UL2018":TTWJetsToLNu_UL2018, "tZq_ll_4f_UL2018":tZq_ll_4f_UL2018,
    "VG_UL2018":VG_UL2018,
    "ZG_UL2018":ZG_UL2018, "WG_UL2018":WG_UL2018,
    "WrongSign_UL2018":WrongSign_UL2018,
    "WWto2L2Nu_UL2018":WWto2L2Nu_UL2018, "GluGluToWWToENEN_UL2018":GluGluToWWToENEN_UL2018, "GluGluToWWToENMN_UL2018":GluGluToWWToENMN_UL2018, "GluGluToWWToENTN_UL2018":GluGluToWWToENTN_UL2018, "GluGluToWWToMNEN_UL2018":GluGluToWWToMNEN_UL2018, "GluGluToWWToMNMN_UL2018":GluGluToWWToMNMN_UL2018, "GluGluToWWToMNTN_UL2018":GluGluToWWToMNTN_UL2018, "GluGluToWWToTNEN_UL2018":GluGluToWWToTNEN_UL2018, "GluGluToWWToTNMN_UL2018":GluGluToWWToTNMN_UL2018, "GluGluToWWToTNTN_UL2018":GluGluToWWToTNTN_UL2018, "ST_tW_top_UL2018":ST_tW_top_UL2018, "ST_tW_antitop_UL2018":ST_tW_antitop_UL2018, "GluGluHToWWTo2L2Nu_UL2018":GluGluHToWWTo2L2Nu_UL2018, "GluGluHToWWToLNuQQ_UL2018":GluGluHToWWToLNuQQ_UL2018, "GluGluHToZZTo4L_UL2018":GluGluHToZZTo4L_UL2018, "GluGluHToTauTau_UL2018":GluGluHToTauTau_UL2018, "VBFHToWWTo2L2Nu_UL2018": VBFHToWWTo2L2Nu_UL2018, "VBFHToTauTau_UL2018":VBFHToTauTau_UL2018, "ttHToNonbb_UL2018":ttHToNonbb_UL2018, "VHToNonbb_UL2018":VHToNonbb_UL2018,

}


merge_dict={
}


class_list=[
]


class_list_bis = [
]

