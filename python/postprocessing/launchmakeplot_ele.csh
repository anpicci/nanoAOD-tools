set folder0 = vUL035 #_tagger_DataSplit_MCnoSplit
#set folder0 = v100
set channel = 'ltau' #
reset

######## year1 #######################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 

######### year1bis #######################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year\_*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"  

######## year2 #######################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"  

####### year3 #######################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --count -v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"  
