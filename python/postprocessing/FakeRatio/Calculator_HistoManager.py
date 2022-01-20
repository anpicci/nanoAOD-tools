import os
import sys
import optparse
import ROOT
import math
import copy
import datetime
import time
import array
import copy
from Calculator_utils import *

from ROOT import TCanvas, TColor, TGaxis, TH1F, TPad

class EfficiencyHisto_manager:
    def __init__(self, lepton):
        print('Creating histo for lepton: ', lepton)
        self.lepton = lepton
        self.hNLoose_Data   = ROOT.TH2F("h2NLoose" + lepton + "_data", lepton + "#loose events",    5, array.array('d', lower_pt), 8, array.array('d', lower_eta_ele))
        self.hNTight_Data   = ROOT.TH2F("h2NTight" + lepton + "_data", lepton + "#loose events",    5, array.array('d', lower_pt), 8, array.array('d', lower_eta_ele))
        self.hNLoose_MC     = ROOT.TH2F("h2NLoose" + lepton + "_MC",   lepton + "#loose events_MC", 5, array.array('d', lower_pt), 8, array.array('d', lower_eta_ele))
        self.hNTight_MC     = ROOT.TH2F("h2NTight" + lepton + "_MC",   lepton + "#loose events_MC", 5, array.array('d', lower_pt), 8, array.array('d', lower_eta_ele))
        self.Efficiency     = ROOT.TH2F("FakeRatio" + lepton + "",     lepton + "Fake Ratio",       5, array.array('d', lower_pt), 8, array.array('d', lower_eta_ele))
        self.Numerator      = ROOT.TH2F("Numerator" + lepton + "",     lepton + " Numerator",       5, array.array('d', lower_pt), 8, array.array('d', lower_eta_ele))
        self.Denumerator    = ROOT.TH2F("Denumerator" + lepton + "",   lepton + " Denumerator",     5, array.array('d', lower_pt), 8, array.array('d', lower_eta_ele))

    def addEvent(self, isTight, isData, pt, eta, SF):
        if(isData):
            if isTight:
                self.hNTight_Data.Fill(pt, eta, SF)
            else:
                self.hNLoose_Data.Fill(pt, eta, SF)
        else:
            if isTight:
                self.hNTight_MC.Fill(pt, eta, SF)
            else:
                self.hNLoose_MC.Fill(pt, eta, SF)

    def SanitizeHisto(self):
        print('Assuring you have no bin with 0 entries')
        
        nBinsX = self.hNLoose_Data.GetNbinsX() +1
        nBinsY  = self.hNLoose_Data.GetNbinsY() +1
        for i in range(nBinsX):
            for j in range(nBinsY):
                if(self.hNLoose_Data.GetBinContent(i,j) == 0):
                    self.hNLoose_Data.SetBinContent(i, j, 3.0)
                if(self.hNTight_Data.GetBinContent(i,j) == 0):
                    self.hNTight_Data.SetBinContent(i, j, 3.0)
                if(self.hNLoose_MC.GetBinContent(i,j) == 0):
                    self.hNLoose_MC.SetBinContent(i, j, 3.0)
                if(self.hNTight_MC.GetBinContent(i,j) == 0 ):
                    self.hNTight_MC.SetBinContent(i, j, 3.0)

    def CalculateEfficiency(self):
        self.Numerator = self.hNTight_Data.Clone()
        self.Numerator.Add(self.hNTight_MC)
        self.Denumerator = self.hNLoose_Data.Clone()
        self.Denumerator.Add(self.hNLoose_MC, -1)
        self.Numerator.Sumw2()
        self.Denumerator.Sumw2()
        self.Efficiency = self.Numerator.Clone()
        self.Efficiency.Divide(self.Denumerator)
        self.Efficiency.SetName("FakeRatio_"+self.lepton)
        self.Efficiency.SetTitle("FakeRatio_"+self.lepton)

    def DrawAll(self, fname):
        c = TCanvas("c", "canvas", 800, 800)
        c.Divide(2,3)
        c.cd(1)
        self.hNLoose_Data.Draw()
        c.cd(2)
        self.hNTight_Data.Draw()
        c.cd(3)
        self.hNLoose_MC.Draw()
        c.cd(4)
        self.hNTight_MC.Draw()
        c.cd(5)
        self.Efficiency.Draw()
        c.Draw()
        c.SaveAs(fname)

    def GetHistos(self):
        return self.hNLoose_Data, self.hNTight_Data, self.hNLoose_MC, self.hNTight_MC, self.Efficiency