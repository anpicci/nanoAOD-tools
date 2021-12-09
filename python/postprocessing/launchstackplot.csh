set LD_PRELOAD=libtcmalloc.so
set year = 2017
set folder = v100 #_xg_sample_29_10_21_no14features_depth2_retrainedBDT

#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder/stack_vsjet2/ #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder/stack_vsjet4/ #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder/stack/* #countings

set LD_PRELOAD=libtcmalloc.so

###### electron #######
#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake incl_vsjet2 #--cut "abs(lepton_eta)<2.&&abs(tau_eta)<2.&&tau_mass<1.5" 
python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s  --wfake incl_vsjet2 
#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake sep_vsjet2 

#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake sep_vsjet2 --bdt #--blinded
#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake incl_vsjet2 --bdt #--blinded

#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake sep_vsjet2 --ebdt #--blinded
#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake incl_vsjet2 --ebdt #--blinded

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep electron --ws -f $folder -s  --wfake incl_vsjet2 
#python makeplot.py -y $year --horn --lep electron --ws -f $folder -s --wfake sep_vsjet2 

#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake sep_vsjet2 --bdt #--blinded
#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake incl_vsjet2 --bdt #--blinded

#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake sep_vsjet2 --ebdt #--blinded
#python makeplot.py -y $year --horn --lep electron --bveto -f $folder -s --wfake incl_vsjet2 --ebdt #--blinded

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep electron --sr -f $folder -s  --wfake incl_vsjet2 
#python makeplot.py -y $year --horn --lep electron --sr -f $folder -s --wfake sep_vsjet2 

#python makeplot.py -y $year --horn --lep electron --sr -f $folder -s --wfake sep_vsjet2 --bdt #--blinded
#python makeplot.py -y $year --horn --lep electron --sr -f $folder -s --wfake incl_vsjet2 --bdt #--blinded

#python makeplot.py -y $year --horn --lep electron --sr -f $folder -s --wfake sep_vsjet2 --ebdt #--blinded
#python makeplot.py -y $year --horn --lep electron --sr -f $folder -s --wfake incl_vsjet2 --ebdt #--blinded

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep electron --wjets -f $folder -s  --wfake incl_vsjet2
#python makeplot.py -y $year --horn --lep electron --wjets -f $folder -s --wfake sep_vsjet2

#python makeplot.py -y $year --horn --lep electron --wjets -f $folder -s --wfake incl_vsjet2 --bdt 
#python makeplot.py -y $year --horn --lep electron --wjets -f $folder -s --wfake sep_vsjet2 --bdt 

#python makeplot.py -y $year --horn --lep electron --wjets -f $folder -s --wfake incl_vsjet2 --ebdt 
#python makeplot.py -y $year --horn --lep electron --wjets -f $folder -s --wfake sep_vsjet2 --ebdt 

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep electron --ttbar -f $folder -s  --wfake incl_vsjet2
#python makeplot.py -y $year --horn --lep electron --ttbar -f $folder -s --wfake sep_vsjet2

#python makeplot.py -y $year --horn --lep electron --ttbar -f $folder -s --wfake incl_vsjet2 --bdt 
#python makeplot.py -y $year --horn --lep electron --ttbar -f $folder -s --wfake sep_vsjet2 --bdt 

#python makeplot.py -y $year --horn --lep electron --ttbar -f $folder -s --wfake incl_vsjet2 --ebdt 
#python makeplot.py -y $year --horn --lep electron --ttbar -f $folder -s --wfake sep_vsjet2 --ebdt 

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s  --wfake incl_vsjet2
#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake sep_vsjet2

#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake incl_vsjet2 --bdt 
#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake sep_vsjet2 --bdt 

#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake incl_vsjet2 --ebdt 
#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake sep_vsjet2 --ebdt 

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep electron --fakes -f $folder -s  --wfake incl_vsjet2
#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake sep_vsjet2

#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake incl_vsjet2 --bdt 
#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake sep_vsjet2 --bdt 

#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake incl_vsjet2 --ebdt 
#python makeplot.py -y $year --horn --lep electron --qcd -f $folder -s --wfake sep_vsjet2 --ebdt 

set LD_PRELOAD=libtcmalloc.so

###### muon #######
python makeplot.py -y $year --horn --lep muon --bveto -f $folder -s --wfake incl_vsjet4 #--blinded
#python makeplot.py -y $year --horn --lep muon --bveto -f $folder -s --wfake sep_vsjet4 #--blinded

