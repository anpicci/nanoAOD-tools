set folder0 = vUL020 #_tagger_DataSplit_MCnoSplit
#set folder0 = v100
set channel = 'ltau' #
reset

######## year1 #######################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #--syst noSyst 
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-syst noSyst -d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #--syst noSyst -d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL #--syst noSyst -d DYJetsToLL_FxFx_$year

######### year1bis #######################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year\_*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count -d #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL #--syst noSyst #-d DYJetsToLL_FxFx_$year

######## year2 #######################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL #--syst noSyst #-d DYJetsToLL_FxFx_$year

####### year3 #######################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #--syst noSyst #-d DYJetsToLL_FxFx_$year
python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL #--syst noSyst #-d DYJetsToLL_FxFx_$year
