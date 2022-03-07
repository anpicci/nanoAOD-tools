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
from Calculator_HistoManager import *
from Calculator_CalculatorManager import *
#from samples.samples import *

if __name__ == "__main__" :
    usage = 'python3 Calculator.py --inf /eos/home-a/apiccine/VBS/nosynch/FR_UL2017/2/ --year 2017'
    parser = optparse.OptionParser(usage)

    parser.add_option('--met',          dest='met_cut',         type=int,   default = '50',                                             help='insert met cut, default 30')
    parser.add_option('--mt',           dest='mt_lepMET_cut',   type=int,   default = '50',                                             help='insert met cut, default 20')
    parser.add_option('-b', '--nobkg',  dest='bkg',                         default = True,    action='store_false',                    help='Do not eliminate contribution fromprompt W+Jets && DY+Jets events, default True')
    parser.add_option('--onlybkg',      dest='onlybkg',                     default = False,    action='store_true',                    help='Only MC prompt contribution, default false')
    parser.add_option('-d', '--debug',  dest='debug',                       default = False,    action='store_true',                    help='Debug mode, only runs in a file for 10000 events')
    parser.add_option('--trig',         dest='trig',            type=str,   default = 'all',                                            help='trigger used, default all')
    parser.add_option('--inf',          dest='infolder',        type=str,   default = '/eos/home-a/apiccine/VBS/nosynch/FR_UL2017/2/',  help='Please enter an input folder folder, default FR_v10/Ele')
    parser.add_option('--user',         dest='user',            type=str,   default = 'mmagheri',                                       help='Enter user, default mmagheri')
    parser.add_option('-y', '--year',   dest='year',            type=str,   default = '2017',                                           help='Enter year, default 2017')
    (opt, args) = parser.parse_args()

    #inf = /eos/home-a/apiccine/VBS/nosynch/FR_UL2017/2/

    time  = datetime.datetime.now()
    print('Starting @ '+ str(time))

    wpTagger = "/FR_UL" + str(opt.year) + "/" 
    wp = opt.infolder.split(wpTagger)
    wp = wp[1]
    wp = wp[0]
    print('wp',wp)
    input_folder = opt.infolder
    outdir = 'FakeRatio_calcs/' + wp + '/'

    if not os.path.isdir(input_folder): 
        raise NameError('ERROR: directory ', input_folder, ' not found')
    else:
        print('Using as input folder: ', input_folder)

    print('Processing events with met cut: ' + str(opt.met_cut) + ' and mT(lep, MET) cut: ' + str(opt.mt_lepMET_cut))

    makeDir(outdir)
    fManager = fileManager(str(opt.trig), str(opt.met_cut), str(opt.mt_lepMET_cut), outdir, opt.bkg, opt.onlybkg, input_folder, opt.year, wp)

    Eleh = EfficiencyHisto_manager('Electron', 1)
    Muh  = EfficiencyHisto_manager('Muon', 1)
    Tauh = EfficiencyHisto_manager('Tau', 5)

    FakeCalc = FakeCalculator_manager('all')
    DataFile, isData = fManager.getData()

    if not FakeCalc.Calc(DataFile, isData, opt.onlybkg, opt.met_cut, opt.mt_lepMET_cut, opt.trig, Eleh, Muh, Tauh):
        exit()
    print("\n")
    bkgFiles, isData = fManager.getBkg()
    fManager.saveFile()

    for pos in bkgFiles:
        if not opt.bkg:
            break
        if not FakeCalc.Calc(pos, isData, opt.onlybkg, opt.met_cut, opt.mt_lepMET_cut, opt.trig, Eleh, Muh, Tauh):
            exit()
        print("\n")
        fManager.saveFile()

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

#running on lxplus726
