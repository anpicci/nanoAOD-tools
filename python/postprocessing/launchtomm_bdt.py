import os
os.system("reset")
bdt_sm_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_SM_UL_vUL008_btagSF.model"
bdt_sm_branch = "BDT_SM_xgb_UL008_no"
bdt_cW_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cW-INT-BSM_UL_vUL008_btagSF.model"
bdt_cW_branch = "BDT_cW_xgb_UL008_no"
bdt_cHW_ul="/eos/user/t/ttedesch/SWAN_projects/VBS_ML_UL/models/not_optimized_xgb_dim6-cHW-INT-BSM_UL_vUL008_btagSF.model"
bdt_cHW_branch = "BDT_cHW_xgb_UL008_no"
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

folder="vUL030"

for year in years:
    #### runna su tutti i samples tranne ttbar
    os.system("python3 add_1finalMVA_chunck.py -y " + year + " -f " + folder + " --paths " + bdt_sm_path + "," + bdt_cW_path + "," + bdt_cHW_path + " --branches " + bdt_sm_branch + "," + bdt_cW_branch + "," + bdt_cHW_branch + " -v TTTo2L2Nu_" + year + ",TT_" + year)# + " -s " + scenario)
    for scenario in scenarios:
        #### runna solo su ttbar tenendo conto delle patologie
        os.system("python3 add_1finalMVA_chunck.py -y " + year + " -f " + folder + " --paths " + bdt_sm_path + "," + bdt_cW_path + "," + bdt_cHW_path + " --branches " + bdt_sm_branch + "," + bdt_cW_branch + "," + bdt_cHW_branch + " -d TTTo2L2Nu_" + year + " -s " + scenario)
