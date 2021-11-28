import os
import optparse
import sys
import time
import copy
from PhysicsTools.NanoAODTools.postprocessing.samples.samplesUL import *

""" module to launch and check crab jobs for UL """

def PrintOutput(readlines):
    lines = list(filter(lambda x : x != "\n", readlines))
    for line in lines:
        print "\t" + line.replace("\n", "")

usage = 'python3 SetAndLaunchCrabJobs.py'
parser = optparse.OptionParser(usage)
parser.add_option('-y', dest='year', type=str, default = 'UL2017', help='Please enter a year, default is UL2017')
parser.add_option('-d', '--dat', dest='dat', type=str, default = '', help='Please enter a dataset name')
#parser.add_option('--status', dest = 'status', default = False, action = 'store_true', help = 'Default do not check the status')
#parser.add_option('--verb', dest = 'verb', default = False, action = 'store_true', help = 'Default do not verbosely check the status')
#parser.add_option('-s', '--sub', dest = 'sub', default = False, action = 'store_true', help = 'Default do not submit')
#parser.add_option('-k', '--kill', dest = 'kill', default = False, action = 'store_true', help = 'Default do not kill')
#parser.add_option('-p', '--purge', dest = 'purge', default = False, action = 'store_true', help = 'Default do not kill')
#parser.add_option('-r', '--resub', dest = 'resub', default = False, action = 'store_true', help = 'Default do not resubmit')
#parser.add_option('-g', '--gout', dest = 'gout', default = False, action = 'store_true', help = 'Default do not do getoutput')
parser.add_option('--sampleFlag',  dest = 'sampleFlag', default = False, action = 'store_true', help = 'Add sample flag')
parser.add_option('--fake',  dest = 'forFR', default = False, action = 'store_true', help = 'configuration for FR samples')
(opt, args) = parser.parse_args()


submitflag = " -s"
if opt.sampleFlag:
    submitflag += " --sampleFlag"

if "UL" not in opt.year:
    raise ValueError("This macro is intended to be use ONLY with UL samples!")

year = str(opt.year)

if opt.dat != "" and year not in opt.dat:
    print "Overriding year..."
    year = opt.dat.split("_")[1]

crabdirs = [cdir.replace("crab_", "") for cdir in os.listdir(".") if os.path.isdir("./" + cdir) and cdir != "macros"]

if not opt.forFR:
    samlist = crab_dict[year]
else:
    samlist = crab_dict_Fake[year]

if opt.dat != "":
    samlist = list(filter(lambda x : x.label == opt.dat, samlist))

if opt.forFR:
    crabc = "python submit_crab_fake.py"
else:
    crabc = "python submit_crab.py"

complist = []
for samp in samlist:
    if hasattr(samp, "components"):
        for c in samp.components:
            complist.append(copy.deepcopy(c))
    else:
        complist.append(copy.deepcopy(samp))

for s in complist:
    print "\n\nConsidering " + s.label + " sample..."
    crabcommand = crabc + " -d " + str(s.label)

    dirlab = s.label
    if opt.forFR:
        dirlab += "_FakeHT"

    if dirlab in crabdirs:
        sstatus = ""
        print "\t" + s.label + " already submitted, check the status..."
        crabcommand += " --status --verb"
        #os.system(crabcommand)
        crabout = os.popen(crabcommand).readlines()
        crabout = list(filter(lambda x : x != "\n", crabout))

        for i, outline in enumerate(crabout):
            if "Jobs status" in outline:
                print "\t" + outline.replace("\n", "")
                j = i + 1
                while j < len(crabout) and crabout[j].startswith("\t"):
                    print "\t" + crabout[j].replace("\n", "")
                    j += 1
                
            if "COMPLETED" in outline:
                sstatus = "COMPLETED"
            elif "FAILED" in outline or "SUBMITFAILED" in outline:
                sstatus = "FAILED"
            #else:
                #sstatus = "PROCESSING"

        if sstatus == "COMPLETED":
            print "\t" + s.label + " is COMPLETED, pass to the next sample..."

        elif sstatus == "FAILED":
            print "\t" + s.label + " is FAILED, let's see what happened there..."
            PrintOutput(crabout)
            toRel = str(raw_input("\tWould you like to relaunch the jobs? (type Y or N)\t"))
            if toRel == "Y":
                crabcommand = crabcommand.replace("--status --verb", "-r")
                print "\tResubmitting..."
                crabout = os.popen(crabcommand).readlines()
                PrintOutput(crabout)
            elif toRel == "N":
                toKill = str(raw_input("\tWould you like to kill the jobs? (type Y or N)\t"))
                if toKill == "Y":
                    crabcommand = crabcommand.replace(" --status --verb", " -k")
                    print "\tKilling..."
                    crabout = os.popen(crabcommand).readlines()
                    PrintOutput(crabout)
                    print "\tWaiting 5 minutes before purging..."
                    time.sleep(300)
                    crabcommand = crabcommand.replace(" -k", " -p")
                    print "\tPurging..."
                    crabout = os.popen(crabcommand).readlines()
                    PrintOutput(crabout)

                    toSub = str(raw_input("\tWould you like to submit another time the jobs? (type Y or N)\t"))
                    if toSub == "Y":
                        crabcommand = crabcommand.replace(" -p", submitflag)
                        print "\t(Re)submitting..."
                        crabout = os.popen(crabcommand).readlines()
                        PrintOutput(crabout)

                    else:
                        pass
                
                else:
                    pass

            else:
                pass
            
            print "\tAnyway, let's pass to the next sample..."

        else:#if sstatus == "PROCESSING":
            print "\n\tCrab is processing " + s.label + "..."

    else:
        print "\tThis sample is not submitted to crab yet..."
        crabcommand += submitflag
        crabout = os.system(crabcommand)
        #crabout = os.popen(crabcommand).readlines()
        #PrintOutput(crabout)

print "\n\n\n...and that's all from crab! Bye!\n\n\n"
