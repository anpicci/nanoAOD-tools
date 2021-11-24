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

######### 2016APV ##########

### ZZtoLep ###

ZZTo2L2Nu_2016APV = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_2016APV")
ZZTo2L2Nu_2016APV.year = "2016APV"
ZZTo2L2Nu_2016APV.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo2L2Nu_2016APV.sigma = 0.9738 #pb NLO

ZZTo4L_2016APV = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_2016APV") ### not sure is the right background
ZZTo4L_2016APV.year = "2016APV"
ZZTo4L_2016APV.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo4L_2016APV.sigma = 13.74 #pb NLO

#### to be produced ####
GluGluToContinToZZTo2e2nu_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_2016APV")
GluGluToContinToZZTo2e2nu_2016APV.year = "2016APV"
GluGluToContinToZZTo2e2nu_2016APV.dataset = ""
GluGluToContinToZZTo2e2nu_2016APV.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_2016APV")
GluGluToContinToZZTo4e_2016APV.year = "2016APV"
GluGluToContinToZZTo4e_2016APV.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo4e_2016APV.sigma = 1.619 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2mu_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_2016APV")
GluGluToContinToZZTo2e2mu_2016APV.year = "2016APV"
GluGluToContinToZZTo2e2mu_2016APV.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_2016APV.sigma = 3.292 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_2016APV")
GluGluToContinToZZTo2e2tau_2016APV.year = "2016APV"
GluGluToContinToZZTo2e2tau_2016APV.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_2016APV.sigma = 3.294 # * 0.001 #pb to be checked

#### in production stage ######
GluGluToContinToZZTo2mu2nu_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_2016APV")
GluGluToContinToZZTo2mu2nu_2016APV.year = "2016APV"
#GluGluToContinToZZTo2mu2nu_2016APV.dataset = ""
GluGluToContinToZZTo2mu2nu_2016APV.sigma = 17.73 # * 0.001 #pb to be checked

#### to be replaced with v9 when available ####
GluGluToContinToZZTo4mu_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_2016APV")
GluGluToContinToZZTo4mu_2016APV.year = "2016APV"
GluGluToContinToZZTo4mu_2016APV.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_2016APV.sigma = 1.608 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_2016APV")
GluGluToContinToZZTo2mu2tau_2016APV.year = "2016APV"
GluGluToContinToZZTo2mu2tau_2016APV.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_2016APV.sigma = 3.294 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_2016APV")
GluGluToContinToZZTo2tau2nu_2016APV.year = "2016APV"
GluGluToContinToZZTo2tau2nu_2016APV.dataset = ""
GluGluToContinToZZTo2tau2nu_2016APV.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_2016APV = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_2016APV")
GluGluToContinToZZTo4tau_2016APV.year = "2016APV"
GluGluToContinToZZTo4tau_2016APV.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_2016APV.sigma = 1.626 # * 0.001 #pb to be checked

ZZtoLep_2016APV = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_2016APV")
ZZtoLep_2016APV.year = "2016APV"
ZZtoLep_2016APV.components = [
    ZZTo2L2Nu_2016APV,
    ZZTo4L_2016APV,
    #GluGluToContinToZZTo2e2nu_2016APV,
    GluGluToContinToZZTo4e_2016APV,
    GluGluToContinToZZTo2e2mu_2016APV,
    GluGluToContinToZZTo2e2tau_2016APV,
    #GluGluToContinToZZTo2mu2nu_2016APV,
    GluGluToContinToZZTo4mu_2016APV,
    GluGluToContinToZZTo2mu2tau_2016APV,
    #GluGluToContinToZZTo2tau2nu_2016APV,
    GluGluToContinToZZTo4tau_2016APV,
]

### TT with quark ###

TT_SemiLep_2016APV = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_2016APV")
TT_SemiLep_2016APV.year = "2016APV"
TT_SemiLep_2016APV.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TT_SemiLep_2016APV.sigma = 365.3 #pb to check

TT_Had_2016APV = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_2016APV")
TT_Had_2016APV.year = "2016APV"
TT_Had_2016APV.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TT_Had_2016APV.sigma = 377.96 #pb to check

TT_2016APV = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_2016APV")
TT_2016APV.year = "2016APV"
TT_2016APV.components = [
    TT_SemiLep_2016APV,
    TT_Had_2016APV,
]

