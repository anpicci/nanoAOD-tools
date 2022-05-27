import os
os.system("reset")
bdt_sm_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_SM_UL_vUL008_btagSF.model"
bdt_sm_branch = "BDT_SM_xgb_UL008_no"
bdt_cW_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cW-INT-BSM_UL_vUL008_btagSF.model"
bdt_cW_branch = "BDT_cW_xgb_UL008_no"
bdt_cHW_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cHW-INT-BSM_UL_vUL008_btagSF.model"
bdt_cHW_branch = "BDT_cHW_xgb_UL008_no"
bdt_sm_allbkg_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_xgb_SM_UL-allBKGs_vUL010_btagSF.model"
bdt_sm_allbkg_branch = "BDT_SM_xgb_UL010_allBKG"
bdt_sm_allbkg_v2_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/really_optimized_xgb_SM_UL-allBKGs_vUL010_btagSF.model"
bdt_sm_allbkg_v2_branch = "BDT_SM_xgb_UL010_allBKG_v2"
bdt_cW_allbkg_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cW-INT-BSM_UL-allBKGs_vUL010_btagSF.model"
bdt_cW_allbkg_branch = "BDT_cW_xgb_UL010_allBKG"
bdt_cW_allbkg_v2_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_xgb_dim6-cW-INT-BSM_UL_vUL010_btagSF.model"
bdt_cW_allbkg_v2_branch = "BDT_cW_xgb_UL010_allBKG_v2"
bdt_cHW_allbkg_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cHW-INT-BSM_UL-allBKGs_vUL010_btagSF.model"
bdt_cHW_allbkg_branch = "BDT_cHW_xgb_UL010_allBKG"

dnn_cW_branch = "DNN_cW_UL010_allBKG"
dnn_cW_path = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cW-INT-BSM_UL-allBKGs_vUL010.h5"
dnn_cW_scaler = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cW-INT-BSM_UL-allBKGs_vUL010.p"
dnn_cHW_branch = "DNN_cHW_UL010_allBKG"
dnn_cHW_path = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cHW-INT-BSM_UL-allBKGs_vUL010.h5"
dnn_cHW_scaler = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cHW-INT-BSM_UL-allBKGs_vUL010.p"
dnn_sm_branch = "DNN_SM_UL010_allBKG"
dnn_sm_path = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_model_SM-allBKGs_UL_vUL010.h5"
dnn_sm_scaler = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_SM_UL-allBKGs_vUL010.p"

dnn_cW_branch_bal = "DNN_cW_UL025_bal"
dnn_cW_path_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced.h5"
dnn_cW_scaler_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced.p"
dnn_cHW_branch_bal = "DNN_cHW_UL025_bal"
dnn_cHW_path_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cHW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced.h5"
dnn_cHW_scaler_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cHW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced.p"
dnn_sm_branch_bal = "DNN_SM_UL025_bal"
dnn_sm_path_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_model_SM-allBKGs_UL_vUL025_optimization_balancing_redoAN_reduced.h5"
dnn_sm_scaler_bal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_SM_UL-allBKGs_vUL025_optimization_balancing_redoAN_reduced.p"

dnn_cW_branch_nobal = "DNN_cW_UL025_nobal"
dnn_cW_path_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_noBalancing_redoAN_reduced.h5"
dnn_cW_scaler_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_noBalancing_redoAN_reduced.p"
dnn_cHW_branch_nobal = "DNN_cHW_UL025_nobal"
dnn_cHW_path_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cHW-INT-BSM_UL-allBKGs_vUL025_optimization_noBalancing_redoAN_reduced_full.h5"
dnn_cHW_scaler_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cHW-INT-BSM_UL-allBKGs_vUL025_optimization_noBalancing_redoAN_reduced_full.p"
dnn_sm_branch_nobal = "DNN_SM_UL025_nobal"
dnn_sm_path_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_model_SM-allBKGs_UL_vUL025_optimization_nobalancing_redoAN_reduced.h5"
dnn_sm_scaler_nobal = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_SM_UL-allBKGs_vUL025_optimization_nobalancing_redoAN_reduced.p"

dnn_cW_branch_bal_v2 = "DNN_cW_UL025_bal_v2"
dnn_cW_path_bal_v2 = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_dnn_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced_loss.h5"
dnn_cW_scaler_bal_v2 = "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_dim6-cW-INT-BSM_UL-allBKGs_vUL025_optimization_Balancing_redoAN_reduced_loss.p"

years = [
    #"UL2016APV",
    #"UL2016",
    #"UL2017",
    "UL2018",
]

scenarios = [
    "nominal",
    "jesUp",
    "jesDown",
    "jerUp",
    "jerDown",
    "TESUp",
    "TESDown",
    "FESUp",
    "FESDown",
]

folder="vUL030"

for year in years:
    for scenario in scenarios:
        os.system("python3 add_1finalMVA_chunck.py -y " + year + " -f " + folder + " --paths " + dnn_cW_path_bal_v2 + " --branches " + dnn_cW_branch_bal_v2 + " --scalers " + dnn_cW_scaler_bal_v2 + " -d TTTo2L2Nu_" + year + " -s " + scenario)
        #os.system("python3 add_1finalMVA_chunck.py -y " + year + " -f " + folder + " --paths " + dnn_sm_path_nobal + "," + dnn_cW_path_nobal + "," + dnn_cHW_path_nobal + " --branches " + dnn_sm_branch_nobal + "," + dnn_cW_branch_nobal + "," + dnn_cHW_branch_nobal + " --scalers " + dnn_sm_scaler_nobal + "," + dnn_cW_scaler_nobal + "," + dnn_cHW_scaler_nobal)# + " -d TTTo2L2Nu_" + year + " -s " + scenario)
        break
