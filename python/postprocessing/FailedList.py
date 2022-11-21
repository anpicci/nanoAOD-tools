import os
def cutToTag(cut):
    newstring = cut.replace("-", "neg").replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("!=","_NEQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
    return newstring

add = ""#--var DNN_dim6_final_2,DNN_dim8_final_3"

os.system("reset")
folder = "vUL050"
errpaths = [
    ("condorplot_" + folder + "_tdmcut/error/", "PlotCondor.py --tDMcut " + add, ""),
    ("condorplot_" + folder + "_test/error/", "PlotCondor.py --test " + add, ""),
    ("condorplot_" + folder + "_tdmcut_flat/error/", "PlotCondor.py --tDMcut --flat " + add, ""),
    ("condorplot_" + folder + "_test_flat/error/", "PlotCondor.py --test --flat " + add, ""),
    ("condorplot_" + folder + "_flat/error/", "PlotCondor.py --flat " + add, ""),
    ("condorplot_" + folder + "_test/error/", "PlotCondor.py --test --cuts \"DNN_SM_final_1>=0.90\" " + add, "DNN_SM_final_1>=0.90"),
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
