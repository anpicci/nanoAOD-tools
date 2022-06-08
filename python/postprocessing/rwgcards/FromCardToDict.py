import os
from collections import OrderedDict

def CardToDict(dim, op):
    coeffdict = OrderedDict()
    
    if not "rwgcard" in os.getcwd():
        rwgcard = open("rwgcards/" + dim + "_" + op + ".txt", "r")
    else:
        rwgcard = open(dim + "_" + op + ".txt", "r")
    interlines = [line.replace("\n","").replace("\t", "") for line in rwgcard.readlines() if line.startswith("launch") or line.startswith("\t")]
    coeff = ""
    valstr = ""
    sign = ""
    idl = 0
    idc = 0
    for idl, line in enumerate(interlines):
        line = interlines[idl]

        if line.startswith("launch"):
            flag = line.split("=")[-1]
            if flag.endswith("_0p0"):
                flag = flag.replace("_0p0", "_0")
            coeff, val = flag.split("_")
            val = val.replace("m", "")
            try:
                coeffdict[coeff] is None
            except KeyError:
                coeffdict[coeff] = OrderedDict()
            else:
                pass

        elif line.startswith("set ano"):
            value = float(line.split("anoinputs")[-1].split(" ")[-1].split("e")[0])

            if (value != 0 and val != "0"):
                if val not in coeffdict[coeff].keys():
                    coeffdict[coeff][val] = [None, None]
                if flag == op:
                    if "_m" in flag:
                        idx = 0
                    else:
                        idx = 1
                    coeffdict[coeff][val][idx] = -1
                    continue
                if value < 0.:
                    coeffdict[coeff][val][0] = idc
                elif value > 0.:
                    coeffdict[coeff][val][1] = idc
                idc += 1

            elif (value == 0 and val == "0"):
                if val not in coeffdict[coeff].keys():
                    coeffdict[coeff][val] = [None, None]
                    coeffdict[coeff][val][0] = idc
                    coeffdict[coeff][val][1] = idc
                    idc += 1
                else:
                    pass

    return coeffdict

print(CardToDict("dim8", "FT1_2p0"))
