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

#inf = /eos/home-a/apiccine/VBS/nosynch/FR_UL2017/2/

DataDict = {
        'Ele' : "DataHT_UL" + str(opt.year) + "/DataHT_UL" + str(opt.year) + ".root",
        'Mu'  : "DataMuFake_UL" + str(opt.year) + "/DataMuFake_UL" + str(opt.year) + ".root",
        'Tau' : "DataHT_UL" + str(opt.year) + "/DataHT_UL" + str(opt.year) + ".root",
        'all' : "DataHT_UL" + str(opt.year) + "/DataHT_UL" + str(opt.year) + ".root",
        }



bkg_files = {
        'DYJetsToLL' : "DYJetsToLL_UL" + str(opt.year) + "/DYJetsToLL_UL" + str(opt.year) + ".root", 
        'WJets'      : "WJets_UL" + str(opt.year) + "/WJets_UL" + str(opt.year) + ".root",
        'ZZToLep'    : "ZZtoLep_UL" + str(opt.year) + "/ZZtoLep_UL" + str(opt.year) + ".root",        
        'TT'    : "TT_UL" + str(opt.year) + "/TT_UL" + str(opt.year) + ".root",        
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

FakeCalc = FakeCalculator_manager('all')
isData = True
FakeCalc.Calc(DataDict[opt.trig], True, opt.onlybkg, opt.met_cut, opt.mt_lepMET_cut, opt.trig, Eleh, Muh, Tauh)
for pos in bkg_files:
    if not opt.bkg: break
    bkg = input_folder + bkg_files[pos]
    FakeCalc.Calc(bkg, False, opt.onlybkg, opt.met_cut, opt.mt_lepMET_cut, opt.trig, Eleh, Muh, Tauh)

Eleh.SanitizeHisto()
Muh.SanitizeHisto()
Tauh.SanitizeHisto()
Eleh.CalculateEfficiency()
Muh.CalculateEfficiency()
Tauh.CalculateEfficiency()
fManager.addEfficiencyHisto(Eleh)
fManager.addEfficiencyHisto(Muh)
fManager.addEfficiencyHisto(Tauh)
fManager.saveFile()
fManager.closeFile()
