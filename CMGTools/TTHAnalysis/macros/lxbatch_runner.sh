#!/bin/bash
export SCRAM_ARCH=slc6_amd64_gcc481
export WORK=$CMSSW_BASE/src/CMGTools/TTHAnalysis/cfg
export SRC=$CMSSW_BASE/src 
cd $SRC; 
eval $(scramv1 runtime -sh);
cd $WORK;
heppy test run_susySinglelepton_test_cfg.py -f -N200 -p0 -o test=74X-MC -o sample=TT -o all=False -o single=True
