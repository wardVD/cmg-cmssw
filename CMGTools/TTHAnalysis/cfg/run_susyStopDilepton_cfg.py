##########################################################
##       CONFIGURATION FOR SUSY STOP DILEPTON TREES     ##
## skim condition: >= 2 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg


#-------- LOAD ALL ANALYZERS -----------

from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *


#-------- REDEFINE WHAT I NEED -----------

# Lepton Skimming
ttHLepSkim.minLeptons = 2
ttHLepSkim.maxLeptons = 999
#ttHLepSkim.idCut  = ""
#ttHLepSkim.ptCuts = []
    
# Lepton Preselection
# Electron
lepAna.loose_electron_id = "POG_MVA_ID_Run2_NonTrig_Loose"
lepAna.loose_electron_pt = 5
#Muon
lepAna.loose_muon_pt = 5


isolation = "miniIso"

if isolation == "miniIso": 
    # Run miniIso
    lepAna.doMiniIsolation = True
    lepAna.packedCandidates = 'packedPFCandidates'
    lepAna.miniIsolationPUCorr = 'rhoArea'
    lepAna.miniIsolationVetoLeptons = None # use 'inclusive' to veto inclusive leptons and their footprint in all isolation cones

    lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.2
    lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.2
elif isolation == None:
    lepAna.loose_muon_isoCut     = lambda muon : True
    lepAna.loose_electron_isoCut = lambda elec : True
else:
    # nothing to do, will use normal relIso03
    pass


#-------- ADDITIONAL ANALYZERS -----------

## Event Analyzer for susy multi-lepton (at the moment, it's the TTH one)
from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

from CMGTools.TTHAnalysis.analyzers.treeProducerSusyStopDilepton import * 
## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusyStopDilepton',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susyStopDilepton_globalVariables,
     globalObjects = susyStopDilepton_globalObjects,
     collections = susyStopDilepton_collections,
)


#-------- SAMPLES AND TRIGGERS -----------


from CMGTools.RootTools.samples.triggers_13TeV_Spring15 import *
triggerFlagsAna.triggerBits = {
    'DoubleMu' : [triggers_mumu_iso[0]],
    'DoubleEl' : triggers_ee,
    'DoubleMuEl' : [triggers_mue[0]],
    'DoubleElMu' : [triggers_mue[1]],
}

from CMGTools.RootTools.samples.samples_13TeV_74X import *

selectedComponents = [DYJetsToLL_M50_HT100to200,DYJetsToLL_M50_HT200to400,DYJetsToLL_M50_HT400to600,DYJetsToLL_M50_HT600toInf,
TTJets, 
WJetsToLNu_HT100to200, WJetsToLNu_HT200to400, WJetsToLNu_HT400to600, WJetsToLNu_HT600toInf
] 
    
#-------- SEQUENCE -----------

sequence = cfg.Sequence(susyCoreSequence+[
        ttHEventAna,
        #ttHJetTauAna,
        #ttHEventAna,
        treeProducer,
    ])
preprocessor = None

#-------- HOW TO RUN -----------

from PhysicsTools.HeppyCore.framework.heppy_loop import getHeppyOption
#test = getHeppyOption('test')

test = 'allbkg'
if test == '1':
    comp = DYJetsToLL_M50
    #comp.files = comp.files[:10]
    comp.fineSplitFactor = 1
    selectedComponents = [ comp ]
elif test == '2':
    for comp in selectedComponents:
        comp.files = comp.files[:1]
        comp.splitFactor = 1
        comp.fineSplitFactor = 1
elif test == 'allbkg':
    for comp in selectedComponents:
        comp.files = comp.files[:1]
        comp.splitFactor = 1
        comp.fineSplitFactor = 1

## output histogram
outputService=[]
from PhysicsTools.HeppyCore.framework.services.tfile import TFileService
output_service = cfg.Service(
    TFileService,
    'outputfile',
    name="outputfile",
    fname='treeProducerSusyStopDilepton/Events.root',
    option='recreate'
    )    
outputService.append(output_service)

# the following is declared in case this cfg is used in input to the heppy.py script
from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
from CMGTools.TTHAnalysis.tools.EOSEventsWithDownload import EOSEventsWithDownload
event_class = EOSEventsWithDownload
if getHeppyOption("nofetch"):
    event_class = Events 
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = outputService, 
                     preprocessor = preprocessor, 
                     events_class = event_class)
