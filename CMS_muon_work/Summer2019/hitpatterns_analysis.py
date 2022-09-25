import ROOT
import sys
from array import array
import matplotlib.pyplot as plt

infilename = sys.argv[1]
#infile2 = sys.argv[2]

f = ROOT.TFile.Open(infilename)
#g = ROOT.TFile.Open(infile2)

t = f.Get("Events")
#t1 = g.Get("Events")

#outputFile = ROOT.TFile.Open("hitpatterns.root", "RECREATE");
#outtree = ROOT.TTree('tout', 'Output tree')

DTHits_gc = []
CSCHits_gc = []
RPCHits_gc = []

DTHits_sa = []
CSCHits_sa = []
RPCHits_sa = []


nentries = t.GetEntries()
#nuntries = t1.GetEntries()

for i in range(nentries):
	t.GetEvent(i)

	n = t.nHits

	for i in range(n):
		DTHits_gc.append(t.DT_gcHits[i])
		CSCHits_gc.append(t.CSC_gcHits[i])
		RPCHits_gc.append(t.RPC_gcHits[i])

		DTHits_sa.append(t.DT_saHits[i])
		CSCHits_sa.append(t.CSC_saHits[i])
		RPCHits_sa.append(t.RPC_saHits[i])

	


f, axes = plt.subplots()

plt.hist(DTHits_sa, bins = 100, alpha=0.5,label="standalone muon DT Hits")
plt.hist(DTHits_gc, bins = 100, alpha=0.5,label="global cosmic muon DT Hits")

axes.set_ylabel("Frequency")
axes.set_xlabel("Number of hits")
axes.set_title("Drift tube hits for global cosmic and standalone muons")

plt.legend()


f, axes = plt.subplots()

plt.hist(CSCHits_sa, bins = 100, alpha=0.5,label="standalone muon CSC Hits")
plt.hist(CSCHits_gc, bins = 100, alpha=0.5,label="global cosmic muon CSC Hits")

axes.set_ylabel("Frequency")
axes.set_xlabel("Number of hits")
axes.set_title("Cathode Strip Chamber hits for global cosmic and standalone muons")

plt.legend()


f, axes = plt.subplots()

plt.hist(RPCHits_sa, bins = 100, alpha=0.5,label="standalone muon RPC Hits")
plt.hist(RPCHits_gc, bins = 100, alpha=0.5,label="global cosmic muon RPC Hits")

axes.set_ylabel("Frequency")
axes.set_xlabel("Number of hits")
axes.set_title("Resistive plate chamber hits for global cosmic and standalone muons")

plt.legend()

plt.show()
