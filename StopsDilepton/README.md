# Stops-dilepton 
cmsrel CMSSW_7_4_7;

cd CMSSW_7_4_7/src ;

cmsenv ;

git cms-addpkg FWCore/Version

git clone https://github.com/wardVD/cmg-cmssw/Stops-dilepton StopsDilepton


** To compile TMVA **
cd TMVA/test; source setup.[c]sh; 
cd ..
make
******************** 

