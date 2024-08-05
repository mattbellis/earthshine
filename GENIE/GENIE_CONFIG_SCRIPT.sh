#!/bin/bash
export GENIE=/home/bellis/Generator
export ROOTSYS=/home/bellis/root_install
export LHAPATH=/home/bellis/LHAPDF-6.5.4
export PATH=$PATH:\
$ROOTSYS/bin:\
$GENIE/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:\
/home/bellis/LHAPDF-6.5.4/:\
/home/bellis/v6_428/lib:\
$ROOTSYS/lib:\
$GENIE/lib
