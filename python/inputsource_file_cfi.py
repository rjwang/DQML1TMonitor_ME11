#
# provide online L1 Trigger DQM input from file(s)
#
# V M Ghete 2010-07-09

import FWCore.ParameterSet.Config as cms

###################### user choices ######################

# choose one sample identifier from the list of data samples
#
#sampleIdentifier = '165633-CAFDQM'
#sampleIdentifier = '195378'
#sampleIdentifier = '195390'
#sampleIdentifier = 'Commissioning2014'
#sampleIdentifier = '225461'
#sampleIdentifier = '245484'
#sampleIdentifier = '237068'
#sampleIdentifier = '237631'
sampleIdentifier = '251131'



#sampleIdentifier = '226144'

#sampleIdentifier = '226667'

#sampleIdentifier = '227055'

#sampleIdentifier = '227449'
#sampleIdentifier = '229965'






#sampleIdentifier = '225602'
#sampleIdentifier = '225608'

#maxNumberEvents = 100#0#0
#maxNumberEvents = 5000#0#0
#maxNumberEvents = 100#0#0
#maxNumberEvents  = 500000
maxNumberEvents = -1#0#0



###################### end user choices ###################

# initialize list of files, of secondary files, list of selected events and luminosity segments
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
selectedEvents = cms.untracked.VEventRange()
selectedLumis= cms.untracked.VLuminosityBlockRange()


maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(maxNumberEvents)
)



if sampleIdentifier == '195378' :
    runNumber = '195378'
    dataset = '/MinimumBias/Run2012B-v1/RAW'
    dataType = 'RAW'
    useDAS = True
    selectedLumis= cms.untracked.VLuminosityBlockRange(
                                                '195378:1275-195378:max'
                                                )

elif sampleIdentifier == '195379' :
    runNumber = '195379'
    dataset = '/MinimumBias/Run2012B-v1/RAW'
    dataType = 'RAW'
    useDAS = True

elif sampleIdentifier == '195390' :
    runNumber = '195390'
    dataset = '/MinimumBias/Run2012B-v1/RAW'
    dataType = 'RAW'
    useDAS = True

# high PU run 2011
elif sampleIdentifier == '179828' :
    runNumber = '179828'
    dataset =  '/ZeroBiasHPF0/Run2011B-v1/RAW'
    dataType = 'RAW'
    useDAS = True


elif sampleIdentifier == '165633-CAFDQM' :
    runNumber = '165633'
    dataset = '/ZeroBiasHPF0/Run2011B-v1/RAW'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
            'file:/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/DQMTest/MinimumBias__RAW__v1__165633__1CC420EE-B686-E011-A788-0030487CD6E8.root'
            ]);

elif sampleIdentifier == '225461' :
    runNumber = '225461'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
            'file:/afs/cern.ch/work/p/peveraer/public/local_run_225461/csctf.root'
            ]);

elif sampleIdentifier == '225602' :
    runNumber = '225602'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/p/peveraer/public/local_run_225602/csctf.root'
            ]);

elif sampleIdentifier == '225608' :
    runNumber = '225608'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/p/peveraer/public/local_run_225608/csctf.root'
            ]);


elif sampleIdentifier == '226129' :
    runNumber = '226129'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    '/store/user/rewang/csctf/local_run_226129_csctf.root'
            ]);


elif sampleIdentifier == '251131' :
    runNumber = '251131'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
'/store/data/Run2015B/SingleMu/RAW/v1/000/251/131/00000/0C18F8EA-FB24-E511-98C6-02163E013455.root',
'/store/data/Run2015B/SingleMu/RAW/v1/000/251/131/00000/584AA782-F524-E511-9277-02163E0119DB.root',
'/store/data/Run2015B/SingleMu/RAW/v1/000/251/131/00000/82298615-F824-E511-8BD6-02163E011FD5.root',
'/store/data/Run2015B/SingleMu/RAW/v1/000/251/131/00000/CCEFE980-F524-E511-A776-02163E013656.root',
'/store/data/Run2015B/SingleMu/RAW/v1/000/251/131/00000/DCAA0D81-F724-E511-BD2C-02163E011ABD.root',
'/store/data/Run2015B/SingleMu/RAW/v1/000/251/131/00000/DE75C18D-FB24-E511-A8AE-02163E011D0D.root',
'/store/data/Run2015B/SingleMu/RAW/v1/000/251/131/00000/EA8CA37D-F724-E511-BB50-02163E01361A.root',
            ]);


elif sampleIdentifier == '245484' :
    runNumber = '245484'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/tmp/rewang/csctf_00245484.root'
            ]);


