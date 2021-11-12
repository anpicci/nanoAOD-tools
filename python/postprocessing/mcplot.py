import ROOT
import os
import sys
import time
from CutsAndValues import *

deltacut = bool(int(sys.argv[2]))
print "deltacut?", deltacut

v = sys.argv[1]

ifolder = "/eos/home-a/apiccine/VBS/nosynch/vmcreco" + v + "/ltau"
ofolder = '/eos/home-a/apiccine/VBS/nosynch/vmcreco' + v + '/plots_jetleptonselections'#_bveto'#

ROOT.gROOT.SetBatch()

if deltacut:
    ofolder += "_deltacut"

if not os.path.exists(ofolder):
    os.makedirs(ofolder)
else:
    os.system("rm -rf " + ofolder + "/*")

prevar = [
    'm_jj',
    'leadjet_IsGenMatched',
    'subleadjet_IsGenMatched',
    'lepton_IsGenMatched',
    'tau_IsGenMatched',
    'deltaEta_jj',
    'leadjet_pt',
    'subleadjet_pt',
    'lepton_pt',
    'tau_pt',
    'lepton_eta',
    'tau_eta',
    'lepton_Zeppenfeld_over_deltaEta_jj',
    'tau_Zeppenfeld_over_deltaEta_jj',
    'event_Zeppenfeld_over_deltaEta_jj',
]


lepcut = "pass_jet_selection==1&&pass_lepton_selection==1&&pass_lepton_veto==1&&pass_tau_selection==1"#&&pass_b_veto==1"


#if not "GenMatched" in prevar:
alist = ['gen', 'gm', 'm', '']
titles = ['GenJets', 'GenMatched Jets', 'Highest Mass Jets', 'Leading Jets']    
colours = [ROOT.kBlack, ROOT.kBlue, ROOT.kRed, ROOT.kGreen+2]

varl = []
for pv in prevar:
    tmpl = []
    for a in alist:
        if "GenMatched" in pv and a == "gen":
            continue
        if "tau" in pv and "GenMatched" in pv and (a == "gen" or a == "gm"):
            continue

        tn = ""
        tn = a + pv
        tmpl.append(tn)
    varl.append(tmpl)

bins_dict = {
    'm_jj': [0., 4000., 80., "m_{jj} [GeV]", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'lepton_IsGenMatched': [-0.5, 1.5, 2, "Is lepton GenMatched?", 700, 560, 0.15, 0.7, 0.45, 0.9],
    'tau_IsGenMatched': [-0.5, 1.5, 2, "Is #tau GenMatched?", 700, 560, 0.15, 0.7, 0.45, 0.9],
    'leadjet_IsGenMatched': [-0.5, 1.5, 2, "Is j_{1} GenMatched?", 700, 560, 0.15, 0.7, 0.45, 0.9],
    'subleadjet_IsGenMatched': [-0.5, 1.5, 2, "Is j_{2} GenMatched?", 700, 560, 0.15, 0.7, 0.45, 0.9],
    'deltaEta_jj': [-10., 10., 80, "#Delta#eta_{jj}", 700, 560, 0.7, 0.75, 0.95, 0.9],
    'leadjet_pt': [0., 800., 80, "j_{1} p_{T}", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'subleadjet_pt': [0., 400., 40, "j_{2} p_{T}", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'lepton_pt': [0., 200., 40, "lepton p_{T}", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'tau_pt': [0., 200., 40, "#tau p_{T}", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'lepton_eta': [-3., 3., 24, "lepton #eta", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'tau_eta': [-3., 3., 24, "#tau #eta", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'lepton_Zeppenfeld_over_deltaEta_jj': [-1.5, 1.5, 24, "lepton z", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'tau_Zeppenfeld_over_deltaEta_jj': [-1.5, 1.5, 24, "#tau z", 700, 560, 0.6, 0.5, 0.9, 0.7],
    'event_Zeppenfeld_over_deltaEta_jj': [-1.5, 1.5, 24, "event z", 700, 560, 0.6, 0.5, 0.9, 0.7],
}

countf = open(ofolder + "/countings.txt", "a")

for vvarl in varl:
    hnames = ["h_" + v for v in vvarl]

    namevar = vvarl[-1]
    title_var = bins_dict[namevar][3]

    htitles = []
    for t in range(len(titles)):
        if len(vvarl)==3 and titles[t] == "GenJets":
            continue
        ttitle = titles[t] + ";" + title_var + ";Countings"
        htitles.append(ttitle)

    wc = bins_dict[namevar][4]
    hc = bins_dict[namevar][5]

    x1 = bins_dict[namevar][6]
    y1 = bins_dict[namevar][7]
    x2 = bins_dict[namevar][8]
    y2 = bins_dict[namevar][9]

    xmin = bins_dict[namevar][0]
    xmax = bins_dict[namevar][1]
    nbin = int(bins_dict[namevar][2])

    filemc = ROOT.TFile.Open(ifolder + "/VBS_SSWW_SM_2017/VBS_SSWW_SM_2017.root")

    histos = [ROOT.TH1F(hnames[hi], htitles[hi], nbin, xmin, xmax) for hi in range(len(hnames))]

    print histos

    trsignal = filemc.Get("events_all")

    #for h in histos:
        #print h.GetName(), h.GetTitle()

    coa = ROOT.TCanvas("coa", "coa")#, wc, hc)
    #coa.SetWindowSize(wc + (wc - coa.GetWw()), hc + (hc - coa.GetWh()))
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetOptTitle(0)

    leg_stack_oa = ROOT.TLegend(x1,y1,x2,y2)

    opthist = "hist same"

    countf.write("\n")

    for hi, h in enumerate(histos):
        countf.write(h.GetName() + "\n")
        cuth = lepcut

        if deltacut:
            if not (vvarl[hi].startswith("g")):
                cuth = "abs(" + alist[-len(histos)+hi] + "deltaEta_jj)>" + str(DELTAETA_JJ_CUT) + "&&" + cuth
            else:
                cuth = "(abs(deltaEta_jj)>" + str(DELTAETA_JJ_CUT) + "||abs(mdeltaEta_jj)>" + str(DELTAETA_JJ_CUT) + ")&&" + cuth
        
        #print h.GetName(), vvarl[hi], cuth

        trsignal.Project(h.GetName(), vvarl[hi], cuth)

        if "GenMatched" in namevar:
            ovhi = 1./float(h.Integral())
            h.Scale(ovhi)

        countf.write("Integral:" + str(h.Integral()) + "\n")

        h.SetLineColor(colours[-len(histos)+hi])
        h.Draw(opthist)
        leg_stack_oa.AddEntry(h, h.GetTitle(), "f")

    maxs = [h.GetMaximum()*1.1 for h in histos]
    maxe = max(maxs)

    for h in histos:
        h.GetYaxis().SetRangeUser(0.0001, maxe)

    leg_stack_oa.Draw("same")
    ROOT.gStyle.SetOptStat(0)
    coa.Print(ofolder + "/" + namevar + ".png")
    #coa.SetLogy(1)
    #coa.Print("./mcplots" + folder.split("/")[0] + "/" + namevar + "_logy.png")

    #try:
    #wait = input("Press Enter to continue.")
    #except:
    
    #time.sleep(5)
    filemc.Close()

countf.close()
print "Bye!"
