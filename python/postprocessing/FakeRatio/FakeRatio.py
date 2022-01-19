from cgitb import handler
import os
import sys
from unittest import installHandler
import ROOT
import math
import datetime
import copy
from array import array
from systWeights import *
from OutTTreeHandler import *
from InTreeHandler import *
from file_list import *

outhandler = OutTTreeHandler("calamaretti")
inhandler = InTreeHandler(file_list)
inhandler.getOutTree(outhandler)
inhandler.SetupChain()
inhandler.loopInTTree()

#not checking the MC stuff, remember to add it