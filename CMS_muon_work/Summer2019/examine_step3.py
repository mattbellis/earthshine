import ROOT
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from array import array

infilename = sys.argv[1]

f = ROOT.TFile.Open(infilename)
f.ls()

t= f.Get("tout")


nentries = t.GetEntries()

single_event = 12

muX = []
muY = []
muZ = []
muE = []
muPT = []
muEta = []
muPhi = []

LX = []
LY = []
LZ = []

BHX = []
BHY = []
BHZ = []

splitX = []
splitY = []
splitZ = []

noX = []
noY = []
noZ = []

t0X = []
t0Y = []
t0Z = []

LHCX = []
LHCY = []
LHCZ = []

for i in range(0, nentries):

	t.GetEvent(i)

	n = t.nrecoMuons
	m = t.recoMuons_muons1Leg
	p = t.recoMuons_muonsBeamHaloEndCaps
	q = t.recoMuons_muonsSplit
	r = t.recoMuons_muonsnoRPC
	s = t.recoMuons_t0Correction
	v = t.recoMuons_LHCSTA

	for i in range(n):
		pt = t.muons_pt[i]
		phi = t.muons_phi[i]
		eta = t.muons_eta[i]

		muPT.append(pt)
		muEta.append(eta)
		muPhi.append(phi)
		muE.append(t.muons_E[i])

		theta = 2 * np.arctan(np.exp(-eta))

		apt = np.abs(pt)

		x = apt * np.cos(phi)
		y = apt * np.sin(phi)
		z = apt / np.tan(theta)

		muX.append(x)
		muY.append(y)
		muZ.append(z)

#	for i in range(m):
#		pt = t.muons1L_pt[i]
#		phi = t.muons1L_phi[i]
#		eta = t.muons1L_eta[i]
#
#		theta = 2 * np.arctan(np.exp(-eta))
#
#		apt = np.abs(pt)
#
#		x = apt * np.cos(phi)
#		y = apt * np.sin(phi)
#		z = apt / np.tan(theta)
#
#		LX.append(x)
#		LY.append(y)
#		LZ.append(z)
#
#	for i in range(p):
#		pt = t.muonsBHEC_pt[i]
#		phi = t.muonsBHEC_phi[i]
#		eta = t.muonsBHEC_eta[i]
#
#		theta = 2 * np.arctan(np.exp(-eta))
#
#		apt = np.abs(pt)
#
#		x = apt * np.cos(phi)
#		y = apt	* np.sin(phi)
#		z = apt	/ np.tan(theta)
#
#		BHX.append(x)		
#		BHY.append(y)
#		BHZ.append(z)
#
#
#	for i in range(q):
#		pt = t.muonsSplit_pt[i]
#		phi = t.muonsSplit_phi[i]
#		eta = t.muonsSplit_eta[i]
#
#		theta = 2 * np.arctan(np.exp(-eta))
#
#		apt = np.abs(pt)
#
#		x = apt * np.cos(phi)
#		y = apt * np.sin(phi)
#		z = apt / np.tan(theta)
#
#		splitX.append(x)
#		splitY.append(y)
#		splitZ.append(z)
#
#	for i in range(r):
#		pt = t.muonsnoRPC_pt[i]
#		phi = t.muonsnoRPC_phi[i]
#		eta = t.muonsnoRPC_eta[i]
#
#		theta = 2 * np.arctan(np.exp(-eta))
#
#		apt = np.abs(pt)
#
#		x = apt * np.cos(phi)
#		y = apt * np.sin(phi)
#		z = apt / np.tan(theta)
#
#		noX.append(x)
#		noY.append(y)
#		noZ.append(z)
#
#	for i in range(s):
#		pt = t.muonst0_pt[i]
#		phi = t.muonst0_phi[i]
#		eta = t.muonst0_eta[i]
#
#		theta = 2 * np.arctan(np.exp(-eta))
#
#		apt = np.abs(pt)
#
#		x = apt * np.cos(phi)
#		y = apt * np.sin(phi)
#		z = apt / np.tan(theta)
#
#		t0X.append(x)
#		t0Y.append(y)
#		t0Z.append(z)
#
#
#	for i in range(v):
#		pt = t.muonsLHCSTA_pt[i]
#		phi = t.muonsLHCSTA_phi[i]
#		eta = t.muonsLHCSTA_eta[i]
#
#		theta = 2 * np.arctan(np.exp(-eta))
#
#		apt = np.abs(pt)
#
#		x = apt * np.cos(phi)
#		y = apt * np.sin(phi)
#		z = apt / np.tan(theta)
#
#		LHCX.append(x)
#		LHCY.append(y)
#		LHCZ.append(z)
#




plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(muX, muY, muZ, 'o', markersize = 10)
plt.title("Reconstructed muon orientation")

plt.figure()
plt.hist(muE, bins = 100)
plt.title("Energy")

plt.figure()
plt.hist(muPT, bins = 100)
plt.title("PT")

plt.figure()
plt.hist(muEta, bins = 100)
plt.title("Eta")

plt.figure()
plt.hist(muPhi, bins = 100)
plt.title("Phi")

plt.figure()
plt.plot(muPhi, muEta, 'o', markersize = 10)
plt.title("Eta vs phi")

#plt.figure()
#ax = plt.axes(projection = '3d')
#ax.plot3D(LX, LY, LZ, 'o', markersize = 10)
#plt.title("Reconstructed muon orientation, 1 Leg")


#plt.figure()
#ax = plt.axes(projection = '3d')
#ax.plot3D(BHX, BHY, BHZ, 'o', markersize = 10)
#plt.title("Reconstructed muon orientation, Beam Halo Endcaps")

#plt.figure()
#ax = plt.axes(projection = '3d')
#ax.plot3D(splitX, splitY, splitZ, 'o', markersize = 10)
#plt.title("Reconstructed muon orientation, Split muons")

#plt.figure()
#ax = plt.axes(projection = '3d')
#ax.plot3D(noX, noY, noZ, 'o', markersize = 10)
#plt.title("Reconstructed muon orientation, no RPC")

#plt.figure()
#ax = plt.axes(projection = '3d')
#ax.plot3D(t0X, t0Y, t0Z, 'o', markersize = 10)
#plt.title("Reconstructed muon orientation, t0 correction")

#plt.figure()
#ax = plt.axes(projection = '3d')
#ax.plot3D(LHCX, LHCY, LHCZ, 'o', markersize = 10)
#plt.title("Reconstructed muon orientation, LHCSTA")






plt.show()

		
