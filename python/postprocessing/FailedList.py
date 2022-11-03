import os
os.system("reset")
folder = "vUL050"
errpaths = [
    ("condorplot_" + folder + "_tdmcut/error/", "PlotCondor.py --tDMcut"),
    ("condorplot_" + folder + "_test/error/", "PlotCondor.py --test"),
    ("condorplot_" + folder + "/error/", "PlotCondor.py"),
    ("condorbranch_" + folder + "/error/", "BranchCondor.py --or --rw"),
    ("condormerge_" + folder + "/error/", "MergeCondor.py --or --rw"),
]

years = [
    "UL2016",
    "UL2016APV",
    "UL2016M",
    "UL2017",
    "UL2018",
    "ULRunII",
]

for errpair in errpaths:
    errpath = errpair[0]
    try:
        errfiles = os.listdir(errpath)
    except:
        continue
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
        
    pycomm = "python3 " + errpair[1] + " -f " + folder
    tosys = ""
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
        if not strerr.endswith(" -d "):
            tosys += pycomm + " " + strerr + " ;\n"
        print(strerr)
        for tor in toremove:
            errfiles.remove(tor)

    print("\n\nto launch:")
    print(tosys)
