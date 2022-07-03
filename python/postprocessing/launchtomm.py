import os
from ML.MLmodels import *
os.system("reset")

years = [
    "UL2016APV",
    #"UL2016",
    "UL2017",
    #"UL2018",
]

branches = [
    bdt_sm_branch,
    bdt_cW_branch,
    bdt_cHW_branch,
    dnn_sm_branch,
    dnn_cW_branch,
    #bdt_pol_branch,
    #dnn_cHW_branch_bal,
    #dnn_pol_branch,
]

paths = [
    bdt_sm_path,
    bdt_cW_path,
    bdt_cHW_path,
    dnn_sm_path,
    dnn_cW_path,
    #bdt_pol_path,
    #dnn_cHW_path_bal,
    #dnn_pol_path,
]

scalers = [
    bdt_sm_scaler,
    bdt_cW_scaler,
    bdt_cHW_scaler,
    dnn_sm_scaler,
    dnn_cW_scaler,
    #bdt_pol_scaler,
    #dnn_cHW_scaler,
    #dnn_pol_scaler,
]

folder="vUL035"

branchstr = "\""
pathstr = "\""
scalerstr = "\""

for idb, branch in enumerate(branches):
    if idb > 0:
        branchstr += ","
        pathstr += ","
        scalerstr += ","
    branchstr += branches[idb]
    pathstr += paths[idb]
    scalerstr += scalers[idb]

branchstr += "\""
pathstr += "\""
scalerstr += "\""

for year in years:
    os.system("python3 add_1finalMVA_test.py -y " + year + " -f " + folder + " --paths " + pathstr + " --branches " + branchstr + " --scalers " + scalerstr + " -v TT_" + year + ",WJets_" + year)
    #os.system("python3 add_1finalMVA_test.py -y " + year + " -f " + folder + " --paths " + pathstr + " --branches " + branchstr + " --scalers " + scalerstr + " -d WZ_" + year + " --ov")
