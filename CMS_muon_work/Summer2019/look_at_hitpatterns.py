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

outputFile = ROOT.TFile.Open("hitpatterns1.root", "RECREATE");
outtree = ROOT.TTree('tout', 'Output tree')

data = {}

data['nHits'] = ['DT_saHits', 'CSC_saHits', 'RPC_saHits', 'DT_gcHits', 'CSC_gcHits', 'RPC_gcHits']
outdata = {}

for key in data.keys():
        outdata[key] = array('i', [-1])
        outtree.Branch(key, outdata[key], key + "/I")

        for branch in data[key]:
                outdata[branch] = array('f', 1024 * [-1.])
                outtree.Branch(branch, outdata[branch], '{0}[{1}]/F'.format(branch,key))


nentries = t.GetEntries()
#nuntries = t1.GetEntries()

for i in range(1):
#for i in range(nentries):
	t.GetEvent(i)

	muons = t.recoTracks_globalCosmicMuons__RECO

	for n,a in enumerate(muons.product()):
		if n < 1024:
			outdata['DT_gcHits'][n] = a.hitPattern().numberOfValidMuonDTHits()
			outdata['CSC_gcHits'][n] = a.hitPattern().numberOfValidMuonCSCHits()
			outdata['RPC_gcHits'][n] = a.hitPattern().numberOfValidMuonRPCHits()
			outdata['nHits'][0] = n + 1
	muon2 = t.recoTracks_standAloneMuons__RECO

	for n,a in enumerate(muon2.product()):
		if n < 1024:
			outdata['DT_saHits'][n] = a.hitPattern().numberOfValidMuonDTHits()
			outdata['CSC_saHits'][n] = a.hitPattern().numberOfValidMuonCSCHits()
			outdata['RPC_saHits'][n] = a.hitPattern().numberOfValidMuonRPCHits()
			outdata['nHits'][0] = n + 1

	outtree.Fill()

outputFile.Write()
outputFile.Close()

