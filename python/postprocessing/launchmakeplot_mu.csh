set LD_PRELOAD=libtcmalloc.so
set folder0 = vUL035
set channel = "ltau" 
reset

#################### year1 #################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count #-v m_o1,m_1T
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count #-v m_o1,m_1T  #--cut "DNN_pol_UL030_v2>0.3269" 

#################### year1bis #################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"   

#################### year2 #################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269" 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"  

#################### year3 #################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"
python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count #-v m_o1,m_1T #--cut "DNN_pol_UL030_v2>0.3269"  
