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
t.Print("*PSimHits*MuonDTH*")
#exit()

# How many entries are there? 
nentries = t.GetEntries()
print("nentries: {0}".format(nentries))


#------------------------------------------------------

DTx=[]
DTy=[] 
DTz=[]
DTn = []
DTt = []
DTdedx = []

RPCx=[]
RPCy=[]
RPCz=[]
RPCn=[]
RPCt=[]
RPCdedx=[]

CSCx=[]
CSCy=[]
CSCz=[]
CSCn=[]
CSCt=[]
CSCdedx=[]

# Loop over events
for i in range(nentries):

    # Get the i'th event and fill the tree from the file
    t.GetEvent(i)

    if i%100==0:
        print(str(i) + " out of " + str(nentries))

    if i>=1000: 
        break 

    # This is where we get the name of a branch
    # I usually find this name using TBrowser unless someone tells me 
    # exactly what the name of the branch is that I have to look at. 
    vars = t.PSimHits_g4SimHits_MuonDTHits_SIM.product()
    mcount =0
    
    # This vars.product thing allows us to get the leaves 
    for var in vars:
        DTx.append(var.localPosition().x())
        DTy.append(var.localPosition().y())
        DTz.append(var.localPosition().z())
        DTt.append(var.tof())
        DTdedx.append(var.energyLoss())
        mcount += 1
    DTn.append(mcount)
    print("var: " + str(mcount))

#####################################################
    # This is where we get the name of a branch
    # I usually find this name using TBrowser unless someone tells me 
    # exactly what the name of the branch is that I have to look at. 
    vars = t.PSimHits_g4SimHits_MuonCSCHits_SIM.product()
    mcount =0
    
    # This vars.product thing allows us to get the leaves 
    for var in vars:
        CSCx.append(var.localPosition().x())
        CSCy.append(var.localPosition().y())
        CSCz.append(var.localPosition().z())
        CSCt.append(var.tof())
        CSCdedx.append(var.energyLoss())
        mcount += 1
    CSCn.append(mcount)
    print("var: " + str(mcount))





    # This is where we get the name of a branch
    # I usually find this name using TBrowser unless someone tells me 
    # exactly what the name of the branch is that I have to look at. 
    vars = t.PSimHits_g4SimHits_MuonRPCHits_SIM.product()
    mcount =0
    
    # This vars.product thing allows us to get the leaves 
    for var in vars:
        RPCx.append(var.localPosition().x())
        RPCy.append(var.localPosition().y())
        RPCz.append(var.localPosition().z())
        RPCt.append(var.tof())
        RPCdedx.append(var.energyLoss())
        mcount += 1
    RPCn.append(mcount)
    print("var: " + str(mcount))
#Finished looping over the file
#Time to write the file !
np.save('output_step1.npy',np.array([DTx,DTy,DTz,DTn,DTt,DTdedx,RPCx,RPCy,RPCz,RPCn,RPCt,RPCdedx,CSCx,CSCy,CSCz,CSCn,CSCt,CSCdedx]))

#print(n)

print("Ran over the entries...")
'''
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

'''
plt.show()
'''


