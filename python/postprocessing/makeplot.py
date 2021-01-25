import os, commands
import sys
import optparse
import ROOT
import math
from variabile import variabile
from CMS_lumi import CMS_lumi
from PhysicsTools.NanoAODTools.postprocessing.samples.samples import *
from array import array

#print TT_2017

print("cavalletti")
usage = 'python makeplot.py'# -y year --lep lepton -d dataset --merpart --lumi --mertree --sel --cut cut_string -p -s'
usageToCopyPaste= "python makeplot.py -y 2017 --lep muon --bveto --user apiccine -f v4 -p"

parser = optparse.OptionParser(usage)
parser.add_option('--merpart', dest='merpart', default = False, action='store_true', help='Default parts are not merged')
parser.add_option('--mertree', dest='mertree', default = False, action='store_true', help='Default make no file is merged')
parser.add_option('--lumi', dest='lumi', default = False, action='store_true', help='Default do not write the normalization weights')
parser.add_option('--sel', dest='sel', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('--bveto', dest='bveto', default = False, action='store_true', help='Default do not apply any selection')
parser.add_option('-p', '--plot', dest='plot', default = False, action='store_true', help='Default make no plots')
parser.add_option('-s', '--stack', dest='stack', default = False, action='store_true', help='Default make no stacks')
parser.add_option('-N', '--notstacked', dest='tostack', default = True, action='store_false', help='Default make plots stacked')
parser.add_option('-L', '--lep', dest='lep', type='string', default = 'incl', help='Default make incl analysis')
parser.add_option('-S', '--syst', dest='syst', type='string', default = 'all', help='Default all systematics added')
parser.add_option('-C', '--cut', dest='cut', type='string', default = 'lepton_eta>-10.', help='Default no cut')
parser.add_option('-y', '--year', dest='year', type='string', default = '2017', help='Default 2016, 2017 and 2018 are included')
parser.add_option('-f', '--folder', dest='folder', type='string', default = 'v7', help='Default folder is v0')
#parser.add_option('-T', '--topol', dest='topol', type='string', default = 'all', help='Default all njmt')
parser.add_option('-d', '--dat', dest='dat', type='string', default = 'all', help="")
parser.add_option('--user', dest='user', type='string', default=str(os.environ.get('USER')), help='User')
parser.add_option('--ttbar', dest='ttbar', default = False, action='store_true', help='Enable ttbar CR, default disabled')
parser.add_option('--wjets', dest='wjets', default = False, action='store_true', help='Enable WJets CR, default disabled')

(opt, args) = parser.parse_args()
print("cavallotti")
#print (opt, args)

folder = opt.folder

filerepo = '/eos/home-'+opt.user[0]+'/'+opt.user+'/VBS/nosynch/' + folder + '/'
plotrepo = '/eos/home-'+opt.user[0]+'/'+opt.user+'/VBS/nosynch/' + folder + '/'

ROOT.gROOT.SetBatch() # don't pop up canvases
if opt.lep != 'incl':
     lepstr = 'plot/' + opt.lep
else:
     lepstr = 'plot'
if opt.plot:
     if not os.path.exists(plotrepo + lepstr):
          os.makedirs(plotrepo + lepstr)
     if not os.path.exists(plotrepo + lepstr):
          os.makedirs(plotrepo + lepstr)
if opt.stack:
     if not os.path.exists(plotrepo + 'stack'):
          os.makedirs(plotrepo + 'stack')

def mergepart(dataset):
     samples = []
     if hasattr(dataset, 'components'): # How to check whether this exists or not
          samples = [sample for sample in dataset.components]# Method exists and was used.
     else:
          samples.append(dataset)
     for sample in samples:
          add = "hadd -f " + filerepo + sample.label + "/"  + sample.label + "_merged.root " + filerepo + sample.label + "/"  + sample.label + "_part*.root" 
          print add
          os.system(str(add))
          check = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + "_merged.root ")
          print "Number of entries of the file %s are %s" %(filerepo + sample.label + "/"  + sample.label + "_merged.root", (check.Get("events_all")).GetEntries())

def mergetree(sample):
     if not os.path.exists(filerepo + sample.label):
          os.makedirs(filerepo + sample.label)
     if hasattr(sample, 'components'): # How to check whether this exists or not
          add = "hadd -f " + filerepo + sample.label + "/"  + sample.label + ".root" 
          for comp in sample.components:
               add+= " " + filerepo + comp.label + "/"  + comp.label + ".root" 
          print add
          os.system(str(add))

