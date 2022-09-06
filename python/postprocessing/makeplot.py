import os 
import sys
import optparse
import ROOT
import math
from variabile import variabile
import copy as copy
from CMS_lumi import CMS_lumi
from array import array
#import pandas as pd
#import uproot
#import pickle
#import numpy as np
#import sklearn
#import xgboost
from rwgcards.FromCardToDict import *

rwgdict = CardToDict("dim8", "FT1_2p0")

desiredop = [
    "FS0_1p0",
    "FS1_1p0",
    "FS2_1p0",
    "FM0_1p0",
    "FM1_0p9",
    "FM6_1p0",
    "FM7_1p0",
    "FT0_1p0",
    "FT1_1p0",
    "FT2_0p9",
]

wcoeff = []
for opname, opdict in rwgdict.items():
    coeffstr = ""
    for val in opdict.keys():
        coeffstr = opname + "_" + val
        if coeffstr in desiredop:
            wcoeff.append(coeffstr)

typcontr = [
    "0",
    "SM",
    "BSM",
]

ROOT.ROOT.EnableThreadSafety()

usage = 'python3 makeplot.py'# -y year --lep lepton -d dataset --merpart --lumi --mertree --sel --cut cut_string -p -s'
usageToCopyPaste= "python3 makeplot.py -y 2017 --lep muon --bveto --user apiccine -f v4 -p"

parser = optparse.OptionParser(usage)
parser.add_option('--merpart', dest='merpart', default = False, action='store_true', help='Default parts are not merged')
parser.add_option('--mertree', dest='mertree', default = False, action='store_true', help='Default make no file is merged')
parser.add_option('--lumi', dest='lumi', default = False, action='store_true', help='Default do not write the normalization weights')
parser.add_option('--sel', dest='sel', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('--bveto', dest='bveto', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('--bbv', dest='bbv', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('--sr', dest='sr', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('--bdt', dest='bdt', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('--ebdt', dest='ebdt', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('--mubdt', dest='mubdt', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('-p', '--plot', dest='plot', default = False, action='store_true', help='Default make no plots')
parser.add_option('-s', '--stack', dest='stack', default = False, action='store_true', help='Default make no stacks')
parser.add_option('-N', '--notstacked', dest='tostack', default = True, action='store_false', help='Default make plots stacked')
parser.add_option('-L', '--lep', dest='lep', type='string', default = 'incl', help='Default make incl analysis')
parser.add_option('-S', '--syst', dest='syst', type='string', default = 'all', help='Default all systematics added')
parser.add_option('-C', '--cut', dest='cut', type='string', default = '1.', help='Default no cut')
parser.add_option('-y', '--year', dest='year', type='string', default = '2017', help='Default 2016, 2017 and 2018 are included')
parser.add_option('-f', '--folder', dest='folder', type='string', default = 'v7', help='Default folder is v0')
parser.add_option('-d', '--dat', dest='dat', type='string', default = 'all', help="")
parser.add_option('--user', dest='user', type='string', default=str(os.environ.get('USER')), help='User')
parser.add_option('--ttbar', dest='ttbar', default = False, action='store_true', help='Enable ttbar CR, default disabled')
parser.add_option('--tDMcut', dest='tDMcut', default = False, action='store_true', help='Enable tau DecayMode cut')
parser.add_option('--test', dest='test', default = False, action='store_true', help='Enable test saving')
parser.add_option('--count', dest='count', default = False, action='store_true', help='Enable countings')
parser.add_option('--HT', dest='HT', default = False, action='store_true', help='Enable CTHT')
parser.add_option('--wfake', dest='wfake', type='string', default = 'fake', help='Enable stackplots with data-driven fake leptons, default disabled')
parser.add_option('--wjets', dest='wjets', default = False, action='store_true', help='Enable WJets CR, default disabled')
parser.add_option('--fakes', dest='fakes', default = False, action='store_true', help='Enable FL CR, default disabled')
parser.add_option('--presel', dest='presel', default = False, action='store_true', help='Enable Presel Region, default disabled')
parser.add_option('--ws', dest='ws', default = False, action='store_true', help='Enable WrongSign CR, default disabled')
parser.add_option('--dy', dest='dy', default = False, action='store_true', help='Enable DY CR, default disabled')
parser.add_option('--wsdy', dest='wsdy', default = False, action='store_true', help='Enable DY+WS CR, default disabled')
parser.add_option('--qcd', dest='qcd', default = False, action='store_true', help='Enable QCD CR, default disabled')
parser.add_option('--blinded', dest='blinded', default = False, action='store_true', help='Activate blinding')
parser.add_option('--signal', dest='signal', default = False, action='store_true', help='Activate only signal')
parser.add_option('--horn', dest='horn', default = False, action='store_true', help='eta horns for 2017')
parser.add_option('--rPrompt', dest='removePrompt', default = False, action='store_true', help='default runs ML')
parser.add_option('--ch', dest='channel', type=str, default = 'ltau', help='Select final state, default is h_tau + lepton')
parser.add_option('-v', dest='varss', type=str, default = 'all', help='Select variables to plot')
parser.add_option('--plot_tag', dest='plot_tag', type=str, default = '', help='Tag to distinguish between different makeplot runs')
parser.add_option('--bvetoL', dest='bvetoL', default = False, action='store_true', help='apply bveto loose in ws and dy CRs')

(opt, args) = parser.parse_args()

#if "UL" in opt.year:
    #from PhysicsTools.NanoAODTools.postprocessing.samples.samplesUL import *
#else:
    #from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *

if "UL" in opt.year:
    from samples.samplesUL import *
else:
    from samples.samples import *


def cutToTag(cut):
    newstring = cut.replace("-", "neg").replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("!=","_NEQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
    return newstring

bvetostring = ""
if opt.bvetoL:
    bvetostring = "pass_b_veto_loose[0]==1"
else:
    bvetostring = "pass_b_veto[0]==1"

folder = opt.folder 
if not "btag" in opt.folder and not(opt.folder.startswith('FR_')) and (("mcreco" in opt.folder and int(opt.folder.split("mcreco")[-1].split("v")[-1]) >= 80) or not "mcreco" in opt.folder):
    folder += "/" + opt.channel
plot_tag = opt.plot_tag
if opt.tDMcut:
    plot_tag = "_tDM"
elif opt.test:
    plot_tag = "_test"
pfolder = opt.folder #+ opt.plot_tag

filerepo = '/eos/home-a/apiccine/VBS/nosynch/' + folder + '/'
plotrepo = '/eos/home-a/apiccine/VBS/nosynch/' + pfolder + '/'
print("pfolder", pfolder, opt.test)
print(filerepo, plotrepo)

FRtag = opt.wfake.split("_")[-1]

ROOT.gROOT.SetBatch() # don't pop up canvases
if opt.lep != 'incl':
    lepstr = 'plot/' + opt.lep
else:
    if opt.channel == 'emu':
        lepstr = 'plot/' + opt.channel
    else:
        lepstr = 'plot/' + opt.lep
if opt.tDMcut:
    lepstr = lepstr.replace("plot", "plot_tDM")
elif opt.test:
    lepstr = lepstr.replace("plot", "plot_test")

cut = opt.cut #default cut must be obvious, for example 1.
vartoplot = opt.varss.split(",")
print("To plot:", vartoplot)

epdgstr = ""
mpdgstr = ""
if opt.channel=="ltau":
    epdgstr = "lepton"
    mpdgstr = "lepton"
elif opt.channel=="emu":
    epdgstr = "electron"
    mpdgstr = "muon"

incl_logic = ''
if opt.channel == 'emu':
    incl_logic = '&&'
else:
    incl_logic = '||'


if opt.bveto:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_upToBVeto==1)*(" + cut + ")", 
                 'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_upToBVeto==1)*(" + cut + ")", 
                 'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_upToBVeto==1)*(" + cut + ")", 
    }
    cut_tag = 'selection_upto_bveto'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut) 

elif opt.ws:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_charge_selection==0&&" + bvetostring + "&&pass_jet_selection==1&&MET_pt>50.)*(" + cut + ")", 
                 'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_charge_selection==0&&" + bvetostring + "&&pass_jet_selection==1&&MET_pt>50.)*(" + cut + ")", 
                 'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==0&&pass_charge_selection==0&&pass_b_veto==1&&pass_jet_selection==1&&pass_tau_veto==1&&MET_pt>50.)*(" + cut + ")", 
    }
    cut_tag = 'wrongsing_CR'
    if opt.bvetoL:
        cut_tag += '_bvetoL'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut) 

elif opt.wsdy:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_charge_selection==0&&" + bvetostring + "&&pass_jet_selection==1)*(" + cut + ")", 
                 'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_charge_selection==0&&" + bvetostring + "&&pass_jet_selection==1)*(" + cut + ")", 
                 'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==0&&pass_charge_selection==0&&pass_b_veto==1&&pass_jet_selection==1&&pass_tau_veto==1)*(" + cut + ")", 
    }
    cut_tag = 'OS_CR'
    if opt.bvetoL:
        cut_tag += '_bvetoL'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut) 

elif opt.sr:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_upToBVeto==1&&m_jj>500.&&MET_pt>50.)*(" + cut + ")", 
                'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_upToBVeto==1&&m_jj>500.&&MET_pt>50.)*(" + cut + ")", 
                'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_upToBVeto==1&&m_jj>500.&&MET_pt>50.)*(" + cut + ")", 
            }
    cut_tag = 'SR'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut) 

elif opt.presel:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1)*(" + cut + ")", 
                'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1)*(" + cut + ")", 
                'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==0)*(" + cut + ")", 
            }
    cut_tag = 'presel'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut)           

elif opt.ttbar:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_charge_selection==0&&pass_b_veto==0&&pass_jet_selection==1&&MET_pt>50.)*(" + cut + ")", 
                'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_charge_selection==0&&pass_b_veto==0&&pass_jet_selection==1&&MET_pt>50.)*(" + cut + ")", 
                'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==0&&pass_charge_selection==0&&pass_jet_selection==1&&pass_b_veto==0&&pass_tau_veto==1&&MET_pt>50.)*(" + cut + ")", 
            }
    cut_tag = 'ttbar_CR'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut)           

elif opt.fakes:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_charge_selection==1&&MET_pt<=50.)*(" + cut + ")", 
                'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_charge_selection==1&&MET_pt<=50.)*(" + cut + ")",
                'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_charge_selection==1&&pass_tau_veto==1&&MET_pt<=50.)*(" + cut + ")",
            }
    cut_tag = 'fakes_CR'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut)
elif opt.wjets:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_charge_selection==1&&MET_pt<=50.&&mT_lep_MET>50.)*(" + cut + ")", 
                'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_charge_selection==1&&MET_pt<=50.&&mT_lep_MET>50.)*(" + cut + ")",
                'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_charge_selection==1&&pass_tau_veto==1&&MET_pt<=50.&&(mT_electron_MET>50.||mT_muon_MET>50.))*(" + cut + ")",
            }
    cut_tag = 'wjets_CR'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut)           
elif opt.qcd:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_charge_selection==1&&MET_pt<=50.&&mT_lep_MET<50.)*(" + cut + ")", 
                'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_charge_selection==1&&pass_jet_selection==1&&MET_pt<=50.&&mT_lep_MET<50.)*(" + cut + ")",
                'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_tau_veto==1&&MET_pt<=50.&&(mT_electron_MET<50.&&mT_muon_MET<50.))*(" + cut + ")",
            }
    cut_tag = 'QCD_CR'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut)           
