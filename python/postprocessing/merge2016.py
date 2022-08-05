import os
os.system("reset")
from samples.samplesUL import *
from rwgcards.FromCardToDict import *

folder = "vUL035"
path = "/eos/home-a/apiccine/VBS/nosynch/" + folder + "/plot_tDM/"
leptons = ["electron", "muon"]

rwgdict = CardToDict("dim8", "FT1_2p0")
desiredop = [
    "FS0_1p0",
    "FS1_1p0",
    "FM0_1p0",
    "FM1_0p9",
    "FM6_1p0",
    "FM7_1p0",
    "FT0_1p0",
    "FT1_1p0",
    "FT2_0p9",
]
wcoeff = []
for opname, opdict in rwgdict.items():
    coeffstr = ""
    for val in opdict.keys():
        coeffstr = opname + "_" + val
        if coeffstr in desiredop:
            wcoeff.append(coeffstr)

typcontr = [
    "0",
    "SM",
    "BSM",
]


class_list = plot_list

samples2016 = [cl.label for cl in class_list if "UL2016" == cl.year]


for sample in samples2016:
    if not "aQGC" in sample:
        continue
    for cstr in wcoeff:
        dimtag = cstr
        for idt, typ in enumerate(typcontr):
            dim8sample = sample.replace("aQGC", dimtag + "_" + typ)
            samples2016.append(dim8sample)
    break

#print([sample for sample in samples2016])

for lepton in leptons:
    compath = path + lepton + "/"
    print("Lepton considered:", lepton)
    #os.system("rm " + compath +"*UL2016M*root")

    for sample in samples2016:
        labelsample = sample.split("_UL")[0]
        infiles = [f for f in os.listdir(path + lepton) if f.startswith(labelsample+"_UL") and ("2016_" in f or "2016APV" in f)]
        #print(infiles)

        if sample.startswith("VBS_SSWW_c"):
            continue

        if len(infiles) == 0:
            continue
        #print(infiles)

        haddcommand = "hadd -f " + compath + sample +"M_" + lepton + ".root "
        for infile in infiles:
            haddcommand += compath + infile + " "
        print("Merging 2016 samples for " + labelsample + "...")
        os.system(haddcommand)
        #print(haddcommand)
        
    print(lepton, "ended")
    
print("That's all!")

