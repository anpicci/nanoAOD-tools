import ROOT
import ROOT.TMath as TMath
import math
import cmath
import copy as copy
from os import path
import array
import types
from Object import *
from Event import *


class Collection:
    def __init__(self,event,prefix,lenVar=None):
        self._event = event
        self._prefix = prefix
        if lenVar != None:
            self._len = getattr(event,lenVar)
        else:
            self._len = getattr(event,"n"+prefix)
        self._cache = {}
    def __getitem__(self,index):
        if type(index) == int and index in self._cache: return self._cache[index]
        if index >= self._len: raise IndexError("Invalid index %r (len is %r) at %s" % (index,self._len,self._prefix))
        ret = Object(self._event,self._prefix,index=index)
        if type(index) == int: self._cache[index] = ret
        return ret
    def __len__(self):
        return self._len