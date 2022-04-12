#set LD_PRELOAD=libtcmalloc.so
set year1 = 2016
set year2 = 2017
set year3 = 2018
#set folder0 = vUL008 #_tagger_DataSplit_MCnoSplit
set folder0 = v100 #_tagger_DataSplit_MCnoSplit
set channel = "ltau" 
set user = 'apiccine'
reset
#################### year1 #################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/*$year1*root 
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year1*
#python3 makeplot.py -y $year1 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user
#python3 makeplot.py -y $year1 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user
#python3 makeplot.py -y $year1 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user
#python3 makeplot.py -y $year1 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user
#python3 makeplot.py -y $year1 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user

#################### year2 #################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/*$year2*root 
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year2*
python3 makeplot.py -y $year2 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --horn
python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --horn
python3 makeplot.py -y $year2 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --horn
python3 makeplot.py -y $year2 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --horn
python3 makeplot.py -y $year2 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --syst noSyst --horn

#################### year3 #################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/*$year3*root 
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year3*
#python3 makeplot.py -y $year3 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
#python3 makeplot.py -y $year3 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
#python3 makeplot.py -y $year3 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
#python3 makeplot.py -y $year3 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
#python3 makeplot.py -y $year3 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user

