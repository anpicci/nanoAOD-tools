set LD_PRELOAD=libtcmalloc.so
set folder0 = vUL040
set channel = "ltau" 
reset

#################### year1 #################
set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year 
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
##python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year

#################### year1bis #################
set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
##python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year

set year = UL2016M
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year

#################### year2 #################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
##python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year

#################### year3 #################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
##python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year

set year = ULRunII
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d VBS_SSWW_aQGC_$year
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --count --tDMcut -v m_o1 -d FakeMuPromptTau_$year #,PromptMuFakeTau_$year,FakeMuFakeTau_$year


#set year = UL2016M
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel -v m_o1 --tDMcut -d FakeMu_$year --syst noSyst -d VBS_SSWW_aQGC_$year
