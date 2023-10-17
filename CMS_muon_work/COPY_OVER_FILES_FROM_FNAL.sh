USERNAME=$1
echo $USERNAME

# FROM WORK WITH TAMAS
scp "${USERNAME}@cmslpc-sl7.fnal.gov:/uscms_data/d3/mbellis/CMSSW_13_0_10/src/CosmicsAnalyzer/EarthAsDMAnalyzer/test/ntuple_test.root" .
