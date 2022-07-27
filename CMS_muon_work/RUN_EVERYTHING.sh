#echo "Staring step 1 --------------------------------------------"
#time cmsRun UndergroundCosmicSPLooseMu_cfi_py_GEN_SIM.py

echo 

echo "Staring step 2 --------------------------------------------"
time cmsDriver.py step2  --conditions auto:phase1_2017_cosmics -s DIGI:pdigi_valid,L1,DIGI2RAW,HLT:@relval2017 --scenario cosmics -n 2000 --datatier GEN-SIM-DIGI-RAW --era Run2_2017 --eventcontent FEVTDEBUG --filein file:step1.root  --fileout file:step2.root  > step2_CosmicsSPLoose_UP17+CosmicsSPLoose_UP17+DIGICOS_UP17+RECOCOS_UP17+ALCACOS_UP17+HARVESTCOS_UP17.log  2>&1

echo 

echo "Staring step 3 --------------------------------------------"
time cmsDriver.py step3  --conditions auto:phase1_2017_cosmics -s RAW2DIGI,L1Reco,RECO,ALCA:MuAlGlobalCosmics,DQM --scenario cosmics -n 2000 --datatier GEN-SIM-RECO,DQMIO --era Run2_2017 --eventcontent RECOSIM,DQM --filein file:step2.root  --fileout file:step3.root  > step3_CosmicsSPLoose_UP17+CosmicsSPLoose_UP17+DIGICOS_UP17+RECOCOS_UP17+ALCACOS_UP17+HARVESTCOS_UP17.log  2>&1




