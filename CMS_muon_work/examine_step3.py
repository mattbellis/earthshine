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

# Stand alone
sa_pt = []
sa_eta = []
sa_phi = []

# Global
global_pt = []
global_eta = []
global_phi = []

for i in range(nentries):

    t.GetEvent(i)

    if i%100==0:
        print(i)

    '''
    hepmc = t.edmHepMCProduct_generatorSmeared__SIM.product()
    genEvent = hepmc.getHepMCData()

    begin = genEvent.particles_begin()
    end = genEvent.particles_end()

    print(genEvent.particles_size())

    particle = genEvent.particle_const_iterator()
    nparticles = genEvent.particles_size()

    for i in range(nparticles):
        print(particle)
        particle.next

    break
    '''

    muons = t.recoTracks_standAloneMuons__RECO
    for muon in muons.product():
        sa_pt.append(muon.pt())
        sa_eta.append(muon.eta())
        sa_phi.append(muon.phi())

    muons = t.recoTracks_globalCosmicMuons__RECO
    for muon in muons.product():
        global_pt.append(muon.pt())
        global_eta.append(muon.eta())
        global_phi.append(muon.phi())

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

plt.savefig('standalonemuons.png')

plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(global_pt,bins=50,range=(0,300),histtype='step',fill=True)
plt.xlabel(r'p$_{T}$ [GeV/c]',fontsize=18)

plt.subplot(1,3,2)
plt.hist(global_eta,bins=50,range=(-3.,3.),histtype='step',fill=True)
plt.xlabel(r'$\eta$',fontsize=18)

plt.subplot(1,3,3)
plt.hist(global_phi,bins=100,range=(-3.2, 3.2),histtype='step',fill=True)
plt.xlabel(r'$\phi$',fontsize=18)

plt.tight_layout()

plt.savefig('globalcosmicsmuons.png')

plt.show()


plt.show()