elif opt.dy:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&" + bvetostring + "&&pass_charge_selection==0&&MET_pt<=50.)*(" + cut + ")", 
                'electron':"(abs(" + epdgstr + "_pdgid)==11&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_lepton_veto==1&&pass_jet_selection==1&&" + bvetostring + "&&pass_charge_selection==0&&MET_pt<=50.)*(" + cut + ")",
                'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&pass_lepton_selection==1&&pass_tau_selection==1&&pass_charge_selection==0&&" + bvetostring + "&&pass_lepton_veto==1&&pass_jet_selection==1&&pass_tau_veto==1&&MET_pt<=50.)*(" + cut + ")",
            }
    cut_tag = 'DY_CR'
    if opt.bvetoL:
        cut_tag += '_bvetoL'
    if opt.cut != "1.":
        cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut)           
elif opt.sel:
    cut_dict = {'muon':"(abs(" + mpdgstr + "_pdgid)==13)*(" + cut + ")*(pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&pass_mjj_cut==1&&pass_MET_cut==1)", 
                'electron':"(abs(" + epdgstr + "_pdgid)==11)*(" + cut + ")*(pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&pass_mjj_cut==1&&pass_MET_cut==1)", 
                'incl':"((abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11))*(" + cut + ")*(pass_lepton_selection==1&&pass_lepton_veto==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&pass_tau_veto==1)", 
            }
    cut_tag = "selection"
    if opt.cut != "1.":
        cut_tag = cut_tag + '_AND_' + cutToTag(opt.cut) 
        
else:
    cut_dict = {'muon':"abs(" + mpdgstr + "_pdgid)==13&&(" + cut + ")",
                'electron':"abs(" + epdgstr + "_pdgid)==11&&(" + cut + ")",
                'incl':"(abs(" + mpdgstr + "_pdgid)==13" + incl_logic + "abs(" + epdgstr + "_pdgid)==11)&&(" + cut + ")",
            }
    cut_tag = cutToTag(opt.cut)

for k, v in cut_dict.items():
    cut_dict[k] = v + "*(abs(deltaEta_jj)>2.5)"

if opt.bdt or opt.ebdt or opt.mubdt:
    bdt_cut = "*(BDT_output"
    if opt.ebdt:
        bdt_cut = bdt_cut + "_ele"
    elif opt.mubdt:
        bdt_cut = bdt_cut + "_mu"

    tresh_bdt = ""
    if opt.bdt:
        tresh_bdt = "-0.425"
    elif opt.ebdt:
        tresh_bdt = "-0.536"
    elif opt.mubdt:
        tresh_bdt = "-0.399"

    sign_bdt = ""
    if opt.bveto or opt.sr:
        sign_bdt = ">"
    elif opt.ttbar or opt.wjets:
        sign_bdt = "<"

    bdt_cut = bdt_cut + sign_bdt + tresh_bdt + ")"

    for k, v in cut_dict.items():
        cut_dict[k] = v + bdt_cut

    if opt.bdt:
        cut_tag = cut_tag + "_BDTcut"
    elif opt.ebdt or opt.mubdt:
        cut_tag = cut_tag + "_lepBDTcut"        

if opt.tDMcut:
    for k, v in cut_dict.items():
        cut_dict[k] = v + "*(tau_DecayMode<5||tau_DecayMode>6)"

lumi = {'2016': 35.9, 'UL2016M': 35.9, 'UL2016APV': 19.5, 'UL2016': 16.8, "2017": 41.53, 'UL2017': 41.5, "2018": 59.7, 'UL2018':59.8, "ULRunII":137.1}

scenarios = [
    "nominal",
    "lepenUp",
    "lepenDown",
    "jesUp",
    "jesDown",
    "jerUp",
    "jerDown",
    "TESUp", 
    "TESDown",
    "FESUp", 
    "FESDown"
]
nomtag = "nominal"

systematicslist = [
    ["", True, ""],
    ["PFUp", True, "exp"],
    ["PFDown", True, "exp"],
    ["lepUp", True, "exp"],
    ["lepDown", True, "exp"],
    ["puUp", True, "exp"],
    ["puDown", True, "exp"],
    ["puIDUp", True, "exp"],
    ["puIDDown", True, "exp"],
    ["btagUp", True, "exp"],
    ["btagDown", True, "exp"],
    ["mistagUp", True, "exp"],
    ["mistagDown", True, "exp"],
    ["tau_vsjet_Up", True, "exp"],
    ["tau_vsjet_Down", True, "exp"],
    ["tau_vsele_Up", True, "exp"],
    ["tau_vsele_Down", True, "exp"],
    ["tau_vsmu_Up", True, "exp"],
    ["tau_vsmu_Down", True, "exp"],
    ["pdf_totalUp", True, "exp"],
    ["pdf_totalDown", True, "exp"],
    ["QCDScaleUp", True, "exp"],
    ["QCDScaleDown", True, "exp"],
    ["VBSUp", True, "exp"],
    ["VBSDown", True, "exp"],
    ["ISRUp", True, "th"],
    ["ISRDown", True, "th"],
    ["FSRUp", True, "th"],
    ["FSRDown", True, "th"],
    ["jesUp", True, "en"],
    ["jesDown", True, "en"],
    ["lepenUp", True, "en"],
    ["lepenDown", True, "en"],
    ["jerUp", True, "en"],
    ["jerDown", True, "en"],
    ["TESUp", True, "en"],
    ["TESDown", True, "en"],
    ["FESUp", True, "en"],
    ["FESDown", True, "en"],
]

#["trigUp", False, "exp"],
#["trigDown", False, "exp"],

wanted_systs = opt.syst.split(",")
systematics = []

if opt.syst!="all" and opt.syst!="noSyst":
     for wsyst in wanted_systs:
         for syst in systematicslist:
             if syst[0] == wsyst:
                 systematics.append(syst)
                 break
             else:
                 continue
elif opt.syst!="all" and opt.syst=="noSyst":
    for syst in systematicslist:
        if syst[0] == "":
            #print("hello", syst)
            systematics.append(syst)
        else:
            continue
else:
    for syst in systematicslist:
        if "lepen" in syst[0]:
            continue
        systematics.append(syst)
if opt.plot or opt.stack:
    print("systematics to plot:")
    for syst in systematics:
        print(syst[0])

print("\ncut_tag:\t", cut_tag)

pathplot = plotrepo + lepstr  + "/"

pathstack = plotrepo + "stack" + "/" + cut_tag + "/"
if opt.tDMcut:
    pathstack = pathstack.replace("stack", "stack_tDM")
elif opt.test:
    pathstack = pathstack.replace("stack", "stack_test")

print(lepstr, pathplot, pathstack) 

if opt.plot:
    if not os.path.exists(pathplot) and cut_tag != "1p":
        os.system("mkdir -p " + pathplot)

if opt.stack:
    if not os.path.exists(plotrepo + 'stack') and cut_tag != "1p":
        os.system("mkdir -p " + plotrepo + 'stack')
    if not os.path.exists(pathstack) and cut_tag != "1p":
        os.system("mkdir -p " + pathstack)

def mergepart(dataset):
    print("\nhello babe\n")
    samples = []
    hascomp = False
    if "UL" in opt.year:
        hascomp = hasattr(dataset, "components")
    else:
        hascomp = dataset.components is not None
    if hascomp:#hasattr(dataset, 'components'): # How to check whether this exists or not
        samples = [sample for sample in dataset.components]# Method exists and was used.
    else:
        samples.append(dataset) 
    
    for sample in samples:
        # merge files 
        add = "hadd -f " + filerepo + sample.label + "/"  + sample.label + "_merged.root " + filerepo + sample.label + "/"  + sample.label + "_part*.root" 
        os.system(str(add))
            
def mergetree(sample):
    if not os.path.exists(filerepo + sample.label):
        os.system("mkdir -p " + filerepo + sample.label)
    hascomp = False
    if "UL" in opt.year:
        hascomp = hasattr(sample, "components")
    else:
        hascomp = sample.components is not None
    if hascomp:#hasattr(sample, 'components'): # How to check whether this exists or not
        add = "hadd -f " + filerepo + sample.label + "/"  + sample.label + ".root" 
        for comp in sample.components:
            add+= " " + filerepo + comp.label + "/"  + comp.label + ".root" 
        os.system(str(add))

def lumi_writer(dataset, lumi):
    samples = []
    hascomp = False
    if "UL" in opt.year:
        hascomp = hasattr(dataset, "components")
    else:
        hascomp = dataset.components is not None
    if hascomp:#hasattr(dataset, 'components'): # How to check whether this exists or not
        samples = [sample for sample in dataset.components]# Method exists and was used.
    else:
        samples.append(dataset)
    
    for sample in samples:
        if not ('Data' in sample.label):# or 'TT_dilep' in sample.label):
            infile =  ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + "_merged.root")
            isthere_gen = bool(infile.GetListOfKeys().Contains("h_genweight"))
            ik = 0
            outfile =  ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root","RECREATE")
            for key in scenarios:
                evtree = "events_" + key
                try:
                    tree = infile.Get(evtree)
                except:
                    continue
                else:
                    pass
                
                print("evtree:", evtree, tree)
                tree.SetBranchStatus('w_nominal', 0)
                tree_new = tree.CloneTree(0)
                h_genw_tmp = ROOT.TH1F(infile.Get("h_genweight"))

                w_nom = array('f', [0.]) 
                tree_new.Branch('w_nominal', w_nom, 'w_nominal/F')
                tree.SetBranchStatus('w_nominal', 1)
                
                print("Calculating renormalization weights for scenario", key)
                for event in range(0, tree.GetEntries()):
                    tree.GetEntry(event)
                    perc = (event+1)/(tree.GetEntries())*100

                    w_nom[0] = tree.w_nominal * sample.sigma * tree.HLT_effLumi * 1000./float(h_genw_tmp.GetBinContent(1))
                    if (int(perc)) != 0 and perc%int(perc) == 0. or event==(tree.GetEntries()-1):
                        sys.stdout.write("\nProcessing event {0}     complete {1:.0f} percent".format(event, 100*event/tree.GetEntries()))
                        print("\nw_nom before:", w_nom[0])
                    if sample.year == "UL2016APV":
                        w_nom[0] *= 0.5373
                        if (int(perc)) != 0 and perc%int(perc) == 0. or event==(tree.GetEntries()-1):
                            print("0.5373 added")
                    elif sample.year == "UL2016":
                        w_nom[0] *= 0.4627
                        if (int(perc)) != 0 and perc%int(perc) == 0. or event==(tree.GetEntries()-1):
                            print("0.4627 added")

                    if (int(perc)) != 0 and perc%int(perc) == 0. or event==(tree.GetEntries()-1):
                        print("w_nom after:", w_nom[0])
                    tree_new.Fill()
                tree_new.Write()
                print("\n")
            outfile.Close()
            print('\n')

        else:
            os.popen("mv " + filerepo + sample.label + "/"  + sample.label + "_merged.root " + filerepo + sample.label + "/"  + sample.label + ".root")


