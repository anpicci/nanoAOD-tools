set year = 2018
set FOLDER="FR_UL"$year
set wp = 8
reset
#python submit_condor_FR_dev.py -f $FOLDER --wpvsJet 2 --nodata -d SampleHTFake_UL$year
#python submit_condor_FR_dev.py -f $FOLDER --wpvsJet 4 -d WJetsHT1200to2500_UL2016
#rm -rf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp

python submit_condor_FR_dev.py -d SampleHTFake_UL$year -f $FOLDER --wpvsJet $wp

#python3 PrepareToPlot.py -f FR_UL$year/2 --fake -y UL$year --ct HT
#python3 PrepareToPlot.py -f FR_UL$year/4 --fake -y UL$year --ct HT --or
#python3 PrepareToPlot.py -f FR_UL$year/8 --fake -y UL$year --ct HT --or 

#cd FakeRatio
#python3 Calculator.py --inf /eos/home-a/apiccine/VBS/nosynch/FR_UL$year/$wp/ --year $year # --nobkg
#cd -
