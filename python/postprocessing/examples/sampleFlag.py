import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module


sampleDict = {"VBS_SSWW_LL_SM_2017": 0}

class sampleFlag(Module):
    def __init__(self, samplename):
        self.writeHistFile=True
        self.samplename = samplename
        pass

    def beginJob(self,histFile=None,histDirName=None):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        self.out.branch("Sample", "I")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        self.out.fillBranch("Sample", sampleDict[self.samplename])
        return True
