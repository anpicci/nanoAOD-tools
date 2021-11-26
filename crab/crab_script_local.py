#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.examples.MCweight_writer import *
from PhysicsTools.NanoAODTools.postprocessing.examples.MET_HLT_Filter import *
from PhysicsTools.NanoAODTools.postprocessing.examples.preselection import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.lepSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *

metCorrector = createJMECorrector(isMC=True, dataYear=2017, jesUncert='All', applyHEMfix=True)
fatJetCorrector = createJMECorrector(isMC=True, dataYear=2017, jesUncert='All', applyHEMfix=True, jetType = 'AK8PFPuppi')

p = PostProcessor('.', ['root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17NanoAODv9/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/20UL17JMENano_106X_mc2017_realistic_v9-v1/40000/014A4BBB-6379-2F48-8D50-25E51BDD1E9E.root'], '', 
                  modules=[
                      #MCweight_writer('TTTo2L2Nu_2017'), MET_HLT_Filter_2017(), 
                      #preselection(), #PrefCorr(), metCorrector(), fatJetCorrector(),
                      lepSF_UL2018(),# btagSF2017()
                  ],
outputbranchsel=os.path.abspath('../scripts/keep_and_drop.txt'), histFileName="histOut.root", histDirName="plots", maxEntries=2, provenance=True, fwkJobReport=True)
p.run()
print('DONE')
#, PrefCorr(), metCorrector(), fatJetCorrector()
