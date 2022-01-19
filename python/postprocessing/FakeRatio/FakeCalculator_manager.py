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
from EfficiencyHisto_manager import *
from FakeRatio_calculator_utils import *


class FakeCalculator_manager:
    def __init__(self, nev):
        self.calc = "Starting all the complex calculations"
        self.nev    = nev

    def Calc(self, sample, isData, onlybkg, met_cut, mt_lepMET_cut, trig, hEle, hMu, hTau):
        print ('workin on sample: ', sample)
        print ('is data?        : ', isData)
        print ('workin on events: ', self.nev)

        chain = ROOT.TChain('events_all')
        chain.Add(sample)
        tree = InputTree(chain)
        isMC = not isData

        if isData and onlybkg:
            print ('the sample: ', sample, 'is tagged as data sample, while you are running in only bkg mode, jumping the sample')
        
        sign = 1    
        if isMC and not onlybkg: sign = -1

        maxEvents = self.nev
        if maxEvents == 'all' or maxEvents>tree.GetEntries():
            maxEvents = tree.GetEntries()
    
        perc = 0
        for i in range(maxEvents):
                
            if i*1.0/maxEvents*100 > perc: 
                print ('Processing at: ', perc, '%', end = '\r')
                perc +=1
            event       = Event(tree, i)
            FakeLepton  = Object(event, "FakeLepton")
            FakeTau     = Object(event, "FakeTau")
            met         = Object(event, "MET")
            mT          = Object(event, "mT")
            w           = Object(event, "w")
            nleps       = Object(event, "nLeps")
            jets        = Object(event, "Jet")
            veto        = Object(event, "Veto")

            SF = 1
            if isMC:
                SF = sign*w.nominal*event.PFSF*event.puSF*event.lepSF*event.tau_vsjet_SF*event.tau_vsele_SF*event.tau_vsmu_SF*event.btagSF
                
            if met.pt>met_cut or mT.lepMET>mt_lepMET_cut or mT.lepMET<0 or met.pt<0:
                continue

            if trig == 'Ele' or trig == 'all' and abs(FakeLepton.pdgid) == 11 and nleps.LightLeptons < 2 and jets.numberSeparate >0 and  abs(FakeLepton.eta)<2.4 and not(abs(FakeLepton.eta)>1.4442 and abs(FakeLepton.eta)<1.566) and FakeLepton.pt>0 and FakeLepton.jetRelIso>=0:
                if isMC and (FakeLepton.isPrompt!=1): 
                    SF = 0
                if not (FakeLepton.eta<-2.4 or FakeLepton.eta>2.4):
                    isTight = False
                    if FakeLepton.pfRelIso04<0.08 and FakeLepton.isTight:
                        isTight = True
                    hEle.addEvent(isTight, isData, FakeLepton.pt, FakeLepton.eta, SF)
            
            elif trig == 'Mu' or trig == 'all' and abs(FakeLepton.pdgid) == 13 and nleps.LightLeptons < 2 and jets.numberSeparate > 0 and  abs(FakeLepton.eta)<2.4 and FakeLepton.pt>0 and FakeLepton.pfRelIso04>=0:
                if isMC and (FakeLepton.isPrompt!=1):
                    SF = 0
                
                isTight = False
                if abs(FakeLepton.pfRelIso04)<0.15 and FakeLepton.isTight:
                    isTight = True
                hMu.addEvent(isTight, isData, FakeLepton.pt, FakeLepton.eta, SF)
            
            if trig == 'HT' or trig == 'all':
                if veto.TauLeptons==1:
                    continue
                if abs(FakeTau.eta)<2.4 and FakeTau.pt>0:
                    if isMC and (FakeTau.isPrompt!=5): 
                        SF = 0
                    isTight = False

                    if FakeTau.DeepTauWP>=64:
                        isTight = True
                hTau.addEvent(isTight, isData, FakeLepton.pt, FakeLepton.eta, SF)

                    