def lumi_writer(dataset, lumi):
     samples = []
     if hasattr(dataset, 'components'): # How to check whether this exists or not
          samples = [sample for sample in dataset.components]# Method exists and was used.
     else:
          samples.append(dataset)
     print samples
     for sample in samples:
          if not ('Data' in sample.label):# or 'TT_dilep' in sample.label):
               infile =  ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + "_merged.root")
               isthere_gen = bool(infile.GetListOfKeys().Contains("h_genweight"))
               isthere_pdf = bool(infile.GetListOfKeys().Contains("h_PDFweight"))
               tree = infile.Get('events_all')
               tree.SetBranchStatus('w_nominal', 0)
               tree.SetBranchStatus('w_PDF', 0)
               outfile =  ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root","RECREATE")
               tree_new = tree.CloneTree(0)
               print("Getting the histos from %s" %(infile))
               h_genw_tmp = ROOT.TH1F(infile.Get("h_genweight"))
               #print("h_genweight first bin content is %f and h_PDFweight has %f bins" %(h_genw_tmp.GetBinContent(1), nbins))
               w_nom = array('f', [0.]) 
               tree_new.Branch('w_nominal', w_nom, 'w_nominal/F')
               if isthere_pdf:# ("WZ" in sample.label):
                    h_pdfw_tmp = ROOT.TH1F(infile.Get("h_PDFweight"))
                    nbins = h_pdfw_tmp.GetXaxis().GetNbins()
                    w_PDF = array('f', [0.]*nbins)
                    print(nbins)
                    print(len(w_PDF))
                    tree_new.Branch('w_PDF', w_PDF, 'w_PDF/F')
               tree.SetBranchStatus('w_nominal', 1)
               for event in xrange(0, tree.GetEntries()):
                    tree.GetEntry(event)
                    if event%10000==1:
                         #print("Processing event %s     complete %s percent" %(event, 100*event/tree.GetEntries()))
                         sys.stdout.write("\rProcessing event {}     complete {} percent".format(event, 100*event/tree.GetEntries()))
                    w_nom[0] = tree.w_nominal * sample.sigma * tree.HLT_effLumi * 1000./float(h_genw_tmp.GetBinContent(1))
                    if isthere_pdf: #not ("WZ" in sample.label):
                         for i in xrange(1, nbins):
                              w_PDF[i] = h_pdfw_tmp.GetBinContent(i+1)/h_genw_tmp.GetBinContent(2) 
                    tree_new.Fill()
               tree_new.Write()
               outfile.Close()
               print('\n')
          else:
               os.popen("mv " + filerepo + sample.label + "/"  + sample.label + "_merged.root " + filerepo + sample.label + "/"  + sample.label + ".root")

def cutToTag(cut):
    newstring = cut.replace("-", "neg").replace(">=","_GE_").replace(">","_G_").replace(" ","").replace("&&","_AND_").replace("||","_OR_").replace("<=","_LE_").replace("<","_L_").replace(".","p").replace("(","").replace(")","").replace("==","_EQ_").replace("!=","_NEQ_").replace("=","_EQ_").replace("*","_AND_").replace("+","_OR_")
    return newstring

def plot(lep, reg, variable, sample, cut_tag, syst=""):
     print "plotting ", variable._name, " for sample ", sample.label, " with cut ", cut_tag, " ", syst,
     ROOT.TH1.SetDefaultSumw2()
     f1 = ROOT.TFile.Open(filerepo + sample.label + "/"  + sample.label + ".root")

     nbins = variable._nbins
     histoname = "h_" + reg + "_" + variable._name + "_" + cut_tag
     if not variable._iscustom:
          h1 = ROOT.TH1F(histoname, variable._name + "_" + reg, variable._nbins, variable._xmin, variable._xmax)
     else:
          h1 = ROOT.TH1F(histoname, variable._name + "_" + reg, variable._nbins, variable._xmin)
     h1.Sumw2()

     cut = variable._taglio

     if 'MC' in variable._name:
          cut = cut + "*(" + str(variable._name) + "!=-100.)"
     
     if "WpWpJJ_EWK" in sample.label:
         cut = cut + "*10."

     print str(cut)
     foutput = plotrepo + lepstr + "/" + sample.label + "_" + lep+".root"
     '''
     else:
          if(syst==""):
            taglio = variable._taglio+"*w_nominal"
            foutput = "Plot/"+lep+"/"+channel+"_"+lep+".root"
        elif(syst.startswith("jer") or syst.startswith("jes")):
            taglio = variable._taglio+"*w_nominal"
            treename = "events_"+reg+"_"+syst
            foutput = "Plot/"+lep+"/"+channel+"_"+lep+"_"+syst+".root"
            if(channel == "WJets_ext" and lep.startswith("electron")):
                taglio = variable._taglio+"*w_nominal*(abs(w)<10)"
     '''
     #print treename
     #TODO: remove events_all which is hardcoded
     f1.Get("events_all").Project(histoname,variable._name,cut)
     #if not 'Data' in sample.label:
     #     h1.Scale((7.5)/35.89)
     h1.SetBinContent(1, h1.GetBinContent(0) + h1.GetBinContent(1))
     h1.SetBinError(1, math.sqrt(pow(h1.GetBinError(0),2) + pow(h1.GetBinError(1),2)))
     h1.SetBinContent(nbins, h1.GetBinContent(nbins) + h1.GetBinContent(nbins+1))
     h1.SetBinError(nbins, math.sqrt(pow(h1.GetBinError(nbins),2) + pow(h1.GetBinError(nbins+1),2)))
     for i in range(0, nbins+1):
          content = h1.GetBinContent(i)
          if(content<0.):
               h1.SetBinContent(i, 0.)
     fout = ROOT.TFile.Open(foutput, "UPDATE")
     fout.cd()
     h1.Write()
     fout.Close()
     f1.Close()

