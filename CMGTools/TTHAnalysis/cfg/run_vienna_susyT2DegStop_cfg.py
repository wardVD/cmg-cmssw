##########################################################
##       CONFIGURATION FOR SUSY SingleLep TREES       ##
## skim condition: >= 0 loose leptons, no pt cuts or id ##
##########################################################
import PhysicsTools.HeppyCore.framework.config as cfg

#Load all analyzers
from CMGTools.TTHAnalysis.analyzers.susyCore_modules_cff import * 

lepAna.inclusive_muon_dxy = 10.0
lepAna.inclusive_muon_dz  = 10.0
lepAna.inclusive_electron_dxy = 10
lepAna.inclusive_electron_dz  = 10.0

lepAna.loose_muon_pt     = 5000 # 5
lepAna.loose_muon_dxy    = 0.02 # 0.02
lepAna.loose_muon_dz     = 0.5 # 0.5
lepAna.loose_muon_relIso = 100 #0.5
lepAna.loose_muon_absIso = 5   #5
#lepAna.mu_isoCorr = "deltaBeta" 
lepAna.mu_isoCorr = "rhoArea"
lepAna.loose_electron_pt  = 7000   # 7
lepAna.loose_electron_dxy    = 0.05 #0.05
lepAna.loose_electron_dz     = 0.5  # 0.5
lepAna.loose_electron_relIso = 100 #0.5
lepAna.loose_electron_absIso = 5 # 5 
lepAna.ele_isoCorr = "rhoArea"
lepAna.ele_tightId = "Cuts_2012"










#lepAna.loose_muon_pt  = 1
#lepAna.loose_muon_relIso = 5000
#lepAna.loose_muon_dz = 20
#lepAna.loose_muon_dxy = 20
##lepAna.mu_isoCorr = "deltaBeta" 
#lepAna.mu_isoCorr = "rhoArea"
#lepAna.loose_electron_pt  = 7
#lepAna.loose_electron_relIso = 5000
#lepAna.ele_isoCorr = "rhoArea"
#lepAna.ele_tightId = "Cuts_2012"





#lepAna.inclusive_muon_id  = "POG_ID_Tight"
#lepAna.inclusive_muon_pt  = 1
#lepAna.inclusive_muon_eta = 2.4
#lepAna.inclusive_muon_dxy = 1
#lepAna.inclusive_muon_dz  = 20.0
##lepAna.# loose muon selection
#lepAna.loose_muon_id     = "POG_ID_Tight"
#lepAna.loose_muon_pt     = 5
#lepAna.loose_muon_eta    = 2.4
#lepAna.loose_muon_dxy    = 0.02
#lepAna.loose_muon_dz     = 0.5 
#lepAna.loose_muon_relIso = 100
#lepAna.loose_muon_absIso = 10
##lepAna.# inclusive very loose electron selection
#lepAna.inclusive_electron_id  = ""
#lepAna.inclusive_electron_pt  = 5
#lepAna.inclusive_electron_eta = 2.4
#lepAna.inclusive_electron_dxy = 1
#lepAna.inclusive_electron_dz  = 1.0
#lepAna.inclusive_electron_lostHits = 1.0
## loose electron selection
#lepAna.loose_electron_id     = ""  #POG_MVA_ID_NonTrig_full5x5",
#lepAna.loose_electron_pt     = 7
#lepAna.loose_electron_eta    = 2.4
#lepAna.loose_electron_dxy    = 0.05
#lepAna.loose_electron_dz     = 0.5
#lepAna.loose_electron_relIso = 100
#lepAna.loose_muon_absIso     = 10
#lepAna.loose_electron_lostHits = 1.0




########################################3


lepAna.verbose=True


##A default config
#    class_object=LeptonAnalyzer,
#    # input collections
#    muons='slimmedMuons',
#    electrons='slimmedElectrons',
#    rhoMuon= 'fixedGridRhoFastjetAll',
#    rhoElectron = 'fixedGridRhoFastjetAll',
###    photons='slimmedPhotons',
#    # energy scale corrections and ghost muon suppression (off by default)
#    doMuScleFitCorrections=False, # "rereco"
#    doRochesterCorrections=False,
#    doElectronScaleCorrections=False, # "embedded" in 5.18 for regression
#    doSegmentBasedMuonCleaning=False,
#    # inclusive very loose muon selection
#    inclusive_muon_id  = "POG_ID_Loose",
#    inclusive_muon_pt  = 3,
#    inclusive_muon_eta = 2.4,
#    inclusive_muon_dxy = 0.5,
#    inclusive_muon_dz  = 1.0,
#    # loose muon selection
#    loose_muon_id     = "POG_ID_Loose",
#    loose_muon_pt     = 5,
#    loose_muon_eta    = 2.4,
#    loose_muon_dxy    = 0.05,
#    loose_muon_dz     = 0.2,
#    loose_muon_relIso = 0.4,
#    # inclusive very loose electron selection
#    inclusive_electron_id  = "",
#    inclusive_electron_pt  = 5,
#    inclusive_electron_eta = 2.5,
#    inclusive_electron_dxy = 0.5,
#    inclusive_electron_dz  = 1.0,
#    inclusive_electron_lostHits = 1.0,
#    # loose electron selection
#    loose_electron_id     = "", #POG_MVA_ID_NonTrig_full5x5",
#    loose_electron_pt     = 7,
#    loose_electron_eta    = 2.4,
#    loose_electron_dxy    = 0.05,
#    loose_electron_dz     = 0.2,
#    loose_electron_relIso = 0.4,
#    loose_electron_lostHits = 1.0,
#    # muon isolation correction method (can be "rhoArea" or "deltaBeta")
#    mu_isoCorr = "rhoArea" ,
#    mu_effectiveAreas = "Phys14_25ns_v1", #(can be 'Data2012' or 'Phys14_25ns_v1')
#    # electron isolation correction method (can be "rhoArea" or "deltaBeta")
#    ele_isoCorr = "rhoArea" ,
#    el_effectiveAreas = "Phys14_25ns_v1" , #(can be 'Data2012' or 'Phys14_25ns_v1')
#    ele_tightId = "Cuts_2012" ,



