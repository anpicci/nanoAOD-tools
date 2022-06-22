import os
from samples.samplesUL import *

os.system("reset")

folder = "vUL030"
path = "/eos/home-a/apiccine/VBS/nosynch/" + folder + "/plot/"
leptons = ["electron", "muon"]

samples = [cl for cl in plot_list if "UL2016" == cl.year]
#print([sample.label for sample in samples])

for lepton in leptons:
    compath = path + lepton + "/"
    print("Lepton considered:", lepton)
    os.system("rm " + compath +"*ULRunII*root")

    for sample in samples:
        sampletag = sample.label.split("_UL")[0]
        infiles = [f for f in os.listdir(path + lepton) if f.startswith(sampletag+"_UL") and not "2016M" in f]

        if len(infiles) == 0:
            continue

        haddcommand = "hadd -f " + compath + sampletag +"_ULRunII_" + lepton + ".root "
        for infile in infiles:
            haddcommand += compath + infile + " "
        print("Merging RunII samples for " + sampletag + "...")
        os.system(haddcommand)
        #print(haddcommand)
        
    print(lepton, "ended")

print("That's all!")
