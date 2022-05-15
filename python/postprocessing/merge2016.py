import os
from samples.samplesUL import *

folder = "vUL025"
path = "/eos/home-a/apiccine/VBS/nosynch/" + folder + "/plot/"
leptons = ["electron", "muon"]

samples2016 = [cl for cl in class_list if "UL2016" == cl.year]
#print([sample.label for sample in samples2016])

for lepton in leptons:
    compath = path + lepton + "/"
    print("Lepton considered:", lepton)
    os.system("rm " + compath +"*UL2016M*root")

    for sample in samples2016:
        infiles = [f for f in os.listdir(path + lepton) if f.startswith(sample.label)]
        if len(infiles) == 0:
            continue
        #print(infiles)
        labelsample = sample.label.split("_UL")[0]
        haddcommand = "hadd -f " + compath + sample.label +"M_" + lepton + ".root "
        for infile in infiles:
            haddcommand += compath + infile + " "
        print("Merging 2016 samples for " + labelsample + "...")
        os.system(haddcommand)
        
    print(lepton, "ended")

print("That's all!")