#python makeplot.py -y $year --horn --lep muon --bveto -f $folder -s --wfake incl_vsjet4 --bdt #--blinded
#python makeplot.py -y $year --horn --lep muon --bveto -f $folder -s --wfake sep_vsjet4 --bdt #--blinded

#python makeplot.py -y $year --horn --lep muon --bveto -f $folder -s --wfake incl_vsjet4 --mubdt #--blinded
#python makeplot.py -y $year --horn --lep muon --bveto -f $folder -s --wfake sep_vsjet4 --mubdt #--blinded

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep muon --ws -f $folder -s --wfake incl_vsjet4 #--blinded
#python makeplot.py -y $year --horn --lep muon --ws -f $folder -s --wfake sep_vsjet4 #--blinded

#python makeplot.py -y $year --horn --lep muon --ws -f $folder -s --wfake incl_vsjet4 --bdt #--blinded
#python makeplot.py -y $year --horn --lep muon --ws -f $folder -s --wfake sep_vsjet4 --bdt #--blinded

#python makeplot.py -y $year --horn --lep muon --ws -f $folder -s --wfake incl_vsjet4 --mubdt #--blinded
#python makeplot.py -y $year --horn --lep muon --ws -f $folder -s --wfake sep_vsjet4 --mubdt #--blinded

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep muon --sr -f $folder -s --wfake incl_vsjet4 #--blinded
#python makeplot.py -y $year --horn --lep muon --sr -f $folder -s --wfake sep_vsjet4 #--blinded

#python makeplot.py -y $year --horn --lep muon --sr -f $folder -s --wfake incl_vsjet4 --bdt #--blinded
#python makeplot.py -y $year --horn --lep muon --sr -f $folder -s --wfake sep_vsjet4 --bdt #--blinded

#python makeplot.py -y $year --horn --lep muon --sr -f $folder -s --wfake incl_vsjet4 --mubdt #--blinded
#python makeplot.py -y $year --horn --lep muon --sr -f $folder -s --wfake sep_vsjet4 --mubdt #--blinded

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep muon --wjets -f $folder -s --wfake incl_vsjet4
#python makeplot.py -y $year --horn --lep muon --wjets -f $folder -s --wfake sep_vsjet4

#python makeplot.py -y $year --horn --lep muon --wjets -f $folder -s --wfake incl_vsjet4 --bdt
#python makeplot.py -y $year --horn --lep muon --wjets -f $folder -s --wfake sep_vsjet4 --bdt 

#python makeplot.py -y $year --horn --lep muon --wjets -f $folder -s --wfake incl_vsjet4 --mubdt
#python makeplot.py -y $year --horn --lep muon --wjets -f $folder -s --wfake sep_vsjet4 --mubdt

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep muon --ttbar -f $folder -s --wfake incl_vsjet4
#python makeplot.py -y $year --horn --lep muon --ttbar -f $folder -s --wfake sep_vsjet4

#python makeplot.py -y $year --horn --lep muon --ttbar -f $folder -s --wfake incl_vsjet4 --bdt
#python makeplot.py -y $year --horn --lep muon --ttbar -f $folder -s --wfake sep_vsjet4 --bdt 

#python makeplot.py -y $year --horn --lep muon --ttbar -f $folder -s --wfake incl_vsjet4 --mubdt
#python makeplot.py -y $year --horn --lep muon --ttbar -f $folder -s --wfake sep_vsjet4 --mubdt

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake incl_vsjet4
#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake sep_vsjet4

#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake incl_vsjet4 --bdt
#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake sep_vsjet4 --bdt 

#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake incl_vsjet4 --mubdt
#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake sep_vsjet4 --mubdt

set LD_PRELOAD=libtcmalloc.so

python makeplot.py -y $year --horn --lep muon --fakes -f $folder -s --wfake incl_vsjet4
#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake sep_vsjet4

#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake incl_vsjet4 --bdt
#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake sep_vsjet4 --bdt 

#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake incl_vsjet4 --mubdt
#python makeplot.py -y $year --horn --lep muon --qcd -f $folder -s --wfake sep_vsjet4 --mubdt

set LD_PRELOAD=libtcmalloc.so


############## emu  #################

set channel = 'emu'

##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake incl_vsjet2 #--blinded
##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake sep_vsjet2 #--blinded

