import ROOT
import matplotlib.pylab as plt
import numpy as np

import sys

# This is the name of the input file
infilename = sys.argv[1]

# This opens the file and assigns it to variable f
f = ROOT.TFile(infilename)

# This gets a ROOT TTree called "Events"
t = f.Get("Events")

# This prints all the TBranches that have "MuonDT" somewhere in the name
#t.Print("*MuonDT*")
#t.Print("*recoMuon*Cosmic*")
t.Print("*recoMuon*")
#exit()

# How many entries are there? 
nentries = t.GetEntries()
print("nentries: {0}".format(nentries))


#------------------------------------------------------

x=[]
y=[] 
z=[]
n = []



# Loop over events
for i in range(nentries):

    # Get the i'th event and fill the tree from the file
    t.GetEvent(i)

    if i%100==0:
        print(str(i) + " out of " + str(nentries))

    if i>=100: 
        break 

    # This is where we get the name of a branch
    # I usually find this name using TBrowser unless someone tells me 
    # exactly what the name of the branch is that I have to look at. 
    #muons = t.recoMuons_muonsFromCosmics__RECO
    muons = t.recoMuons_muonsWitht0Correction__RECO
    mcount =0
    
    # This muons.product thing allows us to get the leaves 
    for muon in muons.product():
        x.append(muon.pt())
        y.append(muon.eta())
        z.append(muon.phi())
        mcount += 1
    n.append(mcount)
    print("muonsFronCosmics: " + str(mcount))

    '''
    muons = t.recoMuons_muonsFromCosmics1Leg__RECO
    mcount =0
    for muon in muons.product():
        oneleg_pt.append(muon.pt())
        oneleg_eta.append(muon.eta())
        oneleg_phi.append(muon.phi())
        mcount += 1
    print("muonsFronCosmics1Leg: " + str(mcount))
    '''

print(n)

print("Ran over the entries...")
plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.hist(x,bins=50,range=(0,300),histtype='step',fill=True)
plt.xlabel(r'p$_{T}$ [GeV/c]',fontsize=18)

plt.subplot(1,3,2)
plt.hist(y,bins=50,range=(-3.,3.),histtype='step',fill=True)
plt.xlabel(r'$\eta$',fontsize=18)

plt.subplot(1,3,3)
plt.hist(z,bins=100,range=(-3.2, 3.2),histtype='step',fill=True)
plt.xlabel(r'$\phi$',fontsize=18)

plt.tight_layout()

plt.savefig('muonsFromCosmics.png')

'''
plt.show()
'''


