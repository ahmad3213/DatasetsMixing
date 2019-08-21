import FWCore.ParameterSet.Config as cms

rootuple = cms.EDAnalyzer('MixingRootupler',
    dimuons = cms.InputTag("onia2MuMuPAT"),
    primaryVertices = cms.InputTag("offlinePrimaryVertices"),
    offlineBeamSpot = cms.InputTag("offlineBeamSpot"),
    muons = cms.InputTag("oniaSelectedMuons"),
    TriggerResults = cms.InputTag("TriggerResults", "", "HLT"),
    TriggerSummaryAOD =  cms.InputTag("hltTriggerSummaryAOD", "", "HLT"),
    hltName = cms.untracked.string("HLT"),
    onia_pdgid = cms.uint32(553),
    onia_mass_cuts = cms.vdouble(0.1,500.0),
    isMC = cms.bool(False),
    OnlyBest = cms.bool(False),
    OnlyGen = cms.bool(False),
    #VERBOSE = cms.untracked.bool(False),
    VERBOSE = cms.untracked.bool(True), 
    triggerList = cms.untracked.vstring(
                                       'HLT_Trimuon5_3p5_2_Upsilon_Muon_v',
     ),
    upsilon_mass = cms.double(9.4603), #9.4603. 3.0969
    triggerCuts = cms.uint32(36),  # 36 for Upsilon, 73 for Jpsi
    TRG_Match_DR = cms.untracked.double(0.2),
    TRG_Match_DP = cms.untracked.double(0.3),
    SecondSource = cms.SecSource(
        "EmbeddedRootSource",
        fileNames = cms.untracked.vstring(
            'SpyFileNameWhichNeedsToBeSet SiStripSpyEventMatcher.SpySource.fileNames'
        ),
        sequential = cms.untracked.bool(True),
    )
)
