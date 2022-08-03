```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_0
```

Once those are created, you don't need to run the above two command. 

Next, we'll clone the github repo.

```
cd CMSSW_10_2_0/src
cmsenv

git clone https://github.com/mattbellis/earthshine.git
```

# Upon logging in to lxplus

```
voms-proxy-init --rfc --voms cms

cd CMSSW_10_2_0/src/earthshine/CMS_muon_work/

cmsenv

```


## Finding cosmics datasets

```
dasgoclient --query="dataset=/*/*Cosmic*/*" --format plain 
```

You can get a list of the actually ROOT files that are in one of these datasets
doing something like the following.

```
dasgoclient --query="file dataset=/Cosmics/Run2017C-CosmicSP-PromptReco-v1/RAW-RECO" --format plain --limit 30
```