########################################





####ttHLepAna.loose_muon_pt  = 5
####ttHLepAna.loose_muon_relIso = 0.4
####ttHLepAna.mu_isoCorr = "deltaBeta"
#####ttHLepAna.loose_muon_absIso5= 10
####ttHLepAna.loose_electron_pt  = 7
####ttHLepAna.loose_electron_relIso = 0.4
#####ttHLepAna.loose_electron_absIso = 10
####ttHLepAna.ele_isoCorr = "rhoArea"




# Redefine what I need
lepAna.doMiniIsolation = True
lepAna.packedCandidates = 'packedPFCandidates'
lepAna.miniIsolationPUCorr = 'rhoArea'
lepAna.miniIsolationVetoLeptons = None


# --- LEPTON SKIMMING ---
ttHLepSkim.minLeptons = 0
ttHLepSkim.maxLeptons = 999
#LepSkim.idCut  = ""
#LepSkim.ptCuts = []

# --- JET-LEPTON CLEANING ---
jetAna.minLepPt = 10 
jetAna.mGT = "PHYS14_25_V2_LowPtHenningFix"
jetAna.doQG = True
jetAna.smearJets = False #should be false in susycore, already
jetAna.recalibrateJets = True #should be true in susycore, already
metAna.recalibrate = False #should be false in susycore, already


#ttHReclusterJets = cfg.Analyzer(
#            'ttHReclusterJetsAnalyzer',
#            )

# Event Analyzer for susy multi-lepton (at the moment, it's the TTH one)

genAna.allGenTaus = True

isoTrackAna.setOff=False

#from CMGTools.TTHAnalysis.analyzers.ttHReclusterJetsAnalyzer  import ttHReclusterJetsAnalyzer
#ttHReclusterJets = cfg.Analyzer(
#    ttHReclusterJetsAnalyzer, name="ttHReclusterJetsAnalyzer",
#    )


from CMGTools.TTHAnalysis.samples.samples_13TeV_private_heplx import T2DegStop_300_270

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


#candAnaMET = cfg.Analyzer(
#    CandidateAnalyzerMET, name='candidateAnalyzerMET',
#    setOff=False,
#    candidates='packedPFCandidates',
#    candidatesTypes='std::vector<pat::PackedCandidate>',
#    )
#
#susyCoreSequence.insert(susyCoreSequence.index(ttHCoreEventAna),
#                        candAnaMET)
#
### Single lepton + ST skim
#from CMGTools.TTHAnalysis.analyzers.ttHSTSkimmer import ttHSTSkimmer
#ttHSTSkimmer = cfg.Analyzer(
#    ttHSTSkimmer, name='ttHSTSkimmer',
#    minST = 175,
#    )


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
     defaultFloatType = 'F', # use Float_t for floating point
     PDFWeights = PDFWeights,
     globalVariables = susySingleLepton_globalVariables,
     globalObjects = susySingleLepton_globalObjects,
     collections = susySingleLepton_collections,
)

#-------- SAMPLES AND TRIGGERS -----------

from CMGTools.TTHAnalysis.samples.samples_13TeV_PHYS14 import *


bkg=1
if bkg:
  selectedComponents =  [TT_PU40bx25]
  TT_PU40bx25.splitFactor=1000 
  #selectedComponents =  [WJetsToLNu]
  #WJetsToLNu.splitFactor=1000 
else:
  selectedComponents =  [T2DegStop_300_270]
  T2DegStop_300_270.splitFactor=1000 



#selectedComponents =  WJetsToLNuHT #[WJetsToLNu] # + WJetsToLNuHT 
#selectedComponents = QCDHT + [WJetsToLNu]  + DYJetsM50HT + SingleTop + [ TTWJets, TTZJets, TTH] + SusySignalSamples
#-------- SEQUENCE

#selectedComponents = [SMS_T5qqqqWW_Gl1500_Chi800_LSP100, SMS_T5qqqqWW_Gl1200_Chi1000_LSP800]

sequence = cfg.Sequence(susyCoreSequence+[
    ttHEventAna,
#    ttHReclusterJets,
#    ttHSTSkimmer,
    treeProducer,
    ])


#-------- HOW TO RUN
test = 1
if test==1:
    # test a single component, using a single thread.
    if bkg:
      #comp = WJetsToLNu
      comp = TT_PU40bx25
    else:
      comp = T2DegStop_300_270
#    comp = SMS_T1tttt_2J_mGl1500_mLSP100
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