elif sampleIdentifier == '237068' :
    runNumber = '237068'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/001F151C-B5C3-E411-BDC4-02163E012632.root'
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/007A9BE4-DDC3-E411-9DA9-02163E0118D4.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/02A816FE-C3C3-E411-852D-02163E011DE8.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/0618FCC3-B8C3-E411-BCB1-02163E012628.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/081A99FE-E1C3-E411-965A-02163E012A42.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/084C1503-DAC3-E411-B1D6-02163E012696.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/0C20E8F1-B8C3-E411-A4A8-02163E011D3D.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/10DA2644-D3C3-E411-A4D2-02163E0127F8.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/120049C9-B8C3-E411-AE6E-02163E0121FD.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/1430E3DB-BBC3-E411-A898-02163E011885.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/18E776E0-D6C3-E411-9A7E-02163E0123EF.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/1A12ABC5-B8C3-E411-B9A7-02163E012AEA.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/1AC39CD4-C5C3-E411-9E79-02163E011885.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/1E9978CB-B9C3-E411-9394-02163E012123.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/1EAE290B-BEC3-E411-92F1-02163E0122E8.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/1EC387CA-B8C3-E411-9120-02163E011D20.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/225C1975-94C3-E411-8E24-02163E01181B.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/229C2211-C3C3-E411-A64D-02163E0129EA.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/22BD64C2-B8C3-E411-B74D-02163E011DD6.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/324E93C0-B8C3-E411-BDC6-02163E0126E7.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/3490A3C1-B8C3-E411-9566-02163E01222D.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/366C3628-E1C3-E411-973B-02163E0126F3.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/3AD68CCD-C7C3-E411-912B-02163E011DFE.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/3C8E3FFC-BDC3-E411-BFFE-02163E012AF1.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/3CB7DA2A-BCC3-E411-97C6-02163E0118E4.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/46BCA12E-97C3-E411-8C41-02163E0120DE.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/4E960FD1-B8C3-E411-836C-02163E0118D4.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/60603DCC-C7C3-E411-9748-02163E011DE0.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/62C40C77-D3C3-E411-A553-02163E011DA9.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/64AB1C90-E4C3-E411-9CF9-02163E012A02.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/7A5DD4C3-B8C3-E411-B3FB-02163E011DF5.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/7C7ECAFA-BDC3-E411-A278-02163E012426.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/7E7B3B43-D3C3-E411-A652-02163E0121F7.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/80C440DB-B8C3-E411-965A-02163E01261F.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/845676DD-B8C3-E411-A462-02163E012380.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/849EC7DC-C5C3-E411-8D38-02163E011DD7.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/867029A3-A6C3-E411-98CE-02163E012593.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/8676CBCA-B8C3-E411-8F03-02163E0127C3.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/88F36618-ABC3-E411-B525-02163E012BD2.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/960C7AFF-B1C3-E411-987E-02163E01223F.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/964FA7CE-B8C3-E411-95E7-02163E011DFE.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/9AAB9DE4-DDC3-E411-A970-02163E01185F.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/9C2E8911-C3C3-E411-B323-02163E012720.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/9C61FC05-97C3-E411-A311-02163E012A1C.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/9E5E6FC2-B8C3-E411-9455-02163E0127F8.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/A0DAFBFC-C3C3-E411-A836-02163E012807.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/A2080AFC-BDC3-E411-92B2-02163E012BD6.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/A2CCE959-94C3-E411-82D9-02163E01217E.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/A6225BE5-DDC3-E411-A72C-02163E011849.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/AAA351D9-C8C3-E411-BFBD-02163E012123.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/AAE38F94-DFC3-E411-9870-02163E0127C3.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/B4323AE0-D6C3-E411-9B86-02163E011DD4.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/BC76A2C7-B8C3-E411-BD9F-02163E012957.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/CA6FFCFB-C3C3-E411-96B8-02163E011897.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/CC883CC0-B8C3-E411-9E10-02163E012AF1.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/CE05A7C6-B9C3-E411-9D2C-02163E01222D.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/CE229CC9-B8C3-E411-9948-02163E012426.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/D018A252-D7C3-E411-A529-02163E012AF1.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/D0733A4B-D7C3-E411-8858-02163E012AEA.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/D0B84D6A-D3C3-E411-9D75-02163E0124A0.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/D4F508F9-BBC3-E411-9008-02163E011DF8.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/DC1AC71F-E1C3-E411-BB89-02163E012A42.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/E2BFD90D-CCC3-E411-A8DF-02163E011DE0.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/E41F30CB-BFC3-E411-8D40-02163E012A56.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/E42A7044-D3C3-E411-9866-02163E012A02.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/E4792DDC-BBC3-E411-823D-02163E011CE6.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/E8874AD6-C9C3-E411-B92D-02163E011DC0.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/E8C53B1B-D8C3-E411-ADB6-02163E011885.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/EA01E8B3-BEC3-E411-8CE5-02163E012188.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/F2B6BDDD-BBC3-E411-AF2E-02163E012209.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/F6FA4CFF-BDC3-E411-B58B-02163E011E06.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/F87CB122-BCC3-E411-B25C-02163E011DC9.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/FA8E720B-CCC3-E411-BCBC-02163E0122AB.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/FCA47CF9-BBC3-E411-8B67-02163E011DC0.root',
#'/store/data/Commissioning2015/Cosmics/RAW/v1/000/237/068/00000/FCF8C0DE-BBC3-E411-99B9-02163E012B7B.root',
            ]);