##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake incl_vsjet2 --bdt #--blinded
##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake sep_vsjet2 --bdt #--blinded

##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake incl_vsjet2 --mubdt #--blinded
##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake sep_vsjet2 --mubdt #--blinded

set LD_PRELOAD=libtcmalloc.so

##python makeplot.py -y $year --horn --lep incl --ws -f $folder -s --ch $channel --wfake incl_vsjet2 #--blinded
##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake sep_vsjet2 #--blinded

##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake incl_vsjet2 --bdt #--blinded
##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake sep_vsjet2 --bdt #--blinded

##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake incl_vsjet2 --mubdt #--blinded
##python makeplot.py -y $year --horn --lep incl --bveto -f $folder -s --ch $channel --wfake sep_vsjet2 --mubdt #--blinded

set LD_PRELOAD=libtcmalloc.so

##python makeplot.py -y $year --horn --lep incl --sr -f $folder -s --ch $channel --wfake incl_vsjet2 #--blinded
##python makeplot.py -y $year --horn --lep incl --sr -f $folder -s --ch $channel --wfake sep_vsjet2 #--blinded

##python makeplot.py -y $year --horn --lep incl --sr -f $folder -s --ch $channel --wfake incl_vsjet2 --bdt #--blinded
##python makeplot.py -y $year --horn --lep incl --sr -f $folder -s --ch $channel --wfake sep_vsjet2 --bdt #--blinded

##python makeplot.py -y $year --horn --lep incl --sr -f $folder -s --ch $channel --wfake incl_vsjet2 --mubdt #--blinded
##python makeplot.py -y $year --horn --lep incl --sr -f $folder -s --ch $channel --wfake sep_vsjet2 --mubdt #--blinded

set LD_PRELOAD=libtcmalloc.so

##python makeplot.py -y $year --horn --lep incl --wjets -f $folder -s --ch $channel --wfake incl_vsjet2
##python makeplot.py -y $year --horn --lep incl --wjets -f $folder -s --ch $channel --wfake sep_vsjet2

##python makeplot.py -y $year --horn --lep incl --wjets -f $folder -s --ch $channel --wfake incl_vsjet2 --bdt
##python makeplot.py -y $year --horn --lep incl --wjets -f $folder -s --ch $channel --wfake sep_vsjet2 --bdt 

##python makeplot.py -y $year --horn --lep incl --wjets -f $folder -s --ch $channel --wfake incl_vsjet2 --mubdt
##python makeplot.py -y $year --horn --lep incl --wjets -f $folder -s --ch $channel --wfake sep_vsjet2 --mubdt

set LD_PRELOAD=libtcmalloc.so

##python makeplot.py -y $year --horn --lep incl --ttbar -f $folder -s --ch $channel --wfake incl_vsjet2
##python makeplot.py -y $year --horn --lep incl --ttbar -f $folder -s --ch $channel --wfake sep_vsjet2

##python makeplot.py -y $year --horn --lep incl --ttbar -f $folder -s --ch $channel --wfake incl_vsjet2 --bdt
##python makeplot.py -y $year --horn --lep incl --ttbar -f $folder -s --ch $channel --wfake sep_vsjet2 --bdt 

##python makeplot.py -y $year --horn --lep incl --ttbar -f $folder -s --ch $channel --wfake incl_vsjet2 --mubdt
##python makeplot.py -y $year --horn --lep incl --ttbar -f $folder -s --ch $channel --wfake sep_vsjet2 --mubdt

set LD_PRELOAD=libtcmalloc.so

##python makeplot.py -y $year --horn --lep incl --qcd -f $folder -s --ch $channel --wfake incl_vsjet2
##python makeplot.py -y $year --horn --lep incl --qcd -f $folder -s --ch $channel --wfake sep_vsjet2

##python makeplot.py -y $year --horn --lep incl --qcd -f $folder -s --ch $channel --wfake incl_vsjet2 --bdt
##python makeplot.py -y $year --horn --lep incl --qcd -f $folder -s --ch $channel --wfake sep_vsjet2 --bdt 

##python makeplot.py -y $year --horn --lep incl --qcd -f $folder -s --ch $channel --wfake incl_vsjet2 --mubdt
##python  makeplot.py -y $year --horn --lep incl --qcd -f $folder -s --ch $channel --wfake sep_vsjet2 --mubdt

set LD_PRELOAD=libtcmalloc.so

