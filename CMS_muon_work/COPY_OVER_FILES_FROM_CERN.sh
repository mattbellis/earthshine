USERNAME=$1
echo $USERNAME
echo scp "${USERNAME}@lxplus.cern.ch:CMSSW_10_2_0/src/earthshine/CMS_muon_work/*.root" .
scp "${USERNAME}@lxplus.cern.ch:CMSSW_10_2_0/src/earthshine/CMS_muon_work/*.root" .
#echo scp "${USERNAME}@lxplus.cern.ch:CMSSW_10_2_0/src/earthshine/CMS_muon_work/*.npy" .
#scp "${USERNAME}@lxplus.cern.ch:CMSSW_10_2_0/src/earthshine/CMS_muon_work/*.npy" .