elif sampleIdentifier == '226144' :
    runNumber = '226144'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/p/peveraer/public/local_run_226144/csctf.root'
            ]);


elif sampleIdentifier == '226667' :
    runNumber = '226667'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/p/peveraer/public/local_run_226667/csctf.root'
            ]);


elif sampleIdentifier == '227055' :
    runNumber = '227055'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/e/evka/public/local_run_227055/csctf.root'
            ]);



elif sampleIdentifier == '227449' :
    runNumber = '227449'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/afs/cern.ch/work/p/peveraer/public/local_run_227449/csctf.root'
            ]);



elif sampleIdentifier == '229965' :
    runNumber = '229965'
    dataset = 'None'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
	    'file:/tmp/rewang/csctf_00229965.root'
            ]);





elif sampleIdentifier == 'Commissioning2014' :
    runNumber = '225956'
    dataset = '/Commissioning2014/Cosmics/RAW'
    dataType = 'RAW'
    useDAS = False
    readFiles.extend( [
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/930/00000/7604F4CA-9D33-E411-A11C-02163E008D1E.root',
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/948/00000/06DDCD46-9E33-E411-89A3-02163E00EF65.root',
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/949/00000/A2C2553D-9E33-E411-912B-02163E00F191.root',
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/953/00000/1A0A48DE-A033-E411-9310-02163E00F11B.root',
       #'/store/data/Commissioning2014/Cosmics/RAW/v3/000/225/956/00000/640CC997-A633-E411-8432-02163E006E23.root'
       #'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/041F728D-A033-E411-8BC5-02163E007A48.root'
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/041F728D-A033-E411-8BC5-02163E007A48.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/104E624D-A133-E411-A31E-02163E00ED8B.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/188EDA50-A133-E411-93F8-02163E00CFD6.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/1C42F5A0-A133-E411-9256-02163E00F120.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/40736BB2-A133-E411-805A-02163E00D44D.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/4490CC4E-A133-E411-9D5E-02163E009F78.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/56DFD7AA-A633-E411-AB4D-02163E008EFB.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/5CC308B3-A133-E411-BDE3-02163E00A1B7.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/60554991-A633-E411-B321-02163E008E84.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/82CA7B9F-A633-E411-A0A9-02163E008E84.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/867E7D31-A133-E411-9CDF-02163E00CFD6.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/9AA49FB1-A133-E411-A607-02163E00F029.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/CA51E093-A633-E411-B34A-02163E008F58.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/E0E0774D-A133-E411-A072-02163E008C0A.root',
'/store/data/Commissioning2014/MinimumBias/RAW/v3/000/225/956/00000/F0EAB950-A133-E411-9DA5-02163E008CEF.root',

            ]);

elif sampleIdentifier == 'FileStream_105760' :
    runNumber = '105760'
    dataset = 'A_Stream'
    dataType = 'FileStream'
    useDAS = False
    readFiles.extend( [
            'file:/lookarea_SM/MWGR_29.00105760.0001.A.storageManager.00.0000.dat'
            ] );

else :
    print 'Error: sample identifier ', sampleIdentifier, ' not defined.\n'
    errorUserOptions = True
    runNumber = '0'
    dataset = 'None'
    dataType = 'None'
    useDAS = False


#
# end of data samples
#

print "   Run number: ", runNumber
print "   Dataset: ", dataset
print "   Data type: ", dataType

if useDAS :
    import das_client
    import os

    # query DAS
    myQuery =  'file dataset=' + dataset + ' run=' + runNumber
    dasClientCommand = 'das_client.py --limit=0 --format=plain --query='+'"'+myQuery+'"'
    data = os.popen(dasClientCommand)
    filePaths = data.readlines()


    print '\n   das_client using the query'
    print '      ', myQuery
    print '   retrieved the following files\n'

    #newPath = []
    for line in filePaths :
        print '      ', line
	#newPath.append('root://eoscms//eos/cms'+line)

    readFiles.extend(filePaths);
    #readFiles.extend(newPath);
    #readFiles.extend('file:');


    # nothing added to secondary files by DAS
    secFiles.extend([
            ])


# for RAW data, run first the RAWTODIGI
if dataType == 'StreamFile' :
    source = cms.Source("NewEventStreamFileReader", fileNames=readFiles)
else :
    source = cms.Source ('PoolSource',
                            fileNames=readFiles,
                            secondaryFileNames=secFiles,
                            lumisToProcess = selectedLumis,
                            eventsToProcess = selectedEvents
                            )

