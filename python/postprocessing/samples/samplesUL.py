import ROOT
import os 
#import json_reader as jr

path = os.path.dirname(os.path.abspath(__file__))

class sample:
    def __init__(self, color, style, fill, leglabel, label, name=""):
        self.color = color
        self.style = style
        self.fill = fill
        self.leglabel = leglabel
        self.label = label
        if name == "":
            self.name = label
        else:
            self.name = name

tag_2016  = 'RunIISummer16NanoAODv7-PUMoriond17_Nano02Apr2020_102X_mcRun2_asymptotic_v8'
tag_2017  = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_102X_mc2017_realistic_v8'
tag1_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_v2_102X_mc2017_realistic_v8'
tag2_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_new_pmx_102X_mc2017_realistic_v8'
tag3_2017 = 'RunIIFall17NanoAODv7-PU2017_12Apr2018_Nano02Apr2020_EXT_102X_mc2017_realistic_v8'
tag_2018 = 'RunIIAutumn18NanoAODv7-Nano02Apr2020_102X_upgrade2018_realistic_v21'

### ZZtoLep ###

ZZTo2L2Nu_2016APV = sample(ROOT.kGray+2, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_2016APV")
ZZTo2L2Nu_2016APV.year = "2016APV"
ZZTo2L2Nu_2016APV.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo2L2Nu_2016APV.sigma = 0.9738 #pb

ZZTo2L2Nu_2016 = sample(ROOT.kGray+2, 1, 1001, "ZZ --> 2l2\nu", "ZZTo2L2Nu_2016APV")
ZZTo2L2Nu_2016.year = "2016"
ZZTo2L2Nu_2016.dataset = "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"
ZZTo2L2Nu_2016.sigma = 0.9738 #pb

sample_dict={
}

merge_dict={
}


class_list=[
]

class_list_bis = [
]

