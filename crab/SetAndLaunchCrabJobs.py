import os
import optparse
import sys
import time
import copy

#from samplesUL import *

""" module to launch and check crab jobs for UL """

def PrintOutput(readlines):
    lines = list(filter(lambda x : x != "\n", readlines))
    for line in lines:
        print "\t" + line.replace("\n", "")

usage = 'python3 SetAndLaunchCrabJobs.py'
parser = optparse.OptionParser(usage)
parser.add_option('-y', dest='year', type=str, default = 'UL2016,UL2016APV,UL2017,UL2018', help='Please enter a year, default is UL2017')
parser.add_option('-d', '--dat', dest='dat', type=str, default = 'all', help='Please enter a dataset name')
parser.add_option('--veto', dest='veto', type=str, default = 'none', help='Please enter a dataset name to veto')
parser.add_option('--save', dest = 'save', default = False, action = 'store_true', help = 'Default do not check the save')
parser.add_option('--resave', dest = 'resave', default = False, action = 'store_true', help = 'Default do not resave')
#parser.add_option('--verb', dest = 'verb', default = False, action = 'store_true', help = 'Default do not verbosely check the status')
parser.add_option('-s', '--sub', dest = 'sub', default = False, action = 'store_true', help = 'Default do not submit')
parser.add_option('-k', '--kill', dest = 'kill', default = False, action = 'store_true', help = 'Default do not kill')
#parser.add_option('-p', '--purge', dest = 'purge', default = False, action = 'store_true', help = 'Default do not kill')
#parser.add_option('-r', '--resub', dest = 'resub', default = False, action = 'store_true', help = 'Default do not resubmit')
#parser.add_option('-g', '--gout', dest = 'gout', default = False, action = 'store_true', help = 'Default do not do getoutput')
parser.add_option('--nosampleFlag',  dest = 'sampleFlag', default = True, action = 'store_false', help = 'Default add sample flag')
parser.add_option('--fake',  dest = 'forFR', default = False, action = 'store_true', help = 'configuration for FR samples')
(opt, args) = parser.parse_args()

if "UL" in opt.year:
    from PhysicsTools.NanoAODTools.postprocessing.samples.samplesUL import *
else:
    from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *

submitflag = " -s"
if opt.sampleFlag:
    submitflag += " --sampleFlag"

#if "UL" not in opt.year:
    #raise ValueError("This macro is intended to be use ONLY with UL samples!")

years = str(opt.year).split(",")
toproc = opt.dat.split(",")
toveto = opt.veto.split(",")

print "toproc:", toproc
print "toveto:", toveto

crabdirs = [cdir.replace("crab_", "") for cdir in os.listdir(".") if os.path.isdir("./" + cdir) and cdir != "macros"]



#if opt.dat != "":
    #samlist = list(filter(lambda x : x.label == opt.dat, samlist))

if opt.forFR:
    crabc = "python submit_crab_fake.py"
else:
    crabc = "python submit_crab.py"

complist = []
   
for year in years:
    if not opt.forFR:
        samlist = crab_dict[year]
    else:
        samlist = crab_dict_Fake[year]
    
    #print([sam.label for sam in samlist])
    for samp in samlist:
        if year not in samp.label:
            print "Overriding year..."
            year = opt.samp.split("_")[1]

        if "UL" in opt.year:
            hascomp = hasattr(samp, "components")
        else:
            hascomp = samp.components is not None

        if hascomp:#hasattr(samp, "components") and samp.components is not None:
            for c in samp.components:
                toProc = False
                toVeto = False

                if opt.dat != "all":
                    #print samp.label 
                    for dtp in toproc:
                        if samp.label.startswith(dtp) or c.label.startswith(dtp):
                            toProc = True
                            break
                        
                    if not toProc:
                        continue
            
                if opt.veto != "none":
                    for dtv in toveto:
                        if samp.label.startswith(dtv) or c.label.startswith(dtv):
                            toVeto = True
                            break
            
                    if toVeto:
                        continue
                #print c.label
                if c.dataset == "":
                    print "Skipping " + c.label + ", its dataset is missing up to now"
                    continue
                
                complist.append(copy.deepcopy(c))
                
                
        else:
            toProc = False
            toVeto = False

            if opt.dat != "all":
                #print samp.label 
                for dtp in toproc:
                    if samp.label.startswith(dtp):
                        toProc = True
                        break
                        
                if not toProc:
                    continue
            
            if opt.veto != "none":
                for dtv in toveto:
                    if samp.label.startswith(dtv):
                        toVeto = True
                        break
            
                if toVeto:
                    continue

            if samp.dataset == "":
                print "Skipping " + c.label + ", its dataset is missing up to now"
                continue
                
            complist.append(copy.deepcopy(samp))
        
