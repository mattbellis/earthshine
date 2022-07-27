import ROOT
import sys
from array import array

infilename = sys.argv[1]

f = ROOT.TFile.Open(infilename)

t = f.Get("Events")

#nentries = t.GetEntries()

outputFile = ROOT.TFile.Open("standAloneStep3.root", "RECREATE");
outtree = ROOT.TTree('tout', 'Output tree')

data = {}

data['nstandAlone'] = ['sa_q', 'sa_p', 'sa_px', 'sa_py', 'sa_pz', 'sa_pt', 'sa_eta', 'sa_phi', 'sa_theta']

outdata = {}

for key in data.keys():
	outdata[key] = array('i', [-1])
	outtree.Branch(key, outdata[key], key + "/I")

	for branch in data[key]:
		outdata[branch] = array('f', 1024 * [-1.])
		outtree.Branch(branch, outdata[branch], '{0}[{1}]/F'.format(branch,key))

nentries = t.GetEntries()


for i in range(nentries):
	t.GetEvent(i)

	muons = t.recoTracks_standAloneMuons__RECO

	for n,a in enumerate(muons.product()):
		if n < 1024:
			outdata['sa_q'][n] = a.charge()
			outdata['sa_p'][n] = a.p()
			outdata['sa_px'][n] = a.px()
			outdata['sa_py'][n] = a.py()
			outdata['sa_pz'][n] = a.pz()
			outdata['sa_pt'][n] = a.pt()
			outdata['sa_eta'][n] = a.eta()
			outdata['sa_phi'][n] = a.phi()
			outdata['sa_theta'][n] = a.theta()
			outdata['nstandAlone'][0] = n + 1


	outtree.Fill()

outputFile.Write()
outputFile.Close()
