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
    dnn_sm_branch_final_1,
    dnn_sm_branch_rec,
    dnn_sm_branch_rec_iter1,
    dnn_sm_branch_rec_iter3,
    dnn_sm_branch_final_1_iter5,
    dnn_dim6_branch_final_2,
    dnn_dim6_branch_final_2_noQUAD,
    dnn_dim8_branch_final_3,
    dnn_dim8_branch_final_3_noQUAD,
]

scenarios = ["nominal", "lepenUp", "lepenDown", "jesUp", "jesDown", "jerUp", "jerDown", "TESUp", "TESDown", "FESUp", "FESDown"]

for year in years:
    for samp in merge_list:
        if samp.year != year:
            continue
 
        if samp.label.startswith("TT_") or samp.label.startswith("WJets") or samp.label.startswith("DYJetsToLL_Jbin_FxFx") or samp.label.startswith("VBS_SSWW_a"):
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
