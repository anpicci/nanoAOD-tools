set year = '2017'
#python submit_crab.py -d TT_$year --status
#python submit_crab.py -d WJets_$year --status
#python submit_crab.py -d WZ_$year --status #--verb
#python submit_crab.py -d DYJetsToLL_$year --status
#python submit_crab.py -d WpWpJJ_EWK_$year --status
#python submit_crab.py -d WpWpJJ_QCD_$year --status
python submit_crab.py -d DataEle_$year --status
python submit_crab.py -d DataMu_$year --status
python submit_crab.py -d DataHT_$year --status

