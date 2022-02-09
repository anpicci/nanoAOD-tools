set year1 = UL2016APV
set year1bis = UL2016
set year2 = UL2017
set year3 = UL2018
set folder0 = vUL003 #_tagger_DataSplit_MCnoSplit
#set folder1 = v96
#set folder2 = v97
#set folder3 = v98
set channel = 'ltau' # 
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder0/plot/electron/ #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder1/plot/electron/ #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder2/plot/electron/ #countings
#rm -rf /eos/home-a/apiccine/VBS/nosynch/$folder3/plot/electron/ #countings

####### year1 #######################

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
##python3 makeplot.py -y $year1 --lep electron --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
#python3 makeplot.py -y $year1 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1
#python3 makeplot.py -y $year1 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count #-d FakeEle_$year1

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 

####### year1bis #######################

python3 makeplot.py -y $year1bis --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
python3 makeplot.py -y $year1bis --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
python3 makeplot.py -y $year1bis --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
##python3 makeplot.py -y $year1bis --lep electron --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
python3 makeplot.py -y $year1bis --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis
python3 makeplot.py -y $year1bis --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count #-d FakeEle_$year1bis

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 

####### year2 #######################

python3 makeplot.py -y $year2 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year2 --lep electron --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
python3 makeplot.py -y $year2 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
##python3 makeplot.py -y $year2 --lep electron --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
python3 makeplot.py -y $year2 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count 
##python3 makeplot.py -y $year2 --lep electron --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
python3 makeplot.py -y $year2 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count
python3 makeplot.py -y $year2 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet4 --count

#python3 makeplot.py -y $year2 --lep electron --ws -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year2 --lep electron --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year2 --lep electron --sr -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year2 --lep electron --wjets -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year2 --lep electron --ttbar -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year2 --lep electron --qcd -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year2 --lep electron --ws -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year2 --lep electron --bveto -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year2 --lep electron --sr -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year2 --lep electron --wjets -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year2 --lep electron --ttbar -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year2 --lep electron --qcd -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year2 --lep electron --ws -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year2 --lep electron --bveto -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year2 --lep electron --sr -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year2 --lep electron --wjets -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year2 --lep electron --ttbar -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year2 --lep electron --qcd -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count

####### year3 #######################

python3 makeplot.py -y $year3 --lep electron --ws -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count
##python3 makeplot.py -y $year3 --lep electron --bveto -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count
python3 makeplot.py -y $year3 --lep electron --sr -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count
##python3 makeplot.py -y $year3 --lep electron --wjets -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count
python3 makeplot.py -y $year3 --lep electron --ttbar -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count 
##python3 makeplot.py -y $year3 --lep electron --qcd -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count
python3 makeplot.py -y $year3 --lep electron --fakes -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count
python3 makeplot.py -y $year3 --lep electron --dy -f $folder0 -p --ch $channel --wfake incl_vsjet2 --count

#python3 makeplot.py -y $year3 --lep electron --ws -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year3 --lep electron --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year3 --lep electron --sr -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year3 --lep electron --wjets -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year3 --lep electron --ttbar -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year3 --lep electron --qcd -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year3 --lep electron --ws -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year3 --lep electron --bveto -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year3 --lep electron --sr -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year3 --lep electron --wjets -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year3 --lep electron --ttbar -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count
#python3 makeplot.py -y $year3 --lep electron --qcd -f $folder2 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year3 --lep electron --ws -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year3 --lep electron --bveto -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year3 --lep electron --sr -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year3 --lep electron --wjets -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year3 --lep electron --ttbar -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 
#python3 makeplot.py -y $year3 --lep electron --qcd -f $folder3 -p --ch $channel --wfake incl_vsjet2 --count 

#python3 makeplot.py -y $year1 --lep electron --ws -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder1 -p --ch $channel --wfake sep_vsjet2 --count

##################### plot with BDT cuts #############################
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --bdt #--blinded
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --ebdt #--blinded

#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --bdt #--blinded
#python3 makeplot.py -y $year1 --lep electron --bveto -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --ebdt #--blinded

#python3 makeplot.py -y $year1 --lep electron --sr -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --bdt #--blinded
#python3 makeplot.py -y $year1 --lep electron --sr -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --ebdt #--blinded

#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --bdt
#python3 makeplot.py -y $year1 --lep electron --wjets -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --ebdt

#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --bdt 
#python3 makeplot.py -y $year1 --lep electron --ttbar -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --ebdt

#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --bdt 
#python3 makeplot.py -y $year1 --lep electron --qcd -f $folder1 -p --ch $channel --wfake incl_vsjet2 --count --ebdt
