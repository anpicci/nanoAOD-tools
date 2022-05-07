import os
import sys
import optparse
import ROOT
import math
import copy
import datetime
import time
from Calculator_HistoManager import *
from Calculator_utils import *

class fileManager:
    def __init__(self, trigger, met, mt_lepMet, directory, bkg, onlybkg, inFolder, year, vsJetWp):
        print('----- STARTING INITIALIZATION OF FILE MANAGER ------')

        #Setting up the output file
        time  = datetime.datetime.now()
        timeStr = str(time)
        newTime = timeStr.replace(" ", "_")
        endTime = newTime.replace(":", "")
        timeToUse = endTime.split(".")
        '''
        self.filename =  "FakeRatio_trigger_" + trigger + "_year_" + year + '_wpDeepTauVsJet_' + vsJetWp + '_METcut_' + met + '_mt_lep_MET_cut_' + mt_lepMet + '_DateTime_' + timeToUse[0]
        print("saving in: ", self.filename)
        if bkg:
            self.filename += '_MCpromptSUBTRACTED'
        if onlybkg:
            self.filename += '_onlymcprompt'
        '''
        self.filename = "FR_vsjet" + vsJetWp + "_UL" + year + "_test"
        self.filename += '.root'
        self.filename = directory + self.filename
        self.f = ROOT.TFile(self.filename, "RECREATE")
        
        #adding histos to be written
        self.histos = []
        
        #Managing input files
        DataDict = {
                'Ele' : "DataHT_UL" + str(year) + "/DataHT_UL" + str(year) + ".root",
                'Mu'  : "DataMuFake_UL" + str(year) + "/DataMuFake_UL" + str(year) + ".root",
                'Tau' : "DataHT_UL" + str(year) + "/DataHT_UL" + str(year) + ".root",
                'all' : "DataHT_UL" + str(year) + "/DataHT_UL" + str(year) + ".root",
                }
        bkg_files = {
                'DYJetsToLL' : "DYJetsToLL_UL" + str(year) + "/DYJetsToLL_UL" + str(year) + ".root", 
                'WJets'      : "WJets_UL" + str(year) + "/WJets_UL" + str(year) + ".root",
                'ZZToLep'    : "ZZtoLep_UL" + str(year) + "/ZZtoLep_UL" + str(year) + ".root",        
                'TT'         : "TT_UL" + str(year) + "/TT_UL" + str(year) + ".root",        
                }
        self.DataFile = inFolder + DataDict[trigger]
        self.BkgFile = []
        for pos in bkg_files:
            self.BkgFile.append(inFolder + bkg_files[pos])
        
        print('opened file in ', self.filename)
        print('----- ENDED INITIALIZATION OF FILE MANAGER ------')

    def closeFile(self):
        print('Closing file: ', self.filename)
        self.f.Close()
    
    def addEfficiencyHisto(self, hManager):
        h1, h2, h3, h4, h5 = hManager.GetHistos()
        self.histos.append(h1)
        self.histos.append(h2)
        self.histos.append(h3)
        self.histos.append(h4)
        self.histos.append(h5)

    def saveFile(self):
        self.f.cd()
        for h in self.histos:
            h.Write()
        #self.f.Close()

    def getData(self):
        if not os.path.exists(self.DataFile):
            print('Data do not exists in path ', self.DataFile)
            return '', False
        return self.DataFile, True
    
    def getBkg(self):
        out = []
        for p in self.BkgFile:
            if os.path.exists(p): out.append(p)
        return out, False
