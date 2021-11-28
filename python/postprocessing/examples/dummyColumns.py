import ROOT
ROOT.PyConfig.IgnoreCommandLineOptions = True

from PhysicsTools.NanoAODTools.postprocessing.framework.datamodel import Collection, Object
from PhysicsTools.NanoAODTools.postprocessing.framework.eventloop import Module


class dummyColumns(Module):
    def init(self):
        self.dummy = -999
        pass

    def beginJob(self,histFile=None,histDirName=None):
        pass

    def endJob(self):
        pass

    def beginFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        self.out = wrappedOutputTree
        # Jet_btagSF_deepjet_M_up Jet_btagSF_deepjet_M_down Jet_btagSF_deepjet_M Jet_partonFlavour PrefireWeight puWeight
        self.out.branch("Muon_genPartFlav", "I", lenVar="nMuon")
        self.out.branch("Electron_genPartFlav", "I", lenVar="nElectron")
        self.out.branch("Tau_genPartFlav", "I", lenVar="nTau")
        self.out.branch("Muon_effSF", "F", lenVar="nMuon")
        self.out.branch("Electron_effSF", "F", lenVar="nElectron")
        self.out.branch("Muon_effSF_errUp", "F", lenVar="nMuon")
        self.out.branch("Electron_effSF_errUp", "F", lenVar="nElectron")
        self.out.branch("Muon_effSF_errDown", "F", lenVar="nMuon")
        self.out.branch("Electron_effSF_errDown", "F", lenVar="nElectron")
        self.out.branch("Jet_btagSF_deepjet_M", "F", lenVar="nJet")
        self.out.branch("Jet_btagSF_deepjet_M_up", "F", lenVar="nJet")
        self.out.branch("Jet_btagSF_deepjet_M_down", "F", lenVar="nJet")
        self.out.branch("Jet_partonFlavour", "I", lenVar="nJet")
        self.out.branch("PrefireWeight", "F")
        self.out.branch("puWeight", "F")

    def endFile(self, inputFile, outputFile, inputTree, wrappedOutputTree):
        pass

    def analyze(self, event):
        print self.dummy
        muons = Collection(event, "Muon")
        electrons = Collection(event, "Electron")
        taus = Collection(event, "Tau")
        jets = Collection(event, "Jet")

        self.out.fillBranch("Muon_genPartFlav", [self.dummy for i in range(0,len(muons))])
        self.out.fillBranch("Electron_genPartFlav", [self.dummy for i in range(0,len(electrons))])
        self.out.fillBranch("Tau_genPartFlav", [self.dummy for i in range(0,len(taus))])
        self.out.fillBranch("Muon_effSF", [self.dummy for i in range(0,len(muons))])
        self.out.fillBranch("Electron_effSF", [self.dummy for i in range(0,len(electrons))])
        self.out.fillBranch("Muon_effSF_errUp", [self.dummy for i in range(0,len(muons))])
        self.out.fillBranch("Electron_effSF_errUp", [self.dummy for i in range(0,len(electrons))])
        self.out.fillBranch("Muon_effSF_errDown", [self.dummy for i in range(0,len(muons))])
        self.out.fillBranch("Electron_effSF_errDown", [self.dummy for i in range(0,len(electrons))])
        self.out.fillBranch("Jet_btagSF_deepjet_M", [self.dummy for i in range(0,len(jets))])
        self.out.fillBranch("Jet_btagSF_deepjet_M_up", [self.dummy for i in range(0,len(jets))])
        self.out.fillBranch("Jet_btagSF_deepjet_M_down", [self.dummy for i in range(0,len(jets))])
        self.out.fillBranch("Jet_partonFlavour", [self.dummy for i in range(0,len(jets))])
        self.out.fillBranch("PrefireWeight", self.dummy)
        self.out.fillBranch("puWeight", self.dummy)

        return True

dummyCol = dummyColumns
