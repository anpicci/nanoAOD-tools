import os
os.system("reset")
folder = "vUL035"
errpaths = [
    "condorplot_" + folder + "_tdmcut/error/",
    "condorbranch_" + folder + "/error/",
    "condormerge_" + folder + "/error/"
]

years = [
    "UL2016",
    "UL2016APV",
    "UL2017",
    "UL2018",
]

for errpath in errpaths:
    errfiles = os.listdir(errpath)
    dimzeros = []
    print("\n" + errpath)
    
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
