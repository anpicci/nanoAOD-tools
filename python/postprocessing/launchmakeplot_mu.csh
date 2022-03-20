#set LD_PRELOAD=libtcmalloc.so
set year1 = UL2016APV
set year1bis = UL2016
set year1bis_ = UL2016_
set year2 = UL2017
#set year2 = 2017
set year3 = UL2018
#set year3 = 2018
set folder0 = vUL008 #_tagger_DataSplit_MCnoSplit
#set folder0 = v100 
set channel = "ltau" 

#################### year1 #################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/*$year1*root 
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year1bis*
python3 makeplot.py -y $year1 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year1 --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL --syst noSyst
##python3 makeplot.py -y $year1 --lep muon --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet2  --count
##python3 makeplot.py -y $year1 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count
##python3 makeplot.py -y $year1 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL
##python3 makeplot.py -y $year1 --lep muon --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet2  --count
##python3 makeplot.py -y $year1 --lep muon --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet2  --count

#################### year1bis #################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/*$year1bis_*root 
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year1bis_*
python3 makeplot.py -y $year1bis --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst
python3 makeplot.py -y $year1bis --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst
python3 makeplot.py -y $year1bis --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst
python3 makeplot.py -y $year1bis --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL --syst noSyst
##python3 makeplot.py -y $year1bis --lep muon --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count
##python3 makeplot.py -y $year1bis --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count
##python3 makeplot.py -y $year1bis --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --bvetoL
##python3 makeplot.py -y $year1bis --lep muon --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count
##python3 makeplot.py -y $year1bis --lep muon --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count
##python3 makeplot.py -y $year1bis --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year1bis --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count  --bvetoL

#################### year2 #################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/*$year2*root 
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year2*
python3 makeplot.py -y $year2 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year2 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst
python3 makeplot.py -y $year2 --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL --syst noSyst
##python3 makeplot.py -y $year2 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet8 --rPrompt --count
##python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet8 --rPrompt --count
##python3 makeplot.py -y $year2 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet8 --rPrompt --count
##python3 makeplot.py -y $year2 --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet8 --rPrompt --count --bvetoL
##python3 makeplot.py -y $year2 --lep muon --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year2 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year2 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL
##python3 makeplot.py -y $year2 --lep muon --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year2 --lep muon --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year2 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count
##python3 makeplot.py -y $year2 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --bvetoL
##python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count -d WrongSign_$year2 # prova per systs

#################### year3 #################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/*$year3*root 
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year3*
python3 makeplot.py -y $year3 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst
python3 makeplot.py -y $year3 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst
python3 makeplot.py -y $year3 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst
python3 makeplot.py -y $year3 --lep muon --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL --syst noSyst
##python3 makeplot.py -y $year3 --lep muon --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year3 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year3 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL
##python3 makeplot.py -y $year3 --lep muon --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year3 --lep muon --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year3 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year3 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL
