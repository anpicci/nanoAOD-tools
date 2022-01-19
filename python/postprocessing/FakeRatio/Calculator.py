import os
#import commands
import sys
import optparse
import ROOT
import math
import copy
import datetime
import time
#from FakeRatio_utils_dev import *
from Calculator_utils import *
from Calculator_fileManager import *
from EfficiencyHisto_manager import *
from FakeCalculator_manager import *
#from samples.samples import *

usage = 'python FakeRatio_calculator_v3.py -b --met 50 --mt 50 --inf FR_24Gen_Ele --trig Ele'
parser = optparse.OptionParser(usage)

parser.add_option('--met',          dest='met_cut',         type=int,   default = '30',                             help='insert met cut, default 30')
parser.add_option('--mt',           dest='mt_lepMET_cut',   type=int,   default = '20',                             help='insert met cut, default 20')
parser.add_option('-b', '--bkg',    dest='bkg',                         default = False,    action='store_true',    help='Eliminate contribution fromprompt W+Jets && DY+Jets events, default false')
parser.add_option('--onlybkg',      dest='onlybkg',                     default = False,    action='store_true',    help='Only MC prompt contribution, default false')
parser.add_option('-d', '--debug',  dest='debug',                       default = False,    action='store_true',    help='Debug mode, only runs in a file for 10000 events')
parser.add_option('--trig',         dest='trig',            type=str,   default = 'all',                            help='trigger used, default all')
parser.add_option('--inf',          dest='infolder',        type=str,   default = '',                               help='Please enter an input folder folder, default FR_v10/Ele')
parser.add_option('--user',         dest='user',            type=str,   default = 'mmagheri',                       help='Enter user, default mmagheri')
parser.add_option('-y', '--year',   dest='year',            type=str,   default = '2017',                           help='Enter year, default 2017')
(opt, args) = parser.parse_args()



DataDict = {
        'Ele' : "DataHT_" + str(opt.year) + "/DataHT_" + str(opt.year) + ".root",
        'Mu'  : "DataMuFake_" + str(opt.year) + "/DataMuFake_" + str(opt.year) + ".root",
        'Tau' : "DataHT_" + str(opt.year) + "/DataHT_" + str(opt.year) + ".root",
        'all' : "DataHT_" + str(opt.year) + "/DataHT_" + str(opt.year) + ".root",
        }


bkg_files = {
        'DYJetsToLL' : "DYJetsToLL_" + str(opt.year) + "/DYJetsToLL_" + str(opt.year) + ".root", 
        'WJets'      : "WJets_" + str(opt.year) + "/WJets_" + str(opt.year) + ".root",
        'ZZToLep'    : "ZZtoLep_" + str(opt.year) + "/ZZtoLep_" + str(opt.year) + ".root",        
        'TT'    : "TT_" + str(opt.year) + "/TT_" + str(opt.year) + ".root",        
        }


time  = datetime.datetime.now()
print('Starting @ '+ str(time))

input_folder = '/eos/user/'+ opt.user[0]+ '/'+opt.user+'/VBS/nosynch/' + opt.infolder + '/'
outdir = 'FakeRatio_calcs/' + opt.infolder + '/'

if not os.path.isdir(input_folder): 
    raise NameError('ERROR: directory ', input_folder, ' not found')
else:
    print('Using as input folder: ', input_folder)

print('Processing events with met cut: ' + str(opt.met_cut) + ' and mT(lep, MET) cut: ' + str(opt.mt_lepMET_cut))

makeDir(outdir)

fManager = fileManager(str(opt.trig), str(opt.met_cut), str(opt.mt_lepMET_cut), outdir, opt.bkg, opt.onlybkg)

Eleh = EfficiencyHisto_manager('Electron')
Muh  = EfficiencyHisto_manager('Muon')
Tauh = EfficiencyHisto_manager('Tau')

FakeCalc = FakeCalculator_manager(10000)
sample = "/eos/home-a/apiccine/VBS/nosynch/FR_UL2017/2/DataHTB_UL2017/DataHTB_UL2017_part9.root"
isData = True
FakeCalc.Calc(sample, isData, opt.onlybkg, opt.met_cut, opt.mt_lepMET_cut, opt.trig, Eleh, Muh, Tauh)
Eleh.SanitizeHisto()
Muh.SanitizeHisto()
Tauh.SanitizeHisto()
Eleh.DrawAll('EleHist.pdf')
fManager.closeFile()




