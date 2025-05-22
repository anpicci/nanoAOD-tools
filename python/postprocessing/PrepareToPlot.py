import os
import optparse
import sys

usage = 'python3 PrepareToPlot.py -y year -f folder'
parser = optparse.OptionParser(usage)
parser.add_option('-y', dest='year', type=str, default = '2017', help='Please enter a year, default is 2017')
parser.add_option('-f', dest='folder', type=str, default = 'v20', help='Please enter a folder, default is v4')
parser.add_option('-c', dest='check', default = False, action = 'store_true', help='Default runs makeplot')
parser.add_option('--rw', dest='rw', default = False, action = 'store_true', help='Default does not rewrite')
parser.add_option('-d', dest='dat', type=str, default = 'all', help='Default is all')
parser.add_option('-v', dest='veto', type=str, default = 'none', help='Default is none')
parser.add_option('--max', dest='maxj', type=int, default = 0, help='Please enter maximum!')
parser.add_option('--fake', dest='isfake', default = False, action = 'store_true', help='Default runs for analysis, true for fake ratio')
parser.add_option('--or', dest='override', default = False, action = 'store_true', help='Default does not override AreAllCondored')
parser.add_option('--ct', dest='ct', type=str, default = '', help='Default is analysis, otherwise specified CT')
parser.add_option('--ch', dest='channel', type=str, default = 'ltau', help='Select final state, default is h_tau + lepton')
parser.add_option('--nodata', dest='nodata', default = False, action='store_true', help='Not processing Data files')

(opt, args) = parser.parse_args()

#print("UL" in opt.year, opt.year)
#condorstatus = [l.replace("\n", "") for l in os.popen("condor_q").readlines() if "apiccine" in l and not "Total" in l]

if "UL" in opt.year:
    print("Processing UL samples")
    from samples.samplesUL import *
else:
    print("Processing RR samples")
    from samples.samples import *

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])

notAll = False
if opt.dat != "all":
    mergesamp = opt.dat.split(",")
    notAll = True
    print("Samples to do:", mergesamp)

toVeto = False
vetosamp = []
if opt.veto != "none":
    vetosamp = opt.veto.split(",")

'''
for line in condorstatus:
    idjob = line.split(" 1 ")[-1]
    sample = ""
    try:
        sample = os.popen("condor_ssh_to_job " + idjob + " \"head snfile.txt\" ").readlines()[0]
    except:
        continue

    if sample != "" and sample.endswith(opt.year):
        if not sample in vetosamp:
            vetosamp.append(sample)
'''
if len(vetosamp) > 0:
    toVeto = True
    print("Samples to veto:", vetosamp)

crabpath = ''
if opt.ct == 'HT':
    crabpath = "../../crab/macros/files/Fake/HT/"
else:
    crabpath = "../../crab/macros/files/"

#username = 'mmagheri'
#inituser = 'm'

ofolder = ''

#if opt.ct != '':
    #ofolder += "CT" + opt.ct + "_"

ofolder += opt.folder# + "/"


path = "/eos/home-" + inituser + "/" + username + "/VBS/nosynch/" + ofolder + "/"
#print(path, opt.isfake)
if not "btag" in opt.folder and not opt.isfake and (("mcreco" in opt.folder and int(opt.folder.split("mcreco")[-1].split("v")[-1]) >= 80) or not "mcreco" in opt.folder):
    path += opt.channel + "/"

#print(path)
#dirlist = [dirs for dirs in os.listdir(path) if os.path.isdir(path+dirs) and opt.folder in dirs]
#datas = opt.dataset + "_" + opt.year

Debug = opt.check # True # False #
split = 50

isWithSysts = False
#if opt.ct != "HT" and ("UL" in opt.folder and "FR" not in opt.folder and int(opt.folder.split("UL")[-1]) > 9):
if opt.ct != "HT" and ("UL" in opt.folder and "FR" not in opt.folder):
    isWithSysts = True
    scenarios = [
        "nominal", 
        "lepenUp", 
        "lepenDown",
        "jesUp", 
        "jesDown",
        "jerUp",
        "jerDown", 
        "TESUp",
        "TESDown",
        "FESUp",
        "FESDown",
        "metUnclustUp",
        "metUnclustDown",
    ]
else:
    scenarios = ["all"]

