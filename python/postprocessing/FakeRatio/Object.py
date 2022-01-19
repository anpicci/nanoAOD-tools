import ROOT
import ROOT.TMath as TMath
import math
import cmath
import copy as copy
from os import path
import array
import types
from CutsAndValues import *
from Event import *
from Collection import *


class Object:
    """Class that allows seeing a set branches plus possibly an index as an Object"""
    def __init__(self,event,prefix,index=None):
        self._event = event
        if not (prefix == 'LHEPdfWeight' or prefix == 'LHEScaleWeight' or prefix == 'PSWeight'):
            self._prefix = prefix+"_"
        else:
            self._prefix = prefix
        self._index = index
    def __getattr__(self,name):
        if name in self.__dict__: return self.__dict__[name]
        if name[:2] == "__" and name[-2:] == "__":
            raise AttributeError
        val = getattr(self._event,self._prefix+name)
        if self._index != None:
            val = val[self._index]
        val = ord(val) if type(val)==str else val # convert char to integer number
        self.__dict__[name] = val ## cache
        return val
    def __getitem__(self,attr):
        return self.__getattr__(attr)
    def p4(self):
        ret = ROOT.TLorentzVector()
        ret.SetPtEtaPhiM(self.pt,self.eta,self.phi,self.mass)
        return ret
    def DeltaR(self,other):
        if isinstance(other,ROOT.TLorentzVector):
          deta = abs(other.Eta()-self.eta)
          dphi = abs(other.Phi()-self.phi)
        else:
          deta = abs(other.eta-self.eta)
          dphi = abs(other.phi-self.phi)
        while dphi > math.pi:
          dphi = abs(dphi - 2*math.pi)
        return math.sqrt(dphi**2+deta**2)
    def subObj(self,prefix):
        return Object(self._event,self._prefix+prefix)
    def __repr__(self):
        return ("<%s[%s]>" % (self._prefix[:-1],self._index)) if self._index != None else ("<%s>" % self._prefix[:-1])
    def __str__(self):
        return self.__repr__()