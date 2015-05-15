##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES         ##
## skim condition: >= 1 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import *

# Lepton Preselection
# ele
lepAna.loose_electron_id = "POG_MVA_ID_Run2_NonTrig_Loose"
lepAna.loose_electron_pt  = 5
# mu
lepAna.loose_muon_pt  = 5

# Redefine what I need
lepAna.packedCandidates = 'packedPFCandidates'

# selec Iso
isolation = "miniIso"

if isolation == "miniIso":
# do miniIso
    lepAna.doMiniIsolation = True
    lepAna.miniIsolationPUCorr = 'rhoArea'
    lepAna.miniIsolationVetoLeptons = None
    lepAna.loose_muon_isoCut     = lambda muon : muon.miniRelIso < 0.4
    lepAna.loose_electron_isoCut = lambda elec : elec.miniRelIso < 0.4
elif isolation == "relIso03":
# normal relIso03
    lepAna.ele_isoCorr = "rhoArea"
    lepAna.mu_isoCorr = "rhoArea"

    lepAna.loose_electron_relIso = 0.5
    lepAna.loose_muon_relIso = 0.5

# --- LEPTON SKIMMING ---
ttHLepSkim.minLeptons = 1
ttHLepSkim.maxLeptons = 999
#LepSkim.idCut  = ""
#LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---
jetAna.minLepPt = 10

jetAna.mcGT = "PHYS14_V4_MC"
jetAna.doQG = True
jetAna.smearJets = False #should be false in susycore, already
jetAna.recalibrateJets = True #should be true in susycore, already
metAna.recalibrate = False #should be false in susycore, already
metAna.otherMETs = [\
  ("metTxy",('slimmedTxyMETs', 'std::vector<pat::MET>')),
  ("metRaw",('slimmedRAWMETs', 'std::vector<pat::MET>')),
  ]

isoTrackAna.setOff=False

from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## Insert the FatJet, SV, HeavyFlavour analyzers in the sequence
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHFatJetAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHSVAna)

## Single lepton + ST skim
from CMGTools.TTHAnalysis.analyzers.ttHSTSkimmer import ttHSTSkimmer
ttHSTSkimmer = cfg.Analyzer(
    ttHSTSkimmer, name='ttHSTSkimmer',
    minST = 200,
    )

from CMGTools.TTHAnalysis.analyzers.ttHReclusterJetsAnalyzer import ttHReclusterJetsAnalyzer
ttHReclusterJets = cfg.Analyzer(
    ttHReclusterJetsAnalyzer, name="ttHReclusterJetsAnalyzer",
    pTSubJet = 30,
    etaSubJet = 5.0,
            )

#from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14  import *

triggerFlagsAna.triggerBits = {
#put trigger here for data
}

# Tree Producer
from CMGTools.TTHAnalysis.analyzers.treeProducerSusySingleLepton import *
## Tree Producer
treeProducer = cfg.Analyzer(
     AutoFillTreeProducer, name='treeProducerSusySingleLepton',
     vectorTree = True,
     saveTLorentzVectors = False,  # can set to True to get also the TLorentzVectors, but trees will be bigger
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susySingleLepton_globalVariables,
     globalObjects = susySingleLepton_globalObjects,
     collections = susySingleLepton_collections,
)


#!# #-------- SAMPLES AND TRIGGERS -----------

#!# # create MC component (file names will be overwritten by heppy_crab_script.py)
#!# from CMGTools.TTHAnalysis.samples.ComponentCreator import ComponentCreator
#!# kreator = ComponentCreator()

#!# TT_PU40bx25 = kreator.makeMCComponent("TT_PU40bx25", "/TT_Tune4C_13TeV-pythia8-tauola/Phys14DR-PU40bx25_tsg_PHYS14_25_V1-v1/MINIAODSIM", "CMS", ".*root",809.1)
#!# selectedComponents = [ TT_PU40bx25 ]

#!# #from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
#!# ##selectedComponents =  [TTJets]
#!# ##TTJets.splitFactor=1000
#!# #from CMGTools.TTHAnalysis.samples.samples_13TeV_private_heplx import *
#!# #selectedComponents = [T2DegStop_300_270]


#!# #from CMGTools.TTHAnalysis.samples.samples_13TeV_private_heplx import *
#!# #selectedComponents = [DYJetsToLL_M50_PU20bx25]#, DYJetsToLLHT100to200_M50_PU20bx25, DYJetsToLLHT200to400_M50_#PU20bx25, DYJetsToLLHT400to600_M50_PU20bx25, DYJetsToLLHT600toInf_M50_PU20bx25]

#!# #selectedComponents = [ TT_PU40bx25 ]
#-------- SEQUENCE

sequence = cfg.Sequence(susyCoreSequence+[
        ttHEventAna,
#    ttHSTSkimmer,
        ttHReclusterJets,
        treeProducer,
        ])


#!# ##-------- HOW TO RUN
#!# #test = 2
#!# #print "selectedComponents1 ",selectedComponents
#!# #if test==1:
#!# #    # test a single component, using a single thread.
#!# #    #comp = TTJets
#!# #    comp = T2DegStop_300_270
#!# ##    comp = SMS_T1tttt_2J_mGl1500_mLSP100
#!# #    comp.files = comp.files[:10]
#!# #    print "Files:",comp.files
#!# #    selectedComponents = [comp]
#!# #    comp.splitFactor = 1
#!# #elif test==2:
#!# #    # test all components (1 thread per component).
#!# #    print "selectedComponents2a ",selectedComponents
#!# #    for comp in selectedComponents:
#!# #        comp.splitFactor = 1
#!# #        comp.files = comp.files[:1]
#!# #    print "selectedComponents2b ",selectedComponents#

#!# from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
#!# #print "selectedComponents3 ",selectedComponents
#!# config = cfg.Config( components = selectedComponents,
#!#                      sequence = sequence,
#!#                      services = [],
#!#                      events_class = Events)

#!# #print "selectedComponents4 ",config.components