def CondoredList(samplename):
    try:
        condlist = [f for f in os.listdir(path+samplename) if "_part" in f]
    except:
        condlist = []

    if len(condlist) > 0:
        toRel = False
        wrongex = False
        for condfile in condlist:
            #print(path+samplename+"/"+condfile)
            if opt.ct != "HT" and os.stat(path+samplename+"/"+condfile).st_size < 10.*1024.:#not samplename.startswith('DY')
                print("Condoring still not ended so far")                
                condlist.remove(condfile)
                #if not opt.check:
                    #os.system("rm -r "+ path + samplename + "/" + condfile)
            elif opt.ct == "HT" and os.stat(path+samplename+"/"+condfile).st_size <= 0:
                condlist.remove(condfile)
                if not opt.check:
                    os.system("rm -r "+ path + samplename + "/" + condfile)
            
            else:
                try:
                    tempf = ROOT.TFile.Open(path+samplename+"/"+condfile, "READ")
                except(OSError, RuntimeWarning):
                    condlist.remove(condfile)
                    toRel = True
                    wrongex = True
                    if not opt.check:
                        print("Removing damaged files...")
                        os.system("rm "+ path + samplename + "/" + condfile)
                else:
                    pass

                for ids, scenario in enumerate(scenarios):
                    if opt.ct == "HT":
                        break
                    try:
                        tempentr = tempf.Get(str("events_" + scenario)).GetEntries()
                    except(AttributeError, ReferenceError):#, RuntimeWarning):
                        try:
                            condlist.remove(condfile)
                            tempf.Close()
                        except:
                            tempf.Close()
                            pass
                        wrongex = True
                        if not opt.check:
                            print("Removing files with damaged " + scenario + " tree...")
                            tempf.Close()
                            os.system("rm "+ path + samplename + "/" + condfile)
                            break
                    else:
                        pass
                    
                    if ids == 0 and (not isWithSysts or "Data" in samplename):
                        break
                try:
                    tempf.Close()
                except:
                    condlist.remove(condfile)
                    toRel = True
                    wrongex = True
                    if not opt.check:
                        print("Removing damaged files...")
                        os.system("rm "+ path + samplename + "/" + condfile)
                else:
                    pass
                    
        if toRel:
            print("Something went wrong during condoring", samplename, "fix it and relaunch")
            if not opt.check:
                return CondoredList(samplename)
        elif wrongex:
            print("Something when remapping rootfiles for ", samplename, "fix it and relaunch")
            if not opt.check:
                return CondoredList(samplename)
       
    return condlist

def DoesSampleExist(samplename):
    samplenamee = samplename.replace("WmWm", "WpWp")
    if samplenamee+".txt" not in os.listdir(crabpath):
        return False
    else:
        return True

def AreAllCondored(crabname, condorname):
    condornamee = condorname.replace("WmWm", "WpWp")
    crabnamee = crabname.replace("WmWm", "WpWp")
    storelist = [line for line in open(crabpath+crabnamee+".txt")]
    condoredlist = CondoredList(condornamee)
    #print(crabpath, crabname,".txt")
    #print(len(storelist), (condoredlist))
    if condornamee+"_merged.root" in condoredlist:
        condoredlist.remove(condornamee+"_merged.root")
    if condornamee+".root" in condoredlist:
        condoredlist.remove(condornamee+".root")

    lenstore = len(storelist)
    
    if 'Data' in crabnamee:
        remainder = int(lenstore%split)
        lenstore = int(lenstore/split)
        if remainder > 0:
            lenstore += 1

    IsThereMaximum = bool(opt.maxj) and bool(opt.maxj < lenstore) and bool("Data" not in crabnamee)
    #print("IsThereMaximum", IsThereMaximum)
    if IsThereMaximum and 'Data' not in crabnamee and len(condoredlist) < opt.maxj:
        print("condored: ", len(condoredlist), "\tlenstore: ", lenstore)
        return False
    elif not IsThereMaximum and len(condoredlist) < (lenstore):
        print("condored: ", len(condoredlist), "\tlenstore: ", lenstore)
        return False
    elif lenstore==0 and len(condoredlist)==0:
        print("Warning for", condorname, "False flag for crabbed files! need to recrab them")
        return False
    else:
        return True

'''
print("samples")
for k, v in merge_dict.items():
    print(k, v)
'''

#datoprocess = opt.dat.split(",")

