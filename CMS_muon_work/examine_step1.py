import ROOT
import matplotlib.pylab as plt

import sys

infilename = sys.argv[1]

f = ROOT.TFile(infilename)

t = f.Get("Events")

nentries = t.GetEntries()

pt = []
eta = []
phi = []

for i in range(nentries):

    t.GetEvent(i)

    particles = t.recoGenParticles_genParticles__SIM.product()

    for particle in particles:
        pt.append(particle.pt())
        eta.append(particle.eta())
        phi.append(particle.phi())

print("Ran over the enries...")

plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(pt,bins=50,range=(0,300),histtype='step',fill=True)
plt.xlabel(r'p$_{T}$ [GeV/c]',fontsize=18)

plt.subplot(1,3,2)
plt.hist(eta,bins=50,range=(-3.,3.),histtype='step',fill=True)
plt.xlabel(r'$\eta$',fontsize=18)

plt.subplot(1,3,3)
plt.hist(phi,bins=100,range=(-3.2, 3.2),histtype='step',fill=True)
plt.xlabel(r'$\phi$',fontsize=18)

plt.tight_layout()

plt.savefig('genmuons.png')

plt.show()
