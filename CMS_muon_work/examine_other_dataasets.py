import ROOT
import matplotlib.pylab as plt
import numpy as np

import sys

infilename = sys.argv[1]

f = ROOT.TFile(infilename)

t = f.Get("Events")
t.Print("*obal*")
#exit()

nentries = t.GetEntries()



#plt.show()

#------------------------------------------------------


infilename = sys.argv[1]

f = ROOT.TFile(infilename)

t = f.Get("Events")
t.Print("*osmic*")
#exit()

nentries = t.GetEntries()

# Stand alone
sa_pt = []
sa_eta = []
sa_phi = []

# Global
global_pt = []
global_eta = []
global_phi = []

# One leg

oneleg_pt=[]
oneleg_eta=[]
oneleg_phi=[]


# Loop over events
for i in range(nentries):

    t.GetEvent(i)

    if i%100==0:
        print(str(i) + " out of " + str(nentries))

    if i>=100: 
        break 

    muons = t.recoMuons_muonsFromCosmics__RECO
    mcount =0
    for muon in muons.product():
        sa_pt.append(muon.pt())
        sa_eta.append(muon.eta())
        sa_phi.append(muon.phi())
        mcount += 1
    print("muonsFronCosmics: " + str(mcount))

    muons = t.recoMuons_muonsFromCosmics1Leg__RECO
    mcount =0
    for muon in muons.product():
        oneleg_pt.append(muon.pt())
        oneleg_eta.append(muon.eta())
        oneleg_phi.append(muon.phi())
        mcount += 1
    print("muonsFronCosmics1Leg: " + str(mcount))

print("Ran over the entries...")
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(sa_pt,bins=50,range=(0,300),histtype='step',fill=True)
plt.xlabel(r'p$_{T}$ [GeV/c]',fontsize=18)

plt.subplot(1,3,2)
plt.hist(sa_eta,bins=50,range=(-3.,3.),histtype='step',fill=True)
plt.xlabel(r'$\eta$',fontsize=18)

plt.subplot(1,3,3)
plt.hist(sa_phi,bins=100,range=(-3.2, 3.2),histtype='step',fill=True)
plt.xlabel(r'$\phi$',fontsize=18)

plt.tight_layout()

plt.savefig('muonsFromCosmics.png')

plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(oneleg_pt,bins=50,range=(0,300),histtype='step',fill=True)
plt.xlabel(r'p$_{T}$ [GeV/c]',fontsize=18)

plt.subplot(1,3,2)
plt.hist(oneleg_eta,bins=50,range=(-3.,3.),histtype='step',fill=True)
plt.xlabel(r'$\eta$',fontsize=18)

plt.subplot(1,3,3)
plt.hist(oneleg_phi,bins=100,range=(-3.2, 3.2),histtype='step',fill=True)
plt.xlabel(r'$\phi$',fontsize=18)

plt.tight_layout()

plt.savefig('muonsFromCosmics1Leg.png')


plt.show()