def makestack(lep_, reg_, variabile_, samples_, cut_tag_, syst_, lumi):
     os.system('set LD_PRELOAD=libtcmalloc.so')

     blind = False
     infile = {}
     histo = []
     tmp = ROOT.TH1F()
     h = ROOT.TH1F()
     if not variabile_._iscustom:
          hdata = ROOT.TH1F('h','h', variabile_._nbins, variabile_._xmin, variabile_._xmax)
     else:
          hdata = ROOT.TH1F('h','h', variabile_._nbins, variabile_._xmin)
     h_sig = []
     h_err = ROOT.TH1F()
     h_bkg_err = ROOT.TH1F()
     print "Variabile:", variabile_._name
     ROOT.gROOT.SetStyle('Plain')
     ROOT.gStyle.SetPalette(1)
     ROOT.gStyle.SetOptStat(0)
     ROOT.TH1.SetDefaultSumw2()
     if(cut_tag_ == ""):
          histoname = "h_" + reg_ + "_" + variabile_._name
          stackname = "stack_" + reg_ + "_" + variabile_._name
          canvasname = "stack_" + reg_ + "_" + variabile_._name + "_" + lep_ + "_" + str(samples_[0].year)
     else:
          histoname = "h_"+reg_+"_"+variabile_._name+"_"+cut_tag_
          stackname = "stack_"+reg_+"_"+variabile_._name+"_"+cut_tag_
          canvasname = "stack_"+reg_+"_"+variabile_._name+"_"+cut_tag_+"_"+lep_ + "_" + str(samples_[0].year)
     if("selection_AND_best_Wpjet_isbtag_AND_best_topjet_isbtag" in cut_tag_ ) or ("selection_AND_best_topjet_isbtag_AND_best_Wpjet_isbtag" in cut_tag_ ):
          blind = True
     stack = ROOT.THStack(stackname, variabile_._name)
     leg_stack = ROOT.TLegend(0.33,0.62,0.91,0.87)
     signal = False

     print samples_
     for s in samples_:
          if('WpWpJJ_EWK' in s.label):
               signal = True
          if(syst_ == ""):
               outfile = plotrepo + "stack_" + str(lep_).strip('[]') + ".root"
               infile[s.label] = ROOT.TFile.Open(plotrepo + lepstr + "/" + s.label + "_" + lep + ".root")
          else:
               outfile = plotrepo + "stack_"+syst_+"_"+str(lep_).strip('[]')+".root"
               infile[s.label] = ROOT.TFile.Open(plotrepo + lepstr + "/" + s.label + "_" + lep + "_" + syst_ + ".root")
     i = 0

     for s in samples_:
          infile[s.label].cd()
          print "opening file: ", infile[s.label].GetName()
          if('Data' in s.label):
               if ("GenPart" in variabile_._name) or ("MC_" in variabile_._name):
                    continue
               if 'DataHT' in s.label or 'DataMET' in s.label:
                    continue
          tmp = (ROOT.TH1F)(infile[s.label].Get(histoname))
          tmp.SetLineColor(ROOT.kBlack)
          tmp.SetName(s.leglabel)
          if('Data' in s.label):
               if ("GenPart" in variabile_._name) or ("MC_" in variabile_._name):
                    continue
               hdata.Add(ROOT.TH1F(tmp.Clone("")))
               hdata.SetMarkerStyle(20)
               hdata.SetMarkerSize(0.9)
               if(i == 0 and not blind): # trick to add Data flag to legend only once
                    leg_stack.AddEntry(hdata, "Data", "ep")
               i += 1
          elif('WpWpJJ_EWK' in s.label):
               #tmp.SetLineStyle(9)
               if opt.tostack:
                    tmp.SetLineColor(s.color)
               else:
                    tmp.SetLineColor(s.color)
               #tmp.SetLineWidth(3)
               tmp.SetMarkerSize(0.)
               tmp.SetMarkerColor(s.color)
               h_sig.append(ROOT.TH1F(tmp.Clone("")))
          else:
               tmp.SetOption("HIST SAME")
               tmp.SetTitle("")
               if opt.tostack:
                    tmp.SetFillColor(s.color)
               else:
                    tmp.SetLineColor(s.color)
               histo.append(tmp.Clone(""))
               stack.Add(tmp.Clone(""))
          tmp.Reset("ICES")
     for hist in reversed(histo):
          if not ('Data' in hist.GetName()):
               leg_stack.AddEntry(hist, hist.GetName(), "f")
     #style options
     print "Is it blind? " + str(blind)
     leg_stack.SetNColumns(2)
     leg_stack.SetFillColor(0)
     leg_stack.SetFillStyle(0)
     leg_stack.SetTextFont(42)
     leg_stack.SetBorderSize(0)
     leg_stack.SetTextSize(0.05)
     c1 = ROOT.TCanvas(canvasname,"c1",50,50,700,600)
     c1.SetFillColor(0)
     c1.SetBorderMode(0)
     c1.SetFrameFillStyle(0)
     c1.SetFrameBorderMode(0)
     c1.SetLeftMargin( 0.12 )
     c1.SetRightMargin( 0.9 )
     c1.SetTopMargin( 1 )
     c1.SetBottomMargin(-1)
     c1.SetTickx(1)
     c1.SetTicky(1)
     c1.cd()

     pad1= ROOT.TPad("pad1", "pad1", 0, 0.31 , 1, 1)
     pad1.SetTopMargin(0.1)
     pad1.SetBottomMargin(0.02)
     pad1.SetLeftMargin(0.12)
     pad1.SetRightMargin(0.05)
     pad1.SetBorderMode(0)
     pad1.SetTickx(1)
     pad1.SetTicky(1)
     pad1.Draw()
     pad1.cd()
     if not blind:
          maximum = max(stack.GetMaximum(),hdata.GetMaximum())
     else:
          maximum = stack.GetMaximum()
     logscale = True # False #
     if(logscale):
          pad1.SetLogy()
          stack.SetMaximum(maximum*1000)
     else:
          stack.SetMaximum(maximum*1.6)
     stack.SetMinimum(0.01)
     if opt.tostack:
          stack.Draw("HIST")
     else:
          stack.Draw("HIST NOSTACK")
     if not variabile_._iscustom:
          step = float(variabile_._xmax - variabile_._xmin)/float(variabile_._nbins)
          print str(step)
          if "GeV" in variabile_._title:
               if step.is_integer():
                    ytitle = "Events"#/ %.0f GeV" %step
               else:
                    ytitle = "Events"# / %.2f GeV" %step
          else:
               if step.is_integer():
                    ytitle = "Events"# / %.0f units" %step
               else:
                    ytitle = "Events"# / %.2f units" %step
     else:
          if "GeV" in variabile_._title:
               ytitle = "Events"# / GeV"
          else:
               ytitle = "Events"# / a.u"
     
     print stack
     stack.GetYaxis().SetTitle(ytitle)
     stack.GetYaxis().SetTitleFont(42)
     stack.GetXaxis().SetLabelOffset(1.8)
     stack.GetYaxis().SetTitleOffset(0.85)
     stack.GetXaxis().SetLabelSize(0.15)
     stack.GetYaxis().SetLabelSize(0.07)
     stack.GetYaxis().SetTitleSize(0.07)
     stack.SetTitle("")
     if(signal):
          for hsig in h_sig:
               #hsig.Scale(1000)
               hsig.Draw("same")
               leg_stack.AddEntry(hsig, hsig.GetName(), "l")
     h_err = stack.GetStack().Last().Clone("h_err")
     h_err.SetLineWidth(100)
     h_err.SetFillStyle(3154)
     h_err.SetMarkerSize(0)
     h_err.SetFillColor(ROOT.kGray+2)
     h_err.Draw("e2same0")
     leg_stack.AddEntry(h_err, "Stat. Unc.", "f")
     if not blind: 
          print(hdata.Integral())
          hdata.Draw("eSAMEpx0")
     else:
          hdata = stack.GetStack().Last().Clone("h_data")
     leg_stack.Draw("same")

     CMS_lumi.writeExtraText = 1
     CMS_lumi.extraText = ""
     if str(lep_).strip('[]') == "muon":
          lep_tag = "#mu+"
     elif str(lep_).strip('[]') == "electron":
          lep_tag = "e+"
     else:
          lep_tag = "incl."
         
     print "lep_tag: ", lep_tag
     lumi_sqrtS = "%s fb^{-1}  (13 TeV)"%(lumi)
     
     iPeriod = 0
     iPos = 11
     CMS_lumi(pad1, lumi_sqrtS, iPos, lep_tag+str(reg_))
     hratio = stack.GetStack().Last()
     
     c1.cd()
     pad2= ROOT.TPad("pad2", "pad2", 0, 0.01 , 1, 0.30)
     pad2.SetTopMargin(0.05)
     pad2.SetBottomMargin(0.45)
     pad2.SetLeftMargin(0.12)
     pad2.SetRightMargin(0.05)
     ROOT.gStyle.SetHatchesSpacing(2)
     ROOT.gStyle.SetHatchesLineWidth(2)
     c1.cd()
     pad2.Draw()
     pad2.cd()
     ratio = hdata.Clone("ratio")
     ratio.SetLineColor(ROOT.kBlack)
     ratio.SetMaximum(10)
     ratio.SetMinimum(0)
     ratio.Sumw2()
     ratio.SetStats(0)
     
     ratio.Divide(hratio)
     ratio.SetMarkerStyle(20)
     ratio.SetMarkerSize(0.9)
     ratio.Draw("epx0e0")
     ratio.SetTitle("")
     
     h_bkg_err = hratio.Clone("h_err")
     h_bkg_err.Reset()
     h_bkg_err.Sumw2()
     for i in range(1,hratio.GetNbinsX()+1):
          h_bkg_err.SetBinContent(i,1)
          if(hratio.GetBinContent(i)):
               h_bkg_err.SetBinError(i, (hratio.GetBinError(i)/hratio.GetBinContent(i)))
          else:
               h_bkg_err.SetBinError(i, 10^(-99))
     h_bkg_err.SetLineWidth(100)

     h_bkg_err.SetMarkerSize(0)
     h_bkg_err.SetFillColor(ROOT.kGray+1)
     h_bkg_err.Draw("e20same")
     
     if not variabile_._iscustom:
          xmin = variabile_._xmin
     else:
          xmin = variabile_._xmin[0]
     f1 = ROOT.TLine(xmin, 1., variabile_._xmax,1.)
     f1.SetLineColor(ROOT.kBlack)
     f1.SetLineStyle(ROOT.kDashed)
     f1.Draw("same")
     
     ratio.GetYaxis().SetTitle("Data / MC")
     ratio.GetYaxis().SetNdivisions(503)
     ratio.GetXaxis().SetLabelFont(42)
     ratio.GetYaxis().SetLabelFont(42)
     ratio.GetXaxis().SetTitleFont(42)
     ratio.GetYaxis().SetTitleFont(42)
     ratio.GetXaxis().SetTitleOffset(1.1)
     ratio.GetYaxis().SetTitleOffset(0.35)
     ratio.GetXaxis().SetLabelSize(0.15)
     ratio.GetYaxis().SetLabelSize(0.15)
     ratio.GetXaxis().SetTitleSize(0.16)
     ratio.GetYaxis().SetTitleSize(0.16)
     ratio.GetYaxis().SetRangeUser(-3.0,3.0)
     ratio.GetXaxis().SetTitle(variabile_._title)
     ratio.GetXaxis().SetLabelOffset(0.04)
     ratio.GetYaxis().SetLabelOffset(0.02)
     ratio.Draw("epx0e0same")

     c1.cd()
     #ROOT.TGaxis.SetMaxDigits(3)
     c1.RedrawAxis()
     pad2.RedrawAxis()
     c1.Update()
     #c1.Print("stack/"+canvasname+".pdf")
     c1.Print(plotrepo + "stack/"+canvasname+".png")
     del histo
     tmp.Delete()
     h.Delete()
     del tmp
     del h
     del h_sig
     h_err.Delete()
     del h_err
     h_bkg_err.Delete()
     del h_bkg_err
     hratio.Delete()
     del hratio
     stack.Delete()
     del stack
     pad1.Delete()
     del pad1
     pad2.Delete()
     del pad2
     c1.Delete()
     del c1
     for s in samples_:
          infile[s.label].Close()
          infile[s.label].Delete()
     os.system('set LD_PRELOAD=libtcmalloc.so')

