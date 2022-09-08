set LD_PRELOAD=libtcmalloc.so
set folder0 = vUL040
set channel = "ltau" 
reset

#################### year1 #################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst

#################### year1bis #################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst

set year = UL2016M
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst

#################### year2 #################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v countings --syst noSyst

#################### year3 #################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -d Triboson_UL2018 #-v countings --syst noSyst
python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -d Triboson_UL2018 #-v countings --syst noSyst
python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -d Triboson_UL2018 #-v countings --syst noSyst
python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -d Triboson_UL2018 #-v countings --syst noSyst
python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --count --tDMcut -d Triboson_UL2018 #-v countings --syst noSyst

set year = ULRunII
#python3 makeplot.py -y $year --lep electron --presel -f $folder0 -p --ch $channel -v DNN_SM_UL035_novar --syst noSyst 
#set year = UL2016M
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel -v m_o1 --tDMcut -d FakeMu_$year --syst noSyst
