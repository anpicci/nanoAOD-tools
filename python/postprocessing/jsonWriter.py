from samples.samplesUL import *
import json


class singleSample:
    sigma = -999
    dataset = ''
    year = -999
    def __init__(self, sigma, dataset, year):
        self.sigma = sigma
        self.dataset = dataset
        self.year = year
    
    def printt(self):
        print('dataset: ', self.dataset)
        print('sigma:   ', self.sigma)
        print('year:    ', self.year)

    def jOut(self):
        output = {
            'dataset' : self.dataset,
            'sigma'   : self.sigma,
            'year'    : self.year
        }
        return output

class process:
    components = []
    color = -999
    style = -999
    fill = -999
    label = ''
    def __init__(self, color, style, fill, label):
        self.components = []
        self.color = color
        self.style = style
        self.fill = fill
        self.label = label

    def addSample(self, s):
        self.components.append(s)

    def printt(self):
        print (self.label)
        for s in self.components:
            s.printt()

    def jOut(self):
        components = []
        for j in self.components:
            components.append(j.jOut()) 
        out = {
            'label'      : self.label,
            'components' : components,
            'color'      : self.color,
            'style'      : self.style,
            'fill'       : self.fill,
        }
        return out

fileName = 'samples/samplesUL.json'
print('checking if sample files exist already')
if os.path.exists(fileName):
    a = input('it does... removing previous one, press y to proceed, any other key to stop \n')
    if a == 'y': 
        os.popen('rm ' + fileName)

allSamples = {}
allSamples['condor_dict'] = []

for s in condor_dict.items():
    #print(s[0])
    data = {}
    data['sample'] = []
    label = s[1].label
    color = s[1].color
    style = s[1].style
    fill = s[1].fill 
    label = s[1].label
    
    p = process(color, style, fill, label)
    print('label from condor: ',s[0])
    components = s[1].components
    if components == None:
        p.addSample(singleSample(s[1].sigma, s[1].dataset, s[1].year))
    if components != None:
        for k in components:
            p.addSample(singleSample(k.sigma, k.dataset, k.year))
    allSamples['condor_dict'].append(p.jOut())


with open(fileName, 'a') as f:
    json.dump(allSamples, f, indent = 4)
