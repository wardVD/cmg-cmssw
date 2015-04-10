import PhysicsTools.HeppyCore.framework.config as cfg

import os
from Workspace.HEPHYPythonTools.helpers import getFileList
from Workspace.HEPHYPythonTools.xsec import xsec

def createComponentFromDPM(name, dbsName, dir, minAgeDPM=0, histname='histo', xrootPrefix='root://hephyse.oeaw.ac.at/', maxN=-1): 
  component = cfg.MCComponent(
      dataset=dbsName,
      name = name,
      files = getFileList(dir, minAgeDPM=0, histname=histname, xrootPrefix=xrootPrefix, maxN=maxN),
      xSection = xsec[dbsName],
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )
  return component
def createComponentFromDirectory(name, dbsName, dir, xSec, histname='histo',  maxN=-1): 
  component = cfg.MCComponent(
      dataset=dbsName,
      name = name,
      files = getFileList(dir, minAgeDPM=0, histname=histname, maxN=maxN),
      xSection = xSec,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )
  return component

allComps=[]

#debugSample = createComponentFromDirectory(\
#  name = 'debugSamples',
#  dbsName='',
#  xSec=0.,
#  dir='/afs/hephy.at/scratch/s/schoefbeck/CMS/CMSSW_7_2_3/src/Workspace/HEPHYPythonTools/crab/pickEvents/crab_0_150122_110053/res/', 
#  histname="pickevents"
#  ) 
#allComps.append(debugSample)

aodDebugSample =   component = cfg.MCComponent(
      dataset='',
      name = 'test',
      files = ['file:/data/schoef/local/WJetsToLNu_HT-100to200_Tune4C_13TeV-madgraph-tauola_PU20bx25_POSTLS170_V5-v1_AODSIM.root'],
      xSection = 1.,
      nGenEvents = 1,
      triggers = [],
      effCorrFactor = 1,
  )
 
allComps.append(aodDebugSample)

DYJetsToLL_M50_PU20bx25           = createComponentFromDPM("DYJetsToLL_M50_PU20bx25",           "/DYJetsToLL_M-50_13TeV-madgraph-pythia8/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "/dpm/oeaw.ac.at/home/cms/store/user/schoef/metTuple3/DYJetsToLL_M-50_13TeV-madgraph-pythia8_Phys14DR-PU20bx25_PHYS14_25_V1-v1_AODSIM")
DYJetsToLLHT100to200_M50_PU20bx25 = createComponentFromDPM("DYJetsToLLHT100to200_M50_PU20bx25", "/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "/dpm/oeaw.ac.at/home/cms/store/user/schoef/metTuple3/DYJetsToLL_M-50_HT-100to200_Tune4C_13TeV-madgraph-tauola_Phys14DR-PU20bx25_PHYS14_25_V1-v1_AODSIM")
DYJetsToLLHT200to400_M50_PU20bx25 = createComponentFromDPM("DYJetsToLLHT200to400_M50_PU20bx25", "/DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "/dpm/oeaw.ac.at/home/cms/store/user/schoef/metTuple3/DYJetsToLL_M-50_HT-200to400_Tune4C_13TeV-madgraph-tauola_Phys14DR-PU20bx25_PHYS14_25_V1-v1_AODSIM")
DYJetsToLLHT400to600_M50_PU20bx25 = createComponentFromDPM("DYJetsToLLHT400to600_M50_PU20bx25", "/DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "/dpm/oeaw.ac.at/home/cms/store/user/schoef/metTuple4/DYJetsToLL_M-50_HT-400to600_Tune4C_13TeV-madgraph-tauola_Phys14DR-PU20bx25_PHYS14_25_V1-v1_AODSIM_2")
DYJetsToLLHT600toInf_M50_PU20bx25 = createComponentFromDPM("DYJetsToLLHT600toInf_M50_PU20bx25", "/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola/Phys14DR-PU20bx25_PHYS14_25_V1-v1/MINIAODSIM", "/dpm/oeaw.ac.at/home/cms/store/user/schoef/metTuple3/DYJetsToLL_M-50_HT-600toInf_Tune4C_13TeV-madgraph-tauola_Phys14DR-PU20bx25_PHYS14_25_V1-v1_AODSIM")
allComps += [DYJetsToLL_M50_PU20bx25, DYJetsToLLHT100to200_M50_PU20bx25, DYJetsToLLHT200to400_M50_PU20bx25, DYJetsToLLHT400to600_M50_PU20bx25, DYJetsToLLHT600toInf_M50_PU20bx25]

from CMGTools.TTHAnalysis.setup.Efficiencies import *
dataDir = os.environ['CMSSW_BASE']+"/src/CMGTools/TTHAnalysis/data"

#Define splitting
for comp in allComps:
    comp.isMC = True
    comp.isData = False
    comp.splitFactor = 1 
    comp.puFileMC=dataDir+"/puProfile_Summer12_53X.root"
    comp.puFileData=dataDir+"/puProfile_Data12.root"
    comp.efficiency = eff2012

T2DegStop_300_270 = createComponentFromDPM("T2DegStop_300_270","/T2DegStop2j_300_270_GENSIM/nrad-T2DegStop2j_300_270_MINIAOD-a279b5108ada7c3c0926210c2a95f22e/USER",'/dpm/oeaw.ac.at/home/cms/store/user/nrad/T2DegStop2j_300_270_GENSIM/T2DegStop2j_300_270_MINIAOD/a279b5108ada7c3c0926210c2a95f22e/',histname='T2Deg')
