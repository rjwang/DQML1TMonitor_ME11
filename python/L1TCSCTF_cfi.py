import FWCore.ParameterSet.Config as cms

l1tCsctf = cms.EDAnalyzer("L1TCSCTF",
    gmtProducer = cms.InputTag("null"),

                PTLUT = cms.PSet(
                        LowQualityFlag = cms.untracked.uint32(4),
                        ReadPtLUT = cms.bool(False),
                        PtMethod = cms.untracked.uint32(32)
                ),

    statusProducer = cms.InputTag("csctfDigis"),
    outputFile = cms.untracked.string(''),
    lctProducer = cms.InputTag("csctfDigis"),
    verbose = cms.untracked.bool(False),
    gangedME11a = cms.untracked.bool(False),
    trackProducer = cms.InputTag("csctfDigis"),
    mbProducer = cms.InputTag("csctfDigis:DT"),
    DQMStore = cms.untracked.bool(True),
    disableROOToutput = cms.untracked.bool(True)
)

#
# Make changes for running in Run 2
#
from Configuration.StandardSequences.Eras import eras
eras.run2_common.toModify( l1tCsctf, gangedME11a = False )
