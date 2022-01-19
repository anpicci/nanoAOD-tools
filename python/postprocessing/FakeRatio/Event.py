import ROOT
import ROOT.TMath as TMath
import math
import cmath
import copy as copy
from os import path
import array
import types
from Object import *
from Collection import *

class Event:
    """Class that allows seeing an entry of a PyROOT TTree as an Event"""
    def __init__(self,tree,entry):
        self._tree = tree
        self._entry = entry
        self._tree.gotoEntry(entry)
    def __getattr__(self,name):
        if name in self.__dict__: return self.__dict__[name]
        return self._tree.readBranch(name)
    def __getitem__(self,attr):
        return self.__getattr__(attr)
    def eval(self,expr):
        """Evaluate an expression, as TTree::Draw would do. 

           This is added for convenience, but it may perform poorly and the implementation is not bulletproof,
           so it's better to rely on reading values, collections or objects directly
        """ 
        if not hasattr(self._tree, '_exprs'):
            self._tree._exprs = {}
            # remove useless warning about EvalInstance()
            import warnings
            warnings.filterwarnings(action='ignore', category=RuntimeWarning, 
                                    message='creating converter for unknown type "const char\*\*"$')
            warnings.filterwarnings(action='ignore', category=RuntimeWarning, 
                                    message='creating converter for unknown type "const char\*\[\]"$')
        if expr not in self._tree._exprs:
            formula = ROOT.TTreeFormula(expr,expr,self._tree)
            if formula.IsInteger():
                formula.go = formula.EvalInstance64
            else:
                formula.go = formula.EvalInstance
            self._tree._exprs[expr] = formula
            # force sync, to be safe
            self._tree.GetEntry(self._entry)
            self._tree.entry = self._entry
            #self._tree._exprs[expr].SetQuickLoad(False)
        else:
            self._tree.gotoEntry(entry)
            formula = self._tree._exprs[expr]
        if "[" in expr: # unclear why this is needed, but otherwise for some arrays x[i] == 0 for all i > 0
            formula.GetNdata()
        return formula.go()