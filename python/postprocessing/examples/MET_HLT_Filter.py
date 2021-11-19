import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection,Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module

class MET_HLT_Filter(Module):
    def __init__(self, year):
        self.year = str(year)
        pass
    def endJob(self):
        pass
    def beginJob(self):
        pass
    def analyze(self, event):
        """process event, return True (go to next module) or False (fail, go to next event)"""
        HLT = Object(event, "HLT")
        L1 = Object(event, "L1")
        flag = Object(event, 'Flag')
        if not "UL" in year:
            good_MET = flag.goodVertices and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter
        else:
            if "2017" in year or "2018" in year:
                good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.BadPFMuonDzFilter and flag.eeBadScFilter and flag.ecalBadCalibFilter
            elif "2016" in year:
                good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.BadPFMuonDzFilter and flag.eeBadScFilter
        if(self.year == "2016"):
            good_HLT = (HLT.Ele27_WPTight_Gsf or HLT.Ele32_WPTight_Gsf or HLT.IsoMu24 or HLT.IsoTkMu24) and flag.globalSuperTightHalo2016Filter
        elif(self.year == "2017"):
            good_HLT = (HLT.IsoMu27 or HLT.Mu50 or HLT.Ele35_WPTight_Gsf or HLT.Ele32_WPTight_Gsf_L1DoubleEG or HLT.Photon200)# or HLT.PFHT250 or HLT.PFHT350)
        elif(self.year == "2018"):
            good_HLT = (HLT.IsoMu27 or HLT.Mu50 or HLT.Ele35_WPTight_Gsf or HLT.Ele32_WPTight_Gsf_L1DoubleEG or HLT.Photon200)# or HLT.PFHT250 or HLT.PFHT350)
        else:
            print("Please specify the year: possible choices are 2016, 2017 or 2018")
        return good_MET and good_HLT

MET_HLT_Filter_2016 = lambda : MET_HLT_Filter("2016")
MET_HLT_Filter_2017 = lambda : MET_HLT_Filter("2017")
MET_HLT_Filter_2018 = lambda : MET_HLT_Filter("2018")
MET_HLT_Filter_UL2016APV = lambda : MET_HLT_Filter("UL2016APV")
MET_HLT_Filter_UL2016 = lambda : MET_HLT_Filter("UL2016")
MET_HLT_Filter_UL2017 = lambda : MET_HLT_Filter("UL2017")
MET_HLT_Filter_UL2018 = lambda : MET_HLT_Filter("UL2018")
