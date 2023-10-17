USERNAME=$1
echo $USERNAME
#echo scp "${USERNAME}@lxplus.cern.ch:CMSSW_10_2_0/src/earthshine/CMS_muon_work/*.root" .
#scp "${USERNAME}@lxplus.cern.ch:CMSSW_10_2_0/src/earthshine/CMS_muon_work/*.root" .
#echo scp "${USERNAME}@lxplus.cern.ch:CMSSW_10_2_0/src/earthshine/CMS_muon_work/*.npy" .
#scp "${USERNAME}@lxplus.cern.ch:CMSSW_10_2_0/src/earthshine/CMS_muon_work/*.npy" .


# FROM WORK WITH TAMAS
scp "${USERNAME}@lxplus.cern.ch:/uscms_data/d3/mbellis/CMSSW_13_0_10/src/CosmicsAnalyzer/EarthAsDMAnalyzer/test/ntuple_test.root" .
