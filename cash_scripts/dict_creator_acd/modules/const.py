types = {
        'unsigned_char':('1','UInt8'),
        'int8_t':('1', 'Int8'),
        'uint16_t':('2', 'UInt16'),
        'uint32_t':('4', 'UInt32'),
        'int32_t':('4', 'Int32'),
        'uint64_t':('8', 'UInt64'),
        'int64_t':('8', 'Int64'),
        'time_t':('8', 'UInt64'),
        'uint8':('1','UInt8'),
        'int8':('1','Int8'),
        'uint16':('2', 'UInt16'),
        'uint32':('4', 'UInt32'),
        'int32':('4', 'Int32')
    }
#rg_cnt = {rep groups in cdw,rep groups bi, rep groups ptc}
rg_cnt = {
    'RG_12002_U': (1,254,0),
    'RG_12004_LTOS': (1,2,0),
    'RG_12005_STOIDS': (1,2,0),
    'RG_12005_MMTF': (1,1,0),
    'RG_12005_SFO1': (1,1,0),
    'RG_12005_SFO2': (1,1,0),
    'RG_12005_ISFO': (2,2,0),
    'RG_12005_IOFO': (2,3,0),
    'RG_12006_FTS': (1,1,0),
    'RG_12006_OF': (1,1,0),
    'RG_12006_CF': (1,1,0),
    'RG_12006_NMOF': (1,1,0),
    'RG_12006_NMSC': (1,1,0),
    'RG_12006_MSC': (1,1,0),
    'RG_12006_CF1': (1,1,0),
    'RG_12006_MCIF': (1,1,0),
    'RG_12006_NMCIF': (1,1,0),
    'RG_12006_ECA': (1,1,0),
    'RG_12006_SF': (1,1,0),
    'RG_12006_OFD': (1,1,0),
    'RG_12006_AI': (1,1,0),
    'RG_12006_SCDNM': (4,4,0),
    'RG_12006_SCDM': (2,2,0),
    'RG_12006_SL': (1,1,0),
    'RG_12007_FTS': (1,1,0),
    'RG_12007_OF': (1,1,0),
    'RG_12007_CF': (1,1,0),
    'RG_12007_NMOF': (1,1,0),
    'RG_12007_NMSC': (1,1,0),
    'RG_12007_MSC': (1,1,0),
    'RG_12007_CF1': (1,1,0),
    'RG_12007_MCIF': (1,1,0),
    'RG_12007_NMCIF': (1,1,0),
    'RG_12007_ECA': (1,1,0),
    'RG_12007_AI': (1,1,0),
    'RG_12007_SCDNM': (4,4,0),
    'RG_12007_SCDM': (2,2,0),
    'RG_12008_QR': (1,1,0),
    'RG_12008_SF': (1,1,0),
    'RG_12008_OFD': (1,1,0),
    'RG_12008_ISFO': (1,1,0),
    'RG_12010_MSC': (1,1,0),
    'RG_12010_SCDM': (2,2,0),
    'RG_12015_MSC': (1,1,0),
    'RG_12018_SC': (3,3,0),
    'RG_12021_SCDNM': (4,4,0),
    'RG_12021_SCDM': (2,2,0),
    'RG_12022_NMSC': (1,1,0),
    'RG_12022_SCDNM': (4,4,0),
    'RG_12050_BQ': (1,1,0),
    'RG_12050_OQ': (1,1,0),
    'RG_12050_CD': (1,1,0),
    'RG_12050_NMSC': (1,1,0),
    'RG_12050_MSC': (1,1,0),
    'RG_12224_EMMPR': (0,254,0),
    'RG_12224_BR': (0,254,0),
    'RG_12224_SPR':(0,254,0),
    'RG_12226_CT1': (1,20,0),
    'RG_12227_CTSR': (1,20,0),
    'RG_12228_APFR': (1,20,0),
    'RG_12229_MMR': (1,1,0),
    'RG_12233_TGEMMP': (0,254,0),
    'RG_12234_TCOS': (1,2,2),
    'RG_12252_IACR': (1,254,0),
    'RG_12255_BASR': (1,254,0),
    'RG_12256_CDS': (1,254,0)
}