#dataset_dict = {'2016':[],'2017':[],'2018':[]}
dataset_dict = {'2017':[],'2018':[]}

if(opt.dat != 'all'):
     if not(opt.dat in sample_dict.keys()):
          print "dataset not found!"
          print sample_dict.keys()
     print opt.dat
     if 'DataMET' in str(opt.dat):
          raise Exception("Not interesting dataset")
     elif 'DataHT' in str(opt.dat) and (opt.plot or opt.stack):
          raise Exception("Not interesting dataset")
     dataset_names = map(str, opt.dat.strip('[]').split(','))
     samples = []
     [samples.append(sample_dict[dataset_name]) for dataset_name in dataset_names]
     [dataset_dict[str(sample.year)].append(sample) for sample in samples]
else:
     for v in class_list:
          if 'DataHT' in v.label or 'DataMET' in v.label:
               continue
          dataset_dict[str(v.year)].append(v)
     '''
          '2017':[WpWpJJ_QCD_2017, WZ_2017, TT_2017, DYJetsToLL_2017, WJets_2017, WpWpJJ_EWK_2017, DataMu_2017, DataEle_2017],#, DataHT_2017],
          #'2016':[TT_2016, WJets_2016, WZ_2016, DYJetsToLL_2016, WpWpJJ_EWK_2016, WpWpJJ_QCD_2016],#[DataMu_2016, DataEle_2016, DataHT_2016],
          '2018':[TT_2018, WpWpJJ_QCD_2018, WZ_2018, DYJetsToLL_2018, WJets_2018, WpWpJJ_EWK_2018], #[DataMu_2017, DataEle_2017, DataHT_2017],
     }


          '2016':[TT_2016, WJets_2016, WZ_2016, DYJetsToLL_2016, WpWpJJ_EWK_2016, WpWpJJ_QCD_2016],#[DataMu_2016, DataEle_2016, DataHT_2016],
          '2018':[TT_2018, WpWpJJ_QCD_2018, WZ_2018, DYJetsToLL_2018, WJets_2018, WpWpJJ_EWK_2018, #[DataMu_2017, DataEle_2017, DataHT_2017],
     '''

