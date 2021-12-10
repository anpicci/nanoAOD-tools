#set LD_PRELOAD=libtcmalloc.so
set year1 = 2017
set year2 = 2018
set folder0 = v100 #_tagger_DataSplit_MCnoSplit
#set folder1 = v96
#set folder2 = v97
#set folder3 = v98
set channel = "ltau" 
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/muon/ #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder1/plot/muon/ #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder2/plot/muon/ #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder3/plot/muon/ #countings

python3 makeplot.py -y $year1 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --horn
python3 makeplot.py -y $year1 --lep muon --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --horn
python3 makeplot.py -y $year1 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --horn
python3 makeplot.py -y $year1 --lep muon --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --horn
python3 makeplot.py -y $year1 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --horn
python3 makeplot.py -y $year1 --lep muon --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --horn
python3 makeplot.py -y $year1 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count --horn
python3 makeplot.py -y $year1 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count --horn

#python3 makeplot.py -y $year1 --lep muon --sr -f $folder1 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --ws -f $folder1 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --wjets -f $folder1 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --ttbar -f $folder1 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --qcd -f $folder1 -p --ch $channel --wfake incl_vsjet4  --count

#python3 makeplot.py -y $year1 --lep muon --sr -f $folder2 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --bveto -f $folder2 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --ws -f $folder2 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --wjets -f $folder2 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --ttbar -f $folder2 -p --ch $channel --wfake incl_vsjet4  --count
#python3 makeplot.py -y $year1 --lep muon --qcd -f $folder2 -p --ch $channel --wfake incl_vsjet4  --count

#python3 makeplot.py -y $year1 --lep muon --sr -f $folder3 -p --ch $channel --wfake incl_vsjet4  --count 
#python3 makeplot.py -y $year1 --lep muon --bveto -f $folder3 -p --ch $channel --wfake incl_vsjet4  --count 
#python3 makeplot.py -y $year1 --lep muon --ws -f $folder3 -p --ch $channel --wfake incl_vsjet4  --count 
#python3 makeplot.py -y $year1 --lep muon --wjets -f $folder3 -p --ch $channel --wfake incl_vsjet4  --count 
#python3 makeplot.py -y $year1 --lep muon --ttbar -f $folder3 -p --ch $channel --wfake incl_vsjet4  --count 
#python3 makeplot.py -y $year1 --lep muon --qcd -f $folder3 -p --ch $channel --wfake incl_vsjet4  --count 


#################### 2018 #################
#python3 makeplot.py -y $year2 --lep muon --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count 
#python3 makeplot.py -y $year2 --lep muon --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4  --count 

#python3 makeplot.py -y $year2 --lep muon --sr -f $folder1 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --ws -f $folder1 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --wjets -f $folder1 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder1 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --qcd -f $folder1 -p --ch $channel --wfake incl_vsjet4 --count

#python3 makeplot.py -y $year2 --lep muon --sr -f $folder2 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --bveto -f $folder2 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --ws -f $folder2 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --wjets -f $folder2 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder2 -p --ch $channel --wfake incl_vsjet4 --count
#python3 makeplot.py -y $year2 --lep muon --qcd -f $folder2 -p --ch $channel --wfake incl_vsjet4 --count

#python3 makeplot.py -y $year2 --lep muon --sr -f $folder3 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year2 --lep muon --bveto -f $folder3 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year2 --lep muon --ws -f $folder3 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year2 --lep muon --wjets -f $folder3 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder3 -p --ch $channel --wfake incl_vsjet4 --count 
#python3 makeplot.py -y $year2 --lep muon --qcd -f $folder3 -p --ch $channel --wfake incl_vsjet4 --count 

#################### plot with BDT cuts ########################
#python3 makeplot.py -y $year2 --lep muon --bveto -f $folder -p --ch $channel --wfake incl_vsjet4 --count --bdt #--blinded
#python3 makeplot.py -y $year2 --lep muon --bveto -f $folder -p --ch $channel --wfake incl_vsjet4 --count --mubdt #--blinded

#python3 makeplot.py -y $year2 --lep muon --bveto -f $folder -p --ch $channel --wfake incl_vsjet4 --count --bdt #--blinded
#python3 makeplot.py -y $year2 --lep muon --bveto -f $folder -p --ch $channel --wfake incl_vsjet4 --count --mubdt #--blinded

#python3 makeplot.py -y $year2 --lep muon --sr -f $folder -p --ch $channel --wfake incl_vsjet4 --count --bdt #--blinded
#python3 makeplot.py -y $year2 --lep muon --sr -f $folder -p --ch $channel --wfake incl_vsjet4 --count --mubdt #--blinded

#python3 makeplot.py -y $year2 --lep muon --wjets -f $folder -p --ch $channel --wfake incl_vsjet4 --count --bdt
#python3 makeplot.py -y $year2 --lep muon --wjets -f $folder -p --ch $channel --wfake incl_vsjet4 --count --mubdt

#python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder -p --ch $channel --wfake incl_vsjet4 --count --bdt 
#python3 makeplot.py -y $year2 --lep muon --ttbar -f $folder -p --ch $channel --wfake incl_vsjet4 --count --mubdt

#python3 makeplot.py -y $year2 --lep muon --qcd -f $folder -p --ch $channel --wfake incl_vsjet4 --count --bdt 
#python3 makeplot.py -y $year2 --lep muon --qcd -f $folder -p --ch $channel --wfake incl_vsjet4 --count --mubdt
