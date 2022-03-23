import os
import optparse
import sys

cshname = "condorrun_tauwp.csh"
split = 50

usage = 'python SetAndLaunchCondorRun.py -y year -j wp_jet -m wp_mu -e wp_ele -f folder --max max_jobs -c -d dataset'
parser = optparse.OptionParser(usage)
parser.add_option('-y', dest='year', type=str, default = '2017', help='Please enter a year, default is 2017')
parser.add_option('-j', dest='jetwp', type=str, default = 'VT', help='Please enter a TauID WP for vsJet')
parser.add_option('-m', dest='muwp', type=str, default = 'T', help='Please enter a TauID WP for vsMu')
parser.add_option('-e', dest='elewp', type=str, default = 'VL', help='Please enter a TauID WP for vsEle')
parser.add_option('-f', dest='fold', type=str, default = 'v30', help='Please enter a folder')
parser.add_option('--max', dest='maxj', type=int, default = 0, help='Please enter a maximum for number of condor jobs')
parser.add_option('-c', dest='check', default = False, action='store_true', help='Default executes condorrun')
parser.add_option('-d', dest='dat', type=str, default = 'all', help='Default is all')
parser.add_option('--rw', dest='rw', default = False, action='store_true', help='Rewrite the files if not are all condored for a specific sample')
parser.add_option('--try', dest='tryy', default = False, action='store_true', help='Rewrite the files if not are all condored for a specific sample')
parser.add_option('--nodata', dest='nodata', default = False, action='store_true', help='Not processing Data files')
parser.add_option('--ch', dest='channel', type=str, default = 'ltau', help='Select final state, default is h_tau + lepton')
parser.add_option('--beff', dest='beff', default = False, action='store_true', help='Launching btag efficiencies study, default does not')
parser.add_option('--mcreco', dest='mcreco', default = False, action='store_true', help='Launching mcreco study, default does not')
parser.add_option('--masscrit', dest='masscr', default = False, action='store_true', help='Applying masscriterion, default does not')
parser.add_option('--deltaeta', dest='deta', default = False, action='store_true', help='Launching deltaEtaCut before selection, default does not')
parser.add_option('--reco', dest='reco', type=str, default = "not", help='Launching specified reco analysis, default does not')

(opt, args) = parser.parse_args()

isWithSysts = False
if "UL" in opt.fold and int(opt.fold.split("UL")[-1]) > 9:
    isWithSysts = True
    scenarios = ["nominal", "jesUp", "jesDown", "jerUp", "jerDown", "TESUp", "TESDown", "FESUp", "FESDown"]
else:
    scenarios = ["all"]

def CondoredList(samplename):
    try:
        condlist = os.listdir(path+samplename)
    except:
        condlist = []

    if len(condlist) > 0:
        toRel = False
        wrongex = False
        for condfile in condlist:
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
                    except(AttributeError, ReferenceError, RuntimeWarning):
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
            return CondoredList(samplename)
        elif wrongex:
            print("Something went wrong when remapping rootfiles for", samplename, "fix it and relaunch")

    return condlist

def DoesSampleExist(samplename):
    if samplename+".txt" not in os.listdir("../../crab/macros/files/"):
        return False
    else:
        return True
                
def AreAllCondored(crabname, condorname):
    condoredlist = CondoredList(condorname)
    if not opt.beff:
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
            return False
        elif lenstore==0 and len(condoredlist)==0:
            print("Warning for", condorname, "False flag for crabbed files! need to recrab them")
            return True
        else:
            return True

    else:
        if len(condoredlist)==0:
            return False
        else:
            return True
        
if not "UL" in opt.year:
    from samples.samples import *
else:
    from samples.samplesUL import *

vsJet_dict = {"VVVL": '1',
              "VVL": '2',
              "VL": '4',
              "L": '8',
              "M": '16',
              "T": '32',
              "VT": '64',
              "VVT": '128',
}

vsMu_dict = {"VL": '1',
             "L": '2',
             "M": '4',
             "T": '8'
}

vsEle_dict = {"VVVL": '1',
              "VVL": '2',
              "VL": '4',
              "L": '8',
              "M": '16',
              "T": '32',
              "VT": '64',
              "VVT": '128',
}

username = str(os.environ.get('USER'))
inituser = str(os.environ.get('USER')[0])

print(username)
print(opt.dat)

if opt.fold == '':
    folder = "Eff_Jet" + opt.jetwp + "_Mu" + opt.muwp + "_Ele" + opt.elewp
else:
    folder = opt.fold
    if not opt.beff:
        folder += "/" + opt.channel
    else:
        opt.channel = 'bjet'

