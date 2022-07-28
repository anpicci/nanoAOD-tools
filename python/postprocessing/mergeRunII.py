import os
from samples.samplesUL import *
from rwgcards.FromCardToDict import *

os.system("reset")

folder = "vUL035"
path = "/eos/home-a/apiccine/VBS/nosynch/" + folder + "/plot/"
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

samples = [cl.label for cl in plot_list if "UL2016" == cl.year]
#print([sample for sample in samples])

for sample in samples:
    if not "aQGC" in sample:
        continue
    for cstr in wcoeff:
        dimtag = cstr
        for idt, typ in enumerate(typcontr):
            dim8sample = sample.replace("aQGC", dimtag + "_" + typ)
            samples.append(dim8sample)
    break

for lepton in leptons:
    compath = path + lepton + "/"
    print("Lepton considered:", lepton)
    os.system("rm " + compath +"*ULRunII*root")

    for sample in samples:
        sampletag = sample.split("_UL")[0]
        infiles = [f for f in os.listdir(path + lepton) if f.startswith(sampletag+"_UL") and not "2016M" in f]
        print(infiles)
   
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
