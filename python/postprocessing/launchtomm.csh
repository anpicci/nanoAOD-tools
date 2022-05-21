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

set dnn_cW_branch_bal = "DNN_cW_UL025_bal"
set dnn_cW_path_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced.h5"
set dnn_cW_scaler_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced.p"
set dnn_cHW_branch_bal = "DNN_cHW_UL025_bal"
set dnn_cHW_path_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cHW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced.h5"
set dnn_cHW_scaler_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cHW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced.p"
set dnn_sm_branch_bal = "DNN_SM_UL025_bal"
set dnn_sm_path_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_model_SM-allBKGs_UL_vUL025_optimization_balancing_redoAN_reduced.h5"
set dnn_sm_scaler_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_SM_UL-allBKGs_vUL025_optimization_balancing_redoAN_reduced.p"

set dnn_cW_branch_nobal = "DNN_cW_UL025_nobal"
set dnn_cW_path_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_noBalancing_redoAN_reduced.h5"
set dnn_cW_scaler_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_noBalancing_redoAN_reduced.p"
set dnn_cHW_branch_nobal = "DNN_cHW_UL025_nobal"
set dnn_cHW_path_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cHW-INT-BSM_UL-allBKGs_vUL025_optimization_noBalancing_redoAN_reduced_full.h5"
set dnn_cHW_scaler_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cHW-INT-BSM_UL-allBKGs_vUL025_optimization_noBalancing_redoAN_reduced_full.p"
set dnn_sm_branch_nobal = "DNN_SM_UL025_nobal"
set dnn_sm_path_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_model_SM-allBKGs_UL_vUL025_optimization_nobalancing_redoAN_reduced.h5"
set dnn_sm_scaler_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_SM_UL-allBKGs_vUL025_optimization_nobalancing_redoAN_reduced.p"


set folder="vUL025"

set year="UL2017"
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_ul,$bdt_cW_allbkg_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_branch,$bdt_cW_allbkg_branch,$bdt_cHW_allbkg_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch #--scalers 
 #python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path_bal,$dnn_cW_path_bal,$dnn_cHW_path_bal --branches $dnn_sm_branch_bal,$dnn_cW_branch_bal,$dnn_cHW_branch_bal --scalers $dnn_sm_scaler_bal,$dnn_cW_scaler_bal,$dnn_cHW_scaler_bal
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path_nobal,$dnn_cW_path_nobal,$dnn_cHW_path_nobal --branches $dnn_sm_branch_nobal,$dnn_cW_branch_nobal,$dnn_cHW_branch_nobal --scalers $dnn_sm_scaler_nobal,$dnn_cW_scaler_nobal,$dnn_cHW_scaler_nobal

set year="UL2018"
##python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers 
##python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_ul,$bdt_cW_allbkg_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_branch,$bdt_cW_allbkg_branch,$bdt_cHW_allbkg_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path_bal,$dnn_cW_path_bal,$dnn_cHW_path_bal --branches $dnn_sm_branch_bal,$dnn_cW_branch_bal,$dnn_cHW_branch_bal --scalers $dnn_sm_scaler_bal,$dnn_cW_scaler_bal,$dnn_cHW_scaler_bal
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path_nobal,$dnn_cW_path_nobal,$dnn_cHW_path_nobal --branches $dnn_sm_branch_nobal,$dnn_cW_branch_nobal,$dnn_cHW_branch_nobal --scalers $dnn_sm_scaler_nobal,$dnn_cW_scaler_nobal,$dnn_cHW_scaler_nobal

set year="UL2016"
##python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers
##python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_ul,$bdt_cW_allbkg_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_branch,$bdt_cW_allbkg_branch,$bdt_cHW_allbkg_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path_bal,$dnn_cW_path_bal,$dnn_cHW_path_bal --branches $dnn_sm_branch_bal,$dnn_cW_branch_bal,$dnn_cHW_branch_bal --scalers $dnn_sm_scaler_bal,$dnn_cW_scaler_bal,$dnn_cHW_scaler_bal
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path_nobal,$dnn_cW_path_nobal,$dnn_cHW_path_nobal --branches $dnn_sm_branch_nobal,$dnn_cW_branch_nobal,$dnn_cHW_branch_nobal --scalers $dnn_sm_scaler_nobal,$dnn_cW_scaler_nobal,$dnn_cHW_scaler_nobal

set year="UL2016APV"
##python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_ul,$bdt_cW_ul,$bdt_cHW_ul --branches $bdt_sm_branch,$bdt_cW_branch,$bdt_cHW_branch #--scalers 
##python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_ul,$bdt_cW_allbkg_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_branch,$bdt_cW_allbkg_branch,$bdt_cHW_allbkg_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $bdt_sm_allbkg_v2_ul,$bdt_cW_allbkg_v2_ul,$bdt_cHW_allbkg_ul --branches $bdt_sm_allbkg_v2_branch,$bdt_cW_allbkg_v2_branch,$bdt_cHW_allbkg_branch #--scalers 
#python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path,$dnn_cW_path,$dnn_cHW_path --branches $dnn_sm_branch,$dnn_cW_branch,$dnn_cHW_branch --scalers $dnn_sm_scaler,$dnn_cW_scaler,$dnn_cHW_scaler
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path_bal,$dnn_cW_path_bal,$dnn_cHW_path_bal --branches $dnn_sm_branch_bal,$dnn_cW_branch_bal,$dnn_cHW_branch_bal --scalers $dnn_sm_scaler_bal,$dnn_cW_scaler_bal,$dnn_cHW_scaler_bal
python3 add_1finalMVA.py -y $year -f $folder --paths $dnn_sm_path_nobal,$dnn_cW_path_nobal,$dnn_cHW_path_nobal --branches $dnn_sm_branch_nobal,$dnn_cW_branch_nobal,$dnn_cHW_branch_nobal --scalers $dnn_sm_scaler_nobal,$dnn_cW_scaler_nobal,$dnn_cHW_scaler_nobal
