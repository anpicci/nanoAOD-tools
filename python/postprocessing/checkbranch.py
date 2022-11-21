import os
import ROOT
from samples.samplesUL import *
from ML.MLmodels import *

os.system("reset")

folder = "vUL050"
path = "/eos/home-a/apiccine/VBS/nosynch/" + folder + "/ltau/"

years = [
    #"UL2016APV",
    #"UL2016",
    "UL2017",
    "UL2018"
    "UL2016M",
    "ULRunII"
]

branches = [
    dnn_sm_branch_1_lower_iter1,
    dnn_sm_branch_1_lower_iter4,
    dnn_sm_branch_bis_lower_iter2,
    dnn_sm_branch_bis_lower_iter4,
    dnn_dim8_branch_final_3_noQUAD_fix,
    dnn_dim8_branch_final_3_1to2,
    dnn_dim8_branch_final_3_again,
    dnn_sm_branch_1_NOMOREDY_test,
    dnn_sm_branch_1_NOMOREDY_test_2000,
    dnn_sm_branch_1_NOMOREDY_test_2001,
    dnn_sm_branch_1_NOMOREDY_test_2002,
    dnn_sm_branch_1_NOMOREDY_test_2003,
    dnn_dim8_branch_3_NOMOREDY_test,
    dnn_dim6_branch_2_NOMOREDY_test,
]

scenarios = ["nominal", "lepenUp", "lepenDown", "jesUp", "jesDown", "jerUp", "jerDown", "TESUp", "TESDown", "FESUp", "FESDown"]

for year in years:
    for samp in merge_list:
        if samp.year != year:
            continue
 
        if samp.label.startswith("TT_") or samp.label.startswith("WJets") or samp.label.startswith("DYJetsToLL_Jbin_FxFx"):# or samp.label.startswith("VBS_SSWW_SM") or samp.label.startswith("VBS_SSWW_c"):
            continue

        rfile = path + samp.label + "/" + samp.label + ".root"
        if not os.path.exists(rfile):
            continue

        #print("\n" + samp.label)
        ifile = ROOT.TFile.Open(rfile, "READ")
        for scenario in scenarios:
            ntree = "events_" + scenario
            try:
                tree = ifile.Get(ntree)
                tree.GetListOfBranches()
            except:
                continue

            #print(ntree)
            for branch in branches:
                if branch in tree.GetListOfBranches():
                    #print(branch + " exists")
                    pass
                else:
                    print(branch + " does not exist in " + ntree + " for " + samp.label)