split_groups = {
#    'RG_12002_U': (1,0),
    'RG_12004_LTOS': (1,0),
    'RG_12005_STOIDS': (1,0),
    'RG_12005_MMTF': (0,0),
    'RG_12005_SFO1': (0,1),
    'RG_12005_SFO2': (0,1),
    'RG_12005_ISFO': (1,0),
    'RG_12005_IOFO': (1,0),
    'RG_12006_FTS': (0,0),
    'RG_12006_OF': (0,0),
    'RG_12006_CF': (0,0),
    'RG_12006_NMOF': (0,0),
    'RG_12006_NMSC': (0,0),
    'RG_12006_MSC': (0,0),
    'RG_12006_CF1': (0,0),
    'RG_12006_MCIF': (0,0),
    'RG_12006_NMCIF': (0,0),
    'RG_12006_ECA': (0,0),
    'RG_12006_SF': (0,1),
    'RG_12006_OFD': (0,0),
    'RG_12006_AI': (0,0),
    'RG_12006_SCDNM': (0,0),
    'RG_12006_SCDM': (0,0),
    'RG_12006_SL': (0,0),
    'RG_12007_FTS': (0,0),
    'RG_12007_OF': (0,0),
    'RG_12007_CF': (0,0),
    'RG_12007_NMOF': (0,0),
    'RG_12007_NMSC': (0,0),
    'RG_12007_MSC': (0,0),
    'RG_12007_CF1': (0,0),
    'RG_12007_MCIF': (0,0),
    'RG_12007_NMCIF': (0,0),
    'RG_12007_ECA': (0,0),
    'RG_12007_AI': (0,0),
    'RG_12007_SCDNM': (0,0),
    'RG_12007_SCDM': (0,0),
    'RG_12008_QR': (0,0),
    'RG_12008_SF': (0,1),
    'RG_12008_OFD': (0,0),
    'RG_12008_ISFO': (0,0),
    'RG_12010_MSC': (0,0),
    'RG_12010_SCDM': (0,0),
#    'RG_12015_MSC': (0,0),
    'RG_12018_SC': (0,0),
    'RG_12021_SCDNM': (0,0),
    'RG_12021_SCDM': (0,0),
    'RG_12022_NMSC': (0,0),
    'RG_12022_SCDNM': (0,0),
    'RG_12031_C': (1,0),
    'RG_12035_SL': (0,1),
    'RG_12035_EMM': (0,1),
    'RG_12040_OR': (0,1),
    'RG_12047_MMPRS':(0,0),
    'RG_12048_CEMMP': (0,1),
    'RG_12048_DPI': (0,1),
    'RG_12050_BQ': (0,0),
    'RG_12050_OQ': (0,0),
    'RG_12050_CD': (0,0),
    'RG_12050_NMSC': (0,0),
    'RG_12050_MSC': (0,0),
    'RG_12054_BMR':(1,0),
    'RG_12055_IMSR': (1,0),
    'RG_12226_CT1': (1,0),
    'RG_12227_CTSR': (1,0),
    'RG_12228_APFR': (1,0),
    'RG_12229_MMR': (0,0),
    'RG_12234_TCOS': (1,0),
    'RG_12252_IACR': (1,0),
    'RG_12255_BASR': (1,0),
    'RG_12256_CDS': (1,0),
    'RG_12260_SDR': (1,0),
    'RG_12263_DS': (0,1),
    'RG_13001_GS': (1,0),
    'RG_13002_IMSS': (1,0),
    'RG_13004_DS': (1,0),
    'RG_13008_BBOFRS': (1,0),
    'RG_13009_DS': (1,0),
    'RG_13102_CS': (1,0)
}

unit_header = [
    ['msgLen', '2', 'Int16'],
    ['blockLen', '2', 'Int16'],
    ['HDR_MESSAGETYPE', '2', 'Int16'],
    ['schemaID', '2', 'Int16'],
    ['versionID', '2', 'Int16']
]

rtf_header = [
    ['protocolVersion', '2', 'Char'],
    ['msgType', '5', 'Char'],
    ['msgLen', '4', 'Char'],
    ['HDR_TOPICID', '8', 'Char'],
    ['HDR_PARTITIONID', '2', 'Int16'],
    ['HDR_OFFSETID', '8', 'Int64'],
    ['Frame', '1', 'Int8'],
    ['HWMProducerID', '8', 'Int64'],
    ['HWMSeqNum', '8', 'Int64'],
    ['SymbolIdx', '4', 'Int32'],
    ['HDR_MIC', '4', 'Char'],
    ['messageLen', '2', 'UInt16'],
    ['blockLen', '2', 'UInt16'],
    ['HDR_MESSAGETYPE', '2', 'UInt16'],
    ['schemaID', '2', 'UInt16'],
    ['versionID', '2', 'UInt16']
]

rtf_parser_header = [
#    ['protocolVersion', '2', 'Char'],
#    ['msgType', '5', 'Char'],
#    ['msgLen', '4', 'Char'],
#    ['HDR_TOPICID', '8', 'Char'],
    ['HDR_PARTITIONID', '2', 'Int16'],
    ['HDR_OFFSETID', '8', 'Int64'],
    ['Frame', '1', 'Int8'],
    ['HWMProducerID', '8', 'Int64'],
    ['HWMSeqNum', '8', 'Int64'],
    ['SymbolIdx', '4', 'Int32'],
    ['HDR_MIC', '4', 'Char'],
    ['messageLen', '2', 'UInt16'],
    ['blockLen', '2', 'UInt16'],
    ['HDR_MESSAGETYPE', '2', 'UInt16'],
    ['schemaID', '2', 'UInt16'],
    ['versionID', '2', 'UInt16']
]

