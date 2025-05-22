set LD_PRELOAD=libtcmalloc.so
set folder0 = vUL060_combo
#set folder0 = vUL060
#set folder0 = vUL045
set channel = "ltau" 
reset

#################### year1 #################
#set year = UL2016APV
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --syst noSyst  
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --syst noSyst 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst 
###python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --syst noSyst 

#################### year1bis #################
#set year = UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --syst noSyst 
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --syst noSyst 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst 
##python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --syst noSyst 

set year = UL2016M
python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB --merge 3 -d WmWmJJ_QCD_$year,WmWmJJ_EWK_$year,WpWpJJ_QCD_$year,WpWpJJ_EWK_$year #VBS_SSWW_aTGC_mixed_$year
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB --merge 3 -d WmWmJJ_QCD_$year,WmWmJJ_EWK_$year,WpWpJJ_QCD_$year,WpWpJJ_EWK_$year #VBS_SSWW_aTGC_mixed_$year
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB --merge 3 -d WmWmJJ_QCD_$year,WmWmJJ_EWK_$year,WpWpJJ_QCD_$year,WpWpJJ_EWK_$year #VBS_SSWW_aTGC_mixed_$year
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB --merge 3 -d WmWmJJ_QCD_$year,WmWmJJ_EWK_$year,WpWpJJ_QCD_$year,WpWpJJ_EWK_$year #VBS_SSWW_aTGC_mixed_$year
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB --merge 3 -d WmWmJJ_QCD_$year,WmWmJJ_EWK_$year,WpWpJJ_QCD_$year,WpWpJJ_EWK_$year #VBS_SSWW_aTGC_mixed_$year
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB --merge 3 -d WmWmJJ_QCD_$year,WmWmJJ_EWK_$year,WpWpJJ_QCD_$year,WpWpJJ_EWK_$year #VBS_SSWW_aTGC_mixed_$year
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB --merge 3 -d WmWmJJ_QCD_$year,WmWmJJ_EWK_$year,WpWpJJ_QCD_$year,WpWpJJ_EWK_$year #VBS_SSWW_aTGC_mixed_$year
#python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB --merge 3 -d WmWmJJ_QCD_$year,WmWmJJ_EWK_$year,WpWpJJ_QCD_$year,WpWpJJ_EWK_$year #VBS_SSWW_aTGC_mixed_$year

#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel -v DNN_SM --merge 2
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel -v DNN_SM --merge 2
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel -v DNN_SM --merge 2
#python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel -v DNN_SM --merge 2


set year = ULRunII
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel -v m_o1 -d WrongSign_$year --syst noSyst --merge 11
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel -v DNN_SM --merge 2
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel -v DNN_SM --merge 2
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel -v DNN_SM --merge 2

#python3 makeplot.py -y $year --lep electron --sr -f $folder0 -p --ch $channel -v DNN_SM --merge 2
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel -v DNN_SM --merge 2
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel -v DNN_SM --merge 2
#python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel -v DNN_SM --merge 2




#################### year2 #################
set year = UL2017
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 --ch $channel --syst noSyst -v m_jj -p #--noweight
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 --ch $channel --syst noSyst -v m_jj -p #--noweight

#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel  -v leadjet_eta,subleadjet_eta --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 

#################### year3 #################
set year = UL2018
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 --ch $channel --syst noSyst -v m_jj -p #--noweight
#python3 makeplot.py -y $year --lep electron --sr -f $folder0 --ch $channel --syst noSyst -v m_jj -p #--noweight

#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --tDMcut -d VBS_SSWW_aQGC_$year --flat --syst noSyst
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel  -v leadjet_eta,subleadjet_eta --syst noSyst --test

set year = ULRunII
#python3 makeplot.py -y $year --lep muon -f $folder0 --ch $channel --syst -v m_jj -p --wsdy --syst noSyst #--noweight
#python3 makeplot.py -y $year --lep electron -f $folder0 --ch $channel --syst -v m_jj -p --wsdy --syst noSyst #--noweight
#python3 makeplot.py -y $year --lep muon --srinv -f $folder0 --ch $channel --syst noSyst -v m_jj -p #--noweight
#python3 makeplot.py -y $year --lep electron --srinv -f $folder0 --ch $channel --syst noSyst -v m_jj -p #--noweight
#python3 makeplot_t.py -y $year --lep electron --sr -f $folder0 --ch $channel --syst noSyst -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB -d FakeEle_ULRunII --syst noSyst -p --merge 2
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --syst noSyst -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB -d FakeMu_ULRunII --cons  #--noweight
#python3 makeplot.py -y $year --lep electron --ttbar -f $folder0 -p --ch $channel --syst noSyst -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB -d FakeEle_ULRunII --cons  #--noweight
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB -d FakeMu_ULRunII --cons  #--noweight
#python3 makeplot.py -y $year --lep electron --fakes -f $folder0 -p --ch $channel --syst noSyst -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB -d FakeEle_ULRunII --cons  #--noweight
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB -d FakeMu_ULRunII --cons  #--noweight #--syst QCDScaleUp,QCDScaleDown -v DNN_ --tDMcut #--noweight
#python3 makeplot.py -y $year --lep electron --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst -v DNN_SM_final_1_NOMOREDY_lower_NONOISE_LCB -d FakeEle_ULRunII --cons  #--noweight #--syst QCDScaleUp,QCDScaleDown -v DNN_ --tDMcut #--noweight
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel --syst noSyst -v DNN_ -d VBS_SSWW_aTGC_mixed_$year


#set year = UL2016M
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --syst noSyst  -d FakeMu_$year --syst noSyst 
