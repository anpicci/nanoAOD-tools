import os
import optparse
import sys
from samples.samples import *

usage = 'python3 PrepareToPlot.py -y year -f folder'
parser = optparse.OptionParser(usage)
parser.add_option('-y', dest='year', type=str, default = '2017', help='Please enter a year, default is 2017')
parser.add_option('-f', dest='folder', type=str, default = 'v20', help='Please enter a folder, default is v4')
parser.add_option('-c', dest='check', default = False, action = 'store_true', help='Default runs makeplot')
parser.add_option('--rw', dest='rw', default = False, action = 'store_true', help='Default does not rewrite')
parser.add_option('-d', dest='dat', type=str, default = 'all', help='Default is all')
parser.add_option('--fake', dest='isfake', default = False, action = 'store_true', help='Default runs for analysis, true for fake ratio')
parser.add_option('--ct', dest='ct', type=str, default = '', help='Default is analysis, otherwise specified CT')
parser.add_option('--ch', dest='channel', type=str, default = 'ltau', help='Select final state, default is h_tau + lepton')

(opt, args) = parser.parse_args()

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

def CondoredList(samplename):
    try:
        condlist = os.listdir(path+samplename)
    except:
        condlist = []

    if len(condlist) > 0:
        toRel = False
        wrongex = False
        for condfile in condlist:
            if os.stat(path+samplename+"/"+condfile).st_size < 1024.:#not samplename.startswith('DY')
                toRel =True
                condlist.remove(condfile)
                if not opt.check:
                    os.system("rm -r "+ path + samplename + "/" + condfile)
            else:
                tempf = ROOT.TFile.Open(path+samplename+"/"+condfile, "READ")
                try:
                    tempentr = tempf.Get("events_all").GetEntries()
                except (AttributeError, ReferenceError, RuntimeWarning) as e:
                    condlist.remove(condfile)
                    wrongex = True
                    if not opt.check:
                        os.system("rm "+ path + samplename + "/" + condfile)
                    
        if toRel:
            print("Something went wrong during condoring", samplename, "fix it and relaunch")
            return CondoredList(samplename)
        elif wrongex:
            print("Something when remapping rootfiles for ", samplename, "fix it and relaunch")

    return condlist

def DoesSampleExist(samplename):
    if samplename+".txt" not in os.listdir(crabpath):
        return False
    else:
        return True

def AreAllCondored(crabname, condorname):
    storelist = [line for line in open(crabpath+crabname+".txt")]
    condoredlist = CondoredList(condorname)

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

    if len(condoredlist) < (lenstore):
        print("condored: ", len(condoredlist), "\tlenstore: ", lenstore)
        return False
    elif lenstore==0 and len(condoredlist)==0:
        print("Warning for", condorname, "False flag for crabbed files! need to recrab them")
        return False
    else:
        return True

#print dirlist

#for dirn in dirlist:
#exsamples = [d for d in os.listdir(path+dirn) if os.path.isdir(path+dirn+"/"+d)]
#print exsamples

#print("samples")
#for k, v in merge_dict.items():
    #print(k, v)

for k, v in merge_dict.items():
    #print("hello", k)
    if opt.year not in k:
        continue

    ismerged = False
    doesexist = []
    merging = []

    kpath = path+k+"/"

    if not opt.isfake:# or opt.ct == '':
        if k.startswith('DY'):# or k.startswith('DataHT'):
            continue

    elif opt.isfake:
        if not (k.startswith('TT_') or k.startswith('DataHT') or k.startswith('DY') or k.startswith('WJets') or k.startswith('GluGluToContin') or k.startswith('ZZ')):
            continue

    if k.startswith('Fake'):
        mergable = False
        for c in v.components:
            if os.path.exists(path + c.label + "/" + c.label + ".root"):
                mergable = True
            else:
                mergable = False
        
        if mergable:
            if Debug:
                print("python3 makeplot.py -y ", opt.year, " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel)
            else:
                os.system("python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel)
        else:
            print(k, "not mergable")
        continue

    if hasattr(v, 'components'):
        for c in v.components:
            if opt.dat != 'all':
                if not str(c.label).startswith(opt.dat):
                    if not k.startswith(opt.dat):
                        continue
            if not DoesSampleExist(c.name):
                print(c.label, "not crabbed yet")
                continue
            cpath = path + c.label + "/"
            if not AreAllCondored(c.name, c.label):
            #if not os.path.exists(cpath):
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
                if Debug:
                    print("python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + c.label + " --folder " + ofolder + " --ch " + opt.channel)
                else:
                    os.system("python3 makeplot.py -y " + opt.year + " --merpart --lumi -d " + c.label + " --folder " + ofolder + " --ch " + opt.channel)
                print("Merged and lumied!")
            else:
                print(c.label + " already merged and lumied")

        samplemerge = False

        #print len(doesexist), len(v.components)
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
                if Debug:
                    print("python3 makeplot.py -y ", opt.year, " --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel)
                else:
                    os.system("python3 makeplot.py -y " + opt.year + " --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel)
        #else:
            #print k + "not ready to be merged"
    else:
        if opt.dat != 'all':
            if not k.startswith(opt.dat):
                continue
        if not DoesSampleExist(v.name):
            print(k + " not crabbed yet")
            continue
        if not AreAllCondored(v.name, v.label):
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
            if Debug:
                print("python3 makeplot.py -y ", opt.year, " --merpart --lumi --mertree -d " + k + " --folder "+ ofolder + " --ch " + opt.channel)
            else:
                os.system("python3 makeplot.py -y " + opt.year + " --merpart --lumi --mertree -d " + k + " --folder " + ofolder + " --ch " + opt.channel)
            print("Merged and lumied!")
        else:
            print(k + " already merged and lumied")
