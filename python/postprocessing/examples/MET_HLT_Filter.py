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
        if not "UL" in self.year:
            good_MET = flag.goodVertices and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter
            if(self.year == "2016"):
                good_HLT = (HLT.Ele27_WPTight_Gsf or HLT.Ele32_WPTight_Gsf or HLT.IsoMu24 or HLT.IsoTkMu24) and flag.globalSuperTightHalo2016Filter
            elif(self.year == "2017"):
                good_HLT = (HLT.IsoMu27 or HLT.Mu50 or HLT.Ele35_WPTight_Gsf or HLT.Ele32_WPTight_Gsf_L1DoubleEG or HLT.Photon200)# or HLT.PFHT250 or HLT.PFHT350)
            elif(self.year == "2018"):
                good_HLT = (HLT.IsoMu27 or HLT.Mu50 or HLT.Ele35_WPTight_Gsf or HLT.Ele32_WPTight_Gsf_L1DoubleEG or HLT.Photon200)# or HLT.PFHT250 or HLT.PFHT350)
            else:
                print("Please specify the year: possible choices are 2016, 2017 or 2018")

        else:
            if "2017" in self.year or "2018" in self.year:
                try:
                    good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.eeBadScFilter and flag.ecalBadCalibFilter and flag.BadPFMuonDzFilter 
                except:
                    good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.eeBadScFilter and flag.ecalBadCalibFilter 
            elif "2016" in self.year:
                try:
                    good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.eeBadScFilter and flag.BadPFMuonDzFilter 
                except:
                    good_MET = flag.goodVertices and flag.globalSuperTightHalo2016Filter and flag.HBHENoiseFilter and flag.HBHENoiseIsoFilter and flag.EcalDeadCellTriggerPrimitiveFilter and flag.BadPFMuonFilter and flag.eeBadScFilter 
        
            if(self.year == "UL2016"):
                good_HLT = (HLT.IsoMu24 or HLT.IsoTkMu24 or HLT.Mu50 or HLT.TkMu50 or HLT.Ele27_WPTight_Gsf or HLT.Ele32_WPTight_Gsf or HLT.Photon175)
            elif(self.year == "UL2016APV"):
                good_HLT = (HLT.IsoMu24 or HLT.Mu50 or HLT.Ele27_WPTight_Gsf or HLT.Ele32_WPTight_Gsf or HLT.Photon175)
            elif(self.year == "UL2017"):
                good_HLT = (HLT.IsoMu27 or HLT.Mu50 or HLT.OldMu100 or HLT.TkMu100 or HLT.Ele35_WPTight_Gsf or HLT.Ele32_WPTight_Gsf_L1DoubleEG) 
                            # and (L1.SingleIsoEG30er2p1 or L1.SingleIsoEG32 or L1.SingleEG40)) or HLT.Photon200)# or HLT.PFHT250 or HLT.PFHT350)
            elif(self.year == "UL2018"):
                good_HLT = (HLT.IsoMu24 or HLT.Mu50 or HLT.OldMu100 or HLT.TkMu100 or HLT.Ele32_WPTight_Gsf or HLT.Photon200)# or HLT.PFHT250 or HLT.PFHT350)
            else:
                print("Please specify the year: possible choices are 2016, 2017 or 2018")

        good_evt = (good_MET and good_HLT)
        return good_evt
        

MET_HLT_Filter_2016 = lambda : MET_HLT_Filter("2016")
MET_HLT_Filter_2017 = lambda : MET_HLT_Filter("2017")
MET_HLT_Filter_2018 = lambda : MET_HLT_Filter("2018")
MET_HLT_Filter_UL2016APV = lambda : MET_HLT_Filter("UL2016APV")
MET_HLT_Filter_UL2016 = lambda : MET_HLT_Filter("UL2016")
MET_HLT_Filter_UL2017 = lambda : MET_HLT_Filter("UL2017")
MET_HLT_Filter_UL2018 = lambda : MET_HLT_Filter("UL2018")
