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
parser.add_option('--max', dest='maxj', type=int, default = 0, help='Please enter maximum!')
parser.add_option('--fake', dest='isfake', default = False, action = 'store_true', help='Default runs for analysis, true for fake ratio')
parser.add_option('--or', dest='override', default = False, action = 'store_true', help='Default does not override AreAllCondored')
parser.add_option('--ct', dest='ct', type=str, default = '', help='Default is analysis, otherwise specified CT')
parser.add_option('--ch', dest='channel', type=str, default = 'ltau', help='Select final state, default is h_tau + lepton')
parser.add_option('--nodata', dest='nodata', default = False, action='store_true', help='Not processing Data files')

(opt, args) = parser.parse_args()

#print("UL" in opt.year, opt.year)

if "UL" in opt.year:
    print("Processing UL samples")
    from samples.samplesUL import *
else:
    print("Processing RR samples")
    from samples.samples import *

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])

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
if "UL" in opt.folder and "FR" not in opt.folder and int(opt.folder.split("UL")[-1]) > 9:
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
        "FESDown"
    ]
else:
    scenarios = ["all"]

def CondoredList(samplename):
    try:
        condlist = os.listdir(path+samplename)
    except:
        condlist = []

    toRel = False
    wrongex = False
 
    if len(condlist) > 0:
        for condfile in condlist:
            logpath = "condor_" + opt.folder + "/ltau/output/" + condfile.split("_part")[0] + "_VTVLT_" + condfile.split(".root")[0].split("_")[-1] + ".out"
            if os.stat(path+samplename+"/"+condfile).st_size == 0.:
                print("Condoring still not ended so far")
                condlist.remove(condfile)
            elif os.stat(path+samplename+"/"+condfile).st_size < 1024.:
                toRel = True
                condlist.remove(condfile)
                if not opt.check:
                    os.system("rm -r "+ path + samplename + "/" + condfile)
            else:
                try:
                    tempf = ROOT.TFile.Open(path+samplename+"/"+condfile, "READ")
                except(RuntimeWarning):
                    condlist.remove(condfile)
                    wrongex = True
                    if not opt.check:
                        print("Removing damaged files...")
                        os.system("rm "+ path + samplename + "/" + condfile)
                else:
                    pass

                for ids, scenario in enumerate(scenarios):
                    try:
                        tempentr = tempf.Get(str("events_" + scenario)).GetEntries()
                    except(AttributeError, ReferenceError):#, RuntimeWarning):                                                                                                                                                                                                                                   
                        try:
                            condlist.remove(condfile)
                        except:
                            pass
                        wrongex = True
                        if not opt.check:
                            print("Removing files with damaged " + scenario + " tree...")
                            os.system("rm "+ path + samplename + "/" + condfile)
                    else:
                        pass

                    if ids == 0 and (not isWithSysts or "Data" in samplename):
                        break

        if toRel:
            print("Something went wrong during condoring", samplename, "fix it and relaunch")
            if not opt.check:
                return CondoredList(samplename)
        elif wrongex:
            print("Something went wrong when remapping rootfiles for", samplename, "fix it and relaunch")
            if not opt.check:
                return CondoredList(samplename)

    return condlist, toRel, wrongex

def DoesSampleExist(samplename):
    if samplename+".txt" not in os.listdir(crabpath):
        return False
    else:
        return True

def AreAllCondored(crabname, condorname):
    toRel = False
    condoredlist, torel, wrongex = CondoredList(condorname)
    if (torel or wrongex):
        toRel = True
        storelist = [line for line in open("../../crab/macros/files/"+crabname+".txt")]

        if condorname+"_merged.root" in condoredlist:
            condoredlist.remove(condorname+"_merged.root")
        if condorname+".root" in condoredlist:
            condoredlist.remove(condorname+".root")

        lenstore = len(storelist)

        if 'Data' in crabname:
            remainder = int(lenstore%split)
            lenstore = int(lenstore/split)
            if remainder > 0:
                lenstore += 1

        if len(condoredlist) < lenstore:
            print("condored: ", len(condoredlist), "\tlenstore: ", lenstore)
            return False, toRel
        elif lenstore==0 and len(condoredlist)==0:
            print("Warning for", condorname, "False flag for crabbed files! need to recrab them")
            return True, toRel
        else:
            return True, toRel

    else:
        if len(condoredlist)==0:
            return False, toRel
        else:
            return True, toRel

'''
print("samples")
for k, v in merge_dict.items():
    print(k, v)
'''

datoprocess = opt.dat.split(",")

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
        IsIncluded = False
        if opt.dat != "all":
            for dat in datoprocess:
                if dat.startswith("Fake"):
                    IsIncluded = True
                    break
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
        for c in v.components:
            if opt.dat != 'all':
                IsIncluded = False
                for dat in datoprocess:
                    if str(c.label).startswith(dat) or k.startswith(dat):
                        IsIncluded = True
                        break

                if not IsIncluded:
                    continue

            elif opt.nodata and 'Data' in c.label:
                continue
            
            if not DoesSampleExist(c.name):
                print(c.label, "not crabbed yet")
                continue
            cpath = path + c.label + "/"
            
            AreCondored, toRel = AreAllCondored(c.name, c.label)
            if not AreCondored and not opt.override:
                print(c.label + " not condorly produced yet")
                continue

            doesexist.append(True)
        
            partmerge = False
            if not os.path.exists(cpath+c.label+".root") or opt.rw:
                partmerge = True
                if os.path.exists(cpath+c.label+"_merged.root") or opt.rw:
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

                print("Merging and luming " + c.label + "...")
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
        if opt.dat != 'all':
            IsIncluded = False
            for dat in datoprocess:
                if k.startswith(opt.dat):
                    IsIncluded = True
                    break
            
            if not IsIncluded:
                continue

        if not DoesSampleExist(v.name):
            print(k + " not crabbed yet")
            continue

        AreCondored, toRel = AreAllCondored(v.name, v.label)
        if not AreCondored and not opt.override:
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
