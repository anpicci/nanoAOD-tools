reset

#######    2017   #######
#python3 SetAndLaunchCondorRun_old.py -f v100 --reco jl --masscrit --deltaeta -y 2017 -d DataMu_2017 --rw
#python3 SetAndLaunchCondorRun_old.py -f v100 --reco jl --masscrit --deltaeta -y 2017 -d DataEle_2017 --rw
#python3 SetAndLaunchCondorRun.py -f v101 --reco lj --masscrit --deltaeta -y 2017
#python3 SetAndLaunchCondorRun.py -f v102 --reco jl --masscrit -y 2017
#python3 SetAndLaunchCondorRun.py -f v103 --reco lj --masscrit -y 2017



#######    2018   #######
#python3 SetAndLaunchCondorRun_old.py -f vUL001 --reco jl --masscrit --deltaeta -y 2017 -d TTTo2L2Nu_UL2017
python3 SetAndLaunchCondorRun_old.py -f vbtag_UL18 --beff -y UL2018 -d TT_beff_UL2018 
#python3 SetAndLaunchCondorRun_old.py -f v101 --reco lj --masscrit --deltaeta -y 2018
#python3 SetAndLaunchCondorRun_old.py -f v102 --reco jl --masscrit -y 2018
#python3 SetAndLaunchCondorRun_old.py -f v103 --reco lj --masscrit -y 2018