def plot(f1, fout, samplelab, lep, reg, variable, sample, cut_tag, systlist=["nominal", ("", False)], sampletagg = "", dim8cut = ""):
    syst = systlist[0]
    isSystCorr = systlist[1]
    systtype = systlist[2]

    if systtype == "en":
        systtree = syst
    else:
        systtree = scenarios[0]

    treename = "events_"

    isdim8 = False
    if (not "_UL" in sample.label and sample.label.startswith("VBS_SSWW_F")) or ("_UL" in sample.label and sample.label.startswith("VBS_SSWW_aQGC")):
        isdim8 = True
  
    ROOT.TH1.SetDefaultSumw2()
    cutbase = variable._taglio
    histag = variable._name
    if variable._name.startswith("min"):
        histag = "min_deltaPhi_MET"
    if variable._name.startswith("max"):
        histag = "max_deltaPhi_MET"
 
    histoname = "h_" + histag + "_" + cut_tag
    treename += systtree

    print("\n" + samplelab)
    if systtype == "exp":
        nominal = syst.replace("Up", "SF").replace("Down", "SF")
        cutbase += '*(1./abs(' + nominal + '))'
    if systtype != "en" and syst != "":
        cutbase += '*(' + syst + ')'

    if syst != "":
        #print("hello", syst)
        histoname += "_" + syst.replace("_Up", "Up").replace("_Down", "Down")
        if not isSystCorr:
            histoname += "_" + str(opt.year).replace("UL", "")
        
    cut = ''
    
    if opt.count and syst == "":# and variable._name == "countings":
        if not "_aQGC_" in sample.label:
            samcountlab = sample.leglabel
        else:
            samcountlab = sampletagg.replace("VBS_SSWW_", "EFT ").replace("_", "=").replace("p", ".")
        countf = open(pathplot + 'countings/' + cut_tag + "/" + variable._name + "_" + str(opt.year) + syst.replace("_Up", "Up").replace("_Down", "Down") + ".csv", "a")
        countf.write(samcountlab)
        countf.write(';')
        #countf.write("\nBin\tContent\tError")
    
    if opt.channel=="ltau":
        l1fstr = "lepton"
        l2fstr = "tau"
    elif opt.channel=="emu":
        l1fstr = "electron"
        l2fstr = "muon"
    
    if 'Fake' in str(sample.label):
        if str(sample.label).startswith('FakeEle_') or str(sample.label).startswith('FakeMu_'):
            if opt.channel == 'ltau':
                cut = cutbase + "*(" + l1fstr + "_LnTRegion==1||" + l2fstr + "_LnTRegion==1)*(event_SFFake)*(event_SFFake>-100.)"
        elif str(sample.label).startswith('FakeElePromptTau') or str(sample.label).startswith('FakeMuPromptTau'):
            if opt.channel == 'ltau':
                cut = cutbase + "*(" + l1fstr + "_LnTRegion==1&&" + l2fstr + "_LnTRegion==0)*(event_SFFake)*(event_SFFake>-100.)"
        elif str(sample.label).startswith('PromptEleFakeTau') or str(sample.label).startswith('PromptMuFakeTau'):
            if opt.channel == 'ltau':
                cut = cutbase + "*(" + l1fstr + "_LnTRegion==0&&" + l2fstr + "_LnTRegion==1)*(event_SFFake)*(event_SFFake>-100.)"
        elif str(sample.label).startswith('FakeEleFakeTau') or str(sample.label).startswith('FakeMuFakeTau'):
            if opt.channel == 'ltau':
                cut = cutbase + "*(" + l1fstr + "_LnTRegion==1&&" + l2fstr + "_LnTRegion==1)*(event_SFFake)*(event_SFFake>-100.)"
        elif str(sample.label).startswith('FakeEleMu'):
            if opt.channel == 'emu':
                cut = cutbase + "*(" + "((" + l1fstr + "_LnTRegion==1&&" + l2fstr + "_LnTRegion==0)*(" + l1fstr + "_SFFake))+((" + l1fstr + "_LnTRegion==0&&" + l2fstr + "_LnTRegion==1)*(" + l2fstr + "_SFFake_vsjet2" + "))+((" + l1fstr + "_LnTRegion==1&&" + l2fstr + "_LnTRegion==1)*(" + l1fstr + "_SFFake*" + l2fstr + "_SFFake))" + ")"

    else:
        cut = cutbase + "*(" + l1fstr + "_TightRegion==1&&" + l2fstr + "_TightRegion==1)"

    '''
    if not ("Data" in sample.label):
        if sample.year == "UL2016APV":
            cut += "*(0.5373)"
        elif sample.year == "UL2016":
            cut += "*(0.4627)"
        else:
            cut += "*(1.)"
    '''

    if not ('Fake' in str(sample.label) or 'Data' in str(sample.label)):
        if opt.channel == 'ltau':
            cut = cut + "*((" + l1fstr + "_isPrompt==1||" + l1fstr + "_isPrompt==15)&&" + l2fstr + "_isPrompt==5)"
        elif opt.channel == 'emu':
             cut = cut + "*((" + l1fstr + "_isPrompt==1||" + l1fstr + "_isPrompt==15)&&(" + l2fstr + "_isPrompt==1||" + l2fstr + "_isPrompt==15))"

    if isdim8:
        if not "_UL" in sample.label:
            cut = "(w_dim8[0])*" + cut
        else:
            cut = "(" + dim8cut + ")*" + cut
            samplelab = sampletagg
    else:
        samplelab = sample.label
    
    #print("after syst applied\tcut", cut, "\nhistoname:", histoname, "\ttreename:", treename)
    print("plotting ", variable._name, "\nsample:", samplelab, "\ncut:", cut_tag, "\nsyst applied:", syst)
    
    nbins = variable._nbins

    if not variable._iscustom:
        h1 = ROOT.TH1F(histoname, variable._name + "_" + reg, variable._nbins, variable._xmin, variable._xmax)
    else:
        h1 = ROOT.TH1F(histoname, variable._name + "_" + reg, variable._nbins, variable._xmin)

    h1.Sumw2()

    vartoproject = ''
    if variable._name == 'countings':
        vartoproject = 'm_jj'
    elif variable._name.startswith("lepBDT_"):
        vartoproject = "BDT_output_"
        if lep == 'muon':
            vartoproject = vartoproject + "mu"
        elif lep == 'electron':
            vartoproject = vartoproject + "ele"
        elif lep == 'incl':
            vartoproject = "BDT_output_ele*(abs(lepton_pdgid)==11)+BDT_output_mu*(abs(lepton_pdgid)==13)"
    else:
        vartoproject = variable._name

    if 'MC' in variable._name:
        cut = cut + "*(" + str(vartoproject) + "!-100.)"
    else:
        cut = cut + "*(" + str(vartoproject) + ">-10.)"

    #if "WpWpJJ_EWK" in samplelab or 'VBS_SSWW' in samplelab:
        #cut = cut + "*10."

    if opt.horn:
        cut = cut + "*(abs(leadjet_eta)>3.2||abs(leadjet_eta)<2.5)*(abs(subleadjet_eta)>3.2||abs(subleadjet_eta)<2.5)"

    foutput = pathplot + sample.label + "_" + lep + ".root"
    #print("at project", histoname,vartoproject,cut)
    f1.Get(treename).Project(histoname,vartoproject,cut)
    h1.SetBinContent(1, h1.GetBinContent(0) + h1.GetBinContent(1))
    h1.SetBinError(1, math.sqrt(pow(h1.GetBinError(0),2) + pow(h1.GetBinError(1),2)))
    h1.SetBinContent(nbins, h1.GetBinContent(nbins) + h1.GetBinContent(nbins+1))
    h1.SetBinError(nbins, math.sqrt(pow(h1.GetBinError(nbins),2) + pow(h1.GetBinError(nbins+1),2)))
    
    tot = 0.
    terr = 0.

    for i in range(0, nbins+1):
        content = h1.GetBinContent(i)
        #print("content bin #" + str(i+1) + ":\t" + str(content))
        if content < 0. and not (isdim8 or "SSWW_c" in sample.label):
            h1.SetBinContent(i, 0.)

    for bidx in range(nbins):          
        bidx_l = bidx + 1
        if str(sample.label).startswith('Fake') or str(sample.label).startswith('Prompt'):
            h1.SetBinError(bidx_l, 0.3*h1.GetBinContent(bidx_l))

        if not (opt.count):# and variable._name == "countings"):
            continue
        else:
            minedge = str(round(h1.GetBinLowEdge(bidx_l), 3))
            maxedge = str(round(h1.GetBinLowEdge(bidx_l) + h1.GetBinWidth(bidx_l), 3))
            bincont = round(h1.GetBinContent(bidx_l), 6)
            tot += bincont
            bincont = str(bincont)
            binerrcont = round(h1.GetBinError(bidx_l), 6)
            terr += binerrcont**2.
            binerrcont = str(binerrcont)

    if opt.count and syst == "":# and variable._name == "countings":
        terr = terr**0.5
        countf.write(str(bincont).replace(".",",") + ";" + str(binerrcont).replace(".",","))
        countf.write("\n")
        countf.close()
    fout.cd()
    h1.Write(h1.GetName(), ROOT.TObject.kWriteDelete)
    