for v in dataset_dict.values():
     print [o.label for o in v]

#print(dataset_dict.keys())

years = []
if(opt.year!='all'):
     years = map(str,opt.year.strip('[]').split(','))
else:
     years = ['2016','2017','2018']
print(years)

leptons = map(str,opt.lep.split(',')) 

cut = opt.cut #default cut must be obvious, for example lepton_eta>-10.

if opt.bveto:
     cut_dict = {'muon':"abs(lepton_pdgid)==13&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&(" + cut + ")", 
                 'electron':"abs(lepton_pdgid)==11&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&(" + cut + ")", 
                 'incl':"(abs(lepton_pdgid)==13||abs(lepton_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&(" + cut + ")", 
          }
     cut_tag = 'selection_upto_bveto'
     if opt.cut != "lepton_eta>-10.":
          cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut) 
elif opt.ttbar:
     cut_dict = {'muon':"abs(lepton_pdgid)==13&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==0&&pass_b_veto==0&&(" + cut + ")", 
                 'electron':"abs(lepton_pdgid)==11&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==0&&pass_b_veto==0&&(" + cut + ")", 
                 'incl':"(abs(lepton_pdgid)==13||abs(lepton_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==0&&pass_b_veto==0&&(" + cut + ")", 
          }
     cut_tag = 'ttbar_CR'
     if opt.cut != "lepton_eta>-10.":
          cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut)           
