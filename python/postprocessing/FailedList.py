import os
def cutToTag(cut):
    newstring = cut.replace("-", "neg").replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("!=","_NEQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
    return newstring

#add = "--var countings,m_o1,m_1T,m_jj,DNN_SM_"
add = "" #--var DNN_"

#os.system("reset")
#folder = "vUL060"
folder = "vUL055"
errpaths = [
    ("condorplot_" + folder + "_merge6/error/", "PlotCondor.py --merge 6 --var DNN_SM,DNN_dim " + add, ""),
    ("condorplot_" + folder + "_merge9/error/", "PlotCondor.py --merge 9 --var DNN_ " + add, ""),
    ("condorplot_" + folder + "_merge10/error/", "PlotCondor.py --merge 10 --var DNN_,m_o1,m_1T " + add, ""),
    ("condorplot_" + folder + "_merge11/error/", "PlotCondor.py --merge 11 --var DNN_ " + add, ""),
    ("condorplot_" + folder + "_merge12/error/", "PlotCondor.py --merge 12 --var DNN_ " + add, ""),

    #("condorbranch_" + folder + "/error/", "BranchCondor.py --or --rw"),
    #("condormerge_" + folder + "/error/", "MergeCondor.py --or --rw"),
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
    print(errpath)
    
    tresh = 0.
    if errpath.startswith("condorbranch_"):
        tresh = 1865.
    for errfile in errfiles:
        #print((errpath + errfile), os.stat(errpath + errfile).st_size)
        if os.stat(errpath + errfile).st_size <= tresh:
            dimzeros.append(errfile)

    for dimzero in dimzeros:
        errfiles.remove(dimzero)
        
    pycomm = "python3 " + errpair[1] + " -f " + folder
    tosys = ""
    for year in years:
        toremove = []
        idy = 0
        strerr = ""
        strerr += "-y " + year + " -d "
        emacsstr = ""
        for iderr, errfile in enumerate(errfiles):

            check = errfile.replace(".err", "")
            check = check.replace("_merge2dis", "").replace("_merge2", "")

            if errpath.startswith("condorplot_"):
                cuttag = "_" + cutToTag(errpair[2])
                if errpair[2] != "":
                    check += cuttag
            if not check.endswith(year):
                continue
            
            #if errfile.startswith("VBS"):
                #continue

            if idy > 0:
                if not errpath.startswith("condormerge_"):
                    strerr += ","
                else:
                    strerr += ":"
            strerr += errfile.replace(".err", "")
            emacsstr += "emacs -nw " + (errpath + errfile) + "\n"
            if errpath.startswith("condorplot_"):
                cuttag = "_" + cutToTag(errpair[2])
                if errpair[2] != "":
                    strerr = strerr.replace(cuttag, "")

            idy += 1
        
            toremove.append(errfile)
        if not strerr.endswith(" -d "):
            tosys += pycomm + " " + strerr + " ;\n"
        print(strerr)
        print(emacsstr)
        for tor in toremove:
            errfiles.remove(tor)

    print("\nto launch:")
    print(tosys)
    print("\n\n\n")
