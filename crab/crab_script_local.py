#!/usr/bin/env python
import os
from PhysicsTools.NanoAODTools.postprocessing.framework.postprocessor import *
from PhysicsTools.NanoAODTools.postprocessing.modules.jme.jetmetHelperRun2 import *
from PhysicsTools.NanoAODTools.postprocessing.framework.crabhelper import inputFiles,runsAndLumis
from PhysicsTools.NanoAODTools.postprocessing.examples.MCweight_writer import *
from PhysicsTools.NanoAODTools.postprocessing.examples.MET_HLT_Filter import *
from PhysicsTools.NanoAODTools.postprocessing.examples.preselection import *
from PhysicsTools.NanoAODTools.postprocessing.examples.sampleFlagUL import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.PrefireCorr import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.puWeightProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.common.lepSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.modules.btv.btagSFProducer import *
from PhysicsTools.NanoAODTools.postprocessing.examples.dummyColumns import *

metCorrector = createJMECorrector(isMC=True, dataYear=2017, jesUncert='All', applyHEMfix=True)
fatJetCorrector = createJMECorrector(isMC=True, dataYear=2017, jesUncert='All', applyHEMfix=True, jetType = 'AK8PFPuppi')

p = PostProcessor('.', [#'root://cms-xrd-global.cern.ch//store/data/Run2017B/SingleMuon/NANOAOD/UL2017_MiniAODv2_NanoAODv9-v1/120000/09FD9FD6-A164-9A45-80BB-F3D1FBF9C462.root'
#'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17NanoAODv9/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/NANOAODSIM/20UL17JMENano_106X_mc2017_realistic_v9-v1/40000/014A4BBB-6379-2F48-8D50-25E51BDD1E9E.root'
'root://cms-xrd-global.cern.ch//store/mc/RunIISummer20UL17NanoAODv9/GluGluToWWToTNMN_TuneCP5_13TeV_MCFM701_pythia8/NANOAODSIM/106X_mc2017_realistic_v9-v1/2520000/07846BC7-40F2-9345-A3EF-C47491B0C916.root',
                    ], '', 
                  modules=[
                      #MCweight_writer('TTTo2L2Nu_2017'), 
                      MET_HLT_Filter_UL2017(), 
                      #preselection(), #PrefCorr(), metCorrector(), fatJetCorrector(),
                      #lepSF_UL2018(),#
                      #btagSF2017(),
                      #btagSFUL2017(),
                      #sampleFlagUL('DataMuB_UL2017'),
                      #dummyCol()
                  ],
                      provenance=True, 
                      fwkJobReport=True,
                      histFileName='hist.root', 
                      histDirName='plots',
outputbranchsel=os.path.abspath('../scripts/keep_and_drop.txt'), maxEntries=2)
p.run()
print('DONE')
#, PrefCorr(), metCorrector(), fatJetCorrector()
