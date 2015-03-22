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

