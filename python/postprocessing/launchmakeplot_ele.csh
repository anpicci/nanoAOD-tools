set folder0 = vUL030 #_tagger_DataSplit_MCnoSplit
#set folder0 = v100
set channel = 'ltau' #
reset

######## year1 #######################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count  
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL 

######### year1bis #######################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year\_*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL 

######## year2 #######################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL 

####### year3 #######################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL 
