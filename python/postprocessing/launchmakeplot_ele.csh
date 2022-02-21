set year1 = UL2016APV
set year1bis = UL2016
set year2 = UL2017
set year2 = 2017
#set year3 = UL2018
set year3 = 2018
#set folder0 = vUL001 #_tagger_DataSplit_MCnoSplit
set folder0 = v100
set channel = 'ltau' #

######## year1 #######################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/*$year1*root #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*$year1*
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
#python3 makeplot.py -y $year1 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1#
#python3 makeplot.py -y $year1 --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL #-d FakeEle_$year1

######### year1bis #######################
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/*$year1bis*root #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*$year1bis*
#python3 makeplot.py -y $year1bis --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
#python3 makeplot.py -y $year1bis --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
#python3 makeplot.py -y $year1bis --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1bis
#python3 makeplot.py -y $year1bis --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL #-d FakeEle_$year1bis

######## year2 #######################

#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/*$year2*root #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*$year2*
python3 makeplot.py -y $year2 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year2
python3 makeplot.py -y $year2 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year2
python3 makeplot.py -y $year2 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year2
#python3 makeplot.py -y $year2 --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL -d VBS_SSWW_FT1_0_$year2
##python3 makeplot.py -y $year2 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL -d VBS_SSWW_FT1_0_$year2
python3 makeplot.py -y $year2 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year2
##python3 makeplot.py -y $year2 --lep electron --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year2
##python3 makeplot.py -y $year2 --lep electron --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year2
##python3 makeplot.py -y $year2 --lep electron --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year2
##python3 makeplot.py -y $year2 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL -d VBS_SSWW_FT1_0_$year2
python3 makeplot.py -y $year2 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year2

####### year3 #######################

#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/*$year3*root #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*$year3*
python3 makeplot.py -y $year3 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year3
python3 makeplot.py -y $year3 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year3
python3 makeplot.py -y $year3 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year3
#python3 makeplot.py -y $year3 --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL -d VBS_SSWW_FT1_0_$year3
python3 makeplot.py -y $year3 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year3
##python3 makeplot.py -y $year3 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL -d VBS_SSWW_FT1_0_$year3
##python3 makeplot.py -y $year3 --lep electron --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count -d VBS_SSWW_FT1_0_$year3
##python3 makeplot.py -y $year3 --lep electron --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count -d VBS_SSWW_FT1_0_$year3
##python3 makeplot.py -y $year3 --lep electron --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count -d VBS_SSWW_FT1_0_$year3
python3 makeplot.py -y $year3 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_FT1_0_$year3
##python3 makeplot.py -y $year3 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL -d VBS_SSWW_FT1_0_$year3
