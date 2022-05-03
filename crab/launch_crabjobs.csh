set year = 'UL2016'
reset
#python submit_crab.py -d TT_$year --status
#python submit_crab.py -d WJets_$year --status
#python submit_crab.py -d WZ_$year --status #
#python submit_crab.py -d DYJetsToLL_$year --status
#python submit_crab.py -d VG_$year --status #
#python submit_crab.py -d TVX_$year --status
#python submit_crab.py -d WrongSign_$year --status
#python submit_crab.py -d TTTo2L2Nu_$year --status
#python submit_crab.py -d Other_$year --status #
#python submit_crab.py -d ZZtoLep_$year --status
#python submit_crab.py -d VBS_SSWW_aQGC_$year --status #
#python submit_crab.py -d WpWpJJ_EWK_$year --status #
#python submit_crab.py -d WpWpJJ_QCD_$year --status #
#python submit_crab.py -d VBS_SSWW_DIM6_SM_$year --status
#python submit_crab.py -d WWZTo3L1Nu2Q_$year -r # -s
#python submit_crab.py -d VBFHToTauTau_$year --status # -s 
#python submit_crab.py -d DataEle_$year --status #
#python submit_crab.py -d DataMu_$year --status #
#python submit_crab.py -d QCD_$year --status #

#set year = '2017'
#python submit_crab.py -d DataEle_$year --status
#python submit_crab.py -d DataMu_$year --status

######### UL ######
#python submit_crab.py -d TTTo2L2Nu_UL2016APV -k #--sampleFlag
python submit_crab.py -d ZZTo4L_UL2016 --status #--sampleFlag
#python submit_crab.py -d TTTo2L2Nu_UL2017 -k #--sampleFlag
#python submit_crab.py -d TTTo2L2Nu_UL2018 -k #--sampleFlag
