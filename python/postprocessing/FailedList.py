import os
os.system("reset")
folder = "vUL035"
errpath = "condorplot_" + folder + "/error/"
#errpath = "condorbranch_" + folder + "/error/"

errfiles = os.listdir(errpath)
dimzeros = []

years = [
    "UL2016",
    "UL2016APV",
    "UL2017",
    "UL2018",
]

tresh = 0.
if errpath.startswith("condorbranch_"):
    tresh = 1865.
for errfile in errfiles:
    if os.stat(errpath + errfile).st_size <= tresh:
        dimzeros.append(errfile)
    #print(errfile, os.stat(errpath + errfile).st_size)

for dimzero in dimzeros:
    errfiles.remove(dimzero)


for year in years:
    toremove = []
    idy = 0
    strerr = ""
    strerr += "-y " + year + " -d "
    for iderr, errfile in enumerate(errfiles):
        if not errfile.replace(".err", "").endswith(year):
            continue
        
        if idy > 0:
            strerr += ","
        strerr += errfile.replace(".err", "")
        idy += 1
        
        toremove.append(errfile)
    
    print(strerr)
    for tor in toremove:
        errfiles.remove(tor)