print(opt.fold, opt.channel, folder)
path = "/eos/home-" + inituser + "/" + username + "/VBS/nosynch/" + folder + "/"
#path = "/eos/home-a/apiccine/VBS/nosynch/" + folder + "/"
print("output path:", path, "\n")

subpy = ""
optstring = " -f " + folder

if opt.beff:
    subpy = "submit_condor_btag.py"
elif opt.tryy:
    subpy = "submit_condor_try.py"
    if opt.channel == "ltau":
        optstring += " --wpjet " + str(opt.jetwp) + " --wpele " + str(opt.elewp) + " --wpmu " + str(opt.muwp)
elif opt.mcreco:# != "not":
    subpy = "submit_condor_mcreco.py"
    optstring += " --wpjet " + str(opt.jetwp) + " --wpele " + str(opt.elewp) + " --wpmu " + str(opt.muwp)
    if opt.reco != "not":
        optstring += " --reco " + opt.reco
elif opt.channel == "ltau":
    subpy = "submit_condor_old.py"
    optstring += " --wpjet " + str(opt.jetwp) + " --wpele " + str(opt.elewp) + " --wpmu " + str(opt.muwp)
    if opt.reco != "not":
        optstring += " --reco " + opt.reco
    if opt.masscr:
        optstring += " --masscrit"
    if opt.deta:
        optstring += " --deltaeta"
elif opt.channel == "emu":
    subpy = "diet_submit_condor.py"

if not os.path.exists(path):
    os.makedirs(path)

if opt.maxj > 0 and not opt.beff:
    optstring = optstring + " --max " + str(opt.maxj)
optstring = optstring + "\n"

f = open(cshname, "w")

dirlist = [dirs for dirs in os.listdir(path) if os.path.isdir(path+dirs)]

#print(condor_dict.items())

for prname, proc in condor_dict.items():
    if not prname.endswith(opt.year):# not in prname:
        continue
    if "Fake" in prname or prname.startswith("DataMET") or '_BSM_INT_' in prname:# or prname.startswith('DY') or prname.startswith('DataHT'):
        continue

    if opt.beff:
        if not '_beff_' in prname:
            continue
    else:
        if '_beff_' in prname:
            continue

    toLaunch = True
    
    if hasattr(proc, 'components'):
        for sample in proc.components:
            if "Fake" in sample.label:
                continue
            elif opt.nodata and 'Data' in sample.label:
                continue
            if opt.dat != 'all':
                if not (str(sample.label).startswith(opt.dat) or prname.startswith(opt.dat)):
                    continue
            
            if not DoesSampleExist(sample.name):
                continue
                #if sample.label in dirlist:
            if os.path.exists(path+sample.label):
                if opt.rw:
                    print('Relaunching all the jobs for', sample.label)
                    os.system("rm -r "+ path + sample.label + "/*")

            if not AreAllCondored(sample.name, sample.label):
                if opt.check:
                    print(sample.label, "not completely condored")
                    print("python " + subpy + " -d " + sample.label+ " " + optstring)
                else:
                    if os.path.exists(path+sample.label):
                        print("Setting jobs for missing condored files...")
                    print("Writing " + sample.label + " in csh...")
                    f.write("python " + subpy + " -d " + sample.label+ " " + optstring)
            else:
                print(sample.label, " completely condored")

    else:

        if opt.dat != 'all':
            if not prname.startswith(opt.dat):
                continue

        if not DoesSampleExist(proc.name):
            continue
        if os.path.exists(path+proc.label):
            if opt.rw:
                print('Relaunching all the jobs for', proc.label)
                os.system("rm -f "+ path + proc.label + "/*")
        if not AreAllCondored(proc.name, proc.label):
            if opt.check:
                print(proc.label, "not completely condored")
                print("python " + subpy + " -d " + proc.label + " " + optstring)
            else:
                if os.path.exists(path+proc.label):
                        print("Setting jobs for missing condored files...")

                print("Writing " + proc.label + " in csh...")  
                f.write("python " + subpy + " -d " + proc.label+ " " + optstring)

        else:
            print(proc.label, " completely condored")

f.close()

