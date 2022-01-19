import os
import sys
import optparse
import ROOT
import math
import copy
import datetime
import time
from EfficiencyHisto_manager import *

class fileManager:

    def __init__(self, trigger, met, mt_lepMet, directory, bkg, onlybkg):
        print('----- STARTING INITIALIZATION OF FILE MANAGER ------')
        time  = datetime.datetime.now()
        date  = datetime.datetime.today()
        timeStr = str(time)
        newTime = timeStr.replace(" ", "_")
        endTime = newTime.replace(":", "")
        timeToUse = endTime.split(".")
        self.filename =  trigger + '_FakeRatio_METcut_' + met + '_mt_lep_MET_cut_' + mt_lepMet + '_DateTime_' + timeToUse[0]
        if bkg:     self.filename += '_MCpromptSUBTRACTED'
        if onlybkg: self.filename += '_onlymcprompt'
        self.filename += '.root'
        self.filename = directory + self.filename
        self.f = ROOT.TFile(self.filename, "RECREATE")
        self.histos = []
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
        self.f.Close()