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

## Inspecting a file

We can use this file for testing. It has about 6000 entries

```
root://eoscms.cern.ch//eos/cms/store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/613/00000/1486B57F-CE66-E511-89D5-02163E0120E8.root
```

To see what is in it, you can run 

```
edmDumpEventContent root://eoscms.cern.ch//eos/cms/store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/613/00000/1486B57F-CE66-E511-89D5-02163E0120E8.root
```
or the following, if you want to redirect the output to a text file (`edmlog.log`)

```
edmDumpEventContent root://eoscms.cern.ch//eos/cms/store/data/Run2015D/SingleMuon/RECO/PromptReco-v3/000/257/613/00000/1486B57F-CE66-E511-89D5-02163E0120E8.root > edmlog.log
```

You can then look in the file (with `vi` for example) and see what type of data is in there that you might want to explore. 

It doesn't always tell you if those entries have momentum information (e.g. `phi`), but eventually we'll learn that. 
