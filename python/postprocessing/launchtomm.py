import os
from ML.MLmodels import *
os.system("reset")

years = [
    "UL2016APV",
    "UL2016",
    "UL2017",
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

branches = [
    bdt_sm_branch_bal,
    bdt_cW_branch_bal,
    bdt_cHW_branch_bal,
    bdt_pol_branch,
    dnn_sm_branch_bal,
    dnn_cW_branch_bal_v2,
    dnn_cHW_branch_bal,
    dnn_pol_branch,
]

paths = [
    bdt_sm_path_bal,
    bdt_cW_path_bal,
    bdt_cHW_path_bal,
    bdt_pol_path,
    dnn_sm_path_bal,
    dnn_cW_path_bal_v2,
    dnn_cHW_path_bal,
    dnn_pol_path,
]

scalers = [
    bdt_sm_scaler_bal,
    bdt_cW_scaler_bal,
    bdt_cHW_scaler_bal,
    bdt_pol_scaler,
    dnn_sm_scaler_bal,
    dnn_cW_scaler_bal_v2,
    dnn_cHW_scaler_bal,
    dnn_pol_scaler,
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
    os.system("python3 add_1finalMVA_test.py -y " + year + " -f " + folder + " --paths " + pathstr + " --branches " + branchstr + " --scalers " + scalerstr + " -v TT_" + year + ",WJets_" + year + ",VBS_SSWW_aQGC_" + year)
    #os.system("python3 add_1finalMVA_test.py -y " + year + " -f " + folder + " --paths " + pathstr + " --branches " + branchstr + " --scalers " + scalerstr + " -d WpWpJJ_QCD_" + year)
