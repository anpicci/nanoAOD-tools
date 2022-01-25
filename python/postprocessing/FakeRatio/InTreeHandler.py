import ROOT
import os
import sys
import math
import datetime
import copy
from OutTTreeHandler import *
from systWeights import *
from Event import *
from Object import *
from Collection import *

class InTreeHandler:
    def __init__(self, file_list):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, " --- INIT InTreeHandler ---")
        print('Adding: ', len(file_list), 'files to the chain')
        self.chain = ROOT.TChain('Events')
        for infile in file_list: 
            print("Adding %s to the chain" %(infile))
            self.chain.Add(infile)
        print(self.chain)
        print('# Events: ', self.chain.GetEntries())
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, " --- ENDED INIT InTreeHandler ---")

    def _makeArrayReader(tree, typ, nam):
        if not tree._ttreereader._isClean: _remakeAllReaders(tree)
        ttra = ROOT.TTreeReaderArray(typ)(tree._ttreereader, nam)
        tree._leafTypes[nam] = typ
        tree._ttras[nam] = ttra;
        return tree._ttras[nam]

    def _makeValueReader(tree, typ, nam):
        if not tree._ttreereader._isClean: _remakeAllReaders(tree)
        ttrv = ROOT.TTreeReaderValue(typ)(tree._ttreereader, nam)
        tree._leafTypes[nam] = typ
        tree._ttrvs[nam] = ttrv
        return tree._ttrvs[nam]
    
    
    def _remakeAllReaders(tree):
        _ttreereader = ROOT.TTreeReader(tree, getattr(tree, '_entrylist', None))
        _ttreereader._isClean = True
        _ttrvs = {}
        for k in tree._ttrvs.keys():
            _ttrvs[k] = ROOT.TTreeReaderValue(tree._leafTypes[k])(_ttreereader,k)
        _ttras = {}
        for k in tree._ttras.keys():
            _ttras[k] = ROOT.TTreeReaderArray(tree._leafTypes[k])(_ttreereader,k)
        tree._ttrvs = _ttrvs
        tree._ttras = _ttras
        tree._ttreereader = _ttreereader
        tree._ttreereaderversion += 1

    def _readAllBranches(tree):
        tree.GetEntry(_currentTreeEntry(tree))

    def _currentTreeEntry(tree):
        if tree._entrylist:
            return tree._entrylist.GetEntry(tree.entry)
        else:
            return tree.entry

    def _gotoEntry(tree, entry, forceCall=False):
        print("in _gotoEntry")
        print(type(tree))
        print(tree)

        tree._ttreereader._isClean = False
        if tree.entry != entry or forceCall:
            if (tree.entry == entry-1 and entry!=0):
                tree._ttreereader.Next()
            else:
                tree._ttreereader.SetEntry(entry)
            tree.entry = entry

    def getArrayReader(tree, branchName):
        """Make a reader for branch branchName containing a variable-length value array."""
        if branchName not in tree._ttras:
            if not tree.GetBranch(branchName): raise RuntimeError("Can't find branch '%s'" % branchName)
            leaf = tree.GetBranch(branchName).GetLeaf(branchName)
            if not bool(leaf.GetLeafCount()): raise RuntimeError("Branch %s is not a variable-length value array" % branchName)
            typ = leaf.GetTypeName()
            tree._ttras[branchName] = _makeArrayReader(tree, typ, branchName)
        return tree._ttras[branchName]

    def getValueReader(tree, branchName):
        """Make a reader for branch branchName containing a single value."""
        if branchName not in tree._ttrvs:
            if not tree.GetBranch(branchName): raise RuntimeError("Can't find branch '%s'" % branchName)
            leaf = tree.GetBranch(branchName).GetLeaf(branchName)
            if bool(leaf.GetLeafCount()) or leaf.GetLen()!=1 : raise RuntimeError("Branch %s is not a value" % branchName)
            typ = leaf.GetTypeName()
            tree._ttrvs[branchName] = _makeValueReader(tree, typ, branchName)
        return tree._ttrvs[branchName]

    def clearExtraBranches(tree):
        tree._extrabranches = {}

    def setExtraBranch(tree,name,val):
        tree._extrabranches[name] = val

    def readBranch(tree, branchName):
        """Return the branch value if the branch is a value, and a TreeReaderArray if the branch is an array"""
        if tree._ttreereader._isClean: raise RuntimeError("readBranch must not be called before calling gotoEntry")
        if branchName in tree._extrabranches:
            return tree._extrabranches[branchName]
        elif branchName in tree._ttras:
            return tree._ttras[branchName]
        elif branchName in tree._ttrvs: 
            ret = tree._ttrvs[branchName].Get()[0]
            return ord(ret) if type(ret)==str else ret
        else:
            branch = tree.GetBranch(branchName)
            if not branch: raise RuntimeError("Unknown branch %s" % branchName)
            leaf = branch.GetLeaf(branchName)
            typ = leaf.GetTypeName()
            if leaf.GetLen() == 1 and not bool(leaf.GetLeafCount()): 
                _vr = _makeValueReader(tree, typ, branchName)
                tree.gotoEntry(tree.entry,forceCall=True) # force calling SetEntry as a new ValueReader was created
                ret = _vr.Get()[0]
                return ord(ret) if type(ret)==str else ret
            else:
                _ar = _makeArrayReader(tree, typ, branchName)
                tree.gotoEntry(tree.entry,forceCall=True) # force calling SetEntry as a new ArrayReader was created
                return _ar

    def SetupChain(self, entrylist=ROOT.nullptr):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, " --- ADDING add to the PyROOT wrapper of a TTree a TTreeReader and methods readBranch, arrayReader, valueReader ---")
        if hasattr(self.chain, '_ttreereader'): 
            print('WARNING: SETUP DONE BEFORE')
            return False # don't initialize twice
        self.chain.entry = -1
        self.chain._entrylist = entrylist
        self.chain._ttreereader = ROOT.TTreeReader(self.chain,self.chain._entrylist)
        self.chain._ttreereader._isClean = True
        self.chain._ttrvs = {}
        self.chain._ttras = {}
        self.chain._leafTypes = {}
        self.chain._ttreereaderversion = 1
        self.chain.arrayReader      = types.MethodType(self.getArrayReader, self.chain)
        self.chain.valueReader      = types.MethodType(self.getValueReader, self.chain)
        self.chain.readBranch       = types.MethodType(self.readBranch, self.chain)
        self.chain.gotoEntry        = types.MethodType(self._gotoEntry, self.chain)
        self.chain.readAllBranches  = types.MethodType(self._readAllBranches, self.chain)
        self.chain.entries          = self.chain._ttreereader.GetEntries(False)
        self.chain._extrabranches   = {}
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, " --- ENDED PyRoot wrapping ---")
        
    def getOutTree(self, out):
        self.OutTree = out

    def loopInTTree(self):

        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time, " --- STARTING TO LOOP OVER THE TTREE ---")
        self.SetupChain()
        for i in range(self.chain.GetEntries()):
            print('Processing event: ', i, "\r")
            event       = Event(self.chain, i)
            electrons   = Collection(event, "Electron")
            muons       = Collection(event, "Muon")
            jets        = Collection(event, "Jet")
            fatjets     = Collection(event, "FatJet")
            taus        = Collection(event, "Tau")
            HT          = Object(event,     "HT")
            PV          = Object(event,     "PV")
            HLT         = Object(event,     "HLT")
            Flag        = Object(event,     'Flag')
            met         = Object(event,     "MET")
            puppimet    = Object(event,     "PuppiMET")

            njets       = len(list(jets))


        print('\n',current_time, " --- ENDED TO LOOP OVER THE TTREE ---")
    
    
        
