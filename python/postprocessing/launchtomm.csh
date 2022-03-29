reset
set bdt_sm_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_SM_UL_vUL008_btagSF.model"
set bdt_sm_branch = "BDT_SM_xgb_UL008_no"
set bdt_cW_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cW-INT-BSM_UL_vUL008_btagSF.model"
set bdt_cW_branch = "BDT_cW_xgb_UL008_no"
set bdt_cHW_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cHW-INT-BSM_UL_vUL008_btagSF.model"
set bdt_cHW_branch = "BDT_cHW_xgb_UL008_no"
set folder="vUL010"

set year="UL2016"
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers -d WJets_$year

set year="UL2016APV"
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers -d WJets_$year

set year="UL2017"
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers -d WJets_$year

set year="UL2018"
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers -d WJets_$year