def makestack(lep_, reg_, variabile_, samples_, cut_tag_, syst_, lumi, year):
    os.system('set LD_PRELOAD=libtcmalloc.so')
    histag = variabile_._name
    if variabile_._name.startswith("min"):
        histag = "min_deltaPhi_MET"
    if variabile_._name.startswith("max"):
        histag = "max_deltaPhi_MET"

    if reg_ == 'ltau':
        if str(lep_).strip('[]') == "muon":
            lep_tag = "#mu+"
        elif str(lep_).strip('[]') == "electron":
            lep_tag = "e+"
        cmsreg = reg_.replace("ltau", "#tau_{h}")
    else:
        lep_tag = "e+#mu"
        cmsreg = ""

    cmsreg = lep_tag + cmsreg 
    
    blind = False
    infile = {}
    histo = []
    tmp = ROOT.TH1F()
    h = ROOT.TH1F()
    if not variabile_._iscustom:
        hdata = ROOT.TH1F('h','h', variabile_._nbins, variabile_._xmin, variabile_._xmax)
    else:
        hdata = ROOT.TH1F('h','h', variabile_._nbins, variabile_._xmin)
    h_sig = []
    h_err = ROOT.TH1F()
    h_bkg_err = ROOT.TH1F()
    print("Variabile:", variabile_._name)
    ROOT.gROOT.SetStyle('Plain')
    ROOT.gStyle.SetPalette(1)
    ROOT.gStyle.SetOptStat(0)
    ROOT.TH1.SetDefaultSumw2()
    if(cut_tag_ == ""):
        histoname = "h_" + histag #variabile_._name
        stackname = "stack_" + reg_ + "_" + histag
        canvasname = "stack_" + reg_ + "_" + histag + "_" + lep_ + "_" + year
    else:
        histoname = "h_" + histag + "_" + cut_tag_ #variabile_._name +
        stackname = "stack_" + reg_ + "_" + histag + "_" + cut_tag_
        canvasname = "stack_" + reg_ + "_" + histag+ "_" + cut_tag_ + "_" + lep_ + "_" + year
    if opt.wfake != 'nofake':
        stackname += "_wFakes"
        canvasname += "_wFakes"
    if syst_ != "":
        histoname += "_" + syst_.replace("_Up", "Up").replace("_Down", "Down")
        stackname += "_" + syst_.replace("_Up", "Up").replace("_Down", "Down")
        canvasname += "_" + syst_.replace("_Up", "Up").replace("_Down", "Down")

    if opt.sr:
        blind = True
    stack = ROOT.THStack(stackname, histag)
    leg_stack = ROOT.TLegend(0.32,0.58,0.93,0.87)
    signal = False

    for s in samples_:
        if s.label.startswith('VBS') and not ('SSWW_SM_' in s.label or 'SSWW_cHW_' in s.label or 'SSWW_cW_' in s.label or '_aQGC_' in s.label) and not str(s.year) in s.label:
            print("not passed")
            continue
        if opt.wfake != 'nofake':
            if s.label.startswith('WJets') or s.label.startswith('QCD') or s.label.startswith('TT_'):
                continue
            elif 'Fake' in s.label:
                if opt.wfake.startswith('incl') and not (s.label.startswith('FakeEle_') or s.label.startswith('FakeMu_') or s.label.startswith('FakeEleMu_')):
                    continue
                elif opt.wfake.startswith('sep') and (s.label.startswith('FakeEle_') or s.label.startswith('FakeMu_')):
                    continue
        else:
            if s.label.startswith('Fake'):
                continue
        if('WpWpJJ_EWK' in s.label or 'VBS_SSWW' in s.label) and not opt.signal:
            signal = True
            #print(s.label)
        
        infile[s.label] = ROOT.TFile.Open(pathplot + s.label + "_" + lep + ".root")

    i = 0

    #print("infile:", infile)

    for s in samples_:
        if s.label.startswith('VBS') and not ('SSWW_SM_' in s.label or 'SSWW_cHW_' in s.label or 'SSWW_cW_' in s.label or '_aQGC_' in s.label) and not str(s.year) in s.label:
            print("not passed")
            continue
        if opt.wfake != 'nofake':
            if s.label.startswith('WJets') or s.label.startswith('QCD') or s.label.startswith('TT_'):# or s.label.startswith('DY')
                continue
            elif 'Fake' in s.label:
                if opt.wfake.startswith('incl') and not (s.label.startswith('FakeEle_') or s.label.startswith('FakeMu_') or s.label.startswith('FakeEleMu_')):
                    continue
                elif opt.wfake.startswith('sep') and (s.label.startswith('FakeEle_') or s.label.startswith('FakeMu_')):
                    continue

        else:
            if s.label.startswith('Fake'):# or s.label.startswith('QCD'):
                continue
          
        infile[s.label].cd()
        print("opening file: ", infile[s.label].GetName())
        #print("isthere?", histoname, infile[s.label].Get(histoname))
        if('Data' in s.label):
            if ("GenPart" in variabile_._name) or ("MC_" in variabile_._name):
                continue
            if 'DataMET' in s.label:# or 'DataHT' in s.label:
                continue

        tmp = (ROOT.TH1F)(infile[s.label].Get(histoname))
        tmp.SetLineColor(ROOT.kBlack)
        tmp.SetName(s.leglabel)
        if('Data' in s.label):
            if ("GenPart" in variabile_._name) or ("MC_" in variabile_._name):
                continue
            hdata.Add(ROOT.TH1F(tmp.Clone("")))
            hdata.SetMarkerStyle(20)
            hdata.SetMarkerSize(0.9)
            if(i == 0 and not blind): # trick to add Data flag to legend only once
                leg_stack.AddEntry(hdata, "Data", "ep")
            i += 1
        elif('WpWpJJ_EWK' in s.label or 'VBS_SSWW' in s.label) and not opt.signal:
            #tmp.SetLineStyle(9)
            if opt.tostack:
                tmp.SetLineColor(s.color)
                tmp.SetLineWidth(2)
            else:
                tmp.SetLineColor(s.color)
                tmp.SetLineWidth(2)
            #tmp.SetLineWidth(3)
            tmp.SetMarkerSize(0.)
            tmp.SetMarkerColor(s.color)
            h_sig.append(ROOT.TH1F(tmp.Clone("")))
            tmp.SetOption("HIST SAME")
        else:
            tmp.SetOption("HIST SAME")
            tmp.SetTitle("")
            if opt.tostack:
                tmp.SetFillColor(s.color)
                tmp.SetLineColor(s.color)
            else:
                tmp.SetLineColor(s.color)
            histo.append(tmp.Clone(""))
            stack.Add(tmp.Clone(""))
        tmp.Reset("ICES")

    for hist in reversed(histo):
        if not ('Data' in hist.GetName()):
            leg_stack.AddEntry(hist, hist.GetName(), "f")
    #style options
    print("Is it blind? " + str(blind))
    leg_stack.SetNColumns(2)
    leg_stack.SetFillColor(0)
    leg_stack.SetFillStyle(0)
    leg_stack.SetTextFont(42)
    leg_stack.SetBorderSize(0)
    leg_stack.SetTextSize(0.035)
    c1 = ROOT.TCanvas(canvasname,"c1",50,50,700,600)
    c1.SetFillColor(0)
    c1.SetBorderMode(0)
    c1.SetFrameFillStyle(0)
    c1.SetFrameBorderMode(0)
    c1.SetLeftMargin( 0.12 )
    c1.SetRightMargin( 0.9 )
    c1.SetTopMargin( 1 )
    c1.SetBottomMargin(-1)
    c1.SetTickx(1)
    c1.SetTicky(1)
    c1.cd()
    
    pad1= ROOT.TPad("pad1", "pad1", 0, 0.31 , 1, 1)
    pad1.SetTopMargin(0.1)
    pad1.SetBottomMargin(0.02)
    pad1.SetLeftMargin(0.12)
    pad1.SetRightMargin(0.05)
    pad1.SetBorderMode(0)
    pad1.SetTickx(1)
    pad1.SetTicky(1)
    pad1.Draw()
    pad1.cd()
    if not blind:
        maximum = max(stack.GetMaximum(),hdata.GetMaximum())
    else:
        maximum = stack.GetMaximum()
    logscale = True # False #
    if(logscale) and stack.GetStack().Last().Integral()>0.:
        stack.SetMinimum(0.01)
        pad1.SetLogy()
        stack.SetMaximum(maximum*10000)
    else:
        stack.SetMaximum(maximum*1.6)

    if opt.tostack:
        stack.Draw("HIST")
    else:
        stack.Draw("HIST NOSTACK")
    if not variabile_._iscustom:
        step = float(variabile_._xmax - variabile_._xmin)/float(variabile_._nbins)
        #print(str(step))
        if "GeV" in variabile_._title:
            if step.is_integer():
                ytitle = "Events/ %.0f GeV" %step
            else:
                ytitle = "Events / %.2f GeV" %step
        else:
            if step.is_integer():
                ytitle = "Events / %.0f units" %step
            else:
                ytitle = "Events / %.2f units" %step
    else:
        if "GeV" in variabile_._title:
            ytitle = "Events / GeV"
        else:
            ytitle = "Events / a.u"
     
    print(stack)
    stack.GetYaxis().SetTitle(ytitle)
    stack.GetYaxis().SetTitleFont(42)
    stack.GetXaxis().SetLabelOffset(1.8)
    stack.GetYaxis().SetTitleOffset(0.85)
    stack.GetXaxis().SetLabelSize(0.15)
    stack.GetYaxis().SetLabelSize(0.07)
    stack.GetYaxis().SetTitleSize(0.07)
    stack.SetTitle("")
    if(signal):
        for hsig in h_sig:
            #hsig.Scale(1000)
            hsig.Draw("hist same")
            leg_stack.AddEntry(hsig, hsig.GetName(), "l")
    h_err = stack.GetStack().Last().Clone("h_err")
    h_err.SetLineWidth(100)
    h_err.SetFillStyle(3154)
    h_err.SetMarkerSize(0)
    h_err.SetFillColor(ROOT.kGray+2)
    h_err.Draw("e2same0")
    leg_stack.AddEntry(h_err, "Stat. Unc.", "f")

    if not blind: 
        print(hdata.Integral())
        hdata.Draw("eSAMEpx0")
    else:
        hdata = stack.GetStack().Last().Clone("h_data")
    leg_stack.Draw("same")

    CMS_lumi.writeExtraText = 1
    CMS_lumi.extraText = ""
         
    print("lep_tag: ", lep_tag)
    lumi_sqrtS = "%s fb^{-1}  (13 TeV)"%(lumi)
    
    iPeriod = 0
    iPos = 11
    CMS_lumi(pad1, lumi_sqrtS, iPos, str(cmsreg))
    hratio = stack.GetStack().Last()
     
    c1.cd()
    pad2= ROOT.TPad("pad2", "pad2", 0, 0.01 , 1, 0.30)
    pad2.SetTopMargin(0.05)
    pad2.SetBottomMargin(0.45)
    pad2.SetLeftMargin(0.12)
    pad2.SetRightMargin(0.05)
    ROOT.gStyle.SetHatchesSpacing(2)
    ROOT.gStyle.SetHatchesLineWidth(2)
    c1.cd()
    pad2.Draw()
    pad2.cd()
    ratio = hdata.Clone("ratio")
    ratio.SetLineColor(ROOT.kBlack)
    ratio.SetMaximum(10)
    ratio.SetMinimum(0)
    ratio.Sumw2()
    ratio.SetStats(0)
    
    ratio.Divide(hratio)
    ratio.SetMarkerStyle(20)
    ratio.SetMarkerSize(0.9)
    ratio.Draw("epx0e0")
    ratio.SetTitle("")
    
    h_bkg_err = hratio.Clone("h_err")
    h_bkg_err.Reset()
    h_bkg_err.Sumw2()
    for i in range(1,hratio.GetNbinsX()+1):
        h_bkg_err.SetBinContent(i,1)
        if(hratio.GetBinContent(i)):
            h_bkg_err.SetBinError(i, (hratio.GetBinError(i)/hratio.GetBinContent(i)))
        else:
            h_bkg_err.SetBinError(i, 10^(-99))
    h_bkg_err.SetLineWidth(100)
    
    h_bkg_err.SetMarkerSize(0)
    h_bkg_err.SetFillColor(ROOT.kGray+1)
    #if not opt.tostack:
    h_bkg_err.Draw("e20same")
     
    if not variabile_._iscustom:
        xmin = variabile_._xmin
    else:
        xmin = variabile_._xmin[0]
    f1 = ROOT.TLine(xmin, 1., variabile_._xmax,1.)
    f1.SetLineColor(ROOT.kBlack)
    f1.SetLineStyle(ROOT.kDashed)
    f1.Draw("same")
     
    ratio.GetYaxis().SetTitle("Data / Bkg")
    ratio.GetYaxis().SetNdivisions(503)
    ratio.GetXaxis().SetLabelFont(42)
    ratio.GetYaxis().SetLabelFont(42)
    ratio.GetXaxis().SetTitleFont(42)
    ratio.GetYaxis().SetTitleFont(42)
    ratio.GetXaxis().SetTitleOffset(1.1)
    ratio.GetYaxis().SetTitleOffset(0.35)
    ratio.GetXaxis().SetLabelSize(0.15)
    ratio.GetYaxis().SetLabelSize(0.15)
    ratio.GetXaxis().SetTitleSize(0.16)
    ratio.GetYaxis().SetTitleSize(0.16)
    if "fakes_" in cut_tag_ or "SR" in cut_tag_:
        ratio.GetYaxis().SetRangeUser(0.5, 1.5)
    elif "ttbar_" in cut_tag_:
        ratio.GetYaxis().SetRangeUser(0.5, 1.5)
    elif "OS_" in cut_tag_:
        ratio.GetYaxis().SetRangeUser(0.5, 1.5)
    else:
        ratio.GetYaxis().SetRangeUser(0.5, 1.5)
    ratio.GetXaxis().SetTitle(variabile_._title)
    ratio.GetXaxis().SetLabelOffset(0.04)
    ratio.GetYaxis().SetLabelOffset(0.02)
    ratio.Draw("epx0e0same")

    c1.cd()
    #ROOT.TGaxis.SetMaxDigits(3)
    c1.RedrawAxis()
    pad2.RedrawAxis()
    c1.Update()
    #c1.Print("stack/"+canvasname+".pdf")
    pathstack_tmp = pathstack + str(year) + "/"
    c1.Print(pathstack_tmp + canvasname + ".png")
    del histo
    tmp.Delete()
    h.Delete()
    del tmp
    del h
    del h_sig
    h_err.Delete()
    del h_err
    h_bkg_err.Delete()
    del h_bkg_err
    hratio.Delete()
    del hratio
    stack.Delete()
    del stack
    pad1.Delete()
    del pad1
    pad2.Delete()
    del pad2
    c1.Delete()
    del c1
    for kf in infile.keys():
        #infile[s.label].Close()
        infile[kf].Close()
        #infile[s.label].Delete()
        infile[kf].Delete()
    #os.system('set LD_PRELOAD=libtcmalloc.so')

