reset
#set folder = vUL035 #### aQGC added, new fakes, systematics completed
set folder = vUL040 #### same as UL035, but SF ele and met unclust sys

#######    2017   #######
set year = 'UL2017'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d DataEle_$year,DataMu_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d DataEle_$year,DataMu_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2018   #######
set year = 'UL2018'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d VBS_SSWW_cHW_UL2018 --rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d DataEle_$year,DataMu_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016   #######
set year = 'UL2016'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d VBS_SSWW_c,VBS_SSWW_SM_ --rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d DataEle_$year,DataMu_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#######    2016APV   #######
set year = 'UL2016APV'
#reset
#python3 PrepareToPlot.py -f $folder -y $year -d VBS_SSWW_cHW_SM_UL2016APV,VBS_SSWW_SM_$year --rw --or
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco jl --masscrit --deltaeta -y $year -d DataEle_$year,DataMu_$year #--rw
#python3 SetAndLaunchCondorRun_old.py -f $folder --reco lj --masscrit --deltaeta -y $year

#set year = 'UL2016M'
set year = 'ULRunII'
python3 PrepareToPlot.py -f $folder -y $year -d DataEle_$year,DataMu_$year --rw