'''
def FakeCalc(sample, isData, nev):
    print 'workin on sample: ' + sample
    print 'is data?        : ', isData
    print 'workin on events: ', nev
    
    print sample
    if not os.path.exists(sample):
        raise NameError('sample do not exists')
    
    print '\n'
    
    looseList = looseDatalist
    tightList = tightDatalist

    chain = ROOT.TChain('events_all')
    chain.Add(sample)
    print (chain)
 
    tree = InputTree(chain)
    
    isMC = not isData
    
    if isMC:
        looseList = looseMClist
        tightlist = tightMClist
    
    if isData and opt.onlybkg:
        print 'the sample: ', sample, 'is tagged as data sample, while you are running in only bkg mode, jumping the sample'
    
    sign = 1    
    if isMC and not opt.onlybkg: sign = -1
    
    maxEvents = nev
    if maxEvents == 'all' or maxEvents>tree.GetEntries():
        maxEvents = tree.GetEntries()
        
    nLooseEle = 0
    nLooseMu  = 0
    nLooseTau = 0
    nTightEle = 0
    
    perc = 0

    for i in range(maxEvents):
            
        if i*1.0/maxEvents*100 > perc: 
            print 'Processing at: ', perc, '%'
            perc +=1
        event       = Event(tree, i)
        FakeLepton  = Object(event, "FakeLepton")
        FakeTau     = Object(event, "FakeTau")

        met         = Object(event, "MET")
        mT          = Object(event, "mT")
        w           = Object(event, "w")
        nleps       = Object(event, "nLeps")
        jets        = Object(event, "Jet")
        veto        = Object(event, "Veto")
        #if i%1000==0: print 'event ---- ', i, '\n', FakeLepton.pt, ' ', FakeLepton.eta)
        SF = 1
        if isMC:
            #SF = sign*w_nominal*PFSF*puSF*lepSF*tau_vsjet_SF*tau_vsele_SF*tau_vsmu_SF*btagSF
            SF = sign*w.nominal*event.PFSF*event.puSF*event.lepSF*event.tau_vsjet_SF*event.tau_vsele_SF*event.tau_vsmu_SF*event.btagSF
            #print SF
            #print sign, w_nominal, PFSF, puSF, lepSF, tau_vsjet_SF, tau_vsele_SF, tau_vsmu_SF, btagSF
            #print sign, event.w_nominal, event.PFSF, event.puSF, event.lepSF, event.tau_vsjet_SF, event.tau_vsele_SF, event.tau_vsmu_SF, event.btagSF
        
        if met.pt>opt.met_cut or mT.lepMET>opt.mt_lepMET_cut or mT.lepMET<0 or met.pt<0:
            continue

        #print 'Checking met ', met.pt, 'checking mT: ', mT.lepMET

        if opt.trig == 'Ele' or opt.trig == 'all' and abs(FakeLepton.pdgid) == 11 and nleps.LightLeptons < 2 and jets.numberSeparate >0 and  abs(FakeLepton.eta)<2.4 and not(abs(FakeLepton.eta)>1.4442 and abs(FakeLepton.eta)<1.566) and FakeLepton.pt>0 and FakeLepton.jetRelIso>=0:
            if isMC and (FakeLepton.isPrompt!=1): 
                SF = 0
            
            if not (FakeLepton.eta<-2.4 or FakeLepton.eta>2.4):
                ptBin  = pTCalculator(FakeLepton.pt)
                etaBin = etaCalculator(FakeLepton.eta)
                dictPos=None
                if FakeLepton.eta>=0:
                    dictPos = str(ptBin) +str(etaBin[1])
                else:
                    dictPos = '-'+str(ptBin) +str(etaBin[1])
                Fake_dicti_ele[dictPos][1] += SF
               
                looseList['Ele'].Fill(FakeLepton.pt, FakeLepton.eta, SF) 

                if FakeLepton.pfRelIso04<0.08 and FakeLepton.isTight:
                    Fake_dicti_ele[dictPos][2] += SF
                    tightList['Ele'].Fill(FakeLepton.pt, FakeLepton.eta, SF) 
        
        elif opt.trig == 'Mu' or opt.trig == 'all' and abs(FakeLepton.pdgid) == 13 and nleps.LightLeptons < 2 and jets.numberSeparate > 0 and  abs(FakeLepton.eta)<2.4 and FakeLepton.pt>0 and FakeLepton.pfRelIso04>=0:
            if isMC and (FakeLepton.isPrompt!=1):
                SF = 0
                  
            ptBin  = pTCalculator(FakeLepton.pt)
            etaBin = etaCalculator(FakeLepton.eta)
                
            dictPos = str(ptBin) +str(etaBin[1])
            Fake_dicti_mu[dictPos][1] += SF
                
            looseList['Mu'].Fill(FakeLepton.pt, abs(FakeLepton.eta), SF) 
                
                #print FakeLepton.pfRelIso04, FakeLepton.isTight

            if abs(FakeLepton.pfRelIso04)<0.15 and FakeLepton.isTight:
                Fake_dicti_mu[dictPos][2] += SF
                tightList['Mu'].Fill(FakeLepton.pt, abs(FakeLepton.eta), SF) 
        
        if opt.trig == 'HT' or opt.trig == 'all':
            
            if veto.TauLeptons==1:
                continue

            if abs(FakeTau.eta)<2.4 and FakeTau.pt>0:
              
                if isMC and (FakeTau.isPrompt!=5): 
                    SF = 0
                  
                ptBin  = pTCalculator(FakeTau.pt)
                etaBin = etaCalculator(FakeTau.eta)
                
                dictPos = str(ptBin) +str(etaBin[1])
                Fake_dicti_tau[dictPos][1] += SF
                
                looseList['Tau'].Fill(FakeTau.pt, abs(FakeTau.eta), SF) 

                if FakeTau.DeepTauWP>=64:
                    Fake_dicti_tau[dictPos][2] += SF
                    tightList['Tau'].Fill(FakeTau.pt, abs(FakeTau.eta), SF) 
        
        if(i%10000000 == 0):
            
            if opt.trig == 'Ele' or opt.trig == 'all':
                print 'Electrons'
                dict_print(Fake_dicti_ele)
                dict_save(Fake_dicti_ele, Fake_dicti_mu, Fake_dicti_tau, outdir+filename)
    
            if opt.trig == 'Mu' or opt.trig == 'all':
                print 'Muons'
                dict_print(Fake_dicti_mu)
                dict_save(Fake_dicti_ele, Fake_dicti_mu, Fake_dicti_tau, outdir+filename)
    
            if opt.trig == 'HT' or opt.trig == 'all':
                print 'Taus'
                dict_print(Fake_dicti_tau)
                dict_save(Fake_dicti_ele, Fake_dicti_mu, Fake_dicti_tau, outdir+filename)
 
 
    for k in Fake_dicti_tau:
        if Fake_dicti_tau[k][2] == 0: Fake_dicti_tau[k][2]=3.0000001
 
    for k in Fake_dicti_ele:
        if Fake_dicti_ele[k][2] == 0: Fake_dicti_ele[k][2]=3.0000001
 
    for k in Fake_dicti_mu:
        if Fake_dicti_mu[k][2] == 0: Fake_dicti_mu[k][2]=3.0000001




    if opt.trig == 'Ele' or opt.trig == 'all':
        print 'Electrons'
        dict_print(Fake_dicti_ele)
        dict_save(Fake_dicti_ele, Fake_dicti_mu, Fake_dicti_tau, outdir+filename)
    
    if opt.trig == 'Mu' or opt.trig == 'all':
        print 'Muons'
        dict_print(Fake_dicti_mu)
        dict_save(Fake_dicti_ele, Fake_dicti_mu, Fake_dicti_tau, outdir+filename)
    
    if opt.trig == 'HT' or opt.trig == 'all':
        print 'Taus'
        dict_print(Fake_dicti_tau)
        dict_save(Fake_dicti_ele, Fake_dicti_mu, Fake_dicti_tau, outdir+filename)
    

    
    hTotList = [looseDatalist, tightDatalist, looseMClist, tightMClist]
   
    print '\n'

    for l in hTotList:
        for h in l:
            l[h].Sumw2()
    
    for i in looseDatalist.keys():
        print i
        xnbins = looseDatalist[i].GetXaxis().GetNbins()
        ynbins = looseDatalist[i].GetYaxis().GetNbins()
        j=1
        

        while j<=ynbins:
            looseDatalist[i].SetBinContent(xnbins, j, looseDatalist[i].GetBinContent(xnbins,j)+looseDatalist[i].GetBinContent(xnbins+1,j))
            looseDatalist[i].SetBinError(xnbins, j, math.sqrt(pow(looseDatalist[i].GetBinError(xnbins,j),2) + pow(looseDatalist[i].GetBinError(xnbins+1,j),2)))
            tightDatalist[i].SetBinContent(xnbins, j, tightDatalist[i].GetBinContent(xnbins,j)+tightDatalist[i].GetBinContent(xnbins+1,j))
            tightDatalist[i].SetBinError(xnbins, j, math.sqrt(pow(tightDatalist[i].GetBinError(xnbins,j),2) + pow(tightDatalist[i].GetBinError(xnbins+1,j),2)))

            looseMClist[i].SetBinContent(xnbins, j, looseMClist[i].GetBinContent(xnbins,j)+looseMClist[i].GetBinContent(xnbins+1,j))
            looseMClist[i].SetBinError(xnbins, j, math.sqrt(pow(looseMClist[i].GetBinError(xnbins,j),2) + pow(looseMClist[i].GetBinError(xnbins+1,j),2)))
            tightMClist[i].SetBinContent(xnbins, j, tightMClist[i].GetBinContent(xnbins,j)+tightMClist[i].GetBinContent(xnbins+1,j))
            tightMClist[i].SetBinError(xnbins, j, math.sqrt(pow(tightMClist[i].GetBinError(xnbins,j),2) + pow(tightMClist[i].GetBinError(xnbins+1,j),2)))
            j+=1

        j = 1
        while j <= xnbins:
            looseDatalist[i].SetBinContent(j, ynbins, looseDatalist[i].GetBinContent(j, ynbins)+looseDatalist[i].GetBinContent(j,ynbins+1))
            looseDatalist[i].SetBinError(j, ynbins, math.sqrt(pow(looseDatalist[i].GetBinError(j,ynbins),2) + pow(looseDatalist[i].GetBinError(j,ynbins+1),2)))
            tightDatalist[i].SetBinContent(j, ynbins, tightDatalist[i].GetBinContent(j,ynbins)+tightDatalist[i].GetBinContent(j,ynbins+1))
            tightDatalist[i].SetBinError(j, ynbins, math.sqrt(pow(tightDatalist[i].GetBinError(j,ynbins),2) + pow(tightDatalist[i].GetBinError(j,ynbins+1),2)))

            looseMClist[i].SetBinContent(j, ynbins, looseMClist[i].GetBinContent(j,ynbins)+looseMClist[i].GetBinContent(j,ynbins+1))
            looseMClist[i].SetBinError(j, ynbins, math.sqrt(pow(looseMClist[i].GetBinError(j,ynbins),2) + pow(looseMClist[i].GetBinError(j,ynbins+1),2)))
            tightMClist[i].SetBinContent(j, ynbins, tightMClist[i].GetBinContent(j,ynbins)+tightMClist[i].GetBinContent(j,ynbins+1))
            tightMClist[i].SetBinError(j, ynbins, math.sqrt(pow(tightMClist[i].GetBinError(j,ynbins),2) + pow(tightMClist[i].GetBinError(j,ynbins+1),2)))
            j+=1

        
        #hFRData = copy.deepcopy(tightDatalist[i])
        #hFRData.SetName(FRDataname[i])
        #print hFRData.GetTitle()
        #hFRData.SetTitle(FRDatatitle[i])
        #print hFRData.GetTitle()
        #hFRData.Divide(looseDatalist[i])
        #print hFRData.GetName()
        
        nX = 1
        nY = 1
        
        
        print "PARAPAAAAA",  tightDatalist[i].GetNbinsX()
        for nX in range(1,tightDatalist[i].GetNbinsX() + 1):
            for nY in range(1, tightDatalist[i].GetNbinsY() + 1):
                if (tightDatalist[i].GetBinContent(nX, nY) == 0):
                    tightDatalist[i].SetBinContent(nX, nY, 3.001)
                    tightDatalist[i].SetBinError(nX, nY, math.sqrt(3.001))
                    #print tightDatalist[i].GetBinContent(nX, nY))

        
        hFRData = tightDatalist[i].Clone(FRDatatitle[i])
        hFRData.SetName(FRDataname[i])
        hFRData.SetTitle(FRDatatitle[i])
        
        for nX in range(1, hFRData.GetNbinsX() + 1):
            for nY in range(1, hFRData.GetNbinsY() + 1):
                if (hFRData.GetBinContent(nX, nY) == 0):
                    hFRData.SetBinContent(nX, nY, 3.001)
                    hFRData.SetBinError(nX, nY, math.sqrt(3.001))
                    #print tightDatalist[i].GetBinContent(nX, nY)

                print nX, nY, hFRData.GetBinContent(nX, nY)
         
        hFRData.Divide(looseDatalist[i])
         
        if opt.bkg:
            hFRMC = tightMClist[i].Clone(FRMCtitle[i])
            hFRMC.SetName(FRMCname[i])
            hFRMC.SetTitle(FRMCtitle[i])
            hFRMC.Divide(looseMClist[i])

            hFRdif = tightDatalist[i].Clone(FRdiftitle[i])
            hFRdif.SetName(FRdifname[i])
            hFRdif.SetTitle(FRdiftitle[i])
            hFRdif.Add(tightMClist[i], -1)
    
            htmp = looseDatalist[i]
            htmp.Add(looseMClist[i], -1)

            hFRdif.Divide(htmp)
        f.Write()




DataDict = {
        'Ele' : "DataEleFake_" + str(opt.year) + "/DataEleFake_" + str(opt.year) + ".root",
        'Mu'  : "DataMuFake_" + str(opt.year) + "/DataMuFake_" + str(opt.year) + ".root",
        'Tau' : "DataHT_" + str(opt.year) + "/DataHT_" + str(opt.year) + ".root",
        'all' : "DataHT_" + str(opt.year) + "/DataHT_" + str(opt.year) + ".root",
        }

DataDict = {
        'Ele' : "DataHT_" + str(opt.year) + "/DataHT_" + str(opt.year) + ".root",
        'Mu'  : "DataMuFake_" + str(opt.year) + "/DataMuFake_" + str(opt.year) + ".root",
        'Tau' : "DataHT_" + str(opt.year) + "/DataHT_" + str(opt.year) + ".root",
        'all' : "DataHT_" + str(opt.year) + "/DataHT_" + str(opt.year) + ".root",
        }


bkg_files = {
        'DYJetsToLL' : "DYJetsToLL_" + str(opt.year) + "/DYJetsToLL_" + str(opt.year) + ".root", 
        'WJets'      : "WJets_" + str(opt.year) + "/WJets_" + str(opt.year) + ".root",
        'ZZToLep'    : "ZZtoLep_" + str(opt.year) + "/ZZtoLep_" + str(opt.year) + ".root",        
        'TT'    : "TT_" + str(opt.year) + "/TT_" + str(opt.year) + ".root",        
        }


if opt.debug:
    file = input_folder + DataDict[opt.trig]
    print '\n'
    print 'debug mode'
    FakeCalc(file, True, 100000)
    dict_print(Fake_dicti_ele)
    dict_print(Fake_dicti_ele)
    print 'Muons onlyData'
    dict_print(Fake_dicti_mu)
    print 'Tau onlyData'
    dict_print(Fake_dicti_tau)
    for pos in bkg_files:
        if not opt.bkg: continue
        bkg = input_folder + bkg_files[pos]
        FakeCalc(bkg, False, 100000)
        print 'Electrons - wo ', pos
        dict_print(Fake_dicti_ele)
        print 'Muons - wo ', pos
        dict_print(Fake_dicti_mu)
        print 'Tau - wo ', pos
        dict_print(Fake_dicti_tau)


else:
    file = input_folder + DataDict[opt.trig]
    FakeCalc(file, True, 'all')
    print 'Electrons - onlyData'
    dict_print(Fake_dicti_ele)
    print 'Muons onlyData'
    dict_print(Fake_dicti_mu)
    print 'Tau onlyData'
    dict_print(Fake_dicti_tau)
    for pos in bkg_files:
        if not opt.bkg: continue
        bkg = input_folder + bkg_files[pos]
        FakeCalc(bkg, False, 'all')
        print 'Electrons - wo ', pos
        dict_print(Fake_dicti_ele)
        print 'Muons - wo ', pos
        dict_print(Fake_dicti_mu)
        print 'Tau - wo ', pos
        dict_print(Fake_dicti_tau)
    



FRData = copy.deepcopy(tightDatalist['Ele'])
FRData.Divide(looseDatalist['Ele'])
FRData.Draw("colz text")

'''