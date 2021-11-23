import ROOT
import math
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module
from PhysicsTools.NanoAODTools.postprocessing.tools import *

class preselection_Fake(Module):
    def __init__(self):
        pass
    def beginJob(self):
        pass
    def endJob(self):
        pass
    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("HT_eventHT",  "F") 
    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass
    def analyze(self, event):
        goodEvent = False

        """process event, return True (go to next module) or False (fail, go to next event)"""

        met = Object(event, "MET")
        pmet = Object(event, "PuppiMET")
        PV = Object(event, "PV")

        eventSum = ROOT.TLorentzVector()

        isGoodPV = (PV.ndof>4 and abs(PV.z)<24 and math.hypot(PV.x, PV.y)<2)

        lowmet = (met < 80. or pmet < 80.)

        looseMu = list(filter(lambda x : x.looseId and x.pfRelIso04_all < 1. and x.pfRelIso04_all>=0. and abs(x.eta) < 2.4, muons))
        looseEle = list(filter(lambda x : x.mvaFall17V2Iso_WPL and x.jetRelIso < 1. and x.jetRelIso >= 0. and ((abs(x.eta) < 1.4442) or (abs(x.eta) > 1.566 and abs(x.eta)< 2.5)), electrons))
        looseTau = list(filter(lambda x : x.idDeepTau2017v2p1VSjet >= 2 and x.idDeepTau2017v2p1VSe >= 4 and x.idDeepTau2017v2p1VSmu >= 8 and x.idDecayModeNewDMs and abs(x.eta) < 2.3, taus))

        for j in jets:
            eventSum += j.p4()

        self.out.fillBranch("HT_eventHT", eventSum.Pt())

        isGoodEvent = (len(looseEle) > 0 or len(looseMu) > 0 or len(looseTau) > 0)

        goodEvent = isGoodPV and isGoodEvent

        return goodEvent

# define modules using the syntax 'name = lambda : constructor' to avoid having them loaded when not needed
#MySelectorModuleConstr = lambda : exampleProducer(jetetaSelection= lambda j : abs(j.eta)<2.4) 
