##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES       ##
## skim condition: >= 0 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg


#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import * 

lepAna.loose_muon_pt  = 5
lepAna.loose_muon_relIso = 0.5
lepAna.mu_isoCorr = "deltaBeta" 
lepAna.loose_electron_pt  = 7
lepAna.loose_electron_relIso = 0.5
lepAna.ele_isoCorr = "rhoArea" 
lepAna.ele_tightId = "Cuts_2012"


# Redefine what I need

# --- LEPTON SKIMMING ---
ttHLepSkim.minLeptons = 0
ttHLepSkim.maxLeptons = 999
#LepSkim.idCut  = ""
#LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---
jetAna.minLepPt = 10 
#JetMCAna.smearJets     = False # do we need to smear the jets?
jetAna.smearJets = False

#ttHReclusterJets = cfg.Analyzer(
#            'ttHReclusterJetsAnalyzer',
#            )

# Event Analyzer for susy multi-lepton (at the moment, it's the TTH one)


isoTrackAna.setOff=False

#from CMGTools.TTHAnalysis.analyzers.ttHReclusterJetsAnalyzer  import ttHReclusterJetsAnalyzer
#ttHReclusterJets = cfg.Analyzer(
#    ttHReclusterJetsAnalyzer, name="ttHReclusterJetsAnalyzer",
#    )
from CMGTools.TTHAnalysis.analyzers.ttHLepEventAnalyzer import ttHLepEventAnalyzer
ttHEventAna = cfg.Analyzer(
    ttHLepEventAnalyzer, name="ttHLepEventAnalyzer",
    minJets25 = 0,
    )

## Insert the SV analyzer in the sequence
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHFatJetAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHSVAna)
susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
                        ttHHeavyFlavourHadronAna)



from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14  import *

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
     PDFWeights = PDFWeights,
     globalVariables = susySingleLepton_globalVariables,
     globalObjects = susySingleLepton_globalObjects,
     collections = susySingleLepton_collections,
)



#-------- SAMPLES AND TRIGGERS -----------

from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *
#selectedComponents = [ SingleMu, DoubleElectron, TTHToWW_PUS14, DYJetsToLL_M50_PU20bx25, TTJets_PUS14 ]
TTJets.splitFactor = 1000
#selectedComponents = [TTJets]

#selectedComponents = [QCD_HT_1000ToInf, QCD_HT_250To500, QCD_HT_500To1000, SMS_T1tttt_2J_mGl1200_mLSP800, SMS_T1tttt_2J_mGl1500_mLSP100, SMS_T2tt_2J_mStop425_mLSP325, SMS_T2tt_2J_mStop500_mLSP325, SMS_T2tt_2J_mStop650_mLSP325, SMS_T2tt_2J_mStop850_mLSP100, TBarToLeptons_sch, TBarToLeptons_tch, TBar_tWch, TTH, TTWJets, TTZJets, TToLeptons_sch, TToLeptons_tch, T_tWch]
#selectedComponents =WJetsToLNuHT +  [WJetsToLNu]  
#selectedComponents = DYJetsM50HT
selectedComponents = [SMS_T5qqqqWW_Gl1500_Chi800_LSP100,  SMS_T5qqqqWW_Gl1200_Chi1000_LSP800]

#selectedComponents = MySamples 
#-------- SEQUENCE

sequence = cfg.Sequence(susyCoreSequence+[
    ttHEventAna,
#    ttHReclusterJets,
    treeProducer,
    ])

#-------- HOW TO RUN
test = 0
if test==1:
    # test a single component, using a single thread.
    comp = TTJets
    comp.files = comp.files[:1]
    selectedComponents = [comp]
    comp.splitFactor = 1
elif test==2:    
    # test all components (1 thread per component).
    for comp in selectedComponents:
        comp.splitFactor = 1
        comp.files = comp.files[:1]

from PhysicsTools.HeppyCore.framework.eventsfwlite import Events
config = cfg.Config( components = selectedComponents,
                     sequence = sequence,
                     services = [],
                     events_class = Events)
