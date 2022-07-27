import ROOT
import sys
from array import array

infilename = sys.argv[1]

f = ROOT.TFile.Open(infilename)

t = f.Get("Events")

outputFile = ROOT.TFile.Open("refPoints.root", "RECREATE");
outtree = ROOT.TTree("tout", 'Output tree')

data = {}

data['nrefPts'] = ['gc_refX', 'gc_refY', 'gc_refZ', 'sa_refX', 'sa_refY', 'saRefZ', 'gc_dxy', 'gc_dz', 'sa_dxy', 'sa_dz']


outdata = {}

for key in data.keys():
        outdata[key] = array('i', [-1])
        outtree.Branch(key, outdata[key], key + "/I")

        for branch in data[key]:
                outdata[branch] = array('f', 1024 * [-1.])
                outtree.Branch(branch, outdata[branch], '{0}[{1}]/F'.format(branch, key))


nentries = t.GetEntries()

for i in range(nentries):
	t.GetEvent(i)

	muon = t.recoTracks_globalCosmicMuons__RECO
	muon2 = t.recoTracks_standAloneMuons__RECO

	for n,a in enumerate(muon.product()):
		if n < 1024:
			pt = a.referencePoint()
			rX = pt.X()
			rY = pt.Y()
			rZ = pt.Z()
			#print(rX)

			dxy = a.dxy()
			dz = a.dz()

			outdata['gc_refX'][n] = rX
			outdata['gc_refY'][n] = rY
			outdata['gc_refZ'][n] = rZ
			outdata['gc_dxy'][n] = dxy
			outdata['gc_dz'][n] = dz
			outdata['nrefPts'][0] = n+1
	x = outdata['nrefPts'][0]
	for n,a in enumerate(muon2.product()):
		if n < 1024:
			pt = a.referencePoint()
			rX = pt.X()
			rY = pt.Y()
			rZ = pt.Z()
                        #print(rX)
        
			dxy = a.dxy()
			dz = a.dz()
        
			outdata['gc_refX'][n] = rX      
			outdata['gc_refY'][n] = rY
			outdata['gc_refZ'][n] = rZ
			outdata['gc_dxy'][n] = dxy
			outdata['gc_dz'][n] = dz
			outdata['nrefPts'][0] = x + n + 1
	outtree.Fill()

outputFile.Write()
outputFile.Close()
