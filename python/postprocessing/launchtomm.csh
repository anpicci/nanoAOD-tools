reset
set bdt_sm_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_SM_UL_vUL008_btagSF.model"
set bdt_sm_branch = "BDT_SM_xgb_UL008_no"
set bdt_cW_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cW-INT-BSM_UL_vUL008_btagSF.model"
set bdt_cW_branch = "BDT_cW_xgb_UL008_no"
set bdt_cHW_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cHW-INT-BSM_UL_vUL008_btagSF.model"
set bdt_cHW_branch = "BDT_cHW_xgb_UL008_no"
set bdt_sm_allbkg_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_xgb_SM_UL-allBKGs_vUL010_btagSF.model"
set bdt_sm_allbkg_branch = "BDT_SM_xgb_UL010_allBKG"
set bdt_sm_allbkg_v2_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/really_optimized_xgb_SM_UL-allBKGs_vUL010_btagSF.model"
set bdt_sm_allbkg_v2_branch = "BDT_SM_xgb_UL010_allBKG_v2"
set bdt_cW_allbkg_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cW-INT-BSM_UL-allBKGs_vUL010_btagSF.model"
set bdt_cW_allbkg_branch = "BDT_cW_xgb_UL010_allBKG"
set bdt_cW_allbkg_v2_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_xgb_dim6-cW-INT-BSM_UL_vUL010_btagSF.model"
set bdt_cW_allbkg_v2_branch = "BDT_cW_xgb_UL010_allBKG_v2"
set bdt_cHW_allbkg_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cHW-INT-BSM_UL-allBKGs_vUL010_btagSF.model"
set bdt_cHW_allbkg_branch = "BDT_cHW_xgb_UL010_allBKG"

set dnn_cW_branch = "DNN_cW_UL010_allBKG"
set dnn_cW_path = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cW-INT-BSM_UL-allBKGs_vUL010.h5"
set dnn_cW_scaler = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cW-INT-BSM_UL-allBKGs_vUL010.p"
set dnn_cHW_branch = "DNN_cHW_UL010_allBKG"
set dnn_cHW_path = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cHW-INT-BSM_UL-allBKGs_vUL010.h5"
set dnn_cHW_scaler = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cHW-INT-BSM_UL-allBKGs_vUL010.p"
set dnn_sm_branch = "DNN_SM_UL010_allBKG"
set dnn_sm_path = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_model_SM-allBKGs_UL_vUL010.h5"
set dnn_sm_scaler = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_SM_UL-allBKGs_vUL010.p"


set folder="vUL025"

set year="UL2017"
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_ul,$bdt_cW_allbkg_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_branch,$bdt_cW_allbkg_branch,$bdt_cHW_allbkg_branch #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch -d TTTo2L2Nu_$year #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler -d TTTo2L2Nu_$year 
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch -d TT_$year #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler -d TT_$year 

set year="UL2018"
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_ul,$bdt_cW_allbkg_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_branch,$bdt_cW_allbkg_branch,$bdt_cHW_allbkg_branch #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch -d TTTo2L2Nu_$year #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler -d TTTo2L2Nu_$year 
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch -d TT_$year #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler -d TT_$year 

set year="UL2016"
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_ul,$bdt_cW_allbkg_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_branch,$bdt_cW_allbkg_branch,$bdt_cHW_allbkg_branch #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch -d TTTo2L2Nu_$year  #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler -d TTTo2L2Nu_$year 
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch -d TT_$year  #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler -d TT_$year 

set year="UL2016APV"
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_ul,$bdt_cW_allbkg_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_branch,$bdt_cW_allbkg_branch,$bdt_cHW_allbkg_branch #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch -d TTTo2L2Nu_$year  #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler -d TTTo2L2Nu_$year 
python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch -d TT_$year  #--scalers 
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler -d TT_$year 

