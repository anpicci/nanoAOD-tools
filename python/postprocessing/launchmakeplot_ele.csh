set year1 = UL2016APV
set year1bis = UL2016
set year1bis_ = UL2016_
set year2 = UL2017
#set year2 = 2017
set year3 = UL2018
#set year3 = 2018
set folder0 = vUL010 #_tagger_DataSplit_MCnoSplit
#set folder0 = v100
set channel = 'ltau' #
reset

######## year1 #######################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year1*
python3 makeplot.py -y $year1 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1 --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL --syst noSyst

######### year1bis #######################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year1bis_*
python3 makeplot.py -y $year1bis --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1bis --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1bis --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1bis --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL --syst noSyst

######## year2 #######################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year2*
python3 makeplot.py -y $year2 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d WrongSign_$year2 --syst noSyst
python3 makeplot.py -y $year2 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d WrongSign_$year2 --syst noSyst
python3 makeplot.py -y $year2 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d WrongSign_$year2 --syst noSyst
python3 makeplot.py -y $year2 --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d WrongSign_$year2 --bvetoL --syst noSyst

####### year3 #######################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year3*
python3 makeplot.py -y $year3 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year3 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year3 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year3 --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL --syst noSyst
