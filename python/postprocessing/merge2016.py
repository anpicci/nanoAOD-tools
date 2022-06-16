import os
os.system("reset")
from samples.samplesUL import *

folder = "vUL030"
path = "/eos/home-a/apiccine/VBS/nosynch/" + folder + "/plot/"
leptons = ["electron", "muon"]

samples2016 = [cl for cl in class_list if "UL2016" == cl.year]
#print([sample.label for sample in samples2016])

for lepton in leptons:
    compath = path + lepton + "/"
    print("Lepton considered:", lepton)
    os.system("rm " + compath +"*UL2016M*root")

    for sample in samples2016:
        labelsample = sample.label.split("_UL")[0]
        infiles = [f for f in os.listdir(path + lepton) if f.startswith(labelsample+"_UL") and ("2016." in f or "2016APV" in f)]
        if len(infiles) == 0:
            continue
        #print(infiles)
        haddcommand = "hadd -f " + compath + sample.label +"M_" + lepton + ".root "
        for infile in infiles:
            haddcommand += compath + infile + " "
        print("Merging 2016 samples for " + labelsample + "...")
        os.system(haddcommand)
        
    print(lepton, "ended")

print("That's all!")
