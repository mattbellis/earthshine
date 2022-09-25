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
exit()

outputFile = ROOT.TFile.Open("output_file.root", "RECREATE");
outtree = ROOT.TTree('tout', 'Output tree')

data = {}

data['nMuonDTHits'] = ['MuonDTHits_lpx' , 'MuonDTHits_lpy', 'MuonDTHits_lpz', 'MuonDTHits_EnX', 'MuonDTHits_EnY', 'MuonDTHits_EnZ', 'MuonDTHits_ExX', 'MuonDTHits_ExY', 'MuonDTHits_ExZ', 'MuonDTHits_pabs', 'MuonDTHits_tof', 'MuonDTHits_eloss', 'MuonDTHits_theta', 'MuonDTHits_phiVal', 'MuonDTHits_phi', 'MuonDTHits_phiDeg', 'MuonDTHits_unitID']
data['nMuonCSCHits'] = ['MuonCSCHits_lpx', 'MuonCSCHits_lpy', 'MuonCSCHits_lpz', 'MuonCSCHits_EnX', 'MuonCSCHits_EnY', 'MuonCSCHits_EnZ', 'MuonCSCHits_ExX', 'MuonCSCHits_ExY', 'MuonCSCHits_ExZ', 'MuonCSCHits_pabs','MuonCSCHits_tof', 'MuonCSCHits_eloss', 'MuonCSCHits_theta', 'MuonCSCHits_phiVal', 'MuonCSCHits_phi', 'MuonCSCHits_phiDeg', 'MuonCSCHits_unitID']
data['nMuonRPCHits'] = ['MuonRPCHits_lpx', 'MuonRPCHits_lpy', 'MuonRPCHits_lpz', 'MuonRPCHits_EnX', 'MuonRPCHits_EnY', 'MuonRPCHits_EnZ', 'MuonRPCHits_ExX', 'MuonRPCHits_ExY', 'MuonRPCHits_ExZ', 'MuonRPCHits_pabs', 'MuonRPCHits_tof', 'MuonRPCHits_eloss', 'MuonRPCHits_theta', 'MuonRPCHits_phiVal', 'MuonRPCHits_phi', 'MuonRPCHits_phiDeg', 'MuonRPCHits_unitID']

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
	
	x = t.PSimHits_g4SimHits_MuonDTHits_SIM
	y = t.PSimHits_g4SimHits_MuonCSCHits_SIM
	z = t.PSimHits_g4SimHits_MuonRPCHits_SIM

	for n,a in enumerate(x.product()):
		b = a.localPosition()
		c = a.entryPoint()
		d = a.exitPoint()

		xEn = c.x()
		yEn = c.y()
		zEn = c.z()

		xExit = d.x()
		yExit = d.y()
		zExit = d.z()

		xLP = b.x()
		yLP = b.y()
		zLP = b.z()

		if n < 1024:
			outdata['MuonDTHits_lpx'][n] = xLP
			outdata['MuonDTHits_lpy'][n] = yLP
			outdata['MuonDTHits_lpz'][n] = zLP
			outdata['MuonDTHits_EnX'][n] = xEn
			outdata['MuonDTHits_EnY'][n] = yEn
			outdata['MuonDTHits_EnZ'][n] = zEn
			outdata['MuonDTHits_ExX'][n] = xExit
			outdata['MuonDTHits_ExY'][n] = yExit
			outdata['MuonDTHits_ExZ'][n] = zExit
			outdata['MuonDTHits_pabs'][n] = a.pabs()
			outdata['MuonDTHits_tof'][n] = a.tof()
			outdata['MuonDTHits_eloss'][n] = a.energyLoss()
			outdata['MuonDTHits_theta'][n] = a.thetaAtEntry()
			outdata['MuonDTHits_phiVal'][n] = a.phiAtEntry().value()
			outdata['MuonDTHits_phi'][n] = a.phiAtEntry()
			outdata['MuonDTHits_phiDeg'][n] = a.phiAtEntry().degrees()
			outdata['MuonDTHits_unitID'][n] = a.detUnitId()

	for n, a in enumerate(y.product()):
		b = a.localPosition()
		c = a.entryPoint()
		d = a.exitPoint()

		xEn = c.x()
		yEn = c.y()
		zEn = c.z()

		xExit = d.x()
		yExit = d.y()
		zExit = d.z()

		xLP = b.x()
		yLP = b.y()
		zLP = b.z()


		if n < 1024:
			outdata['MuonCSCHits_lpx'][n] = xLP
			outdata['MuonCSCHits_lpy'][n] = yLP
			outdata['MuonCSCHits_lpz'][n] = zLP
			outdata['MuonCSCHits_EnX'][n] = xEn
			outdata['MuonCSCHits_EnY'][n] = yEn
			outdata['MuonCSCHits_EnZ'][n] = zEn
			outdata['MuonCSCHits_ExX'][n] = xExit
			outdata['MuonCSCHits_ExY'][n] = yExit
			outdata['MuonCSCHits_ExZ'][n] = zExit
			outdata['MuonCSCHits_pabs'][n] = a.pabs()
			outdata['MuonCSCHits_tof'][n] = a.tof()
			outdata['MuonCSCHits_eloss'][n] = a.energyLoss()
			outdata['MuonCSCHits_theta'][n] = a.thetaAtEntry()
			outdata['MuonCSCHits_phiVal'][n] = a.phiAtEntry().value()
			outdata['MuonCSCHits_phi'][n] = a.phiAtEntry()
			outdata['MuonCSCHits_phiDeg'][n] = a.phiAtEntry().degrees()
			outdata['MuonCSCHits_unitID'][n] = a.detUnitId()


	for n, a in enumerate(z.product()):
		b = a.localPosition()
		c = a.entryPoint()
		d = a.exitPoint()

		xEn = c.x()
		yEn = c.y()
		zEn = c.z()

		xExit = d.x()
		yExit = d.y()
		zExit = d.z()

		xLP = b.x()
		yLP = b.y()
		zLP = b.z()


		if n < 1024:
			outdata['MuonRPCHits_lpx'][n] = xLP
			outdata['MuonRPCHits_lpy'][n] = yLP
			outdata['MuonRPCHits_lpz'][n] = zLP
			outdata['MuonRPCHits_EnX'][n] = xEn
			outdata['MuonRPCHits_EnY'][n] = yEn
			outdata['MuonRPCHits_EnZ'][n] = zEn
			outdata['MuonRPCHits_ExX'][n] = xExit
			outdata['MuonRPCHits_ExY'][n] = yExit
			outdata['MuonRPCHits_ExZ'][n] = zExit
			outdata['MuonRPCHits_pabs'][n] = a.pabs()
			outdata['MuonRPCHits_tof'][n] = a.tof()
			outdata['MuonRPCHits_eloss'][n] = a.energyLoss()
			outdata['MuonRPCHits_theta'][n] = a.thetaAtEntry()
			outdata['MuonRPCHits_phiVal'][n] = a.phiAtEntry().value()
			outdata['MuonRPCHits_phi'][n] = a.phiAtEntry()
			outdata['MuonRPCHits_phiDeg'][n] = a.phiAtEntry().degrees()
			outdata['MuonRPCHits_unitID'][n] = a.detUnitId()




