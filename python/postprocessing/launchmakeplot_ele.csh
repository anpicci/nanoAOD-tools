set folder0 = vUL030 #_tagger_DataSplit_MCnoSplit
#set folder0 = v100
set channel = 'ltau' #
reset

######## year1 #######################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year --bvetoL

######### year1bis #######################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year\_*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count  -d Triboson_$year
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count  -d Triboson_$year
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count  -d Triboson_$year
python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL  -d Triboson_$year

######## year2 #######################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count  -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count  -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --bvetoL  -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year

####### year3 #######################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
#python3 makeplot_tt.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot_tt.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot_tt.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
#python3 makeplot_tt.py -y $year --lep electron --wsdy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count --bvetoL  -d VBS_SSWW_LL_SM_$year,VBS_SSWW_TL_SM_$year,VBS_SSWW_TT_SM_$year
