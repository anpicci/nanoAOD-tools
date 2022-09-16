import os
#import commands
import sys
import optparse
import ROOT
import math
import copy
import datetime
import time
from Calculator_utils import *
from Calculator_fileManager import *
from Calculator_HistoManager import *
from Calculator_utils import *


class FakeCalculator_manager:
    def __init__(self, nev):
        self.calc = "Starting all the complex calculations"
        self.nev    = nev

    def Calc(self, sample, isData, onlybkg, met_cut, mt_lepMET_cut, trig, hEle, hMu, hTau):

        start  = datetime.datetime.now()
        print ('workin on sample: ', sample)
        print ('is data?        : ', isData)
        print ('workin on events: ', self.nev)

        if not os.path.isfile(sample):
            print('Sample: ', sample, ' does not exists')
            return False
        
        f = ROOT.TFile.Open(sample, "READ")
        if (f.IsZombie()):
            print("Zombie file: ", sample, " skipping")
            return False
        f.Close()
        
        chain = ROOT.TChain('events_all')
        chain.Add(sample)
        tree = InputTree(chain)
        isMC = not isData

        if isData and onlybkg:
            print ('the sample: ', sample, 'is tagged as data sample, while you are running in only bkg mode, jumping the sample')
        '''
        cut_ele_l = "abs(FakeLepton_pdgid)==11&&nLeps_LightLeptons>0&&nLeps_LightLeptons<=2&&abs(FakeLepton_eta)<2.4&&(abs(FakeLepton_eta)<1.4442||abs(FakeLepton_eta)>1.566)&&FakeLepton_pt>=0&&FakeLepton_pfRelIso04>=0"#&&Jet_numberSeparateLep>0
        cut_ele_t = "FakeLepton_pfRelIso04<0.08&&FakeLepton_isTight"
        cut_mu_l =  "abs(FakeLepton_pdgid)==13&&nLeps_LightLeptons>0&&nLeps_LightLeptons<=2&&abs(FakeLepton_eta)<2.4&&FakeLepton_pt>=0&&FakeLepton_pfRelIso04>=0"#&&Jet_numberSeparateLep>0
        cut_mu_t = "FakeLepton_pfRelIso04<0.15&&FakeLepton_isTight"
        cut_tau_l = "FakeTau_pt>=0&&abs(FakeTau_eta)<=2.4&&Veto_TauLeptons!=1"
        cut_tau_t = "FakeTau_DeepTauWP>=64"
        region = "(MET_pt>=0.&&MET_pt<=" + str(met_cut) + ")&&(mT_lepMET>=0.&&mT_lepMET<="+ str(mt_lepMET_cut) + ")"
        '''
        cut_ele_l = "abs(FakeLepton_pdgid)==11&&nLeps_LightLeptons>0&&nLeps_LightLeptons<=2&&abs(FakeLepton_eta)<2.4&&(abs(FakeLepton_eta)<1.4442||abs(FakeLepton_eta)>1.566)&&FakeLepton_pt>=0&&FakeLepton_pfRelIso04>=0"#&&Jet_numberSeparate>0"
        cut_ele_t = "FakeLepton_pfRelIso04<0.08&&FakeLepton_isTight"
        cut_mu_l =  "abs(FakeLepton_pdgid)==13&&nLeps_LightLeptons>0&&nLeps_LightLeptons<=2&&abs(FakeLepton_eta)<2.4&&FakeLepton_pt>=0&&FakeLepton_pfRelIso04>=0"#&&Jet_numberSeparate>0"
        cut_mu_t = "FakeLepton_pfRelIso04<0.15&&FakeLepton_isTight"
        cut_tau_l = "FakeTau_pt>=0&&abs(FakeTau_eta)<=2.4"#&&Veto_TauLeptons!=1"
        cut_tau_t = "FakeTau_DeepTauWP>=64"
        region = "(MET_pt>=0.&&MET_pt<=" + str(met_cut) + ")&&(mT_lepMET>=0.&&mT_lepMET<="+ str(mt_lepMET_cut) + ")"
                
        hEle.ProjectTree(tree, isData, cut_ele_l, cut_ele_t, region)
        hMu.ProjectTree(tree, isData, cut_mu_l, cut_mu_t, region)
        hTau.ProjectTree(tree, isData, cut_tau_l, cut_tau_t, region)

        return True
                    
