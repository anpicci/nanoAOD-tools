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
    def __init__(self, lepton, leptonPrompt=5):
        print(array.array('d', lower_pt), array.array('d', lower_eta_ele))
        print('Creating histo for lepton: ', lepton)
        self.lepton = lepton
        self.leptonPrompt = leptonPrompt
        self.hNLoose_Data   = ROOT.TH2F("h2NLoose" + lepton + "_data", lepton + "#loose events",    (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))
        self.hNTight_Data   = ROOT.TH2F("h2NTight" + lepton + "_data", lepton + "#tight events",    (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))
        self.hNLoose_MC     = ROOT.TH2F("h2NLoose" + lepton + "_MC",   lepton + "#loose events_MC", (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))
        self.hNTight_MC     = ROOT.TH2F("h2NTight" + lepton + "_MC",   lepton + "#tight events_MC", (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))
        self.Efficiency     = ROOT.TH2F("FakeRatio" + lepton + "",     lepton + "Fake Ratio",       (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))
        self.Numerator      = ROOT.TH2F("Numerator" + lepton + "",     lepton + " Numerator",       (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))
        self.Denumerator    = ROOT.TH2F("Denumerator" + lepton + "",   lepton + " Denumerator",     (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))

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

    def ProjectTree(self, tree, isData, cut_l, cut_t, region):
        if isData:
            hNLoose_Data   = ROOT.TH2F("h2NLoose" + self.lepton + "_data_temp", self.lepton + "#loose events",    (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))
            hNTight_Data   = ROOT.TH2F("h2NTight" + self.lepton + "_data_temp", self.lepton + "#tight events",    (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))

        else:
            hNLoose_MC     = ROOT.TH2F("h2NLoose" + self.lepton + "_MC_temp",   self.lepton + "#loose events_MC", (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))
            hNTight_MC     = ROOT.TH2F("h2NTight" + self.lepton + "_MC_temp",   self.lepton + "#tight events_MC", (len(lower_pt)-1), array.array('d', lower_pt), (len(lower_eta_ele)-1), array.array('d', lower_eta_ele))

        print("hello, i'm projecting", tree.GetName(), "in", self.lepton)
        variables = "Fake" + self.lepton + "_eta:Fake" + self.lepton + "_pt"
        cut_loose = "(" + cut_l + ")*(" + region + ")"
        cut_tight = "(" + cut_l + ")*(" + cut_t + ")*(" + region + ")"
        if isData:
            SF = "(1.)"
        else:
            SF = "(w_nominal[0]*PFSF[0]*puSF[0]*lepSF[0]*tau_vsjet_SF[0]*tau_vsele_SF[0]*tau_vsmu_SF[0]*btagSF[0]*(Fake" + str(self.lepton) + "_isPrompt==" + str(self.leptonPrompt) + "))"

        cutstring_loose = cut_loose + "*" + SF
        cutstring_tight = cut_tight + "*" + SF
        print("cut_loose:", cutstring_loose, "cut_tight:", cutstring_tight)
        if isData:
            print(tree.Project(hNLoose_Data.GetName(), variables, cutstring_loose))
            print(tree.Project(hNTight_Data.GetName(), variables, cutstring_tight))
            print("hl name:", hNLoose_Data.GetName(), "ht name:", hNTight_Data.GetName())
            print("hl entries", hNLoose_Data.GetEntries(), "ht entries", hNTight_Data.GetEntries())
            self.hNLoose_Data.Add(hNLoose_Data)#.Clone()
            self.hNTight_Data.Add(hNTight_Data)#.Clone()

        else:
            print(tree.Project(hNLoose_MC.GetName(), variables, cutstring_loose))
            print(tree.Project(hNTight_MC.GetName(), variables, cutstring_tight))
            print("hl entries", hNLoose_MC.GetEntries(), "ht entries", hNTight_MC.GetEntries())
            self.hNLoose_MC.Add(hNLoose_MC)#.Clone()
            self.hNTight_MC.Add(hNTight_MC)#.Clone()

    def SanitizeHisto(self):
        print('Assuring you have no bin with 0 entries')
        
        nBinsX = self.hNLoose_Data.GetNbinsX() +1
        nBinsY  = self.hNLoose_Data.GetNbinsY() +1
        
        for i in range(nBinsX):
            for j in range(nBinsY):
                if(self.hNLoose_Data.GetBinContent(i,j) == 0):
                    self.hNLoose_Data.SetBinContent(i, j, 3.0)
                    self.hNLoose_Data.SetBinError(i, j, math.sqrt(3.0))
                #if(self.hNTight_Data.GetBinContent(i,j) == 0):
                    #self.hNTight_Data.SetBinContent(i, j, 3.0)

        xnbins = nBinsX - 1
        ynbins = nBinsY - 1

        j=1
        while j<=ynbins:
            self.hNLoose_Data.SetBinContent(xnbins, j, self.hNLoose_Data.GetBinContent(xnbins,j)+self.hNLoose_Data.GetBinContent(xnbins+1,j))
            self.hNLoose_Data.SetBinError(xnbins, j, math.sqrt(pow(self.hNLoose_Data.GetBinError(xnbins,j),2) + pow(self.hNLoose_Data.GetBinError(xnbins+1,j),2)))
            self.hNTight_Data.SetBinContent(xnbins, j, self.hNTight_Data.GetBinContent(xnbins,j)+self.hNTight_Data.GetBinContent(xnbins+1,j))
            self.hNTight_Data.SetBinError(xnbins, j, math.sqrt(pow(self.hNTight_Data.GetBinError(xnbins,j),2) + pow(self.hNTight_Data.GetBinError(xnbins+1,j),2)))

            self.hNLoose_MC.SetBinContent(xnbins, j, self.hNLoose_MC.GetBinContent(xnbins,j)+self.hNLoose_MC.GetBinContent(xnbins+1,j))
            self.hNLoose_MC.SetBinError(xnbins, j, math.sqrt(pow(self.hNLoose_MC.GetBinError(xnbins,j),2) + pow(self.hNLoose_MC.GetBinError(xnbins+1,j),2)))
            self.hNTight_MC.SetBinContent(xnbins, j, self.hNTight_MC.GetBinContent(xnbins,j)+self.hNTight_MC.GetBinContent(xnbins+1,j))
            self.hNTight_MC.SetBinError(xnbins, j, math.sqrt(pow(self.hNTight_MC.GetBinError(xnbins,j),2) + pow(self.hNTight_MC.GetBinError(xnbins+1,j),2)))
            j+=1

        j = 1
        while j <= xnbins:
            self.hNLoose_Data.SetBinContent(j, ynbins, self.hNLoose_Data.GetBinContent(j, ynbins)+self.hNLoose_Data.GetBinContent(j,ynbins+1))
            self.hNLoose_Data.SetBinError(j, ynbins, math.sqrt(pow(self.hNLoose_Data.GetBinError(j,ynbins),2) + pow(self.hNLoose_Data.GetBinError(j,ynbins+1),2)))
            self.hNTight_Data.SetBinContent(j, ynbins, self.hNTight_Data.GetBinContent(j,ynbins)+self.hNTight_Data.GetBinContent(j,ynbins+1))
            self.hNTight_Data.SetBinError(j, ynbins, math.sqrt(pow(self.hNTight_Data.GetBinError(j,ynbins),2) + pow(self.hNTight_Data.GetBinError(j,ynbins+1),2)))

            self.hNLoose_MC.SetBinContent(j, ynbins, self.hNLoose_MC.GetBinContent(j,ynbins)+self.hNLoose_MC.GetBinContent(j,ynbins+1))
            self.hNLoose_MC.SetBinError(j, ynbins, math.sqrt(pow(self.hNLoose_MC.GetBinError(j,ynbins),2) + pow(self.hNLoose_MC.GetBinError(j,ynbins+1),2)))
            self.hNTight_MC.SetBinContent(j, ynbins, self.hNTight_MC.GetBinContent(j,ynbins)+self.hNTight_MC.GetBinContent(j,ynbins+1))
            self.hNTight_MC.SetBinError(j, ynbins, math.sqrt(pow(self.hNTight_MC.GetBinError(j,ynbins),2) + pow(self.hNTight_MC.GetBinError(j,ynbins+1),2)))
            j+=1


    def CalculateEfficiency(self):
        Numerator = self.hNTight_Data.Clone()
        Numerator.Add(self.hNTight_MC, -1)
        Denumerator = self.hNLoose_Data.Clone()
        Denumerator.Add(self.hNLoose_MC, -1)
        Numerator.Sumw2()
        Denumerator.Sumw2()
        self.Efficiency = Numerator.Clone()
        self.Efficiency.Divide(Denumerator)
        self.Efficiency.SetName("FakeRatio_"+self.lepton)
        self.Efficiency.SetTitle("FakeRatio_"+self.lepton)


    def getHistoFromFile(self, fname, lepton):
        inf = ROOT.TFile.Open(fname)
        self.hNLoose_Data   = inf.Get("h2NLoose" + lepton + "_data")
        self.hNTight_Data   = inf.Get("h2NTight" + lepton + "_data")
        self.hNLoose_MC     = inf.Get("h2NLoose" + lepton + "_MC")  
        self.hNTight_MC     = inf.Get("h2NTight" + lepton + "_MC")

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