elif opt.wjets:
     cut_dict = {'muon':"abs(lepton_pdgid)==13&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_charge_selection==1&&((tau_DeepTau_WP/1000000)>=1)&&(((tau_DeepTau_WP%1000000)/1000)>=1)&&((tau_DeepTau_WP%1000)>=1)&&pass_b_veto==1&&MET_pt>=20.&&(" + cut + ")", 
                 'electron':"abs(lepton_pdgid)==11&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_charge_selection==1&&((tau_DeepTau_WP/1000000)>=1)&&(((tau_DeepTau_WP%1000000)/1000)>=1)&&((tau_DeepTau_WP%1000)>=1)&&pass_b_veto==1&&MET_pt>=20.&&(" + cut + ")",
                 'incl':"(abs(lepton_pdgid)==13||abs(lepton_pdgid)==11)&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_charge_selection==1&&((tau_DeepTau_WP/1000000)>=1)&&(((tau_DeepTau_WP%1000000)/1000)>=1)&&((tau_DeepTau_WP%1000)>=1)&&pass_b_veto==1&&MET_pt>=20.(" + cut + ")",
          }
     cut_tag = 'wjets_CR'
     if opt.cut != "lepton_eta>-10.":
          cut_tag = cut_tag+ '_AND_' + cutToTag(opt.cut)           
elif opt.sel:
     cut_dict = {'muon':"abs(lepton_pdgid)==13&&(" + cut + ")&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&pass_mjj_cut==1&&pass_MET_cut==1", 
                 'electron':"abs(lepton_pdgid)==11&&(" + cut + ")&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&pass_mjj_cut==1&&pass_MET_cut==1", 
                 'incl':"(abs(lepton_pdgid)==13||abs(lepton_pdgid)==11)&&(" + cut + ")pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1&&pass_charge_selection==1&&pass_jet_selection==1&&pass_b_veto==1&&pass_mjj_cut==1&&pass_MET_cut==1", 
          }
     cut_tag = "selection"
     if opt.cut != "lepton_eta>-10.":
          cut_tag = cut_tag + '_AND_' + cutToTag(opt.cut) 

else:
     cut_dict = {'muon':"abs(lepton_pdgid)==13&&(" + cut + ")",
                 'electron':"abs(lepton_pdgid)==11&&(" + cut + ")",
                 'incl':"(abs(lepton_pdgid)==13||abs(lepton_pdgid)==11)&&(" + cut + ")",
     }
     cut_tag = cutToTag(opt.cut)

lumi = {'2016': 35.9, "2017": 41.53, "2018": 59.7}

