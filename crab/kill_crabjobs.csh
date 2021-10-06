set year = '2018'
reset
python submit_crab.py -d TT_$year -r # --status 
python submit_crab.py -d WJets_$year -r # --status 
#python submit_crab.py -d WZ_$year -s 
python submit_crab.py -d DYJetsToLL_$year -r # --status 
#python submit_crab.py -d VG_$year -s 
#python submit_crab.py -d TVX_$year -s 
#python submit_crab.py -d WrongSign_$year -s 
python submit_crab.py -d TTTo2L2Nu_$year -r # --status
#python submit_crab.py -d Other_$year -s
python submit_crab.py -d ZZtoLep_$year --status
#python submit_crab.py -d ZZTo2L2Nu_$year -s
#python submit_crab.py -d GluGluToContinToZZTo4e_$year -s
#python submit_crab.py -d GluGluToContinToZZTo4mu_$year -s
#python submit_crab.py -d GluGluToContinToZZTo2mu2tau_$year -s
#python submit_crab.py -d GluGluToContinToZZTo2mu2nu_$year -s
#python submit_crab.py -d GluGluToContinToZZTo2e2tau_$year -s
#python submit_crab.py -d GluGluToContinToZZTo2e2mu_$year -s
#python submit_crab.py -d GluGluToContinToZZTo4L_$year -s
#python submit_crab.py -d WpWpJJ_EWK_$year -s
#python submit_crab.py -d WpWpJJ_QCD_$year --status
#python submit_crab.py -d VBS_SSWW_DIM6_SM_$year --status # --status
python submit_crab.py -d VBS_SSWW_TL_SM_$year -r # -s 
python submit_crab.py -d VBS_SSWW_TT_SM_$year -r # -s
#python submit_crab.py -d DataEle_$year -s
#python submit_crab.py -d DataMu_$year -s
