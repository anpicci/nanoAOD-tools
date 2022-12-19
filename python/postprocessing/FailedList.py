import os
def cutToTag(cut):
    newstring = cut.replace("-", "neg").replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("!=","_NEQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
    return newstring

add = " --var DNN_,m_o1,m_1T,m_jj,countings "

#os.system("reset")
folder = "vUL055"
errpaths = [
    ("condorplot_" + folder + "_tdmcut/error/", "PlotCondor.py --tDMcut " + add, ""),
    ("condorplot_" + folder + "_test/error/", "PlotCondor.py --test " + add, ""),
    ("condorplot_" + folder + "/error/", "PlotCondor.py " + add, ""),
    ("condorplot_" + folder + "_vbroad/error/", "PlotCondor.py --vbroad " + add, ""),
    ("condorplot_" + folder + "_vvbroad/error/", "PlotCondor.py --vvbroad " + add, ""),
    ("condorplot_" + folder + "_vvvbroad/error/", "PlotCondor.py --vvvbroad " + add, ""),
    ("condorplot_" + folder + "_tdmcut_noflat/error/", "PlotCondor.py --tDMcut --noflat " + add, ""),
    ("condorplot_" + folder + "_test_noflat/error/", "PlotCondor.py --test --noflat " + add, ""),
    ("condorplot_" + folder + "_noflat/error/", "PlotCondor.py --noflat " + add, ""),

    ("condorplot_" + folder + "/error/", "PlotCondor.py " + add, ""),
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
            check = errfile.replace(".err", "")
            if errpath.startswith("condorplot_"):
                cuttag = "_" + cutToTag(errpair[2])
                if errpair[2] != "":
                    check += cuttag
            if not check.endswith(year):
                continue
            
            if idy > 0:
                strerr += ","
            strerr += errfile.replace(".err", "")
            if errpath.startswith("condorplot_"):
                cuttag = "_" + cutToTag(errpair[2])
                if errpair[2] != "":
                    strerr = strerr.replace(cuttag, "")

            idy += 1
        
            toremove.append(errfile)
        if not strerr.endswith(" -d "):
            tosys += pycomm + " " + strerr + " ;\n"
        print(strerr)
        for tor in toremove:
            errfiles.remove(tor)

    print("\n\nto launch:")
    print(tosys)
