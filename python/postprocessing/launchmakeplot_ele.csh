set LD_PRELOAD=libtcmalloc.so
set folder0 = vUL035
set channel = "ltau" 
reset

#################### year1 #################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2 
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2 
#python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2 

#################### year1bis #################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2 
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2 
#python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2   

#################### year2 #################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
#python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2

#################### year3 #################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/countings/*/*$year*
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --count -v m_o1,DNN_SM_UL035_v2,BDT_SM_UL035_v2
