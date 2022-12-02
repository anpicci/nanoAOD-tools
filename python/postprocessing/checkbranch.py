import os
import ROOT
from samples.samplesUL import *
from ML.MLmodels import *

os.system("reset")

folder = "vUL050"
path = "/eos/home-a/apiccine/VBS/nosynch/" + folder + "/ltau/"

years = [
    "UL2016APV",
    "UL2016",
    "UL2017",
    "UL2018"
    #"UL2016M",
    #"ULRunII"
]

branches = [
    dnn_dim6_branch_2_NOMOREDY_lower_halfway_fixedseed_100001,
    dnn_dim8_branch_3_NOMOREDY_lower_fixedseed_100000,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed_100000,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed_100001,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed_100002,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed_100003,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed_100006,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed_100007,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed_100011,
    dnn_sm_branch_1_NOMOREDY_lower_fixedseed_100012,
]

scenarios = ["nominal", "lepenUp", "lepenDown", "jesUp", "jesDown", "jerUp", "jerDown", "TESUp", "TESDown", "FESUp", "FESDown"]

for year in years:
    for samp in merge_list:
        if samp.year != year:
            continue
 
        if samp.label.startswith("TT_") or samp.label.startswith("WJets") or samp.label.startswith("DYJetsToLL_Jbin_FxFx") or samp.label.startswith("VBS_SSWW_SM") or samp.label.startswith("VBS_SSWW_c"):
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
