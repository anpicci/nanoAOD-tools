set LD_PRELOAD=libtcmalloc.so
set folder0 = vUL050
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
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year -v m_jj --count --syst noSyst --noweight
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel  -v leadjet_eta,subleadjet_eta --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 

#################### year2 #################
set year = UL2017
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year\_*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel  -v leadjet_eta,subleadjet_eta --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 

#################### year3 #################
set year = UL2018
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/countings/*/*$year*
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --tDMcut -v m_o1 -d WpWpJJ_EWK_$year,FakeMu_$year --flat --syst noSyst
#python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel
#python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst --test -d WrongSign_$year,DYJetsToLL_FxFx_$year,TTTo2L2Nu_$year,FakeMu_$year,DataMu_$year 
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel  -v leadjet_eta,subleadjet_eta --syst noSyst --test

set year = ULRunII
python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --syst noSyst --tDMcut --flat --count -v DNN_SM_final_1 #--noweight
python3 makeplot.py -y $year --lep muon --ttbar -f $folder0 -p --ch $channel --syst noSyst --tDMcut --flat --count -v DNN_SM_final_1 #--noweight
python3 makeplot.py -y $year --lep muon --fakes -f $folder0 -p --ch $channel --syst noSyst --tDMcut --flat --count -v DNN_SM_final_1 #--noweight
python3 makeplot.py -y $year --lep muon --wsdy --bvetoL -f $folder0 -p --ch $channel --syst noSyst --tDMcut --flat --count -v DNN_SM_final_1 #--noweight
#python3 makeplot.py -y $year --lep muon --presel -f $folder0 -p --ch $channel  -v leadjet_eta,subleadjet_eta --syst noSyst


#set year = UL2016M
#python3 makeplot.py -y $year --lep muon --sr -f $folder0 -p --ch $channel --syst noSyst  -d FakeMu_$year --syst noSyst 