splitted_msgs = [
    '12002',
    '12004',
    '12005',#IAShortTrade
    '12226', #'IATimeTable',
    '12227',#'IATickTable',
    '12228',#'IAAuthorizedPriceFluctuation'
    '12234', #'IATradeClearing'
    '12252', #'IAConstituents'
    '12255', #'IABondAmortizationSchedule'
    '12256' #'IACouponDate'
]

alpha_msgs = [
    '12224', #'IAInstrument',
    '12233'#'IATradingGroup'
]

ENR = {
  'HDR_MIC':'mIC'
, 'ENR_ISIN' : 'iSIN'
, 'ENR_PRICEDECIMALS':'priceDecimals'
, 'ENR_AMOUNTDECIMALS':'amountDecimals'
, 'ENR_QUANTITYDECIMALS':'quantityDecimals'
, 'ENR_INSTRUMENTID':'instrumentID'
, 'ENR_INSTRUMENTGROUPCODE':'instrumentGroupCode'
, 'ENR_OFFICIALSEGMENT':'officialSegment'
, 'ENR_TRADINGCURRENCY':'tradingCurrency'
, 'ENR_CURRENCYCOEFFICIENT':'currencyCoefficient'
, 'ENR_TRADINGCURRENCYINDICATOR':'tradingCurrencyIndicator'
, 'ENR_POOLFACTOR': 'poolFactor'
, 'ENR_INSTRUMENTDECIMALSRATIO': 'instrumentDecimalsRatio'
}

ENR_list = [
    ['HDR_MIC', '4', 'Char'],
    ['ENR_ISIN', '12', 'Char'],
    ['ENR_PRICEDECIMALS', '1', 'UInt8'],
    ['ENR_AMOUNTDECIMALS', '1', 'UInt8'],
    ['ENR_QUANTITYDECIMALS', '1', 'UInt8'],
    ['ENR_INSTRUMENTID', '8', 'UInt64'],
    ['ENR_INSTRUMENTGROUPCODE', '2', 'Char'],
    ['ENR_OFFICIALSEGMENT', '70', 'Char'],
    ['ENR_TRADINGCURRENCY', '3', 'Char'],
    ['ENR_CURRENCYCOEFFICIENT', '4', 'UInt32'],
    ['ENR_TRADINGCURRENCYINDICATOR', '1', 'UInt8'],
    ['ENR_POOLFACTOR','4', 'UInt32'],
    ['ENR_INSTRUMENTDECIMALSRATIO', '1', 'UInt8'],
]

HDR_list = [
    ['HDR_TOPICID', '10', 'Char'],
    ['HDR_PARTITIONID', '1', 'UInt8'],
    ['HDR_BATCHID', '1', 'UInt8'],
    ['HDR_OFFSETID', '8', 'UInt64'],
    ['HDR_PRODUCETIME', '8', 'UInt64'],
    ['HDR_CONSUMETIME', '8', 'UInt64'],
    ['HDR_THREADID', '30', 'Char']
]

rtf_HDR_list = [
#    ['HDR_TOPICID', '10', 'Char'],
#    ['HDR_PARTITIONID', '1', 'UInt8'],
    ['HDR_BATCHID', '1', 'UInt8'],
    ['HDR_APPLKEYSEQUENCENUMBER', '8', 'UInt64'],
#    ['HDR_OFFSETID', '8', 'UInt64'],
    ['HDR_FRAMESN',  '1', 'UInt8'],
    ['HDR_RECEIVETIME',  '8', 'UInt64'],
    ['HDR_HWMSEQUENCENUMBER', '8', 'UInt64'],
    ['HDR_HWMPRODUCERID', '4', 'UInt32']
]

