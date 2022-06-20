set LD_PRELOAD=libtcmalloc.so
set folder0 = vUL030
set channel = "ltau" 
reset

#################### year1 #################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
python3 makeplot.py -y $year --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL 

#################### year1bis #################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL  

#################### year2 #################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL 

#################### year3 #################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL 