leptons = opt.lep.split(',')

#dataset_dict = {'2016':[],'2017':[],'2018':[]}
if not "UL" in opt.year:
    dataset_dict = {'2017':[],'2018':[]}
else:
    dataset_dict = {'UL2016APV':[], 'UL2016': [], 'UL2016M':[], 'UL2017':[], 'UL2018':[], "ULRunII":[]}
#print(class_list)

if opt.stack:
    class_list = stack_list
else:# opt.plot:
    class_list = plot_list
#else:
    #class_list = merge_list

#print(class_list)

if(opt.dat != 'all'):
     #print("opt.dat", opt.dat)
     #print(opt.dat)
     if 'DataMET' in str(opt.dat):
          raise Exception("Not interesting dataset")
     elif not opt.folder.startswith('CTHT') and 'DataHT' in str(opt.dat) and (opt.plot or opt.stack):
          raise Exception("Not interesting dataset")
     dataset_names = opt.dat.strip('[]').split(',')
     #print("dataset_names", dataset_names)
     for dat in dataset_names:
          if not(dat in sample_dict.keys()):
              raise Exception("dataset not found!")
              #print(sample_dict.keys())
        
     samples = []
     [samples.append(sample_dict[dataset_name]) for dataset_name in dataset_names]
     [dataset_dict[str(sample.year)].append(sample) for sample in samples]


else:
     for v in class_list:

          if opt.signal and not ('WpWpJJ_EWK' in v.label or 'VBS_SSWW' in v.label):
               continue
          if opt.channel == 'ltau' and 'EleMu_' in v.label:
               continue

          #elif opt.channel == 'emu' and 'Fake' in v.label and not 'EleMu_' in v.label:
               #continue
          if 'DataMET' in v.label:
               continue
          elif ('DataHT' in v.label and not opt.folder.startswith('CTHT')):
               continue
          elif (opt.folder.startswith('CTHT') and ('DataEle' in v.label or 'DataMu' in v.label or 'QCD' in v.label)):
               continue

          if 'electron' in leptons:
               if 'DataMu' in v.label or 'FakeMu' in v.label or 'PromptMu' in v.label or 'DataEleMu' in v.label or 'FakeEleMu' in v.label:
                    continue
          elif 'muon' in leptons:
               if 'DataEle' in v.label or 'FakeEle' in v.label or 'PromptEle' in v.label or 'DataEleMu' in v.label or 'FakeEleMu' in v.label:
                    continue
          elif 'incl' in leptons:
               if 'DataEle_' in v.label or 'FakeEleP' in v.label or 'FakeEleF' in v.label or 'FakeEle_' in v.label or 'PromptEle' in v.label or 'DataMu' in v.label or 'FakeMu' in v.label or 'PromptMu' in v.label:
                   continue
                

          dataset_dict[str(v.year)].append(v)

#print("dataset_dict", dataset_dict)

years = []
if(opt.year!='all'):
     years = opt.year.strip('[]').split(',')
else:
     years = ['UL2016APV','UL2016', "UL2016M", 'UL2017','UL2018', 'ULRunII']

for year in years:
    #if year == "UL2016M":
        #continue
    for sample in dataset_dict[year]:
        if opt.merpart:
            print("\n")
            mergepart(sample)
        if opt.lumi:
            lumi_writer(sample, lumi[year])
        if opt.mertree:
            mergetree(sample)

