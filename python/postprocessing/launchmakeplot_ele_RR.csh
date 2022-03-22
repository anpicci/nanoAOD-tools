set year1 = 2016
set year2 = 2017
set year3 = 2018
set folder0 = v008 #_tagger_DataSplit_MCnoSplit
set channel = 'ltau' #
set user = "ttedesch"

######## year1 #######################
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/*$year1*root 
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year1*
python3 makeplot.py -y $year1 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user
python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user
python3 makeplot.py -y $year1 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user
python3 makeplot.py -y $year1 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user
python3 makeplot.py -y $year1 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --syst noSyst --user $user

######## year2 #######################
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/*$year2*root 
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year2*
python3 makeplot.py -y $year2 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
python3 makeplot.py -y $year2 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
python3 makeplot.py -y $year2 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
python3 makeplot.py -y $year2 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
python3 makeplot.py -y $year2 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user

####### year3 #######################
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/*$year3*root 
rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year3*
python3 makeplot.py -y $year3 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
python3 makeplot.py -y $year3 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
python3 makeplot.py -y $year3 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
python3 makeplot.py -y $year3 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user
python3 makeplot.py -y $year3 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --syst noSyst --user $user

