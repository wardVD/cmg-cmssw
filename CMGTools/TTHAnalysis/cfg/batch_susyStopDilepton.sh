#Lxplus Batch Job Script

export DIR="/afs/cern.ch/work/w/wvandrie/public/STOPS/CMSSW_7_4_7/src/CMGTools/TTHAnalysis/cfg/"
export CFG_FILE=$DIR"run_susySingleLepton_wTrigg_cfg.py"
echo $CFG_FILE

cd "/afs/cern.ch/work/w/wvandrie/public/STOPS/CMSSW_7_4_7/src/"
eval `scramv1 runtime -sh`
cd $DIR
heppy test run_susyStopDilepton_cfg.py -p0 -f -N200