if not opt.check:
    t = open("CutsAndValues_" + str(opt.year) + ".py", "w")
    t.write("# In this file values for cuts and constant will be stored and then recalled from the whole analysis function\n")
    t.write("#Using nanoAOD version 102X\n")
    t.write("ONLYELE=1\n")
    t.write("ONLYMU=0\n\n")
    t.write("PT_CUT_MU=  30\n")
    t.write("ETA_CUT_MU= 2.4\n")
    t.write("ISO_CUT_MU= 0.15\n\n")

    if "UL2016" in opt.year:
        t.write("PT_CUT_ELE=  30\n")
    elif "UL2017" in opt.year:
        t.write("PT_CUT_ELE=  38\n")
    elif "UL2018" in opt.year:
        t.write("PT_CUT_ELE=  35\n")
    t.write("ETA_CUT_ELE= 2.4\n")
    t.write("ISO_CUT_ELE= 0.08\n\n")
    
    t.write("REL_ISO_CUT_LEP_VETO_ELE=   0.2\n")
    t.write("PT_CUT_LEP_VETO_ELE=        15\n")
    t.write("ETA_CUT_LEP_VETO_ELE=       2.4\n")
    t.write("REL_ISO_CUT_LEP_VETO_MU=    0.4\n")
    t.write("PT_CUT_LEP_VETO_MU=         10\n")
    t.write("ETA_CUT_LEP_VETO_MU=        2.4\n\n")
    
    t.write("DR_OVERLAP_CONE_TAU=        0.5\n")
    t.write("DR_OVERLAP_CONE_OTHER=      0.4\n\n")
    
    t.write("PT_CUT_JET= 30\n")
    t.write("ETA_CUT_JET=5\n\n")
    
    t.write("DELTAETA_JJ_CUT=2.5\n\n")
    
    #t.write("#btag info: l 13 skimtree_utils.BTAG_ALGO='CSVv2'   #CSVv2, DeepCSV, DeepFLV\n")
    t.write("BTAG_PT_CUT =   30\n")
    t.write("BTAG_ETA_CUT=   5\n")
    t.write("BTAG_ALGO   =   'DeepFlv'\n")
    t.write("BTAG_WP     =   'M'\n")
    t.write("BTAG_WP_LOOSE     =   'L'\n")
    if opt.fold != "vUL001":
        if opt.year == "UL2016APV":
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_ELE = 8" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n") ## old was 4
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_ELE = 8" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n") 
            #t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_MU = 4" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_MU = 4" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n") ## old was 2
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_MU = 4" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
        elif opt.year == "UL2016":
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_ELE = 4" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n") 
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_ELE = 4" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n") 
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_MU = 8" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n") 
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_MU = 8" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n") 
        elif "UL2017" in opt.year:
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_ELE = 16" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_ELE = 16" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_MU = 8" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_MU = 8" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
        elif "UL2018" in opt.year:
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_ELE = 16" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_ELE = 16" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_MU = 16" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
            t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_MU = 16" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
    else:
        t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_ELE = 8" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
        t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_ELE = 2" + " #Bydeeptau2017v2p1vsjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
        t.write("ID_TAU_RECO_DEEPTAU_VSJET_LOOSE_MU = 8" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
        t.write("ID_TAU_RECO_DEEPTAU_VSJET_VETO_MU = 2" + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
    
    t.write("ID_TAU_RECO_DEEPTAU_VSJET = " + vsJet_dict[opt.jetwp] + " #byDeepTau2017v2p1VSjet ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
    t.write("ID_TAU_RECO_DEEPTAU_VSELE = " + vsEle_dict[opt.elewp] + "  #byDeepTau2017v2p1VSe ID working points (deepTau2017v2p1): bitmask 1 = VVVLoose, 2 = VVLoose, 4 = VLoose, 8 = Loose, 16 = Medium, 32 = Tight, 64 = VTight, 128 = VVTight\n")
    t.write("ID_TAU_RECO_DEEPTAU_VSMU = " + vsMu_dict[opt.muwp] + "  #byDeepTau2017v2p1VSmu ID working points (deepTau2017v2p1): bitmask 1 = VLoose, 2 = Loose, 4 = Medium, 8 = Tight\n")
    t.write("ID_TAU_RECO_MVA=            8 #IsolationMVArun2v1DBoldDMwLT ID working point (2017v1): bitmask 1 = VVLoose, 2 = VLoose, 4 = Loose, 8 = Medium, 16 = Tight, 32 = VTight, 64 = VVTight\n")
    t.write("ID_TAU_ANTIMU=              1 #Anti-muon discriminator V3: : bitmask 1 = Loose, 2 = Tight\n")
    t.write("ID_TAU_ANTIELE=             2 #Anti-electron MVA discriminator V6 (2015): bitmask 1 = VLoose, 2 = Loose, 4 = Medium, 8 = Tight, 16 = VTight\n")
    t.write("PT_CUT_TAU=30\n")
    t.write("ETA_CUT_TAU=2.3\n")
    t.write("M_JJ_CUT=   500\n")
    t.write("MET_CUT=    40\n")
    t.close()
    
    print("Launching jobs on condor...")
    os.system("source ./" + cshname)
    print("Done! Goodbye my friend :D")