TTTo2L2Nu_2016APV = sample(TTdilepcolor, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_2016APV")
TTTo2L2Nu_2016APV.year = "2016APV"
TTTo2L2Nu_2016APV.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
TTTo2L2Nu_2016APV.sigma = 88.29 #pb

### TVX ###

TTGJets_2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> qq", "TTGJets_2016APV")
TTGJets_2016APV.year = "2016APV"
TTGJets_2016APV.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
TTGJets_2016APV.sigma = 3.757

TTZToQQ_2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_2016APV")
TTZToQQ_2016APV.year = "2016APV"
TTZToQQ_2016APV.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"
TTZToQQ_2016APV.sigma = 0.5104

TTZToLLNuNu_2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_2016APV")
TTZToLLNuNu_2016APV.year = "2016APV"
TTZToLLNuNu_2016APV.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTZToLLNuNu_2016APV.sigma = 0.2439

#### to be replaced with v9 when available ####
TTWJetsToQQ_2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_2016APV")
TTWJetsToQQ_2016APV.year = "2016APV"
TTWJetsToQQ_2016APV.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToQQ_2016APV.sigma = 0.4377

#### to be replaced with v9 when available ####
TTWJetsToLNu_2016APV = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_2016APV")
TTWJetsToLNu_2016APV.year = "2016APV"
TTWJetsToLNu_2016APV.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToLNu_2016APV.sigma = 0.216

tZq_ll_4f_2016APV = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_2016APV")
tZq_ll_4f_2016APV.year = "2016APV"
tZq_ll_4f_2016APV.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
tZq_ll_4f_2016APV.sigma = 0.07561

TVX_2016APV = sample(TVXcolor, 1, 1001, "tVX", "TVX_2016APV")
TVX_2016APV.year = "2016APV"
TVX_2016APV.components = [
    TTGJets_2016APV,
    TTZToQQ_2016APV,
    TTZToLLNuNu_2016APV,
    TTWJetsToQQ_2016APV,
    TTWJetsToLNu_2016APV,
    tZq_ll_4f_2016APV,
]

### VG ###

#### to be replaced with v9 when available ####
ZG_2016APV = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_2016APV")
ZG_2016APV.year = "2016APV"
ZG_2016APV.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
ZG_2016APV.sigma = 51.1 # to check

WG_2016APV = sample(VGcolor, 1, 1001, "W #gamma", "WG_2016APV")
WG_2016APV.year = "2016APV"
WG_2016APV.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
WG_2016APV.sigma = 191.3 # to check

VG_2016APV = sample(VGcolor, 1, 1001, "V#gamma", "VG_2016APV")
VG_2016APV.year = "2016APV"
VG_2016APV.components = [
    ZG_2016APV,
    WG_2016APV,
]

######### 2016 ##########

### ZZtoLep ###

ZZTo2L2Nu_2016 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_2016")
ZZTo2L2Nu_2016.year = "2016"
ZZTo2L2Nu_2016.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo2L2Nu_2016.sigma = 0.9738 #pb NLO

ZZTo4L_2016 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_2016") ### not sure is the right background
ZZTo4L_2016.year = "2016"
ZZTo4L_2016.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
ZZTo4L_2016.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_2016")
GluGluToContinToZZTo2e2nu_2016.year = "2016"
GluGluToContinToZZTo2e2nu_2016.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2nu_2016.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_2016")
GluGluToContinToZZTo4e_2016.year = "2016"
GluGluToContinToZZTo4e_2016.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
GluGluToContinToZZTo4e_2016.sigma = 1.619 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_2016")
GluGluToContinToZZTo2e2mu_2016.year = "2016"
GluGluToContinToZZTo2e2mu_2016.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2mu_2016.sigma = 3.292 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_2016")
GluGluToContinToZZTo2e2tau_2016.year = "2016"
GluGluToContinToZZTo2e2tau_2016.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2e2tau_2016.sigma = 3.294 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_2016")
GluGluToContinToZZTo2mu2nu_2016.year = "2016"
GluGluToContinToZZTo2mu2nu_2016.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_2016.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4mu_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_2016")
GluGluToContinToZZTo4mu_2016.year = "2016"
GluGluToContinToZZTo4mu_2016.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"
GluGluToContinToZZTo4mu_2016.sigma = 1.608 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_2016")
GluGluToContinToZZTo2mu2tau_2016.year = "2016"
GluGluToContinToZZTo2mu2tau_2016.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_2016.sigma = 3.294 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_2016")
GluGluToContinToZZTo2tau2nu_2016.year = "2016"
GluGluToContinToZZTo2tau2nu_2016.dataset = ""
GluGluToContinToZZTo2tau2nu_2016.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_2016 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_2016")
GluGluToContinToZZTo4tau_2016.year = "2016"
GluGluToContinToZZTo4tau_2016.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
GluGluToContinToZZTo4tau_2016.sigma = 1.626 # * 0.001 #pb to be checked

ZZtoLep_2016 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_2016")
ZZtoLep_2016.year = "2016"
ZZtoLep_2016.components = [
    ZZTo2L2Nu_2016,
    ZZTo4L_2016,
    GluGluToContinToZZTo2e2nu_2016,
    GluGluToContinToZZTo4e_2016,
    GluGluToContinToZZTo2e2mu_2016,
    GluGluToContinToZZTo2e2tau_2016,
    GluGluToContinToZZTo2mu2nu_2016,
    GluGluToContinToZZTo4mu_2016,
    GluGluToContinToZZTo2mu2tau_2016,
    #GluGluToContinToZZTo2tau2nu_2016,
    GluGluToContinToZZTo4tau_2016,
]

### TT with quark ###

TT_SemiLep_2016 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_2016")
TT_SemiLep_2016.year = "2016"
TT_SemiLep_2016.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TT_SemiLep_2016.sigma = 365.3 #pb to check

TT_Had_2016 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_2016")
TT_Had_2016.year = "2016"
TT_Had_2016.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TT_Had_2016.sigma = 377.96 #pb to check

TT_2016 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_2016")
TT_2016.year = "2016"
TT_2016.components = [
    TT_SemiLep_2016,
    TT_Had_2016,
]

TTTo2L2Nu_2016 = sample(TTdilepcolor, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_2016")
TTTo2L2Nu_2016.year = "2016"
TTTo2L2Nu_2016.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-20UL16JMENano_106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTTo2L2Nu_2016.sigma =  88.29 #pb

### TVX ###

TTGJets_2016 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_2016")
TTGJets_2016.year = "2016"
TTGJets_2016.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTGJets_2016.sigma = 3.757

TTZToQQ_2016 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_2016")
TTZToQQ_2016.year = "2016"
TTZToQQ_2016.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTZToQQ_2016.sigma = 0.5104

TTZToLLNuNu_2016 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_2016")
TTZToLLNuNu_2016.year = "2016"
TTZToLLNuNu_2016.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTZToLLNuNu_2016.sigma = 0.2439

TTWJetsToQQ_2016 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_2016")
TTWJetsToQQ_2016.year = "2016"
TTWJetsToQQ_2016.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
TTWJetsToQQ_2016.sigma = 0.4377

TTWJetsToLNu_2016 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_2016")
TTWJetsToLNu_2016.year = "2016"
TTWJetsToLNu_2016.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv2-106X_mcRun2_asymptotic_preVFP_v9-v1/NANOAODSIM"
TTWJetsToLNu_2016.sigma = 0.216

tZq_ll_4f_2016 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_2016")
tZq_ll_4f_2016.year = "2016"
tZq_ll_4f_2016.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
tZq_ll_4f_2016.sigma = 0.07561

TVX_2016 = sample(TVXcolor, 1, 1001, "tVX", "TVX_2016")
TVX_2016.year = "2016"
TVX_2016.components = [
    TTGJets_2016,
    TTZToQQ_2016,
    TTZToLLNuNu_2016,
    TTWJetsToQQ_2016,
    TTWJetsToLNu_2016,
    tZq_ll_4f_2016,
]

### VG ###

ZG_2016 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_2016")
ZG_2016.year = "2016"
ZG_2016.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
ZG_2016.sigma = 51.1 # to check

WG_2016 = sample(VGcolor, 1, 1001, "W #gamma", "WG_2016")
WG_2016.year = "2016"
WG_2016.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"
WG_2016.sigma = 191.3 # to check

VG_2016 = sample(VGcolor, 1, 1001, "V#gamma", "VG_2016")
VG_2016.year = "2016"
VG_2016.components = [
    ZG_2016,
    WG_2016,
]


######### 2017 ##########

### ZZtoLep ###

ZZTo2L2Nu_2017 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_2017")
ZZTo2L2Nu_2017.year = "2017"
ZZTo2L2Nu_2017.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZZTo2L2Nu_2017.sigma = 0.9738 #pb NLO

ZZTo4L_2017 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_2017") ### not sure is the right background
ZZTo4L_2017.year = "2017"
ZZTo4L_2017.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZZTo4L_2017.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_2017")
GluGluToContinToZZTo2e2nu_2017.year = "2017"
GluGluToContinToZZTo2e2nu_2017.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2nu_2017.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_2017")
GluGluToContinToZZTo4e_2017.year = "2017"
GluGluToContinToZZTo4e_2017.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4e_2017.sigma = 1.619 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_2017")
GluGluToContinToZZTo2e2mu_2017.year = "2017"
GluGluToContinToZZTo2e2mu_2017.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_2017.sigma = 3.292 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_2017")
GluGluToContinToZZTo2e2tau_2017.year = "2017"
GluGluToContinToZZTo2e2tau_2017.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_2017.sigma = 3.294 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_2017")
GluGluToContinToZZTo2mu2nu_2017.year = "2017"
GluGluToContinToZZTo2mu2nu_2017.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_2017.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4mu_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_2017")
GluGluToContinToZZTo4mu_2017.year = "2017"
GluGluToContinToZZTo4mu_2017.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4mu_2017.sigma = 1.608 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_2017")
GluGluToContinToZZTo2mu2tau_2017.year = "2017"
GluGluToContinToZZTo2mu2tau_2017.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_2017.sigma = 3.294 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_2017")
GluGluToContinToZZTo2tau2nu_2017.year = "2017"
GluGluToContinToZZTo2tau2nu_2017.dataset = ""
GluGluToContinToZZTo2tau2nu_2017.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_2017 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_2017")
GluGluToContinToZZTo4tau_2017.year = "2017"
GluGluToContinToZZTo4tau_2017.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_2017.sigma = 1.626 # * 0.001 #pb to be checked

ZZtoLep_2017 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_2017")
ZZtoLep_2017.year = "2017"
ZZtoLep_2017.components = [
    ZZTo2L2Nu_2017,
    ZZTo4L_2017,
    GluGluToContinToZZTo2e2nu_2017,
    GluGluToContinToZZTo4e_2017,
    GluGluToContinToZZTo2e2mu_2017,
    GluGluToContinToZZTo2e2tau_2017,
    GluGluToContinToZZTo2mu2nu_2017,
    GluGluToContinToZZTo4mu_2017,
    GluGluToContinToZZTo2mu2tau_2017,
    #GluGluToContinToZZTo2tau2nu_2017,
    GluGluToContinToZZTo4tau_2017,
]

### TT with quark ###

TT_SemiLep_2017 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_2017")
TT_SemiLep_2017.year = "2017"
TT_SemiLep_2017.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM"
TT_SemiLep_2017.sigma = 365.3 #pb to check

#### in production stage ####
TT_Had_2017 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_2017")
TT_Had_2017.year = "2017"
TT_Had_2017.dataset = ""
TT_Had_2017.sigma = 377.96 #pb to check

TT_2017 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_2017")
TT_2017.year = "2017"
TT_2017.components = [
    TT_SemiLep_2017,
    #TT_Had_2017,
]

TTTo2L2Nu_2017 = sample(TTdilepcolor, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_2017")
TTTo2L2Nu_2017.year = "2017"
TTTo2L2Nu_2017.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-20UL17JMENano_106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTTo2L2Nu_2017.sigma =  88.29 #pb

### TVX ###

TTGJets_2017 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_2017")
TTGJets_2017.year = "2017"
TTGJets_2017.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTGJets_2017.sigma = 3.757

TTZToQQ_2017 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_2017")
TTZToQQ_2017.year = "2017"
TTZToQQ_2017.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTZToQQ_2017.sigma = 0.5104

TTZToLLNuNu_2017 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_2017")
TTZToLLNuNu_2017.year = "2017"
TTZToLLNuNu_2017.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTZToLLNuNu_2017.sigma = 0.2439

TTWJetsToQQ_2017 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_2017")
TTWJetsToQQ_2017.year = "2017"
TTWJetsToQQ_2017.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
TTWJetsToQQ_2017.sigma = 0.4377

TTWJetsToLNu_2017 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_2017")
TTWJetsToLNu_2017.year = "2017"
TTWJetsToLNu_2017.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
TTWJetsToLNu_2017.sigma = 0.216

tZq_ll_4f_2017 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_2017")
tZq_ll_4f_2017.year = "2017"
tZq_ll_4f_2017.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
tZq_ll_4f_2017.sigma = 0.07561

TVX_2017 = sample(TVXcolor, 1, 1001, "tVX", "TVX_2017")
TVX_2017.year = "2017"
TVX_2017.components = [
    TTGJets_2017,
    TTZToQQ_2017,
    TTZToLLNuNu_2017,
    TTWJetsToQQ_2017,
    TTWJetsToLNu_2017,
    tZq_ll_4f_2017,
]

### VG ###

ZG_2017 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_2017")
ZG_2017.year = "2017"
ZG_2017.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
ZG_2017.sigma = 51.1 # to check

WG_2017 = sample(VGcolor, 1, 1001, "W #gamma", "WG_2017")
WG_2017.year = "2017"
WG_2017.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"
WG_2017.sigma = 191.3 # to check

VG_2017 = sample(VGcolor, 1, 1001, "V#gamma", "VG_2017")
VG_2017.year = "2017"
VG_2017.components = [
    ZG_2017,
    WG_2017,
]


######### 2018 ##########

### ZZtoLep ###

ZZTo2L2Nu_2018 = sample(ZZcolor, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_2018")
ZZTo2L2Nu_2018.year = "2018"
ZZTo2L2Nu_2018.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZZTo2L2Nu_2018.sigma = 0.9738 #pb NLO

ZZTo4L_2018 = sample(ZZcolor, 1, 1001, "ZZ --> 4l", "ZZTo4L_2018") ### not sure is the right background
ZZTo4L_2018.year = "2018"
ZZTo4L_2018.dataset = "/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZZTo4L_2018.sigma = 13.74 #pb NLO

GluGluToContinToZZTo2e2nu_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2nu", "GluGluToContinToZZTo2e2nu_2018")
GluGluToContinToZZTo2e2nu_2018.year = "2018"
GluGluToContinToZZTo2e2nu_2018.dataset = "/GluGluToContinToZZTo2e2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2nu_2018.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4e_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4e", "GluGluToContinToZZTo4e_2018")
GluGluToContinToZZTo4e_2018.year = "2018"
GluGluToContinToZZTo4e_2018.dataset = "/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo4e_2018.sigma = 1.619 # * 0.001 #pb

GluGluToContinToZZTo2e2mu_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2mu", "GluGluToContinToZZTo2e2mu_2018")
GluGluToContinToZZTo2e2mu_2018.year = "2018"
GluGluToContinToZZTo2e2mu_2018.dataset = "/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2mu_2018.sigma = 3.292 # * 0.001 #pb to be checked

GluGluToContinToZZTo2e2tau_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2e2tau", "GluGluToContinToZZTo2e2tau_2018")
GluGluToContinToZZTo2e2tau_2018.year = "2018"
GluGluToContinToZZTo2e2tau_2018.dataset = "/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2e2tau_2018.sigma = 3.294 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2nu_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2nu", "GluGluToContinToZZTo2mu2nu_2018")
GluGluToContinToZZTo2mu2nu_2018.year = "2018"
GluGluToContinToZZTo2mu2nu_2018.dataset = "/GluGluToContinToZZTo2mu2nu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2nu_2018.sigma = 17.73 # * 0.001 #pb to be checked

#### to be replaced with v9 when available ######
GluGluToContinToZZTo4mu_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4mu", "GluGluToContinToZZTo4mu_2018")
GluGluToContinToZZTo4mu_2018.year = "2018"
GluGluToContinToZZTo4mu_2018.dataset = "/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
GluGluToContinToZZTo4mu_2018.sigma = 1.608 # * 0.001 #pb to be checked

GluGluToContinToZZTo2mu2tau_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2mu2tau", "GluGluToContinToZZTo2mu2tau_2018")
GluGluToContinToZZTo2mu2tau_2018.year = "2018"
GluGluToContinToZZTo2mu2tau_2018.dataset = "/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo2mu2tau_2018.sigma = 3.294 # * 0.001 #pb to be checked

#### to be produced ####
GluGluToContinToZZTo2tau2nu_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 2tau2nu", "GluGluToContinToZZTo2tau2nu_2018")
GluGluToContinToZZTo2tau2nu_2018.year = "2018"
GluGluToContinToZZTo2tau2nu_2018.dataset = ""
GluGluToContinToZZTo2tau2nu_2018.sigma = 17.73 # * 0.001 #pb to be checked

GluGluToContinToZZTo4tau_2018 = sample(ZZcolor, 1, 1001, "gg --> ZZ --> 4tau", "GluGluToContinToZZTo4tau_2018")
GluGluToContinToZZTo4tau_2018.year = "2018"
GluGluToContinToZZTo4tau_2018.dataset = "/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"
GluGluToContinToZZTo4tau_2018.sigma = 1.626 # * 0.001 #pb to be checked

ZZtoLep_2018 = sample(ZZcolor, 1, 1001, "ZZ", "ZZtoLep_2018")
ZZtoLep_2018.year = "2018"
ZZtoLep_2018.components = [
    ZZTo2L2Nu_2018,
    ZZTo4L_2018,
    GluGluToContinToZZTo2e2nu_2018,
    GluGluToContinToZZTo4e_2018,
    GluGluToContinToZZTo2e2mu_2018,
    GluGluToContinToZZTo2e2tau_2018,
    GluGluToContinToZZTo2mu2nu_2018,
    GluGluToContinToZZTo4mu_2018,
    GluGluToContinToZZTo2mu2tau_2018,
    #GluGluToContinToZZTo2tau2nu_2018,
    GluGluToContinToZZTo4tau_2018,
]

TT_SemiLep_2018 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_SemiLep_2018")
TT_SemiLep_2018.year = "2018"
TT_SemiLep_2018.dataset = "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TT_SemiLep_2018.sigma = 687.1 #pb to check

TT_Had_2018 = sample(TTcolor, 1, 1001, "t#bar{t} semileptonic", "TT_Had_2018")
TT_Had_2018.year = "2018"
TT_Had_2018.dataset = "/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TT_Had_2018.sigma = 687.1 #pb to check

TT_2018 = sample(TTcolor, 1, 1001, "t#bar{t} hadronic + semileptonic", "TT_2018")
TT_2018.year = "2018"
TT_2018.components = [
    TT_SemiLep_2018,
    TT_Had_2018,
]

TTTo2L2Nu_2018 = sample(TTdilepcolor, 1, 1001, "t#bar{t} DiLep", "TTTo2L2Nu_2018")
TTTo2L2Nu_2018.year = "2018"
TTTo2L2Nu_2018.dataset = "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-20UL18JMENano_106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTTo2L2Nu_2018.sigma =  88.29 #pb

### TVX ###

TTGJets_2018 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTGJets_2018")
TTGJets_2018.year = "2018"
TTGJets_2018.dataset = "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTGJets_2018.sigma = 3.757

TTZToQQ_2018 = sample(TVXcolor, 1, 1001, "t#bar{t}#gamma + jets", "TTZToQQ_2018")
TTZToQQ_2018.year = "2018"
TTZToQQ_2018.dataset = "/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTZToQQ_2018.sigma = 0.5104

TTZToLLNuNu_2018 = sample(TVXcolor, 1, 1001, "t#bar{t}Z --> 2l2#nu", "TTZToLLNuNu_2018")
TTZToLLNuNu_2018.year = "2018"
TTZToLLNuNu_2018.dataset = "/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTZToLLNuNu_2018.sigma = 0.2439

TTWJetsToQQ_2018 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToQQ_2018")
TTWJetsToQQ_2018.year = "2018"
TTWJetsToQQ_2018.dataset = "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
TTWJetsToQQ_2018.sigma = 0.4377

#### to be replaced with v9 when available ####
TTWJetsToLNu_2018 = sample(TVXcolor, 1, 1001, "t#bar{t}W+jets --> qq", "TTWJetsToLNu_2018")
TTWJetsToLNu_2018.year = "2018"
TTWJetsToLNu_2018.dataset = "/TTWJetsToLNu_TuneCP5down_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"
TTWJetsToLNu_2018.sigma = 0.216

#### to be replaced with v9 when available ####
tZq_ll_4f_2018 = sample(TVXcolor, 1, 1001, "tZq --> ll", "tZq_ll_4f_2018")
tZq_ll_4f_2018.year = "2018"
tZq_ll_4f_2018.dataset = "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv2-106X_upgrade2018_realistic_v15_L1v1-v1/NANOAODSIM"
tZq_ll_4f_2018.sigma = 0.07561

TVX_2018 = sample(TVXcolor, 1, 1001, "tVX", "TVX_2018")
TVX_2018.year = "2018"
TVX_2018.components = [
    TTGJets_2018,
    TTZToQQ_2018,
    TTZToLLNuNu_2018,
    TTWJetsToQQ_2018,
    TTWJetsToLNu_2018,
    tZq_ll_4f_2018,
]

### VG ###

ZG_2018 = sample(VGcolor, 1, 1001, "Z #gamma", "ZG_2018")
ZG_2018.year = "2018"
ZG_2018.dataset = "/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
ZG_2018.sigma = 51.1 # to check

WG_2018 = sample(VGcolor, 1, 1001, "W #gamma", "WG_2018")
WG_2018.year = "2018"
WG_2018.dataset = "/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"
WG_2018.sigma = 191.3 # to check

VG_2018 = sample(VGcolor, 1, 1001, "V#gamma", "VG_2018")
VG_2018.year = "2018"
VG_2018.components = [
    ZG_2018,
    WG_2018,
]


########################################################

sample_dict={
    "ZZtoLep_2016APV":ZZtoLep_2016APV,
    "ZZTo2L2Nu_2016APV":ZZTo2L2Nu_2016APV, "ZZTo4L_2016APV":ZZTo4L_2016APV, "GluGluToContinToZZTo4e_2016APV":GluGluToContinToZZTo4e_2016APV, "GluGluToContinToZZTo2e2mu_2016APV":GluGluToContinToZZTo2e2mu_2016APV, "GluGluToContinToZZTo2e2tau_2016APV":GluGluToContinToZZTo2e2tau_2016APV,"GluGluToContinToZZTo2mu2nu_2016APV":GluGluToContinToZZTo2mu2nu_2016APV, "GluGluToContinToZZTo4mu_2016APV":GluGluToContinToZZTo4mu_2016APV, "GluGluToContinToZZTo2mu2tau_2016APV":GluGluToContinToZZTo2mu2tau_2016APV, "GluGluToContinToZZTo2tau2nu_2016APV":GluGluToContinToZZTo2tau2nu_2016APV, "GluGluToContinToZZTo4tau_2016APV":GluGluToContinToZZTo4tau_2016APV, "GluGluToContinToZZTo2e2nu_2016APV":GluGluToContinToZZTo2e2nu_2016APV,
    "TT_2016APV":TT_2016APV,
    "TT_SemiLep_2016APV":TT_SemiLep_2016APV, "TT_Had_2016APV":TT_Had_2016APV,
    "TTTo2L2Nu_2016APV":TTTo2L2Nu_2016APV,
    "TVX_2016APV":TVX_2016APV,
    "TTGJets_2016APV":TTGJets_2016APV, "TTZToQQ_2016APV":TTZToQQ_2016APV, "TTZToLLNuNu_2016APV":TTZToLLNuNu_2016APV, "TTWJetsToQQ_2016APV":TTWJetsToQQ_2016APV, "TTWJetsToLNu_2016APV":TTWJetsToLNu_2016APV, "tZq_ll_4f_2016APV":tZq_ll_4f_2016APV,
    "VG_2016APV":VG_2016APV,
    "ZG_2016APV":ZG_2016APV, "WG_2016APV":WG_2016APV,

    "ZZtoLep_2016":ZZtoLep_2016,
    "ZZTo2L2Nu_2016":ZZTo2L2Nu_2016, "ZZTo4L_2016":ZZTo4L_2016, "GluGluToContinToZZTo4e_2016":GluGluToContinToZZTo4e_2016, "GluGluToContinToZZTo2e2mu_2016":GluGluToContinToZZTo2e2mu_2016, "GluGluToContinToZZTo2e2tau_2016":GluGluToContinToZZTo2e2tau_2016, "GluGluToContinToZZTo2mu2nu_2016":GluGluToContinToZZTo2mu2nu_2016, "GluGluToContinToZZTo4mu_2016":GluGluToContinToZZTo4mu_2016, "GluGluToContinToZZTo2mu2tau_2016":GluGluToContinToZZTo2mu2tau_2016, "GluGluToContinToZZTo2tau2nu_2016":GluGluToContinToZZTo2tau2nu_2016, "GluGluToContinToZZTo4tau_2016":GluGluToContinToZZTo4tau_2016, "GluGluToContinToZZTo2e2nu_2016":GluGluToContinToZZTo2e2nu_2016,
    "TT_2016":TT_2016,
    "TT_SemiLep_2016":TT_SemiLep_2016, "TT_Had_2016":TT_Had_2016,
    "TTTo2L2Nu_2016":TTTo2L2Nu_2016,
    "TVX_2016":TVX_2016,
    "TTGJets_2016":TTGJets_2016, "TTZToQQ_2016":TTZToQQ_2016, "TTZToLLNuNu_2016":TTZToLLNuNu_2016, "TTWJetsToQQ_2016":TTWJetsToQQ_2016, "TTWJetsToLNu_2016":TTWJetsToLNu_2016, "tZq_ll_4f_2016":tZq_ll_4f_2016,
    "VG_2016":VG_2016,
    "ZG_2016":ZG_2016, "WG_2016":WG_2016,

    "ZZtoLep_2017":ZZtoLep_2017,
    "ZZTo2L2Nu_2017":ZZTo2L2Nu_2017, "ZZTo4L_2017":ZZTo4L_2017, "GluGluToContinToZZTo4e_2017":GluGluToContinToZZTo4e_2017, "GluGluToContinToZZTo2e2mu_2017":GluGluToContinToZZTo2e2mu_2017, "GluGluToContinToZZTo2e2tau_2017":GluGluToContinToZZTo2e2tau_2017, "GluGluToContinToZZTo2mu2nu_2017":GluGluToContinToZZTo2mu2nu_2017, "GluGluToContinToZZTo4mu_2017":GluGluToContinToZZTo4mu_2017, "GluGluToContinToZZTo2mu2tau_2017":GluGluToContinToZZTo2mu2tau_2017, "GluGluToContinToZZTo2tau2nu_2017":GluGluToContinToZZTo2tau2nu_2017, "GluGluToContinToZZTo4tau_2017":GluGluToContinToZZTo4tau_2017, "GluGluToContinToZZTo2e2nu_2017":GluGluToContinToZZTo2e2nu_2017,
    "TT_2017":TT_2017,
    "TT_SemiLep_2017":TT_SemiLep_2017, "TT_Had_2017":TT_Had_2017,
    "TTTo2L2Nu_2017":TTTo2L2Nu_2017,
    "TVX_2017":TVX_2017,
    "TTGJets_2017":TTGJets_2017, "TTZToQQ_2017":TTZToQQ_2017, "TTZToLLNuNu_2017":TTZToLLNuNu_2017, "TTWJetsToQQ_2017":TTWJetsToQQ_2017, "TTWJetsToLNu_2017":TTWJetsToLNu_2017, "tZq_ll_4f_2017":tZq_ll_4f_2017,
    "VG_2017":VG_2017,
    "ZG_2017":ZG_2017, "WG_2017":WG_2017,

    "ZZtoLep_2018":ZZtoLep_2018,
    "ZZTo2L2Nu_2018":ZZTo2L2Nu_2018, "ZZTo4L_2018":ZZTo4L_2018, "GluGluToContinToZZTo4e_2018":GluGluToContinToZZTo4e_2018, "GluGluToContinToZZTo2e2mu_2018":GluGluToContinToZZTo2e2mu_2018, "GluGluToContinToZZTo2e2tau_2018":GluGluToContinToZZTo2e2tau_2018, "GluGluToContinToZZTo2mu2nu_2018":GluGluToContinToZZTo2mu2nu_2018, "GluGluToContinToZZTo4mu_2018":GluGluToContinToZZTo4mu_2018, "GluGluToContinToZZTo2mu2tau_2018":GluGluToContinToZZTo2mu2tau_2018, "GluGluToContinToZZTo2tau2nu_2018":GluGluToContinToZZTo2tau2nu_2018, "GluGluToContinToZZTo4tau_2018":GluGluToContinToZZTo4tau_2018, "GluGluToContinToZZTo2e2nu_2018":GluGluToContinToZZTo2e2nu_2018,
    "TT_2018":TT_2018,
    "TT_SemiLep_2018":TT_SemiLep_2018, "TT_Had_2018":TT_Had_2018,
    "TTTo2L2Nu_2018":TTTo2L2Nu_2018,
    "TVX_2018":TVX_2018,
    "TTGJets_2018":TTGJets_2018, "TTZToQQ_2018":TTZToQQ_2018, "TTZToLLNuNu_2018":TTZToLLNuNu_2018, "TTWJetsToQQ_2018":TTWJetsToQQ_2018, "TTWJetsToLNu_2018":TTWJetsToLNu_2018, "tZq_ll_4f_2018":tZq_ll_4f_2018,
    "VG_2018":VG_2018,
    "ZG_2018":ZG_2018, "WG_2018":WG_2018,
]

]

}

merge_dict={
}


class_list=[
]

class_list_bis = [
]

