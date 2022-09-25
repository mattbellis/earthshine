import ROOT
import sys

import numpy as np
import matplotlib.pylab as plt

infilename = sys.argv[1]

f = ROOT.TFile(infilename)
t = f.Get("Events")

t.Print()

exit()

nevents = t.GetEntries()

for i in range(nevents):

    t.GetEvent(i)

    x = t.PSimHits_g4SimHits_MuonCSCHits_SIM