print cut_tag

for year in years:
    for sample in dataset_dict[year]:
          if(opt.merpart):
               mergepart(sample)
          if(opt.lumi):
               lumi_writer(sample, lumi[year])
          if(opt.mertree):
               mergetree(sample)

print "\nStarting"
for year in years:
     print year
     for lep in leptons:
          print lep
          dataset_new = dataset_dict[year]
          print [h.label for h in dataset_new]
          #dataset_new.remove(sample_dict['DataMET_'+str(year)])
          if lep == 'muon' and sample_dict['DataEle_'+str(year)] in dataset_new:
               dataset_new.remove(sample_dict['DataEle_'+str(year)])
          elif lep == 'electron' and sample_dict['DataMu_'+str(year)] in dataset_new:
               dataset_new.remove(sample_dict['DataMu_'+str(year)])

          variables = []
          wzero = 'w_nominal*PFSF*puSF'#*lepSF'
          cut = cut_dict[lep]


          variables.append(variabile('lepton_eta', 'lepton #eta', wzero+'*('+cut+')', 20, -5., 5.))
          variables.append(variabile('lepton_phi', 'lepton #phi',  wzero+'*('+cut+')', 14, -3.50, 3.50))
          bin_lepton_pt = array("f", [0., 100., 200., 300., 400., 600., 800., 1000., 1500.])
          nbin_lepton_pt = len(bin_lepton_pt)-1
          variables.append(variabile('lepton_pt',  'Lepton p_{T} [GeV]',  wzero+'*('+cut+')', nbin_lepton_pt, bin_lepton_pt))#30, 1500))


          variables.append(variabile('lepton_pdgid', 'lepton pdgid',  wzero+'*('+cut+')', 31, -15.5, 15.5))
          variables.append(variabile('lepton_pfRelIso04', 'lepton rel iso',  wzero+'*('+cut+')', 15, 0, 0.15))

          bin_taupt = array("f", [0., 100., 200., 300., 400., 600., 800., 1000., 1500.])
          nbin_taupt = len(bin_taupt) - 1
          variables.append(variabile('tau_pt',  '#tau p_{T} [GeV]',  wzero+'*('+cut+')', nbin_taupt, bin_taupt))
          variables.append(variabile('tau_eta', '#tau #eta',  wzero+'*('+cut+')', 20, -5, 5))
          variables.append(variabile('tau_phi', '#tau #Phi',  wzero+'*('+cut+')',  14, -3.50, 3.50))

          '''                                                                                                                                                                                                                                               
          variables.append(variabile('TMath::Log2(tau_DeepTauVsEle_WP+1)', 'log_2(#tau DeepTauVsEle WP)',  wzero+'*('+cut+')'+'*(tau_DeepTauVsEle_WP>0)',  8, -0.5, 7.5))                                                                                   
          variables.append(variabile('TMath::Log2(tau_DeepTauVsMu_WP+1)', 'log_2(#tau DeepTauVsMu WP)',  wzero+'*('+cut+')'+'*(tau_DeepTauVsMu_WP>0)',  4, -0.5, 3.5))                                                                                      
          variables.append(variabile('TMath::Log2(tau_DeepTauVsJet_WP+1)', 'log_2(#tau DeepTauVsJet WP)',  wzero+'*('+cut+')'+'*(tau_DeepTauVsJet_WP>0)',  8, -0.5, 7.5))                                                                                   
          '''

          variables.append(variabile('tau_DeepTauVsEle_raw', '#tau DeepTauVsEle raw',  wzero+'*('+cut+')',  20, 0.35, 1.35))
          variables.append(variabile('tau_DeepTauVsMu_raw', '#tau DeepTauVsMu raw',  wzero+'*('+cut+')',  20, 0.2, 1.2))
          variables.append(variabile('tau_DeepTauVsJet_raw', '#tau DeepTauVsJet raw',  wzero+'*('+cut+')',  20, 0.35, 1.35))

          bin_leadjet_pt = array("f", [0., 100., 200., 300., 400., 600., 800., 1000., 1500.])
          nbin_leadjet_pt = len(bin_leadjet_pt)-1
          variables.append(variabile('leadjet_pt',  'Lead jet p_{T} [GeV]',  wzero+'*('+cut+')', nbin_leadjet_pt, bin_leadjet_pt))#30, 1500))

          variables.append(variabile('leadjet_eta', 'Lead jet #eta',  wzero+'*('+cut+')', 20, -5., 5.))
          variables.append(variabile('leadjet_phi', 'Lead jet #Phi',  wzero+'*('+cut+')',  14, -3.50, 3.50))


          bin_subleadjet_pt = array("f", [0., 50., 100., 150., 200., 300., 400., 600., 1000.])
          nbin_subleadjet_pt = len(bin_subleadjet_pt) - 1
          variables.append(variabile('subleadjet_pt',  'Sublead jet p_{T} [GeV]',  wzero+'*('+cut+')', nbin_subleadjet_pt, bin_subleadjet_pt))#40, 30, 1000))
          variables.append(variabile('subleadjet_eta', 'Sublead jet #eta',  wzero+'*('+cut+')', 20, -5., 5.))
          variables.append(variabile('subleadjet_phi', 'Sublead jet #Phi',  wzero+'*('+cut+')',  14, -3.50, 3.50))

          variables.append(variabile('nJets', 'n jets',  wzero+'*('+cut+')',  11, -0.5, 10.5))
          variables.append(variabile('nBJets', 'n bjets (DeepJet M)',  wzero+'*('+cut+')',  6, -0.5, 5.5))

          bin_metpt = array("f", [0., 25., 50., 75., 100., 125., 150., 175., 200., 250., 300., 350., 400., 500., 600.])
          nbin_metpt = len(bin_metpt) - 1
          variables.append(variabile('MET_pt', 'p_{T}^{miss} [GeV]',  wzero+'*('+cut+')', nbin_metpt, bin_metpt))#30, 40, 500))

          bin_mjj = array("f", [0., 100., 200., 300., 400., 500., 600., 700., 800., 900., 1000., 1100., 1200., 1350., 1500., 1650., 1800., 2000., 2200.])
          nbin_mjj = len(bin_mjj) - 1 
          variables.append(variabile('mjj', 'M_{jj} [GeV]',  wzero+'*('+cut+')', nbin_mjj, bin_mjj))# 20, 500, 2000))

          bin_mTs = array("f", [0., 25., 50., 75., 100., 125., 150., 200., 250., 300., 400., 500.])
          nbin_mTs = len(bin_mTs) - 1

          variables.append(variabile('mT_lep_MET', 'M_{T}(lep, MET) [GeV]',  wzero+'*('+cut+')', nbin_mTs, bin_mTs))
          variables.append(variabile('mT_tau_MET', 'M_{T}(#tau, MET) [GeV]',  wzero+'*('+cut+')', nbin_mTs, bin_mTs))
          variables.append(variabile('mT_leptau_MET', 'M_{T}(lep, #tau, MET) [GeV]',  wzero+'*('+cut+')', nbin_mTs, bin_mTs))

          bin_deltaeta_jj = array("f", [0., 0.2, 0.4, 0.6, 0.8, 1., 1.2, 1.4, 1.6, 1.8, 2., 2.2, 2.4, 2.6, 2.8, 3., 3.2, 3.4, 3.6, 3.8, 4., 4.2, 4.4, 4.6, 4.8, 5., 5.2, 5.4, 5.6, 5.8, 6., 6.4, 6.8, 7.2, 8., 8.8, 10.])
          nbin_deltaeta_jj = len(bin_deltaeta_jj) - 1
          variables.append(variabile('deltaEta_jj', '#Delta #eta_{jj}',  wzero+'*('+cut+')', nbin_deltaeta_jj, bin_deltaeta_jj))#20, 0, 10))

          variables.append(variabile('deltaPhi_jj', '#Delta #phi_{jj}',  wzero+'*('+cut+')',  16, -4., 4.))
          variables.append(variabile('deltaPhi_taulep', '#Delta #phi_{#tau l}',  wzero+'*('+cut+')',  16, -4., 4.))
          variables.append(variabile('deltaPhi_tauj1', '#Delta #phi_{#tau j_{1}}',  wzero+'*('+cut+')',  16, -4., 4.))
          variables.append(variabile('deltaPhi_tauj2', '#Delta #phi_{#tau j_{2}}',  wzero+'*('+cut+')',  16, -4., 4.))
          variables.append(variabile('deltaPhi_lepj1', '#Delta #phi_{l j_{1}}',  wzero+'*('+cut+')', 16, -4., 4.))
          variables.append(variabile('deltaPhi_lepj2', '#Delta #phi_{l j_{2}}',  wzero+'*('+cut+')', 16, -4., 4.))


          for sample in dataset_new:
               if 'DataHT' in sample.label or 'DataMET' in sample.label:
                    continue
               if(opt.plot):
                    for var in variables:
                         if (("GenPart" in var._name) or ("MC_" in var._name)) and "Data" in sample.label:
                              continue
                         plot(lep, 'jets', var, sample, cut_tag, "")

          if(opt.stack):
               for var in variables:
                    print var._xmax
                    os.system('set LD_PRELOAD=libtcmalloc.so')
                    makestack(lep, 'jets', var, dataset_new, cut_tag, "", lumi[str(year)])
                    os.system('set LD_PRELOAD=libtcmalloc.so')

          if lep == 'muon':
               dataset_new.append(sample_dict['DataEle_'+str(year)])
          elif lep == 'electron':
               dataset_new.append(sample_dict['DataMu_'+str(year)])