for s in complist:
    print "\n\nConsidering " + s.label + " sample..."
    crabcommand = crabc + " -d " + str(s.label)
    if not ("UL" in opt.year or "UL" in s.label):
        crabcommand += " --notUL"

    dirlab = s.label
    if opt.forFR:
        dirlab += "_FakeHT"

    if not opt.kill:
    
        if dirlab in crabdirs:
            sstatus = ""
            print "\t" + s.label + " already submitted, check the status..."
            crabcommand += " --status --verb"
            os.system(crabcommand)
            crabout = os.popen(crabcommand).readlines()
            crabout = list(filter(lambda x : x != "\n", crabout))
                

            for i, outline in enumerate(crabout):
                if "COMPLETED" in outline:
                    sstatus = "COMPLETED"
                    break
                elif "FAILED" in outline or "SUBMITFAILED" in outline:# or "failed" in outline:
                    sstatus = "FAILED"
                    break
                elif "Cannot find .requestcache" in outline or "Cannot retrieve the status_cache" in outline:
                    sstatus = "FAILED"
                    break
                #else:
                #sstatus = "PROCESSING"

            toPrint = False
            toSub = ""
            if sstatus == "COMPLETED":
                print "\t" + s.label + " is COMPLETED!"
                printpath = "./macros/files/"
                if opt.forFR:
                    printpath += "Fake/HT/"

                printpath += s.label + ".txt"

                #if not os.path.exists(printpath):
                toPrint = True #str(raw_input("\tWould you like to print out the file paths? (type Y or N)\t"))

            elif sstatus == "FAILED":
                print "\t" + s.label + " is FAILED, let's see what happened there..."
                #PrintOutput(crabout)
                toRel = str(raw_input("\tWould you like to relaunch the jobs? (type Y or N)\t"))
                if toRel == "Y":
                    crabcommand = crabcommand.replace("--status --verb", "-r")
                    print "\tResubmitting..."
                    #crabout = os.popen(crabcommand).readlines()
                    #PrintOutput(crabout)
                    os.system(crabcommand)

                elif toRel == "N":
                    toKill = str(raw_input("\tWould you like to kill the jobs? (type Y or N)\t"))
                    if toKill == "Y":
                        crabcommand = crabcommand.replace(" --status --verb", " -k")
                        print "\tKilling..."
                        #crabout = os.popen(crabcommand).readlines()
                        #PrintOutput(crabout)
                        os.system(crabcommand)
                        #print "\tWaiting 1 minutes before purging..."
                        #time.sleep(60)
                        #crabcommand = crabcommand.replace(" -k", " -p")
                        #print "\tPurging..."
                        #crabout = os.popen(crabcommand).readlines()
                        #PrintOutput(crabout)
                        #os.system(crabcommand)

                        toSub = str(raw_input("\tWould you like to submit another time the jobs? (type Y or N)\t"))
                        if toSub == "Y":
                            crabcommand = crabcommand.replace(" -k", submitflag)
                            print "\t(Re)submitting..."
                            #crabout = os.popen(crabcommand).readlines()
                            #PrintOutput(crabout)
                            os.system(crabcommand)

                        else:
                            pass
                
                    else:
                        pass

                else:
                    pass
            
                print "\tAnyway, let's pass to the next sample..."

            else:#if sstatus == "PROCESSING":
                print "\n\tCrab is processing " + s.label + "..."

            if (toPrint and opt.save) or (opt.resave and (toSub == "N" or toSub == "")):
                printcommand = "cd macros; python files_writer_new.py -d " + s.label
                if opt.forFR:
                    printcommand += " --fake -t HT"
                printcommand += "; cd -;"
                        
                print "\tSaving Pisa paths in txts..."
                os.system(printcommand)
            else:
                #print "\tFile paths already printed out! Let's pass to the next sample..."
                print "\tLet's pass to the next sample..."

        else:
            print "\tThis sample is not submitted to crab yet..."
            crabcommand += submitflag
            crabout = os.system(crabcommand)
            #crabout = os.popen(crabcommand).readlines()
            #PrintOutput(crabout)
    else:
        crabcommand += " -k"
        crabout = os.system(crabcommand)

print "\n\n\n...and that's all from crab! Bye!\n\n\n"