print("\nStarting")
for year in years:
    if not os.path.exists(pathstack + str(year) + "/") and cut_tag != "1p":
        os.system("mkdir -p " + pathstack + str(year) + "/")
    print(year)
    for lep in leptons:
        print(lep)
        dataset_new = dataset_dict[year]

        #dataset_new.remove(sample_dict['DataMET_'+str(year)])
        if lep == 'muon' and sample_dict['DataEle_'+str(year)] in dataset_new:
            dataset_new.remove(sample_dict['DataEle_'+str(year)])
            dataset_new.remove(sample_dict['FakeEle_'+str(year)])
        elif lep == 'electron' and sample_dict['DataMu_'+str(year)] in dataset_new:
            dataset_new.remove(sample_dict['DataMu_'+str(year)])
            dataset_new.remove(sample_dict['FakeMu_'+str(year)])

        variables = []
        
        lep1 = ["", ""]
        lep2 = ["", ""]
        lep12 = ["", ""]
        
        if opt.channel == "ltau":
            lep1 = ["lepton", "lepton"]
            lep2 = ["tau", "#tau"]
            lep12 = ["taulep", "#tau l"]
        
        elif opt.channel == "emu":
            lep1 = ["electron", "e"]
            lep2 = ["muon", "#mu"]
            lep12 = ["electronmuon", "e #mu"]
              
        wzero = ""
        if opt.channel == 'ltau':
            wzero = 'w_nominal*QCDScaleSF*PFSF*puSF*lepSF*tau_vsjet_SF*tau_vsele_SF*tau_vsmu_SF*btagSF*puIDSF*VBSSF'
        elif opt.channel == 'emu':
            wzero = 'w_nominal*PFSF*puSF*lepSF*btagSF*puIDSF*QCDScaleSF'
        #print("wzero", wzero)

        cutbase = cut_dict[lep]


        ######### with systematics ###########
        
        variables.append(variabile('countings', 'countings', wzero+'*('+cutbase+')', True, 1, -0.5, 0.5))
        
        #bin_bdtsm = array("d", [0., 0.1, 0.2, 0.4, 0.6, 1.])
        bin_bdtsm = array("d", [0., 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.])
        nbin_bdtsm = len(bin_bdtsm) - 1

        bin_bdtsm_dev = array("d", [0., 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.])
        nbin_bdtsm_dev = len(bin_bdtsm_dev) - 1
        
        '''
        variables.append(variabile('BDT_SM_UL035_novar_sr_allbkg', 'SM BDT output (novar SR allbkg)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('BDT_SM_UL035_novar_truesr_allbkg', 'SM BDT output (novar true SR allbkg)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))        
        variables.append(variabile('DNN_SM_UL035_novar_sr_allbkg', 'SM DNN output (novar SR allbkg)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_SM_UL035_novar_truesr_allbkg', 'SM DNN output (novar true SR allbkg)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))        
        
        variables.append(variabile('DNN_SM_UL035_novar_truesr_allbkg_nomet_256bs', 'SM DNN output (novar SR allbkg nomet 256bs)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_SM_UL035_novar_truesr_allbkg_nomet', 'SM DNN output (novar SR allbkg nomet)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_SM_UL035_novar_truesr_allbkg_moresteps_1', 'SM DNN output (novar trueSR allbkg moresteps)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))

        #variables.append(variabile('DNN_SM_UL035_v2', 'SM DNN output', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_SM_UL035_novar', 'SM DNN output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_SM_UL035_novar_sr', 'SM DNN output (novar SR)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        #variables.append(variabile('DNN_SM_UL035_T_DYL', 'SM DNN output (T DY_L)', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        #variables.append(variabile('DNN_cW_UL035_v2', 'c_{W} DNN output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('DNN_cW_UL035_novar', 'c_{W} DNN output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        #variables.append(variabile('DNN_cHW_UL035_v2', 'c_{HW} DNN output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('DNN_cHW_UL035_novar', 'c_{HW} DNN output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))

        #variables.append(variabile('DNN_aQGC_UL035_v2', 'aQGC DNN output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('DNN_aQGC_UL035_novar', 'aQGC DNN output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_FS_UL035_novar', 'f_{S} DNN output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_FM_UL035_novar', 'f_{M} DNN output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_FT_UL035_novar', 'f_{T} DNN output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_FS_UL035_novar_fix', 'f_{S} DNN output (novar fix)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_FM_UL035_novar_fix', 'f_{M} DNN output (novar fix)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        variables.append(variabile('DNN_FT_UL035_novar_fix', 'f_{T} DNN output (novar fix)', wzero+'*('+cutbase+')', True, nbin_bdtsm_dev, bin_bdtsm_dev))
        '''
        #variables.append(variabile('DNN_pol_UL030', 'LL vs TX VBS DNN output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        '''
        variables.append(variabile('BDT_SM_UL035_v2', 'SM BDT output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_SM_UL035_novar', 'SM BDT output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_SM_UL035_novar_SR', 'SM BDT output (novar SR)', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_SM_UL035_T_DYL', 'SM BDT output (T DY_L)', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_cW_UL035_v2', 'c_{W} BDT output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_cW_UL035_novar', 'c_{W} BDT output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_cHW_UL035_v2', 'c_{HW} BDT output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_cHW_UL035_novar', 'c_{HW} BDT output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_aQGC_UL035_v2', 'aQGC BDT output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        variables.append(variabile('BDT_aQGC_UL035_novar', 'aQGC BDT output (novar)', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        '''
        #variables.append(variabile('BDT_pol_UL030', 'LL vs TX VBS BDT output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
        #variables.append(variabile('DNN_pol_UL030', 'LL vs TX VBS DNN output', wzero+'*('+cutbase+')', True, nbin_bdtsm, bin_bdtsm))
       
        bin_m1T = array("d", [0., 100., 150., 200., 300., 400., 500.])#, 1000.])
        #if not opt.sr:
        #bin_mo1 = array("d", [0., 50., 100., 150., 200., 300., 500.])#, 1000.])
        bin_mo1 = array("d", [0., 100., 150., 200., 300., 500.])#, 1000.])
        #else:
            #bin_mo1 = array("d", [0., 100., 150., 200., 300.])
        nbin_m1T = len(bin_m1T) - 1 
        nbin_mo1 = len(bin_mo1) - 1 
        variables.append(variabile('m_1T', 'M_{1T} [GeV]',  wzero+'*('+cutbase+')', True, nbin_m1T, bin_m1T))
        variables.append(variabile('m_o1', 'M_{o1} [GeV]',  wzero+'*('+cutbase+')', True, nbin_mo1, bin_mo1))
        
        if opt.sr:
            bin_mjj = array("d", [500., 600., 800., 1000., 1200., 1400., 1600., 1800., 2000., 2200., 2400., 2600., 2800.])
        else:
            bin_mjj = array("d", [0., 200., 400., 600., 800., 1000., 1200., 1400., 1600., 1800., 2000., 2200., 2400., 2600.])
        nbin_mjj = len(bin_mjj) - 1 
        variables.append(variabile('m_jj', 'invariant mass j_{1} j_{2} [GeV]',  wzero+'*('+cutbase+')', True, nbin_mjj, bin_mjj))
        
        ######### without systematics ###########
        
        #try:
            #variables.append(variabile('taggerScore', 'VBS jet tagger score', wzero+'*('+cutbase+')', 10, 0., 1.))
        #except:
            #pass
        #variables.append(variabile('BDT_output_ele', 'eleBDT output', wzero+'*('+cutbase+')', 8, -2., 2.))
        #variables.append(variabile('BDT_output_mu', '#muBDT output', wzero+'*('+cutbase+')', 8, -2., 2.))
        #variables.append(variabile('lepBDT_output', 'lepBDT output', wzero+'*('+cutbase+')', 8, -2., 2.))
        
        variables.append(variabile(lep1[0] + '_eta', lep1[1] + ' #eta', wzero+'*('+cutbase+')', True, 10, -2.5, 2.5))
        variables.append(variabile(lep1[0] + '_phi', lep1[1] + ' #phi',  wzero+'*('+cutbase+')', True, 7, -3.50, 3.50))

        bin_lepton_pt = array("d", [30., 40., 50., 60., 70., 80., 100., 120., 140., 160., 200.])
        nbin_lepton_pt = len(bin_lepton_pt)-1
        variables.append(variabile(lep1[0] + '_pt',  lep1[1] + ' p_{T} [GeV]',  wzero+'*('+cutbase+')', True, nbin_lepton_pt, bin_lepton_pt))

        #variables.append(variabile(lep1[0] + '_pdgid', lep1[1] + ' pdgid',  wzero+'*('+cutbase+')', False, 31, -15.5, 15.5))
        #variables.append(variabile(lep1[0] + '_pfRelIso04', lep1[1] + ' pfRelIso04',  wzero+'*('+cutbase+')', False, 15, 0, 0.15))
        
        if opt.wjets or opt.qcd or opt.fakes or opt.dy or opt.sr:
            bin_zepp = array("d", [-1., -0.7, -0.4, -0.2, 0., 0.2, 0.4, 0.7, 1.])
            nbin_zepp = len(bin_zepp)-1
        else:
            bin_zepp = array("d", [-1., -0.7, -0.4, -0.2, 0., 0.2, 0.4, 0.7, 1.])
            nbin_zepp = len(bin_zepp)-1
        variables.append(variabile('event_Zeppenfeld_over_deltaEta_jj', 'event Zeppenfeld',  wzero+'*('+cutbase+')', True, nbin_zepp, bin_zepp))
        #variables.append(variabile(lep1[0] + '_Zeppenfeld_over_deltaEta_jj', 'z_{l}',  wzero+'*('+cutbase+')', False, nbin_zepp, bin_zepp))
        

        if opt.wjets or opt.qcd or opt.fakes or opt.dy or opt.sr:
            bin_taupt = array("d", [30., 45., 60., 80., 100., 150.])
        else:
            bin_taupt = array("d", [30., 45., 60., 80., 100., 125., 150, 175., 200.])
        nbin_taupt = len(bin_taupt) - 1
        variables.append(variabile(lep2[0] + '_pt',  lep2[1] + ' p_{T} [GeV]',  wzero+'*('+cutbase+')', True, nbin_taupt, bin_taupt))
        
        bin_taum = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0])
        nbin_taum = len(bin_taum) - 1
        variables.append(variabile(lep2[0] + '_mass',  lep2[1] + ' mass [GeV]',  wzero+'*('+cutbase+')', True, nbin_taum, bin_taum))
        
        variables.append(variabile(lep2[0] + '_eta', lep2[1] + ' #eta',  wzero+'*('+cutbase+')', True, 10, -2.5, 2.5))
        #variables.append(variabile(lep2[0] + '_Zeppenfeld', lep2[1] + ' Zeppenfeld',  wzero+'*('+cutbase+')', False, 20, -5, 5))
        #variables.append(variabile(lep2[0] + '_Zeppenfeld_over_deltaEta_jj', 'z_{#tau}',  wzero+'*('+cutbase+')', False, 12, -1.5, 1.5))
        variables.append(variabile('tau_DecayMode', '#tau Decay Mode',  wzero+'*('+cutbase+')', True, 12, -0.5, 11.5))
        variables.append(variabile(lep2[0] + '_phi', lep2[1] + ' #Phi',  wzero+'*('+cutbase+')', True,  7, -3.50, 3.50))

        if opt.channel == "ltau":
            #variables.append(variabile(lep2[0] + '_DecayMode', '#tau decay mode',  wzero+'*('+cutbase+')', False, 12, -0.5, 11.5))
            
            variables.append(variabile('tauleadTk_ptOverTau',  '#tau LeadTk relative p_{T}',  wzero+'*('+cutbase+')', True, 10, 0, 1))
            #variables.append(variabile('tauleadTk_deltaPhi',  '#tau LeadTk relative #Delta#phi',  wzero+'*('+cutbase+')', False, 8, -0.1, 0.1))
            #variables.append(variabile('tauleadTk_deltaEta',  '#tau LeadTk relative #Delta#eta',  wzero+'*('+cutbase+')', False, 8, -0.1, 0.1))
            variables.append(variabile('tauleadTk_Gamma',  '#tau LeadTk #Upsilon',  wzero+'*('+cutbase+')', True, 10, -1., 1.))
            
            #bin_taujetrelpt = array("d", [0.85, 0.9, 0.92, 0.94, 0.96, 0.98, 1.])
            #nbin_taujetrelpt = len(bin_taujetrelpt) - 1
            #variables.append(variabile('taujet_relpt',  '#tau jet relative p_{T}',  wzero+'*('+cutbase+')', False, nbin_taujetrelpt, bin_taujetrelpt))
            #variables.append(variabile('taujet_deltaPhi',  '#tau jet relative #Delta#phi',  wzero+'*('+cutbase+')', False, 5, -0.25, 0.24))
            #variables.append(variabile('taujet_deltaEta',  '#tau jet relative #Delta#eta',  wzero+'*('+cutbase+')', False, 5, -0.25, 0.25))
            #if opt.wjets or opt.qcd or opt.fakes or opt.dy or opt.sr:
                #bin_taujetrelpt = array("d", [-1., -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.])
            #else:
                #bin_taujetrelpt = array("d", [-1., -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.])
            #nbin_taujetrelpt = len(bin_taujetrelpt) - 1

            #bin_taujethg = array("d", [-1., -0.4, -0.2, 0., 0.2, 0.4, 0.6, 0.8, 1.])
            #nbin_taujethg = len(bin_taujethg) - 1
            #variables.append(variabile('taujet_HadGamma',  '#tau jet had. #Upsilon',  wzero+'*('+cutbase+')', False, nbin_taujethg, bin_taujethg))
            #variables.append(variabile('taujet_EmGamma',  '#tau jet em. #Upsilon',  wzero+'*('+cutbase+')', False, 8, -1., 1.))

            #variables.append(variabile('taujet_HEGamma',  '#tau jet had.+em. #Upsilon',  wzero+'*('+cutbase+')', False, 8, -1., 1.))

            variables.append(variabile('tau_DeepTauVsEle_raw', '#tau DeepTauVsEle raw',  wzero+'*('+cutbase+')', True, 7, 0.3, 1.))
            variables.append(variabile('tau_DeepTauVsMu_raw', '#tau DeepTauVsMu raw',  wzero+'*('+cutbase+')', True, 7, 0.3, 1.))
            #variables.append(variabile('tau_DeepTauVsJet_raw', '#tau DeepTauVsJet raw',  wzero+'*('+cutbase+')', False,  10, 0., 1.))

            #variables.append(variabile('tau_DeepTauVsEle_WP', '#tau DeepTauVsEle WP',  wzero+'*('+cutbase+')', False,  11, -0.5, 10.5))
            #variables.append(variabile('tau_DeepTauVsMu_WP', '#tau DeepTauVsMu WP',  wzero+'*('+cutbase+')', False,  11, -0.5, 10.5))
            #variables.append(variabile('tau_DeepTauVsJet_WP', '#tau DeepTauVsJet WP',  wzero+'*('+cutbase+')', False,  11, -0.5, 10.5))

        bin_leadjet_pt = array("d", [0., 50., 100., 150., 250., 400.])
        nbin_leadjet_pt = len(bin_leadjet_pt)-1
        variables.append(variabile('leadjet_pt',  'Lead jet p_{T} [GeV]',  wzero+'*('+cutbase+')', True, nbin_leadjet_pt, bin_leadjet_pt))
        variables.append(variabile('leadjet_eta', 'Lead jet #eta',  wzero+'*('+cutbase+')', True, 16, -4., 4.))
        variables.append(variabile('leadjet_phi', 'Lead jet #Phi',  wzero+'*('+cutbase+')', True,  7, -3.50, 3.50))

        variables.append(variabile('leadjet_qgl', 'Lead jet QGL',  wzero+'*('+cutbase+')', False,  8, 0., 1.))
        variables.append(variabile('subleadjet_qgl', 'Sublead jet QGL',  wzero+'*('+cutbase+')', False,  8, 0., 1.))

        bin_leadjet_mass = array("d", [0., 10., 20., 30., 50.])
        nbin_leadjet_mass = len(bin_leadjet_mass)-1
        variables.append(variabile('leadjet_mass',  'Lead jet mass [GeV]',  wzero+'*('+cutbase+')', True, nbin_leadjet_mass, bin_leadjet_mass))
        #bin_ak8leadjet_pt = array("d", [0., 100., 200., 300., 400., 500., 600., 800., 1200.])
        #nbin_ak8leadjet_pt = len(bin_ak8leadjet_pt)-1
        #variables.append(variabile('AK8leadjet_pt',  'AK8 Lead jet p_{T} [GeV]',  wzero+'*('+cutbase+')', False, nbin_ak8leadjet_pt, bin_ak8leadjet_pt))#30, 1500))
        
        #bin_ak8leadjet_mass = array("d", [0., 50., 100., 150., 300.])
        #nbin_ak8leadjet_mass = len(bin_ak8leadjet_mass)-1
        #variables.append(variabile('AK8leadjet_mass',  'AK8 Lead jet mass [GeV]',  wzero+'*('+cutbase+')', False, nbin_ak8leadjet_mass, bin_ak8leadjet_mass))#30, 1500))
        
        #variables.append(variabile('AK8leadjet_eta', 'AK8 Lead jet #eta',  wzero+'*('+cutbase+')', False, 20, -5., 5.))
        #variables.append(variabile('AK8leadjet_phi', 'AK8 Lead jet #Phi',  wzero+'*('+cutbase+')', False,  14, -3.50, 3.50))
        #variables.append(variabile('AK8leadjet_tau21', 'AK8 Lead jet #tau_{21}',  wzero+'*('+cutbase+')', False,  10, 0., 1.))
        #variables.append(variabile('AK8leadjet_tau32', 'AK8 Lead jet #tau_{32}',  wzero+'*('+cutbase+')', False,  10, 0., 1.))
        #variables.append(variabile('AK8leadjet_tau43', 'AK8 Lead jet #tau_{43}',  wzero+'*('+cutbase+')', False,  10, 0., 1.))
        
        #bin_ak8subleadjet_pt = array("d", [0., 100., 200., 300., 400., 500., 600., 800., 1200.])
        #nbin_ak8subleadjet_pt = len(bin_ak8subleadjet_pt)-1
        #variables.append(variabile('AK8subleadjet_pt',  'AK8 Sublead jet p_{T} [GeV]',  wzero+'*('+cutbase+')', False, nbin_ak8subleadjet_pt, bin_ak8subleadjet_pt))#30, 1500))
        
        #bin_ak8subleadjet_mass = array("d", [0., 50., 100., 150., 300.])#, 500., 600., 700., 800., 1000., 1200., 1400., 1600., 2000.])
        #nbin_ak8subleadjet_mass = len(bin_ak8subleadjet_mass)-1
        #variables.append(variabile('AK8subleadjet_mass',  'AK8 Sublead jet mass [GeV]',  wzero+'*('+cutbase+')', False, nbin_ak8subleadjet_mass, bin_ak8subleadjet_mass))#30, 1500))
        
        #variables.append(variabile('AK8subleadjet_eta', 'AK8 Sublead jet #eta',  wzero+'*('+cutbase+')', False, 20, -5., 5.))
        #variables.append(variabile('AK8subleadjet_phi', 'AK8 Sublead jet #Phi',  wzero+'*('+cutbase+')', False,  14, -3.50, 3.50))
        #variables.append(variabile('AK8subleadjet_tau21', 'AK8 Sublead jet #tau_{21}',  wzero+'*('+cutbase+')', False,  10, 0., 1.))
        #variables.append(variabile('AK8subleadjet_tau32', 'AK8 Sublead jet #tau_{32}',  wzero+'*('+cutbase+')', False,  10, 0., 1.))
        #variables.append(variabile('AK8subleadjet_tau43', 'AK8 Sublead jet #tau_{43}',  wzero+'*('+cutbase+')', False,  10, 0., 1.))

        if opt.wjets or opt.qcd or opt.fakes or opt.dy or opt.sr:
            bin_subleadjet_pt = array("d", [0., 50., 100., 200.])
        else:
            bin_subleadjet_pt = array("d", [0., 50., 100., 150., 250.])
        nbin_subleadjet_pt = len(bin_subleadjet_pt) - 1
        variables.append(variabile('subleadjet_pt', 'Sublead jet p_{T} [GeV]',  wzero+'*('+cutbase+')', True, nbin_subleadjet_pt, bin_subleadjet_pt))
        variables.append(variabile('subleadjet_eta', 'Sublead jet #eta',  wzero+'*('+cutbase+')', True, 16, -4., 4.))
        variables.append(variabile('subleadjet_phi', 'Sublead jet #Phi',  wzero+'*('+cutbase+')', True,  7, -3.50, 3.50))
        
        bin_subleadjet_mass = array("d", [0., 5., 10., 15., 25.])
        nbin_subleadjet_mass = len(bin_subleadjet_mass)-1
        variables.append(variabile('subleadjet_mass',  'Sublead jet mass [GeV]',  wzero+'*('+cutbase+')', True, nbin_subleadjet_mass, bin_subleadjet_mass))
        
        variables.append(variabile('nJets', 'n jets',  wzero+'*('+cutbase+')', True,  11, -0.5, 10.5))
        variables.append(variabile('nBJets', 'n bjets (DeepJet M)',  wzero+'*('+cutbase+')', True,  6, -0.5, 5.5))

        if opt.sr:
            bin_metpt = array("d", [50., 100., 150., 200., 300.])
        elif opt.wjets or opt.qcd or opt.fakes or opt.dy:
            bin_metpt = array("d", [0., 10., 15., 20., 25., 30., 35., 40., 45., 50.])
        elif opt.ttbar:
            bin_metpt = array("d", [50., 75., 100., 125., 150., 175., 200., 225., 250., 275., 300., 325., 350.,400.,450.,500.])
        else:
            bin_metpt = array("d", [0., 25., 50., 75., 100., 125., 150., 175., 200., 225., 250., 275., 300.])
        nbin_metpt = len(bin_metpt) - 1
        variables.append(variabile('MET_pt', 'p_{T}^{miss} [GeV]',  wzero+'*('+cutbase+')', True, nbin_metpt, bin_metpt))

        if opt.sr:
            bin_invm = array("d", [600., 800., 1000., 1200., 1400., 1600., 1800., 2000., 2200., 2400.])
        elif opt.fakes or opt.wsdy:
            bin_invm = array("d", [0., 200., 400., 600., 800., 1000., 1200., 1400., 1600., 1800., 2000., 2200., 2400., 2600.])
        else:
            bin_invm = array("d", [0., 200., 400., 600., 800., 1000., 1200., 1400., 1600., 1800., 2000., 2200., 2400., 2600.])
       
        nbin_invm = len(bin_invm) - 1 

        if opt.channel == 'ltau':
            variables.append(variabile('m_jj' + lep12[0], 'invariant mass j_{1} j_{2} ' + lep12[1] + ' [GeV]',  wzero+'*('+cutbase+')', True, nbin_invm, bin_invm))
        elif opt.channel == 'emu':
            variables.append(variabile('m_jjleps', 'invariant mass j_{1} j_{2} ' + lep12[1] + ' [GeV]',  wzero+'*('+cutbase+')', True, nbin_invm, bin_invm))

        variables.append(variabile('m_jj' + lep2[0], 'invariant mass j_{1} j_{2} ' + lep2[1] + ' [GeV]',  wzero+'*('+cutbase+')', True, nbin_invm, bin_invm))

        bin_invmtl = array("d", [0., 50., 100., 150., 200., 250., 300.])
        nbin_invmtl = len(bin_invmtl) - 1 
          
        variables.append(variabile('m_' + lep12[0], 'invariant mass ' + lep12[1] + ' [GeV]',  wzero+'*('+cutbase+')', True, nbin_invmtl, bin_invmtl))

        if opt.sr:
            bin_mTs = array("d", [0., 25., 50., 75., 100., 150., 200.])
            nbin_mTs = len(bin_mTs) - 1
        elif opt.fakes:
            bin_mTs = array("d", [0., 25., 50., 75., 100., 125., 150.])
            nbin_mTs = len(bin_mTs) - 1
        else:
            bin_mTs = array("d", [0., 25., 50., 75., 100., 125., 150., 200., 250.])
            nbin_mTs = len(bin_mTs) - 1

        variables.append(variabile('mT_' + lep1[0].split("to")[0] + '_MET', 'M_{T}(' + lep1[1] + ', MET) [GeV]',  wzero+'*('+cutbase+')', True, nbin_mTs, bin_mTs))
        variables.append(variabile('mT_' + lep2[0] + '_MET', 'M_{T}(' + lep2[1] + ', MET) [GeV]',  wzero+'*('+cutbase+')', True, nbin_mTs, bin_mTs))
        if opt.channel == "ltau":
            variables.append(variabile('mT_leptau_MET', 'M_{T}(l,  ' + lep2[1] + ', MET) [GeV]',  wzero+'*('+cutbase+')', True, nbin_mTs, bin_mTs))
        #elif opt.channel == "emu":
            #variables.append(variabile('mT_' + lep12[0] + '_MET', 'M_{T}(' + lep12[1] + ', MET) [GeV]',  wzero+'*('+cutbase+')', False, nbin_mTs, bin_mTs))


        bin_deltaeta_jj = array("d", [-8., -5., -3.5, -2.5, 2.5, 3.5, 5., 8.])
        nbin_deltaeta_jj = len(bin_deltaeta_jj) - 1
        variables.append(variabile('deltaEta_jj', '#Delta #eta_{jj}',  wzero+'*('+cutbase+')', True, nbin_deltaeta_jj, bin_deltaeta_jj))

        variables.append(variabile('deltaPhi_jj', '#Delta #phi_{jj}',  wzero+'*('+cutbase+')', True,  14, -3.5, 3.5))
        #variables.append(variabile('deltaPhi_' + lep12[0], '#Delta #phi_{' + lep12[1] + '}',  wzero+'*('+cutbase+')', False,  14, -3.5, 3.5))
        variables.append(variabile('deltaPhi_' + lep2[0] + 'j1', '#Delta #phi_{' + lep2[1] + ' j_{1}}',  wzero+'*('+cutbase+')', True,  14, -3.5, 3.5))
        variables.append(variabile('deltaPhi_' + lep2[0] + 'j2', '#Delta #phi_{' + lep2[1] + ' j_{2}}',  wzero+'*('+cutbase+')', True,  14, -3.5, 3.5))
        variables.append(variabile('deltaPhi_' + lep1[0].split("to")[0] + 'j1', '#Delta #phi_{' + lep1[1] + ' j_{1}}',  wzero+'*('+cutbase+')', True, 14, -3.5, 3.5))
        variables.append(variabile('deltaPhi_' + lep1[0].split("to")[0] + 'j2', '#Delta #phi_{' + lep1[1] + ' j_{2}}',  wzero+'*('+cutbase+')', True, 14, -3.5, 3.5))
        variables.append(variabile('deltaPhi_METj1', '#Delta #phi (p_{T}^{miss} j_{1})',  wzero+'*('+cutbase+')', False,  14, -3.5, 3.5))
        variables.append(variabile('deltaPhi_METj2', '#Delta #phi (p_{T}^{miss} j_{2})',  wzero+'*('+cutbase+')', False,  14, -3.5, 3.5))
        variables.append(variabile('deltaPhi_METlep', '#Delta #phi (p_{T}^{miss} lep)',  wzero+'*('+cutbase+')', False, 14, -3.5, 3.5))
        variables.append(variabile('deltaPhi_METtau', '#Delta #phi (p_{T}^{miss} #tau)',  wzero+'*('+cutbase+')', False, 14, -3.5, 3.5))
        variables.append(variabile('min(min(abs(deltaPhi_METj1),abs(deltaPhi_METj2)),min(abs(deltaPhi_METtau),abs(deltaPhi_METlep)))', 'minimum #Delta #phi (p_{T}^{miss}, vis. object)',  wzero+'*('+cutbase+')', False, 12, 0., 3))
        variables.append(variabile('max(max(abs(deltaPhi_METj1),abs(deltaPhi_METj2)),max(abs(deltaPhi_METtau),abs(deltaPhi_METlep)))', 'maximum #Delta #phi (p_{T}^{miss}, vis. object)',  wzero+'*('+cutbase+')', False, 12, 0., 3))
        
        bin_deltaeta_ll = array("d", [-5., -3., -2., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 2., 3., 5.])
        nbin_deltaeta_ll = len(bin_deltaeta_ll) - 1
        
        variables.append(variabile('deltaEta_' + lep12[0], '#Delta #eta_{' + lep12[1] + '}',  wzero+'*('+cutbase+')', True,  nbin_deltaeta_ll, bin_deltaeta_ll))

        bin_deltaeta_lj = array("d", [-6., -4., -3., -2., -1., 0., 1., 2., 3., 4., 6.])
        nbin_deltaeta_lj = len(bin_deltaeta_lj) - 1
        #variables.append(variabile('deltaEta_' + lep2[0] + 'j1', '#Delta #eta_{' + lep2[1] + ' j_{1}}',  wzero+'*('+cutbase+')', False,  nbin_deltaeta_lj, bin_deltaeta_lj))
        #variables.append(variabile('deltaEta_' + lep2[0] + 'j2', '#Delta #eta_{' + lep2[1] + ' j_{2}}',  wzero+'*('+cutbase+')', False, nbin_deltaeta_lj, bin_deltaeta_lj))
        #variables.append(variabile('deltaEta_' + lep1[0].split("to")[0] + 'j1', '#Delta #eta_{' + lep1[1] + ' j_{1}}',  wzero+'*('+cutbase+')', False, nbin_deltaeta_lj, bin_deltaeta_lj))
        #variables.append(variabile('deltaEta_' + lep1[0].split("to")[0] + 'j2', '#Delta #eta_{' + lep1[1] + ' j_{2}}',  wzero+'*('+cutbase+')', False, nbin_deltaeta_lj, bin_deltaeta_lj))


        bin_deltatheta_jj = array("d", [-1., -0.8, -0.4, 0.4, 0.8, 1.])
        nbin_deltatheta_jj = len(bin_deltatheta_jj) - 1
        #variables.append(variabile('deltaTheta_jj', 'cos(#Delta#theta_{jj})',  wzero+'*('+cutbase+')', False, nbin_deltatheta_jj, bin_deltatheta_jj))
        variables.append(variabile('deltaTheta_' + lep12[0], 'cos(#Delta#theta_{' + lep12[1] + '})',  wzero+'*('+cutbase+')', True,  nbin_deltatheta_jj, bin_deltatheta_jj))
        #variables.append(variabile('deltaTheta_' + lep2[0] + 'j1', 'cos(#Delta#theta_{' + lep2[1] + ' j_{1}})',  wzero+'*('+cutbase+')', False,  nbin_deltatheta_jj, bin_deltatheta_jj))
        #variables.append(variabile('deltaTheta_' + lep2[0] + 'j2', 'cos(#Delta#theta_{' + lep2[1] + ' j_{2}})',  wzero+'*('+cutbase+')', False,  nbin_deltatheta_jj, bin_deltatheta_jj))
        #variables.append(variabile('deltaTheta_' + lep1[0].split("to")[0] + 'j1', 'cos(#Delta#theta_{' + lep1[1] + ' j_{1}})',  wzero+'*('+cutbase+')', False, nbin_deltatheta_jj, bin_deltatheta_jj))
        #variables.append(variabile('deltaTheta_' + lep1[0].split("to")[0] + 'j2', 'cos(#Delta#theta_{' + lep1[1] + ' j_{2}})',  wzero+'*('+cutbase+')', False, nbin_deltatheta_jj, bin_deltatheta_jj))

        bin_ptRel_2 = array("d", [0., 50., 75., 100., 125, 150., 175., 200., 225., 250.])
        nbin_ptRel_2 = len(bin_ptRel_2) - 1    
        #variables.append(variabile('ptRel_jj', 'relative p_{T} j_{1} j_{2}',  wzero+'*('+cutbase+')', False, nbin_ptRel, bin_ptRel))
        #variables.append(variabile('ptRel_' + lep12[0], 'relative p_{T} ' + lep12[1],  wzero+'*('+cutbase+')', False, nbin_ptRel_2, bin_ptRel_2))
        variables.append(variabile('ptRel_' + lep2[0] + 'j1', 'relative p_{T} ' + lep2[1] + ' j_{1}',  wzero+'*('+cutbase+')', True, nbin_ptRel_2, bin_ptRel_2))
        variables.append(variabile('ptRel_' + lep2[0] + 'j2', 'relative p_{T} ' + lep2[1] + ' j_{2}',  wzero+'*('+cutbase+')', True, nbin_ptRel_2, bin_ptRel_2))
        variables.append(variabile('ptRel_' + lep1[0].split("to")[0] + 'j1', 'relative p_{T} ' + lep1[1] + ' j_{1}',  wzero+'*('+cutbase+')', True, nbin_ptRel_2, bin_ptRel_2))
        variables.append(variabile('ptRel_' + lep1[0].split("to")[0] + 'j2', 'relative p_{T} ' + lep1[1] + ' j_{2}',  wzero+'*('+cutbase+')', True, nbin_ptRel_2, bin_ptRel_2))
        
        if opt.fakes or opt.wsdy:
            bin_rt = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.4, 2.8, 3.2, 3.6, 4.4, 5.])
            nbin_rt = len(bin_rt) - 1    
        elif opt.ttbar:
            bin_rt = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.8, 3.2, 3.6, 4.4, 5.])
            nbin_rt = len(bin_rt) - 1    
        else:
            bin_rt = array("d", [0., 0.2, 0.4, 0.6, 0.8, 1.0, 1.4, 1.8, 2.4, 5.])
            nbin_rt = len(bin_rt) - 1    
        variables.append(variabile('event_RT', 'R_{T}',  wzero+'*('+cutbase+')', True, nbin_rt, bin_rt))

        if opt.fakes or opt.ttbar:
            bin_df = array("d", [0., 0.1, 0.2, 0.4, 0.6, 0.8, 0.9, 1.0])
            nbin_df = len(bin_df) - 1    
        elif opt.wsdy:
            bin_df = array("d", [0., 0.05, 0.1, 0.15, 0.2])
            nbin_df = len(bin_df) - 1    
        else:
            bin_df = array("d", [0., 0.1, 0.2, 0.4])
            nbin_df = len(bin_df) - 1    
        
        variables.append(variabile('leadjet_DeepFlv_b', 'leading jet DeepFlavour b raw',  wzero+'*('+cutbase+')', True, nbin_df, bin_df))
        variables.append(variabile('subleadjet_DeepFlv_b', 'subleading jet DeepFlavour b raw',  wzero+'*('+cutbase+')', True, nbin_df, bin_df))

        for sample in dataset_new:
            print(sample.label, sample.name)
            if ('DataHT' in sample.label or 'DataMET' in sample.label) and not opt.folder.startswith("CTHT"):# or "WJets" in sample.label:
                continue
            elif ('DataMu' in sample.label or 'DataEle' in sample.label or 'DataMET' in sample.label or 'QCD' in sample.label) and opt.folder.startswith("CTHT"):
                continue

            IsDim8 = False
            if "_aQGC_" in sample.label:
                IsDim8 = True

            if(opt.plot):
                dimsamplenames = []
                samplelabs = []
                dimcuts = []
                if IsDim8:
                    for cstr in wcoeff:
                        dimtag = cstr
                        for idt, typ in enumerate(typcontr):
                            if idt != 1:
                                idarray = str(idt + 3)
                                dimcut = dimtag + "[" + idarray + "]"
                            else:
                                dimcut = dimtag + "[3]+" + dimtag + "[4]+" + dimtag + "[5]"
                            dimcuts.append(dimcut)
                            dimsamplenames.append(sample.label.replace("aQGC", dimtag + "_" + typ))
                            samplelabs.append(sample.label.replace("aQGC", dimtag + "_" + typ))
                else:
                    dimcuts.append("")
                    dimsamplenames.append("")
                    samplelabs.append(sample.label)
                for idsl, samplelab in enumerate(samplelabs):
                    dimcut = dimcuts[idsl]
                    dimsamplename = dimsamplenames[idsl]
                    foutput = pathplot + samplelab + "_" + lep + ".root"
                    fout = ROOT.TFile.Open(foutput, "UPDATE")
                    print(samplelab)
                    f1name = ""
                    if 'Fake' in str(samplelab):
                        if sample.year == "UL2016M" or sample.year == "ULRunII":
                            f1name = filerepo + sample.label.replace("Fake", "Data") + "/"  + sample.label.replace("Fake", "Data") + ".root"
                        elif (not opt.folder.startswith('CTHT') and not opt.removePrompt):
                            #f1 = ROOT.TFile.Open(filerepo + sample.components[0].label + "/"  + sample.components[0].label + ".root")
                            f1name = filerepo + sample.components[0].label + "/"  + sample.components[0].label + ".root"
                        elif opt.removePrompt:
                            #f1 = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root")
                            f1name = filerepo + sample.label + "/"  + sample.label + ".root"
                        
                        else:
                            #f1 = ROOT.TFile.Open(filerepo + sample.components[1].label + "/"  + sample.components[1].label + ".root")
                            f1name = filerepo + sample.components[1].label + "/"  + sample.components[1].label + ".root"
                       
                    else:
                        #f1 = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root")
                        f1name = filerepo + sample.label + "/"  + sample.label + ".root"
                    
                    if os.path.exists(f1name):
                        f1 = ROOT.TFile.Open(f1name)
                    else:
                        raise ValueError(samplelab + " not ready to be plotted, skipping")
                        continue
                    
                    for ids, syst in enumerate(systematics):
                        if syst[0] != "" and ("Data" in sample.label or "Fake" in sample.label):
                            continue
                        for var in variables:
                            if syst[0] != "" and not var.IsSystApplied():
                                continue
                            if not "all" in vartoplot:
                                if not var._name in vartoplot:
                                    continue
                            if opt.count:
                                if os.path.exists(pathplot + 'countings/'):
                                    pass
                                else:
                                    os.makedirs(pathplot + 'countings/')
                                if not os.path.exists(pathplot + 'countings/' + cut_tag):
                                    os.makedirs(pathplot + 'countings/' + cut_tag)
                                if not os.path.exists(pathplot + 'countings/' + cut_tag + "/" + var._name + "_" + str(opt.year) + ".csv"):
                                    tmp_f = open(pathplot + 'countings/' + cut_tag + "/" + var._name + "_" + str(opt.year) + ".csv", "w")
                                    tmp_f.write("Process,yields,error\n")
                                    tmp_f.close()
                            if (("GenPart" in var._name) or ("MC_" in var._name)) and "Data" in sample.label:
                                continue
                            plot(f1, fout, samplelab, lep, opt.channel, var, sample, cut_tag, syst, dimsamplename, dimcut)
                    
                    fout.Close()
                    f1.Close()

        if opt.stack:
            for var in variables:
                if not "all" in vartoplot:
                    if not var._name in vartoplot:
                        continue
                            
                print("var to stack", var._name)
                os.system('set LD_PRELOAD=libtcmalloc.so')
                print("channel", opt.channel)
                makestack(lep, opt.channel, var, dataset_new, cut_tag, "", lumi[str(year)], year)
                os.system('set LD_PRELOAD=libtcmalloc.so')

        if lep == 'muon':
            dataset_new.append(sample_dict['DataEle_'+str(year)])
        elif lep == 'electron':
            dataset_new.append(sample_dict['DataMu_'+str(year)])
