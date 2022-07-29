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
