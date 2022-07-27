import ROOT
import sys
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
from array import array

infilename = sys.argv[1]

f = ROOT.TFile.Open(infilename)
t = f.Get("Events")
t.Print()
print()

t.Print("Muon")
#exit()

outputFile = ROOT.TFile.Open("output_fileStep3.root", "RECREATE");
outtree = ROOT.TTree('tout', 'Output tree')

data = {}

data['nrecoMuons'] = ['muons_pt' , 'muons_eta', 'muons_phi', 'muons_E', 'muons_px', 'muons_py', 'muons_pz', 'muons_p', 'muons_mass']
data['recoMuons_muons1Leg'] = ['muons1L_pt', 'muons1L_eta', 'muons1L_phi', 'muons1L_E', 'muons1L_px' , 'muons1L_py', 'muons1L_pz', 'muons1L_p', 'muons1L_mass']
data['recoMuons_muonsBeamHaloEndCaps'] = ['muonsBHEC_pt', 'muonsBHEC_eta', 'muonsBHEC_phi', 'muonsBHEC_E', 'muonsBHEC_px', 'muonsBHEC_py', 'muonsBHEC_pz', 'muonsBHEC_p', 'muonsBHEC_mass']
data['recoMuons_muonsSplit'] = ['muonsSplit_pt', 'muonsSplit_eta', 'muonsSplit_phi', 'muonsSplit_E', 'muonsSplit_px', 'muonsSplit_py', 'muonsSplit_pz', 'muonsSplit_p', 'muonsSplit_mass']
data['recoMuons_muonsnoRPC'] = ['muonsnoRPC_pt', 'muonsnoRPC_eta', 'muonsnoRPC_phi', 'muonsnoRPC_E', 'muonsnoRPC_px', 'muonsnoRPC_py', 'muonsnoRPC_pz', 'muonsnoRPC_p', 'muonsnoRPC_mass']
data['recoMuons_t0Correction'] = ['muonst0_pt', 'muonst0_eta', 'muonst0_phi', 'muonst0_E', 'muonst0_px', 'muonst0_py', 'muonst0_pz', 'muonst0_p', 'muonst0_mass']
data['recoMuons_LHCSTA'] = ['muonsLHCSTA_pt', 'muonsLHCSTA_eta', 'muonsLHCSTA_phi', 'muonsLHCSTA_E', 'muonsLHCSTA_px', 'muonsLHCSTA_py', 'muonsLHCSTA_pz', 'muonsLHCSTA_p', 'muonsLHCSTA_mass']


outdata = {}

for key in data.keys():
	outdata[key] = array('i', [-1])
	outtree.Branch(key, outdata[key], key + "/I")
	
	for branch in data[key]:
		outdata[branch] = array('f', 1024 * [-1.])
		outtree.Branch(branch, outdata[branch], '{0}[{1}]/F'.format(branch, key))


nentries = t.GetEntries()

single_event = 12