for k, v in merge_dict.items():
    
    #if opt.year not in k:
    if not k.endswith(opt.year):
        continue

    ismerged = False
    doesexist = []
    merging = []

    kpath = path+k+"/"

    if not opt.isfake:# or opt.ct == '':
        pass
        #if k.startswith('DY'):# or k.startswith('DataHT'):
            #pass #continue

    elif opt.isfake:
        if not (k.startswith('TT_') or k.startswith('DataHT') or k.startswith('DY') or k.startswith('WJets') or k.startswith('GluGluToContin') or k.startswith('ZZ')):
            continue
    
    if k.startswith('Fake'):
        continue
        if opt.dat != "all":
            IsIncluded = False
            for dat in mergesamp:
                if dat.startswith("Fake"):
                    IsIncluded = True
                    break
        else:
            IsIncluded = True        
        if not IsIncluded:
            continue
            
        if os.path.exists(path + k + "/" + k + ".root"):
            if not opt.rw:
                continue
            
        mergable = False

        for c in v.components:
            if os.path.exists(path + c.label + "/" + c.label + ".root"):
                mergable = True
            else:
                mergable = False
            
        if mergable:
            cmdstring = "python3 makeplot.py -y " + opt.year +  " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel
            if Debug:
                print(cmdstring)
            else:
                os.system(cmdstring)#"python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel)
        else:
            print(k, "not mergable")
        continue

    if hasattr(v, 'components') and v.components is not None:
       
        if toVeto:
            toContinue = False
            for vs in vetosamp:
                if v.label.startswith(vs):
                    toContinue = True
                    break
                #else:
                    #for c in v.components:
                        #if c.label.startswith(vs):
                            #toContinue = True
                            #break
                    #if toContinue:
                        #break

            if toContinue:
                continue        

        if notAll:
            toPass = False
            for ms in mergesamp:
                if v.label.startswith(ms):
                    toPass = True
                    break
                #else:
                    #for c in v.components:
                        #if c.label.startswith(ms):
                            #toPass = True
                            #break
                    #if toPass:
                        #break

            if not toPass:
                continue

        print("hello", v.label)
        for c in v.components:
            if opt.nodata and 'Data' in c.label:
                continue
            
            if not DoesSampleExist(c.name) and not (opt.year == "UL2016M" or opt.year == "ULRunII"):
                print(c.label, "not crabbed yet")
                continue
            cpath = path + c.label + "/"
            if not (opt.year == "UL2016M" or opt.year == "ULRunII"):
                if (not AreAllCondored(c.name, c.label) and not opt.override):
                    print(c.label + " not condorly produced yet")
                    continue

            doesexist.append(True)
        
            partmerge = False
            if (not os.path.exists(cpath+c.label+".root") or opt.rw) and not (opt.year == "UL2016M" or opt.year == "ULRunII"):
                partmerge = True
                if (os.path.exists(cpath+c.label+"_merged.root") or opt.rw):
                    if Debug:
                        print("rm -f " + cpath + c.label + "_merged.root")
                    else:
                        os.system("rm -f " + cpath + c.label + "_merged.root")

            if partmerge:
                print(c.label + " not merged so far")

                if os.path.exists(cpath+c.label+".root"):
                    if Debug:
                        print("rm -f " + cpath + c.label + ".root")
                    else:
                        os.system("rm -f " + cpath + c.label + ".root")

                print("Merging and luming " + c.label + "... compon")
                merging.append(True)
                cmdstring = "python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + c.label + " --folder " + ofolder + " --ch " + opt.channel
                if Debug:
                    print(cmdstring)
                else:
                    os.system(cmdstring)
                print("Merged and lumied!")
            else:
                print(c.label + " already merged and lumied")

        samplemerge = False

        #print(len(doesexist), len(v.components))
        if len(doesexist) == len(v.components):
            if len(merging) == 0:
                if os.path.exists(kpath+k+".root") and not opt.rw:
                    print(k + " already merged")
                    samplemerge = False
                else:
                    samplemerge = True
            else:
                samplemerge = True

            if samplemerge:
                if os.path.exists(kpath+k+".root"):
                    if Debug:
                        print("rm -f "+kpath+k+".root")
                    else:
                        os.system("rm -f "+kpath+k+".root")
                cmdstring = "python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel
                if Debug:
                    print(cmdstring)
                else:
                    os.system(cmdstring)
        #else:
            #print k + "not ready to be merged"
        
        
    else:
        '''
        if opt.dat != 'all':
            IsIncluded = False
            for dat in datoprocess:
                if k.startswith(opt.dat):
                    IsIncluded = True
                    break
            
            if not IsIncluded:
                continue
        '''
        
        if toVeto:
            toContinue = False
            for vs in vetosamp:
                if k.startswith(vs):
                    toContinue = True
                    break
            if toContinue:
                continue

        if notAll:
            toPass = False
            for ms in mergesamp:
                if k.startswith(ms):
                    toPass = True
                    break
            if not toPass:
                continue

        if not DoesSampleExist(v.name):
            print(k + " not crabbed yet")
            continue

        if not AreAllCondored(v.name, v.label) and not opt.override:
        #if not os.path.exists(kpath+k):
            print(k + " not condored at all yet")
            continue

        doesexist.append(True)
        samplemerge = False
        if not os.path.exists(kpath+k+".root") or opt.rw:
            samplemerge = True
            if os.path.exists(kpath+k+"_merged.root") or opt.rw:
                if Debug:
                    print("rm -f " + kpath + k + "_merged.root")
                else:
                    os.system("rm -f " + kpath + k + "_merged.root")

        if samplemerge:
            if os.path.exists(kpath+k+".root"):
                if Debug:
                    print("rm -f " + kpath + k + ".root")
                else:
                    os.system("rm -f " + kpath + k + ".root")
            print(k + " neither merged nor lumied so far")
            print("Merging and luming " + k + "...")
            cmdstring = "python3 makeplot.py -y " + opt.year + " --merpart --lumi --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel
            if Debug:
                print(cmdstring)
            else:
                os.system(cmdstring)
            print("Merged and lumied!")
        else:
            print(k + " already merged and lumied")
