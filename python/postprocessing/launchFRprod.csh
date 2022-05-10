reset
set wp = 16
#set wp = 8
echo $wp

set year = 2018
set FOLDER="FR_UL"$year
#python submit_condor_FR_dev.py -f $FOLDER --wpvsJet $wp -d SampleHTFake_UL$year
#rm -rf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp
#python3 PrepareToPlot.py -f FR_UL$year/$wp --fake -y UL$year --ct HT --max 20 #--or 
cd FakeRatio
python3 Calculator.py --inf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp/ --year $year # --nobkg
cd -



set year = 2017
set FOLDER="FR_UL"$year

#python submit_condor_FR_dev.py -f $FOLDER --wpvsJet $wp -d SampleHTFake_UL$year 
#rm -rf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp
#python3 PrepareToPlot.py -f FR_UL$year/$wp --fake -y UL$year --ct HT --max 20 #--or 
cd FakeRatio
python3 Calculator.py --inf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp/ --year $year # --nobkg
cd -




set year = 2016
set FOLDER="FR_UL"$year

#python submit_condor_FR_dev.py -f $FOLDER --wpvsJet $wp -d SampleHTFake_UL$year 
#rm -rf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp
#python3 PrepareToPlot.py -f FR_UL$year/$wp --fake -y UL$year --ct HT --max 20 #--or 
cd FakeRatio
python3 Calculator.py --inf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp/ --year $year # --nobkg
cd -




#set year = 2016APV
#set FOLDER="FR_UL"$year

#python submit_condor_FR_dev.py -f $FOLDER --wpvsJet $wp -d SampleHTFake_UL$year 
#rm -rf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp
#python3 PrepareToPlot.py -f FR_UL$year/$wp --fake -y UL$year --ct HT --max 20 #--or 
cd FakeRatio
python3 Calculator.py --inf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp/ --year $year # --nobkg
cd -
