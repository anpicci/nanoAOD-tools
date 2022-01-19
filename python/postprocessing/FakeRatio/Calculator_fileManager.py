import os
import sys
import optparse
import ROOT
import math
import copy
import datetime
import time

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
        print('opened file in ', self.filename)
        print('----- ENDED INITIALIZATION OF FILE MANAGER ------')

    def closeFile(self):
        print('Closing file: ', self.filename)
        self.f.Close()