topicid = {
  'SURRND.ALL.MTXC.REF-DATA.OUT' : 'MTXCREFD',
  'OPTIQv2.EQU.FULLMSG.PACK-FULLORD.OUT': '2EQUFORD',
  'OPTIQv2.EQU.FULLMSG.PACK-FULLTRAD.OUT': '2EQUFTRD',
  'OPTIQv2.EQU.MECONSUMR.PACK-TOL.OUT': '2EQUPTOL',
  'OPTIQv2.ETF.FULLMSG.PACK-FULLORD.OUT': '2ETFFORD',
  'OPTIQv2.ETF.FULLMSG.PACK-FULLTRAD.OUT': '2ETFFTRD',
  'OPTIQv2.ETF.MECONSUMR.PACK-TOL.OUT': '2ETFPTOL',
  'OPTIQv2.FXI.FULLMSG.PACK-FULLORD.OUT': '2FXIFORD',
  'OPTIQv2.FXI.FULLMSG.PACK-FULLTRAD.OUT': '2FXIFTRD',
  'OPTIQv2.FXI.MECONSUMR.PACK-TOL.OUT': '2FXIPTOL',
  'OPTIQv2.WAR.FULLMSG.PACK-FULLORD.OUT': '2WARFORD',
  'OPTIQv2.WAR.FULLMSG.PACK-FULLTRAD.OUT': '2WARFTRD',
  'OPTIQv2.WAR.MECONSUMR.PACK-TOL.OUT': '2WARPTOL',
  'OPTIQv2.BLK.FULLMSG.PACK-FULLORD.OUT': '2BLKFORD',
  'OPTIQv2.BLK.FULLMSG.PACK-FULLTRAD.OUT': '2BLKFTRD',
  'OPTIQv2.BLK.MECONSUMR.PACK-TOL.OUT': '2BLKPTOL',
  'SURRND.ALL.TCS.OUT': 'TCSALLOU',
  'SURRND.ALL.TCS.IN': 'TCSALLIN',
  'SURRND.ANY.TCS.PACK-FULLTRAD.OUT': 'TCSANYFT',
  'SURRND.OTC.SATURN.PACK-FULLTRAD.OUT': 'OSATFTRD',
  'SURRND.IDX.GIS.PACK-IDX.OUT': 'GISXPIDX',
  'SURRND.ETF.TCS.PACK-PRIC.OUT':'ETFMTXPO',
  'OPTIQv2.RECOVERY.FULLTRAD.OUT': 'RECOFTRD',
  'SURRND.WAR.GBOX.PACK-STATE.OUT': 'SWARPSTS',
  'SURRND.CASH.PTB.PACK-POSTTRAD.BOTH': 'PTBCPTRD',
  'SURRND.ANY.LPMON.MM-ALERTS.OUT': 'SLPMONAL',
  'SURRND.ANY.LPMON.MM-ALERTS.OUT': 'LPMALERT',
  'SURRND.CASH.DSS.PACK-POSTTRAD.OUT': 'PTBCRESP',
  'RECON.EQU.FULLMSG.PACK-FULLTRAD.OUT': 'RECOEQUT',
  'RECON.ETF.FULLMSG.PACK-FULLTRAD.OUT': 'RECOETFT',
  'RECON.BLK.FULLMSG.PACK-FULLTRAD.OUT': 'RECOBLKT',
  'RECON.FXI.FULLMSG.PACK-FULLTRAD.OUT': 'RECOFXIT',
  'RECON.WAR.FULLMSG.PACK-FULLTRAD.OUT': 'RECOWART'
}
threadid = {
    'MTXCREFD': 'K2CDWMTXCREFD',
    '2EQUFORD': 'K2CDW2EQUFORD',
    '2EQUFTRD': 'K2CDW2EQUFTRD',
    '2EQUPTOL': 'K2CDW2EQUPTOL',
    '2ETFFORD': 'K2CDW2ETFFORD',
    '2ETFFTRD': 'K2CDW2ETFFTRD',
    'ETFMTXPO': 'K2CDWETFMTXPO',
    '2ETFPTOL': 'K2CDW2ETFPTOL',
    '2FXIFORD': 'K2CDW2FXIFORD',
    '2FXIFTRD': 'K2CDW2FXIFTRD',
    '2FXIPTOL': 'K2CDW2FXIPTOL',
    '2WARFORD': 'K2CDW2WARFORD',
    '2WARFTRD': 'K2CDW2WARFTRD',
    '2WARPTOL': 'K2CDW2WARPTOL',
    '2BLKFORD': 'K2CDW2BLKFORD',
    '2BLKFTRD': 'K2CDW2BLKFTRD',
    '2BLKPTOL': 'K2CDW2BLKPTOL',
    'TCSALLOU': 'K2CDWTCSALLOU',
    'GISXPIDX': 'K2CDWGISXPIDX',
    'SWARPSTS': 'K2CDWSWARPSTS',
    'PTBCPTRD': 'K2CDWPTBCPTRD',
    'TCSALLIN': 'K2CDWTCSALLIN',
    'OSATFTRD': 'K2CDWOSATFTRD',
    'LPMALERT': 'K2CDWLPMALERT',
    'RECOEQUT': 'K2CDWRECOEQUT',
    'RECOETFT': 'K2CDWRECOETFT',
    'RECOBLKT': 'K2CDWRECOBLKT',
    'RECOFXIT': 'K2CDWRECOFXIT',
    'RECOWART': 'K2CDWRECOWART'
    }
