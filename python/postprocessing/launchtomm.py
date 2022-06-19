import os
from ML.MLmodels import *
os.system("reset")

years = [
    "UL2016APV",
    #"UL2016",
    #"UL2017",
    #"UL2018",
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

branches = [
    #bdt_sm_branch_bal,
    #bdt_cW_branch_bal,
    #bdt_cHW_branch_bal,
    #bdt_pol_branch,
    #dnn_sm_branch_bal,
    #dnn_cW_branch_bal_v2,
    #dnn_cHW_branch_bal,
    #dnn_pol_branch,
    "DNN_pol_UL030_v2",
    "BDT_pol_UL030_v2"
]

paths = [
    #bdt_sm_path_bal,
    #bdt_cW_path_bal,
    #bdt_cHW_path_bal,
    #bdt_pol_path,
    #dnn_sm_path_bal,
    #dnn_cW_path_bal_v2,
    #dnn_cHW_path_bal,
    #dnn_pol_path,
    "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/optimized_model_SM-allBKGs_UL_vUL030_polDNN_v2.h5",
    "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/polUL-vUL030_polBDT_v2.model"
]

scalers = [
    #bdt_sm_scaler_bal,
    #bdt_cW_scaler_bal,
    #bdt_cHW_scaler_bal,
    #bdt_pol_scaler,
    #dnn_sm_scaler_bal,
    #dnn_cW_scaler_bal_v2,
    #dnn_cHW_scaler_bal,
    #dnn_pol_scaler,
    "/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/minmaxscaler_SM_UL-allBKGs_vUL030_polDNN_v2.p",
    ""
]

folder="vUL030"

branchstr = ""
pathstr = ""
scalerstr = ""

for idb, branch in enumerate(branches):
    if idb > 0:
        branchstr += ","
        pathstr += ","
        scalerstr += ","
    branchstr += branches[idb]
    pathstr += paths[idb]
    scalerstr += scalers[idb]

for year in years:
    #os.system("python3 add_1finalMVA_test.py -y " + year + " -f " + folder + " --paths " + pathstr + " --branches " + branchstr + " --scalers " + scalerstr + " -d WZ_" + year + " -v TT_" + year + ",WJets_" + year + ",VBS_SSWW_aQGC_" + year)
    os.system("python3 add_1finalMVA_test.py -y " + year + " -f " + folder + " --paths " + pathstr + " --branches " + branchstr + " --scalers " + scalerstr + " -d WZ_" + year + " --ov")
