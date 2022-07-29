import ROOT
import sys
from array import array

infilename = sys.argv[1]

f = ROOT.TFile.Open(infilename)

t = f.Get("Events")

#nentries = t.GetEntries()

outputFile = ROOT.TFile.Open("globalCosmicStep3.root", "RECREATE");
outtree = ROOT.TTree('tout', 'Output tree')

data = {}

data['nglobalCosmic'] = ['gc_q', 'gc_p', 'gc_px', 'gc_py', 'gc_pz', 'gc_pt', 'gc_eta', 'gc_phi', 'gc_theta']

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

	muons = t.recoTracks_globalCosmicMuons__RECO

	for n,a in enumerate(muons.product()):
		if n < 1024:
			outdata['gc_q'][n] = a.charge()
			outdata['gc_p'][n] = a.p()
			outdata['gc_px'][n] = a.px()
			outdata['gc_py'][n] = a.py()
			outdata['gc_pz'][n] = a.pz()
			outdata['gc_pt'][n] = a.pt()
			outdata['gc_eta'][n] = a.eta()
			outdata['gc_phi'][n] = a.phi()
			outdata['gc_theta'][n] = a.theta()
			outdata['nglobalCosmic'][0] = n + 1


	outtree.Fill()

outputFile.Write()
outputFile.Close()
