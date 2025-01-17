#!/bin/bash
export GENIE=/home/bellis/Generator_MAIN
export ROOTSYS=/home/bellis/root_install
export LHAPATH=/home/bellis/LHAPDF-6.5.4
export LHAPDF6_INC=/usr/local/lib/
export LHAPDF6_LIB=/usr/local/include/LHAPDF/
export PATH=$PATH:\
$ROOTSYS/bin:\
$GENIE/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:\
/home/bellis/LHAPDF-6.5.4/:\
/home/bellis/v6_428/lib:\
$ROOTSYS/lib:\
$GENIE/lib