for i in range(0, nentries):
	t.GetEvent(i)
	
	x = t.recoMuons_muons__RECO
	y = t.recoMuons_muons1Leg__RECO
	z = t.recoMuons_muonsBeamHaloEndCapsOnly__RECO
	s = t.recoMuons_splitMuons__RECO
	p = t.recoMuons_muonsNoRPC__RECO
	q = t.recoMuons_muonsWitht0Correction__RECO
	r = t.recoMuons_lhcSTAMuons__RECO

	for n,a in enumerate(x.product()):
		if n < 1024:
			outdata['muons_pt'][n] = a.pt()
			outdata['muons_eta'][n] = a.eta()
			outdata['muons_phi'][n] = a.phi()
			outdata['muons_E'][n] = a.energy()
			outdata['muons_px'][n] = a.px()
			outdata['muons_py'][n] = a.py()
			outdata['muons_pz'][n] = a.pz()
			outdata['muons_p'][n] = a.p()
			outdata['muons_mass'][n] = a.mass()
			outdata['nrecoMuons'][0] = n+1

	
	for n, a in enumerate(y.product()):
		if n < 1024:
			outdata['muons1L_pt'][n] = a.pt()
			outdata['muons1L_eta'][n] = a.eta()
			outdata['muons1L_phi'][n] = a.phi()
			outdata['muons1L_E'][n] = a.energy()
			outdata['muons1L_px'][n] = a.px()
			outdata['muons1L_py'][n] = a.py()
			outdata['muons1L_pz'][n] = a.pz()
			outdata['muons1L_p'][n] = a.p()
			outdata['muons1L_mass'][n] = a.mass()
			outdata['recoMuons_muons1Leg'][0] = n+1

	for n, a in enumerate(z.product()):
		if n < 1024:
			outdata['muonsBHEC_pt'][n] = a.pt()
			outdata['muonsBHEC_eta'][n] = a.eta()
			outdata['muonsBHEC_phi'][n] = a.phi()
			outdata['muonsBHEC_E'][n] = a.energy()
			outdata['muonsBHEC_px'][n] = a.px()
			outdata['muonsBHEC_py'][n] = a.py()
			outdata['muonsBHEC_pz'][n] = a.pz()
			outdata['muonsBHEC_p'][n] = a.p()
			outdata['muonsBHEC_mass'][n] = a.mass()
			outdata['recoMuons_muonsBeamHaloEndCaps'][0] = n+1

	for n, a in enumerate(s.product()):
		if n < 1024:
			outdata['muonsSplit_pt'][n] = a.pt()
			outdata['muonsSplit_eta'][n] = a.eta()
			outdata['muonsSplit_phi'][n] = a.phi()
			outdata['muonsSplit_E'][n] = a.energy()
			outdata['muonsSplit_px'][n] = a.px()
			outdata['muonsSplit_py'][n] = a.py()
			outdata['muonsSplit_pz'][n] = a.pz()
			outdata['muonsSplit_p'][n] = a.p()
			outdata['muonsSplit_mass'][n] = a.mass()
			outdata['recoMuons_muonsSplit'][0] = n+1

	for n, a in enumerate(p.product()):
		if n < 1024:
			outdata['muonsnoRPC_pt'][n] = a.pt()
			outdata['muonsnoRPC_eta'][n] = a.eta()
			outdata['muonsnoRPC_phi'][n] = a.phi()
			outdata['muonsnoRPC_E'][n] = a.energy()
			outdata['muonsnoRPC_px'][n] = a.px()
			outdata['muonsnoRPC_py'][n] = a.py()
			outdata['muonsnoRPC_pz'][n] = a.pz()
			outdata['muonsnoRPC_p'][n] = a.p()
			outdata['muonsnoRPC_mass'][n] = a.mass()
			outdata['recoMuons_muonsnoRPC'][0] = n+1

	for n, a in enumerate(q.product()):
		if n < 1024:
			outdata['muonst0_pt'][n] = a.pt()
			outdata['muonst0_eta'][n] = a.eta()
			outdata['muonst0_phi'][n] = a.phi()
			outdata['muonst0_E'][n] = a.energy()
			outdata['muonst0_px'][n] = a.px()
			outdata['muonst0_py'][n] = a.py()
			outdata['muonst0_pz'][n] = a.pz()
			outdata['muonst0_p'][n] = a.p()
			outdata['muonst0_mass'][n] = a.mass()
			outdata['recoMuons_t0Correction'][0] = n+1


	for n, a in enumerate(r.product()):
		if n < 1024:
			outdata['muonsLHCSTA_pt'][n] = a.pt()
			outdata['muonsLHCSTA_eta'][n] = a.eta()
			outdata['muonsLHCSTA_phi'][n] = a.phi()
			outdata['muonsLHCSTA_E'][n] = a.energy()
			outdata['muonsLHCSTA_px'][n] = a.px()
			outdata['muonsLHCSTA_py'][n] = a.py()
			outdata['muonsLHCSTA_pz'][n] = a.pz()
			outdata['muonsLHCSTA_p'][n] = a.p()
			outdata['muonsLHCSTA_mass'][n] = a.mass()
			outdata['recoMuons_LHCSTA'][0] = n+1
	

	outtree.Fill()


outputFile.Write()
outputFile.Close()
