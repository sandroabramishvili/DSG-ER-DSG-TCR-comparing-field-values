# -*- coding: utf-8 -*-

msgs = {}

msgids = {
	'12224A': 'RG_12224_EMMPR',
	'12233A': 'RG_12233_TGEMMP',
	'540': 'DeclarationEntryInternal',
	'541': 'DeclarationEntryAckInternal',
	'542': 'DeclarationNoticeInternal',
	'543': 'DeclarationCancelAndRefusalInternal',
	'544': 'FundPriceInputInternal',
	'545': 'FundPriceInputAckInternal',
	'546': 'DeclarationEntryRejectInternal',
	'12001': 'IAMarketStatusChange',
	'12002': 'IAMarketLimits',
	'12003': 'IAPriceUpdate',
	'12004': 'IALongTrade',
	'12005': 'IAShortTrade',
	'12006': 'IALongOrder',
	'12007': 'IAOrderNewModify',
	'12008': 'IAShortOrderFill',
	'12009': 'IAShortOrderCancel',
	'12010': 'IAShortOrderReject',
	'12011': 'IAShortOrderTrigger',
	'12012': 'IAShortOrderRefill',
	'12013': 'IAShortOrderMTL',
	'12014': 'IAShortOrderVFAVFC',
	'12015': 'IAShortOrderConfirmation',
	'12016': 'IAShortTradeCancellation',
	'12017': 'IAShortOrderStopQueue',
	'12018': 'IAStaticCollars',
	'12019': 'IAShortOpenOrderRequest',
	'12020': 'IAShortOwnershipRequest',
	'12021': 'IATradeBustNotification',
	'12022': 'IAQuoteRequest',
	'12023': 'IATradePublication',
	'12041': 'IACalendar',
	'12044': 'IAHeaderRefData',
	'12067': 'IAClosingPrice',
	'12050': 'IAQuote',
	'12051': 'IAAFQRFE',
	'12052': 'IAPriceInput',
	'12053': 'IAWarrantStatusUpdate',
	'12215': 'IACountry',
	'12216': 'IACurrency',
	'12217': 'IAReportingRegulator',
	'12218': 'IAParticipantAttributesDef',
	'12219': 'IAParticipantType',
	'12220': 'IAMIC',
	'12221': 'IAParticipantCashAuthor',
	'12222': 'IAParticipant',
	'12223': 'IAMarketPlace',
	'12224': 'IAInstrument',
	'12226': 'IATimetable',
	'12227': 'IATicktable',
	'12228': 'IAAuthorizedPriceFluctuation',
	'12229': 'IAMarketMaker',
	'12231': 'IAMarketMakerObligations',
	'12232': 'IAIssuer',
	'12233': 'IATradingGroup',
	'12234': 'IATradeClearing',
	'12240': 'IAIndexLevel',
	'12241': 'IAIndexReferential'
}

topicid = {
	'SURRND.ALL.MTXC.REF-DATA.OUT': 'MTXCREFD',
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
	'SURRND.ETF.TCS.PACK-PRIC.OUT': 'ETFMTXPO',
	'OPTIQv2.RECOVERY.FULLTRAD.OUT': 'RECOFTRD',
	'SURRND.WAR.GBOX.PACK-STATE.OUT': 'SWARPSTS',
	'SURRND.CASH.PTB.PACK-POSTTRAD.BOTH': 'PTBCPTRD',
	'SURRND.ANY.LPMON.MM-ALERTS.OUT': 'LPMALERT',
	'SURRND.CASH.DSS.PACK-POSTTRAD.OUT': 'PTBCRESP',
	'RECON.EQU.FULLMSG.PACK-FULLTRAD.OUT': 'RECOEQUT',
	'RECON.ETF.FULLMSG.PACK-FULLTRAD.OUT': 'RECOETFT',
	'RECON.BLK.FULLMSG.PACK-FULLTRAD.OUT': 'RECOBLKT',
	'RECON.FXI.FULLMSG.PACK-FULLTRAD.OUT': 'RECOFXIT',
	'RECON.WAR.FULLMSG.PACK-FULLTRAD.OUT': 'RECOWART'
}

threadid = {
	'K2CDWMTXCREFD': ['0'],
	'K2CDW2EQUFORD01': ['0', '4', '8', '12', '16', '20', '24', '28', '32', '36', '40', '44', '48', '52', '56'],
	'K2CDW2EQUFORD02': ['1', '5', '9', '13', '17', '21', '25', '29', '33', '37', '41', '45', '49', '53', '57'],
	'K2CDW2EQUFORD03': ['2', '6', '10', '14', '18', '22', '26', '30', '34', '38', '42', '46', '50', '54', '58'],
	'K2CDW2EQUFORD04': ['3', '7', '11', '15', '19', '23', '27', '31', '35', '39', '43', '47', '51', '55', '59'],
	'K2CDW2EQUFTRD': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],
	'K2CDW2EQUPTOL01': ['0', '4', '8', '12', '16', '20', '24', '28', '32', '36', '40', '44', '48', '52', '56'],
	'K2CDW2EQUPTOL02': ['1', '5', '9', '13', '17', '21', '25', '29', '33', '37', '41', '45', '49', '53', '57'],
	'K2CDW2EQUPTOL03': ['2', '6', '10', '14', '18', '22', '26', '30', '34', '38', '42', '46', '50', '54', '58'],
	'K2CDW2EQUPTOL04': ['3', '7', '11', '15', '19', '23', '27', '31', '35', '39', '43', '47', '51', '55', '59'],
	'K2CDW2ETFFORD01': ['0', '5', '10'],
	'K2CDW2ETFFORD02': ['1', '6', '11'],
	'K2CDW2ETFFORD03': ['2', '7', '12'],
	'K2CDW2ETFFORD04': ['3', '8', '13'],
	'K2CDW2ETFFORD05': ['4', '9', '14'],
	'K2CDW2ETFFTRD': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDWETFMTXPO': ['0'],
	'K2CDW2ETFPTOL01': ['0', '5', '10'],
	'K2CDW2ETFPTOL02': ['1', '6', '11'],
	'K2CDW2ETFPTOL03': ['2', '7', '12'],
	'K2CDW2ETFPTOL04': ['3', '8', '13'],
	'K2CDW2ETFPTOL05': ['4', '9', '14'],
	'K2CDW2FXIFORD': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDW2FXIFTRD': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDW2FXIPTOL': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDW2WARFORD01': ['0', '6', '12', '18', '24'],
	'K2CDW2WARFORD02': ['1', '7', '13', '19', '25'],
	'K2CDW2WARFORD03': ['2', '8', '14', '20', '26'],
	'K2CDW2WARFORD04': ['3', '9', '15', '21', '27'],
	'K2CDW2WARFORD05': ['4', '10', '16', '22', '28'],
	'K2CDW2WARFORD06': ['5', '11', '17', '23', '29'],
	'K2CDW2WARFTRD': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'],
	'K2CDW2WARPTOL01': ['0', '6', '12', '18', '24'],
	'K2CDW2WARPTOL02': ['1', '7', '13', '19', '25'],
	'K2CDW2WARPTOL03': ['2', '8', '14', '20', '26'],
	'K2CDW2WARPTOL04': ['3', '9', '15', '21', '27'],
	'K2CDW2WARPTOL05': ['4', '10', '16', '22', '28'],
	'K2CDW2WARPTOL06': ['5', '11', '17', '23', '29'],
	'K2CDW2BLKFORD': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDW2BLKFTRD': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDW2BLKPTOL': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDWTCSALLOU': ['0'],
	'K2CDWGISXPIDX': ['0'],
	'K2CDWSWARPSTS': ['0'],
	'K2CDWPTBCPTRD': ['0'],
	'K2CDWTCSALLIN': ['0'],
	'K2CDWOSATFTRD': ['0'],
	'K2CDWRECOEQUT': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'],
	'K2CDWRECOETFT': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDWRECOBLKT': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDWRECOFXIT': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'],
	'K2CDWRECOWART': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29'],
	'K2CDWLPMALERT': ['0', '1']
}

unit_header = [
	['msgLen', '2', 'Int16'],
	['blockLen', '2', 'Int16'],
	['HDR_MESSAGETYPE', '2', 'Int16'],
	['schemaID', '2', 'Int16'],
	['versionID', '2', 'Int16']
]

ENR = {
	'HDR_MIC': 'mIC',
	'ENR_ISIN': 'iSIN',
	'ENR_PRICEDECIMALS': 'priceDecimals',
	'ENR_AMOUNTDECIMALS': 'amountDecimals',
	'ENR_QUANTITYDECIMALS': 'quantityDecimals',
	'ENR_INSTRUMENTID': 'instrumentID',
	'ENR_INSTRUMENTGROUPCODE': 'instrumentGroupCode',
	'ENR_OFFICIALSEGMENT': 'officialSegment',
	'ENR_TRADINGCURRENCY': 'tradingCurrency',
	'ENR_CURRENCYCOEFFICIENT': 'currencyCoefficient',
	'ENR_TRADINGCURRENCYINDICATOR': 'tradingCurrencyIndicator',
	'ENR_POOLFACTOR': 'poolFactor',
	'ENR_INSTRUMENTDECIMALSRATIO': 'instrumentDecimalsRatio'
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
	['ENR_POOLFACTOR', '4', 'UInt32'],
	['ENR_INSTRUMENTDECIMALSRATIO', '1', 'UInt8']
]

splitted_msgs = [
'12002', '12004', '12005', '12226', '12227', '12228', '12234', '12252', '12255', '12256']

alpha_msgs = [
'12224', '12233']

HDR_list = [
	['HDR_TOPICID', '10', 'Char'],
	['HDR_PARTITIONID', '1', 'UInt8'],
	['HDR_BATCHID', '1', 'UInt8'],
	['HDR_OFFSETID', '8', 'UInt64'],
	['HDR_PRODUCETIME', '8', 'UInt64'],
	['HDR_CONSUMETIME', '8', 'UInt64'],
	['HDR_THREADID', '30', 'Char']
]

msgs['DeclarationEntryInternal'] = [
	['oESessionID', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['messageSendingTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['operationType', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['enteringCounterparty', '8', 'Char'],
	['side', '1', 'UInt8'],
	['quantity', '8', 'UInt64'],
	['price', '8', 'Int64'],
	['executionWithinFirmShortCode', '4', 'Int32'],
	['clientIdentificationShortCode', '4', 'Int32'],
	['mICofSecondaryListing', '4', 'Char'],
	['centralisationDate', '10', 'Char'],
	['clearingFirmID', '8', 'Char'],
	['accountType', '1', 'UInt8'],
	['accountTypeCross', '1', 'UInt8'],
	['tradingCapacity', '1', 'UInt8'],
	['tradingCapacityCross', '1', 'UInt8'],
	['settlementPeriod', '1', 'UInt8'],
	['settlementFlag', '1', 'UInt8'],
	['guaranteeFlag', '1', 'UInt8'],
	['miFIDIndicators', '1', 'UInt8'],
	['transactionPriceType', '1', 'UInt8'],
	['principalCode', '8', 'Char'],
	['principalCodeCross', '8', 'Char'],
	['startTimeVwap', '4', 'UInt32'],
	['endTimeVwap', '4', 'UInt32'],
	['grossTradeAmount', '8', 'Int64'],
	['accountNumber', '12', 'Char'],
	['accountNumberCross', '12', 'Char'],
	['freeText', '18', 'Char'],
	['freeTextCross', '18', 'Char'],
	['investmentDecisionWFirmShortCode', '4', 'Int32'],
	['clientIdentificationShortCodeCross', '4', 'Int32']
]

msgs['DeclarationEntryAckInternal'] = [
	['oESessionID', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['messageSendingTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['declarationID', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['mICofSecondaryListing', '4', 'Char'],
	['operationType', '1', 'UInt8'],
	['preMatchingType', '1', 'UInt8'],
	['waiverIndicator', '1', 'UInt8']
]

msgs['DeclarationNoticeInternal'] = [
	['firmID', '8', 'Char'],
	['clientOrderID', '8', 'Int64'],
	['declarationID', '8', 'UInt64'],
	['declarationStatus', '1', 'UInt8'],
	['operationType', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['enteringCounterparty', '8', 'Char'],
	['side', '1', 'UInt8'],
	['quantity', '8', 'UInt64'],
	['price', '8', 'Int64'],
	['preMatchingType', '1', 'UInt8'],
	['tradeTime', '8', 'UInt64'],
	['mICofSecondaryListing', '4', 'Char'],
	['centralisationDate', '10', 'Char'],
	['clearingFirmID', '8', 'Char'],
	['accountType', '1', 'UInt8'],
	['accountTypeCross', '1', 'UInt8'],
	['tradingCapacity', '1', 'UInt8'],
	['tradingCapacityCross', '1', 'UInt8'],
	['settlementFlag', '1', 'UInt8'],
	['settlementPeriod', '1', 'UInt8'],
	['guaranteeFlag', '1', 'UInt8'],
	['transactionPriceType', '1', 'UInt8'],
	['principalCode', '8', 'Char'],
	['principalCodeCross', '8', 'Char'],
	['startTimeVwap', '4', 'UInt32'],
	['endTimeVwap', '4', 'UInt32'],
	['grossTradeAmount', '8', 'Int64'],
	['accountNumber', '12', 'Char'],
	['accountNumberCross', '12', 'Char'],
	['freeText', '18', 'Char'],
	['freeTextCross', '18', 'Char'],
	['waiverIndicator', '1', 'UInt8'],
	['previousDayIndicator', '1', 'UInt8'],
	['miscellaneousFeeAmount', '8', 'Int64'],
	['cCPID', '1', 'UInt8'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['DeclarationCancelAndRefusalInternal'] = [
	['oESessionID', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['messageSendingTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['declarationID', '8', 'UInt64'],
	['actionType', '1', 'UInt8'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['FundPriceInputInternal'] = [
	['oESessionID', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['messageSendingTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['price', '8', 'Int64'],
	['bypassIndicator', '1', 'UInt8']
]

msgs['FundPriceInputAckInternal'] = [
	['oESessionID', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['messageSendingTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['price', '8', 'Int64'],
	['bypassIndicator', '1', 'UInt8']
]

msgs['DeclarationEntryRejectInternal'] = [
	['oESessionID', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['messageSendingTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['mICofSecondaryListing', '4', 'Char'],
	['operationType', '1', 'UInt8'],
	['errorCode', '2', 'UInt16'],
	['rejectedMessage', '1', 'UInt8'],
	['rejectedMessageID', '2', 'UInt16']
]

msgs['IAMarketStatusChange'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['phaseId', '1', 'UInt8'],
	['tradingGroupState', '1', 'UInt8'],
	['instrumentState', '1', 'UInt8'],
	['changeType', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['eventTime', '8', 'UInt64'],
	['bookState', '1', 'UInt8'],
	['statusReason', '1', 'UInt8'],
	['phaseQualifier', '2', 'UInt16'],
	['tradingPeriod', '1', 'UInt8'],
	['tradingSide', '1', 'UInt8'],
	['priceLimits', '1', 'UInt8'],
	['quoteSpreadMultiplier', '1', 'UInt8'],
	['orderEntryQualifier', '1', 'UInt8'],
	['session_', '1', 'UInt8'],
	['scheduledEvent', '1', 'UInt8'],
	['scheduledEventTime', '8', 'UInt64'],
	['tradingGroupOrderEntryQualifier', '1', 'UInt8'],
	['instrumentOrderEntryQualifier', '1', 'UInt8'],
	['phaseTime', '8', 'UInt64'],
	['contractSymbolIndex', '4', 'UInt32'],
	['priceLimitStyle', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['startTimeSMC', '8', 'UInt64'],
	['actualEventTime', '8', 'UInt64']
]

msgs['IAMarketLimits'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['eventTime', '8', 'UInt64'],
	['sequenceTime', '8', 'UInt64'],
	['RG_12002_U', 1, 1, 0]
]

msgs['RG_12002_U'] = [
	['updateType', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['numberOfOrders', '2', 'UInt16'],
	['price', '8', 'Int64'],
	['quantity', '8', 'UInt64']
]

msgs['IAPriceUpdate'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['eventTime', '8', 'UInt64'],
	['priceType', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['price', '8', 'Int64'],
	['quantity', '8', 'UInt64'],
	['imbalanceQty', '8', 'UInt64'],
	['imbalanceQtySide', '1', 'UInt8'],
	['priceDate', '8', 'UInt64'],
	['sequenceTime', '8', 'UInt64']
]

msgs['IALongTrade'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['executionID', '4', 'UInt32'],
	['eventId', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['lastTradedPx', '8', 'Int64'],
	['lastShares', '8', 'UInt64'],
	['tradeType', '1', 'UInt8'],
	['tradeQualifier', '1', 'UInt8'],
	['transparencyIndicator', '1', 'UInt8'],
	['tradeTime', '8', 'UInt64'],
	['publicationTime', '8', 'UInt64'],
	['execPhase', '1', 'UInt8'],
	['session_', '1', 'UInt8'],
	['externalClearingIndicator', '1', 'UInt8'],
	['crossOrderIndicator', '1', 'UInt8'],
	['bestBid', '8', 'Int64'],
	['bestOffer', '8', 'Int64'],
	['counterpartyReasonType', '1', 'UInt8'],
	['settlementPeriod', '1', 'UInt8'],
	['guaranteeFlag', '1', 'UInt8'],
	['indicativePrice', '8', 'Int64'],
	['finalTradedPx', '8', 'Int64'],
	['temporaryTradedPx', '8', 'Int64'],
	['lISTransactionID', '4', 'UInt32'],
	['wholesaleTradeType', '1', 'UInt8'],
	['messagePriceNotation', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['rFCID', '4', 'UInt32'],
	['exchangeCode', '1', 'Char'],
	['tradeUniqueIdentifier', '16', 'Char'],
	['RG_12004_LTOS', 1, 1, 0]
]

msgs['RG_12004_LTOS'] = [
	['orderID', '8', 'UInt64'],
	['orderPx', '8', 'Int64'],
	['orderType', '1', 'UInt8'],
	['orderSide', '1', 'UInt8'],
	['firmID', '8', 'Char'],
	['logicalAccessID', '4', 'UInt32'],
	['oEPartitionID', '2', 'UInt16'],
	['bookIn', '8', 'UInt64'],
	['tradeQualifier', '1', 'UInt8'],
	['accountTypeInternal', '1', 'UInt8'],
	['timeInForce', '1', 'UInt8'],
	['tradingCapacity', '1', 'UInt8'],
	['clientOrderID', '8', 'Int64'],
	['miFIDIndicators', '1', 'UInt8'],
	['lPRole', '1', 'UInt8'],
	['freeText', '18', 'Char'],
	['clearingFirmID', '8', 'Char'],
	['clientID', '8', 'Char'],
	['accountNumber', '12', 'Char'],
	['technicalOrigin', '1', 'UInt8'],
	['openClose', '2', 'UInt16'],
	['clearingInstruction', '2', 'UInt16'],
	['originalClientIDShortCode', '4', 'Int32'],
	['originalExecWFirmShortCode', '4', 'Int32'],
	['originalInvestDecisWFirmShortCode', '4', 'Int32'],
	['originalNonExecBrokerShortCode', '4', 'Int32'],
	['cCPID', '1', 'UInt8'],
	['marketPhaseFlag', '1', 'UInt8'],
	['marginTradingFlag', '1', 'UInt8'],
	['accessFlag', '1', 'UInt8'],
	['traderID', '16', 'Char'],
	['senderLocationID', '11', 'Char'],
	['deskID', '11', 'Char'],
	['originalInvestorID', '16', 'Char'],
	['clearingAccount', '16', 'Char'],
	['symbolIndex', '4', 'UInt32'],
	['executionID', '4', 'UInt32'],
	['strategyCode', '1', 'Char'],
	['tradeLegSide', '1', 'UInt8'],
	['longClientID', '16', 'Char'],
	['exchangeIOIID', '8', 'Int64'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['IAShortTrade'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['executionID', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['lastTradedPx', '8', 'Int64'],
	['lastShares', '8', 'UInt64'],
	['tradeType', '1', 'UInt8'],
	['tradeQualifier', '1', 'UInt8'],
	['transparencyIndicator', '1', 'UInt8'],
	['miFIDIndicators', '1', 'UInt8'],
	['tradeTime', '8', 'UInt64'],
	['publicationTime', '8', 'UInt64'],
	['execPhase', '1', 'UInt8'],
	['session_', '1', 'UInt8'],
	['externalClearingIndicator', '1', 'UInt8'],
	['crossOrderIndicator', '1', 'UInt8'],
	['bestBid', '8', 'Int64'],
	['bestOffer', '8', 'Int64'],
	['counterpartyReasonType', '1', 'UInt8'],
	['vWAP', '8', 'Int64'],
	['indicativePrice', '8', 'Int64'],
	['temporaryTradedPx', '8', 'Int64'],
	['finalTradedPx', '8', 'Int64'],
	['rFCID', '4', 'UInt32'],
	['strategyExecutionID', '4', 'UInt32'],
	['messagePriceNotation', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['exchangeCode', '1', 'Char'],
	['strategyTradedPrice', '8', 'Int64'],
	['strategyTradedQuantity', '8', 'UInt64'],
	['tradeUniqueIdentifier', '16', 'Char'],
	['RG_12005_STOIDS', 1, 1, 0],
	['RG_12005_MMTF', 1, 0, 0],
	['RG_12005_SFO1', 1, 0, 0],
	['RG_12005_SFO2', 1, 0, 0],
	['RG_12005_ISFO', 2, 0, 0]
]

msgs['RG_12005_STOIDS'] = [
	['orderID', '8', 'UInt64'],
	['orderSide', '1', 'UInt8'],
	['miFIDIndicators', '1', 'UInt8'],
	['counterpartFirmID', '8', 'Char'],
	['quoteIndicator', '1', 'UInt8'],
	['leavesQty', '8', 'UInt64'],
	['displayedQty', '8', 'UInt64'],
	['orderPx', '8', 'Int64'],
	['orderQty', '8', 'UInt64'],
	['orderPriority', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['executionID', '4', 'UInt32'],
	['strategyCode', '1', 'Char'],
	['postingAction', '2', 'UInt16'],
	['strategyIACAFinishDC', '1', 'UInt8'],
	['tradeLegSide', '1', 'UInt8'],
	['iACAFinishRegulatoryInstructions', '1', 'UInt8'],
	['orderQualifiers', '1', 'UInt8'],
	['cCPID', '1', 'UInt8'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['RG_12005_MMTF'] = [
	['mMTTradingMode', '1', 'Char'],
	['mMTNegotiationIndicator', '4', 'Char'],
	['mMTAgencyCrossTradeIndicator', '4', 'Char'],
	['mMTAlgorithmicIndicator', '4', 'Char']
]

msgs['RG_12005_SFO1'] = [
	['legLastPx', '8', 'Int64'],
	['legLastQty', '8', 'UInt64'],
	['legInstrumentID', '4', 'UInt32'],
	['legSide', '1', 'UInt8'],
	['executionID', '4', 'UInt32'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['RG_12005_SFO2'] = [
	['legLastPx', '8', 'Int64'],
	['legLastQty', '8', 'UInt64'],
	['legInstrumentID', '4', 'UInt32'],
	['legSide', '1', 'UInt8'],
	['executionID', '4', 'UInt32'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['RG_12005_ISFO'] = [
	['symbolIndex', '4', 'UInt32'],
	['orderSide', '1', 'UInt8'],
	['orderPx', '8', 'Int64'],
	['orderQty', '8', 'UInt64'],
	['lastTradedPx', '8', 'Int64'],
	['lastShares', '8', 'UInt64']
]

msgs['IALongOrder'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['accountTypeInternal', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookIn', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['darkExecutionInstruction', '1', 'UInt8'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['executionInstruction', '1', 'UInt8'],
	['firmID', '8', 'Char'],
	['indicativeAuctionPrice', '8', 'Int64'],
	['indicativeAuctionVolume', '8', 'UInt64'],
	['oESessionID', '8', 'UInt64'],
	['lPRole', '1', 'UInt8'],
	['miFIDIndicators', '1', 'UInt8'],
	['oEGINFromMember', '8', 'UInt64'],
	['oEGOUTTimeToME', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['orderPriority', '8', 'UInt64'],
	['orderPx', '8', 'Int64'],
	['orderQty', '8', 'UInt64'],
	['orderSide', '1', 'UInt8'],
	['orderType', '1', 'UInt8'],
	['origClientOrderID', '8', 'Int64'],
	['sTPID', '2', 'UInt16'],
	['symbolIndex', '4', 'UInt32'],
	['timeInForce', '1', 'UInt8'],
	['displayedQty', '8', 'UInt64'],
	['crossOrderIndicator', '1', 'UInt8'],
	['counterpartFirmID', '8', 'Char'],
	['executionID', '4', 'UInt32'],
	['executionPhase', '1', 'UInt8'],
	['lastShares', '8', 'UInt64'],
	['lastTradedPx', '8', 'Int64'],
	['leavesQty', '8', 'UInt64'],
	['tradeQualifier', '1', 'UInt8'],
	['tradeTime', '8', 'UInt64'],
	['tradeType', '1', 'UInt8'],
	['killReason', '2', 'UInt16'],
	['breachedCollarPrice', '8', 'Int64'],
	['collarRejType', '1', 'UInt8'],
	['rejectedMessage', '1', 'UInt8'],
	['errorCode', '2', 'UInt16'],
	['stopQueuePriority', '8', 'UInt64'],
	['counterpartyReasonType', '1', 'UInt8'],
	['quoteIndicator', '1', 'UInt8'],
	['quoteReqID', '8', 'UInt64'],
	['lISTransactionID', '4', 'UInt32'],
	['wholesaleTradeType', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['regulatorDisplayedQuantity', '8', 'UInt64'],
	['eSCBMembership', '1', 'UInt8'],
	['rFCID', '4', 'UInt32'],
	['isInitiator', '1', 'UInt8'],
	['exchangeIOIID', '8', 'Int64'],
	['tradeUniqueIdentifier', '16', 'Char'],
	['RG_12006_FTS', 1, 0, 0],
	['RG_12006_OF', 1, 0, 0],
	['RG_12006_CF', 1, 0, 0],
	['RG_12006_NMOF', 1, 0, 0],
	['RG_12006_NMSC', 1, 0, 0],
	['RG_12006_MSC', 1, 0, 0],
	['RG_12006_CF1', 1, 0, 0],
	['RG_12006_MCIF', 1, 0, 0],
	['RG_12006_NMCIF', 1, 0, 0],
	['RG_12006_ECA', 1, 0, 0],
	['RG_12006_SF', 1, 0, 0],
	['RG_12006_OFD', 1, 0, 0],
	['RG_12006_AI', 1, 0, 0],
	['RG_12006_SCDNM', 4, 0, 0],
	['RG_12006_SCDM', 2, 0, 0],
	['RG_12006_SL', 1, 0, 0]
]

msgs['RG_12006_FTS'] = [
	['freeText', '18', 'Char']
]

msgs['RG_12006_OF'] = [
	['stopPx', '8', 'Int64'],
	['pegOffset', '1', 'Int8'],
	['undisclosedPrice', '8', 'Int64'],
	['disclosedQty', '8', 'UInt64'],
	['orderExpirationTime', '4', 'UInt32'],
	['orderExpirationDate', '2', 'UInt16'],
	['tradingSession', '1', 'UInt8'],
	['stopTriggeredTimeInForce', '1', 'UInt8'],
	['undisclosedIcebergType', '1', 'UInt8']
]

msgs['RG_12006_CF'] = [
	['clearingFirmID', '8', 'Char'],
	['clientID', '8', 'Char'],
	['accountNumber', '12', 'Char'],
	['technicalOrigin', '1', 'UInt8'],
	['openClose', '2', 'UInt16'],
	['clearingInstruction', '2', 'UInt16']
]

msgs['RG_12006_NMOF'] = [
	['tradingCapacity', '1', 'UInt8'],
	['minimumOrderQuantity', '8', 'UInt64'],
	['accountTypeCross', '1', 'UInt8']
]

msgs['RG_12006_NMSC'] = [
	['originalClientIDShortCode', '4', 'Int32'],
	['originalExecWFirmShortCode', '4', 'Int32'],
	['originalInvestDecisWFirmShortCode', '4', 'Int32'],
	['originalNonExecBrokerShortCode', '4', 'Int32']
]

msgs['RG_12006_MSC'] = [
	['eventClientIDShortCode', '4', 'Int32'],
	['eventExecWFirmShortCode', '4', 'Int32']
]

msgs['RG_12006_CF1'] = [
	['marketPhaseFlag', '1', 'UInt8'],
	['marginTradingFlag', '1', 'UInt8'],
	['accessFlag', '1', 'UInt8'],
	['traderID', '16', 'Char'],
	['senderLocationID', '11', 'Char'],
	['deskID', '11', 'Char']
]

msgs['RG_12006_MCIF'] = [
	['eventInvestorID', '16', 'Char']
]

msgs['RG_12006_NMCIF'] = [
	['originalInvestorID', '16', 'Char']
]

msgs['RG_12006_ECA'] = [
	['clearingAccount', '16', 'Char']
]

msgs['RG_12006_SF'] = [
	['legLastPx', '8', 'Int64'],
	['legLastQty', '8', 'UInt64'],
	['legInstrumentID', '4', 'UInt32'],
	['legSide', '1', 'UInt8'],
	['executionID', '4', 'UInt32'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['RG_12006_OFD'] = [
	['evaluatedPrice', '8', 'Int64'],
	['messagePriceNotation', '1', 'UInt8'],
	['finalSymbolIndex', '4', 'UInt32'],
	['finalExecutionID', '4', 'UInt32']
]

msgs['RG_12006_AI'] = [
	['longClientID', '16', 'Char']
]

msgs['RG_12006_SCDNM'] = [
	['originalShortCodeType', '1', 'UInt8'],
	['shortCodeRole', '1', 'UInt8'],
	['shortCodeRoleQualifier', '1', 'UInt8']
]

msgs['RG_12006_SCDM'] = [
	['eventShortCodeType', '1', 'UInt8'],
	['shortCodeRole', '1', 'UInt8'],
	['shortCodeRoleQualifier', '1', 'UInt8']
]

msgs['RG_12006_SL'] = [
	['orderSide', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['executionID', '4', 'UInt32'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['IAOrderNewModify'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['accountType', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookIn', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['darkExecutionInstruction', '1', 'UInt8'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['executionInstruction', '1', 'UInt8'],
	['firmID', '8', 'Char'],
	['indicativeAuctionPrice', '8', 'Int64'],
	['indicativeAuctionVolume', '8', 'UInt64'],
	['leavesQty', '8', 'UInt64'],
	['oESessionID', '8', 'UInt64'],
	['lPRole', '1', 'UInt8'],
	['miFIDIndicators', '1', 'UInt8'],
	['oEGINFromMember', '8', 'UInt64'],
	['oEGOUTTimeToME', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['orderPriority', '8', 'UInt64'],
	['orderPx', '8', 'Int64'],
	['orderQty', '8', 'UInt64'],
	['orderSide', '1', 'UInt8'],
	['orderType', '1', 'UInt8'],
	['origClientOrderID', '8', 'Int64'],
	['sTPID', '2', 'UInt16'],
	['symbolIndex', '4', 'UInt32'],
	['timeInForce', '1', 'UInt8'],
	['displayedQty', '8', 'UInt64'],
	['crossOrderIndicator', '1', 'UInt8'],
	['quoteReqID', '8', 'UInt64'],
	['lISTransactionID', '4', 'UInt32'],
	['wholesaleTradeType', '1', 'UInt8'],
	['eSCBMembership', '1', 'UInt8'],
	['isInitiator', '1', 'UInt8'],
	['messagePriceNotation', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['regulatorDisplayedQuantity', '8', 'UInt64'],
	['rFCID', '4', 'UInt32'],
	['exchangeIOIID', '8', 'Int64'],
	['RG_12007_FTS', 1, 0, 0],
	['RG_12007_OF', 1, 0, 0],
	['RG_12007_CF', 1, 0, 0],
	['RG_12007_NMOF', 1, 0, 0],
	['RG_12007_NMSC', 1, 0, 0],
	['RG_12007_MSC', 1, 0, 0],
	['RG_12007_CF1', 1, 0, 0],
	['RG_12007_MCIF', 1, 0, 0],
	['RG_12007_NMCIF', 1, 0, 0],
	['RG_12007_ECA', 1, 0, 0],
	['RG_12007_AI', 1, 0, 0],
	['RG_12007_SCDNM', 4, 0, 0],
	['RG_12007_SCDM', 2, 0, 0]
]

msgs['RG_12007_FTS'] = [
	['freeText', '18', 'Char']
]

msgs['RG_12007_OF'] = [
	['stopPx', '8', 'Int64'],
	['pegOffset', '1', 'Int8'],
	['undisclosedPrice', '8', 'Int64'],
	['disclosedQty', '8', 'UInt64'],
	['orderExpirationTime', '4', 'UInt32'],
	['orderExpirationDate', '2', 'UInt16'],
	['tradingSession', '1', 'UInt8'],
	['stopTriggeredTimeInForce', '1', 'UInt8'],
	['undisclosedIcebergType', '1', 'UInt8']
]

msgs['RG_12007_CF'] = [
	['clearingFirmID', '8', 'Char'],
	['clientID', '8', 'Char'],
	['accountNumber', '12', 'Char'],
	['technicalOrigin', '1', 'UInt8'],
	['openClose', '2', 'UInt16'],
	['clearingInstruction', '2', 'UInt16']
]

msgs['RG_12007_NMOF'] = [
	['tradingCapacity', '1', 'UInt8'],
	['minimumOrderQuantity', '8', 'UInt64'],
	['accountTypeCross', '1', 'UInt8']
]

msgs['RG_12007_NMSC'] = [
	['originalClientIDShortCode', '4', 'Int32'],
	['originalExecWFirmShortCode', '4', 'Int32'],
	['originalInvestDecisWFirmShortCode', '4', 'Int32'],
	['originalNonExecBrokerShortCode', '4', 'Int32']
]

msgs['RG_12007_MSC'] = [
	['eventClientIDShortCode', '4', 'Int32'],
	['eventExecWFirmShortCode', '4', 'Int32']
]

msgs['RG_12007_CF1'] = [
	['marketPhaseFlag', '1', 'UInt8'],
	['marginTradingFlag', '1', 'UInt8'],
	['accessFlag', '1', 'UInt8'],
	['traderID', '16', 'Char'],
	['senderLocationID', '11', 'Char'],
	['deskID', '11', 'Char']
]

msgs['RG_12007_MCIF'] = [
	['eventInvestorID', '16', 'Char']
]

msgs['RG_12007_NMCIF'] = [
	['originalInvestorID', '16', 'Char']
]

msgs['RG_12007_ECA'] = [
	['clearingAccount', '16', 'Char']
]

msgs['RG_12007_AI'] = [
	['longClientID', '16', 'Char']
]

msgs['RG_12007_SCDNM'] = [
	['originalShortCodeType', '1', 'UInt8'],
	['shortCodeRole', '1', 'UInt8'],
	['shortCodeRoleQualifier', '1', 'UInt8']
]

msgs['RG_12007_SCDM'] = [
	['eventShortCodeType', '1', 'UInt8'],
	['shortCodeRole', '1', 'UInt8'],
	['shortCodeRoleQualifier', '1', 'UInt8']
]

msgs['IAShortOrderFill'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['crossOrderIndicator', '1', 'UInt8'],
	['counterpartFirmID', '8', 'Char'],
	['executionID', '4', 'UInt32'],
	['executionPhase', '1', 'UInt8'],
	['lastShares', '8', 'UInt64'],
	['lastTradedPx', '8', 'Int64'],
	['leavesQty', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['tradeQualifier', '1', 'UInt8'],
	['tradeTime', '8', 'UInt64'],
	['tradeType', '1', 'UInt8'],
	['counterpartyReasonType', '1', 'UInt8'],
	['tradingSession', '1', 'UInt8'],
	['displayedQty', '8', 'UInt64'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['regulatorDisplayedQuantity', '8', 'UInt64'],
	['tradeUniqueIdentifier', '16', 'Char'],
	['RG_12008_QR', 1, 0, 0],
	['RG_12008_SF', 1, 0, 0],
	['RG_12008_OFD', 1, 0, 0],
	['RG_12008_ISFO', 1, 0, 0]
]

msgs['RG_12008_QR'] = [
	['bidSize', '8', 'UInt64'],
	['bidPx', '8', 'Int64'],
	['bidQuotePriority', '8', 'UInt64'],
	['offerSize', '8', 'UInt64'],
	['offerPx', '8', 'Int64'],
	['offerQuotePriority', '8', 'UInt64']
]

msgs['RG_12008_SF'] = [
	['legLastPx', '8', 'Int64'],
	['legLastQty', '8', 'UInt64'],
	['legInstrumentID', '4', 'UInt32'],
	['legSide', '1', 'UInt8'],
	['executionID', '4', 'UInt32'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['RG_12008_OFD'] = [
	['evaluatedPrice', '8', 'Int64'],
	['messagePriceNotation', '1', 'UInt8'],
	['finalSymbolIndex', '4', 'UInt32'],
	['finalExecutionID', '4', 'UInt32']
]

msgs['RG_12008_ISFO'] = [
	['symbolIndex', '4', 'UInt32'],
	['orderSide', '1', 'UInt8'],
	['orderPx', '8', 'Int64'],
	['orderQty', '8', 'UInt64'],
	['lastTradedPx', '8', 'Int64'],
	['lastShares', '8', 'UInt64']
]

msgs['IAShortOrderCancel'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['bookIn', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['indicativeAuctionPrice', '8', 'Int64'],
	['indicativeAuctionVolume', '8', 'UInt64'],
	['oESessionID', '8', 'UInt64'],
	['oEGINFromMember', '8', 'UInt64'],
	['oEGOUTTimeToME', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['killReason', '2', 'UInt16'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['strategyIACAFinishDC', '1', 'UInt8']
]

msgs['IAShortOrderReject'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['bookIn', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['oEGINFromMember', '8', 'UInt64'],
	['oEGOUTTimeToME', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['breachedCollarPrice', '8', 'Int64'],
	['collarRejType', '1', 'UInt8'],
	['rejectedMessage', '1', 'UInt8'],
	['errorCode', '2', 'UInt16'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['executionWithinFirmShortCode', '4', 'Int32'],
	['clientIdentificationShortCode', '4', 'Int32'],
	['miFIDIndicators', '1', 'UInt8'],
	['oESessionID', '8', 'UInt64'],
	['orderSide', '1', 'UInt8'],
	['timeInForce', '1', 'UInt8'],
	['RG_12010_MSC', 1, 0, 0],
	['RG_12010_SCDM', 2, 0, 0]
]

msgs['RG_12010_MSC'] = [
	['eventClientIDShortCode', '4', 'Int32'],
	['eventExecWFirmShortCode', '4', 'Int32']
]

msgs['RG_12010_SCDM'] = [
	['eventShortCodeType', '1', 'UInt8'],
	['shortCodeRole', '1', 'UInt8'],
	['shortCodeRoleQualifier', '1', 'UInt8']
]

msgs['IAShortOrderTrigger'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['indicativeAuctionPrice', '8', 'Int64'],
	['indicativeAuctionVolume', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['orderPriority', '8', 'UInt64'],
	['orderType', '1', 'UInt8'],
	['timeInForce', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8']
]

msgs['IAShortOrderRefill'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['orderPriority', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['displayedQty', '8', 'UInt64'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['regulatorDisplayedQuantity', '8', 'UInt64']
]

msgs['IAShortOrderMTL'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['orderType', '1', 'UInt8'],
	['orderID', '8', 'UInt64'],
	['orderPriority', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['orderPx', '8', 'Int64'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8']
]

msgs['IAShortOrderVFAVFC'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['indicativeAuctionPrice', '8', 'Int64'],
	['indicativeAuctionVolume', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['orderPriority', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8']
]

msgs['IAShortOrderConfirmation'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['bookIn', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['orderID', '8', 'UInt64'],
	['originalClientOrderID', '8', 'Int64'],
	['symbolIndex', '4', 'UInt32'],
	['oESessionID', '8', 'UInt64'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['RG_12015_MSC', 1, 0, 0]
]

msgs['RG_12015_MSC'] = [
	['eventClientIDShortCode', '4', 'Int32'],
	['eventExecWFirmShortCode', '4', 'Int32']
]

msgs['IAShortTradeCancellation'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['executionID', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['bookIn', '8', 'UInt64'],
	['lastTradedPx', '8', 'Int64'],
	['lastShares', '8', 'UInt64'],
	['vWAP', '8', 'Int64'],
	['tradeTime', '8', 'UInt64'],
	['tradeType', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['IAShortOrderStopQueue'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookIn', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['orderType', '1', 'UInt8'],
	['timeInForce', '1', 'UInt8'],
	['stopQueuePriority', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8']
]

msgs['IAStaticCollars'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['RG_12018_SC', 3, 0, 0]
]

msgs['RG_12018_SC'] = [
	['updateType', '1', 'UInt8'],
	['price', '8', 'Int64']
]

msgs['IAShortOpenOrderRequest'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['bookINTime', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['executionWithinFirmShortCode', '4', 'Int32'],
	['clientIdentificationShortCode', '4', 'Int32'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8']
]

msgs['IAShortOwnershipRequest'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['orderEventType', '1', 'UInt8'],
	['ackPhase', '1', 'UInt8'],
	['ackQualifiers', '1', 'UInt8'],
	['ackType', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['bookINTime', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['oESessionID', '8', 'UInt64'],
	['executionWithinFirmShortCode', '4', 'Int32'],
	['clientIdentificationShortCode', '4', 'Int32'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8']
]

msgs['IATradeBustNotification'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['firmID', '8', 'Char'],
	['oESessionID', '8', 'UInt64'],
	['orderSide', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['bookINTime', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['executionID', '4', 'UInt32'],
	['lastShares', '8', 'UInt64'],
	['lastTradedPx', '8', 'Int64'],
	['orderID', '8', 'UInt64'],
	['miFIDIndicators', '1', 'UInt8'],
	['clearingFirmID', '8', 'Char'],
	['tradingCapacity', '1', 'UInt8'],
	['oEGINFromMember', '8', 'UInt64'],
	['executionPhase', '1', 'UInt8'],
	['tradeQualifier', '1', 'UInt8'],
	['counterpartFirmID', '8', 'Char'],
	['orderType', '1', 'UInt8'],
	['timeInForce', '1', 'UInt8'],
	['clearingInstruction', '2', 'UInt16'],
	['technicalOrigin', '1', 'UInt8'],
	['freeText', '18', 'Char'],
	['accountNumber', '12', 'Char'],
	['accountType', '1', 'UInt8'],
	['lPRole', '1', 'UInt8'],
	['openClose', '2', 'UInt16'],
	['originalInvestDecisWFirmShortCode', '4', 'Int32'],
	['originalNonExecBrokerShortCode', '4', 'Int32'],
	['eventClientIDShortCode', '4', 'Int32'],
	['eventExecWFirmShortCode', '4', 'Int32'],
	['originalClientIDShortCode', '4', 'Int32'],
	['originalExecWFirmShortCode', '4', 'Int32'],
	['clearingAccount', '16', 'Char'],
	['lISTransactionID', '4', 'UInt32'],
	['parentExecID', '4', 'UInt32'],
	['parentSymbolIndex', '4', 'UInt32'],
	['sequenceTime', '8', 'UInt64'],
	['tradeUniqueIdentifier', '16', 'Char'],
	['parentTradeUniqueIdentifier', '16', 'Char'],
	['RG_12021_SCDNM', 4, 0, 0],
	['RG_12021_SCDM', 2, 0, 0]
]

msgs['RG_12021_SCDNM'] = [
	['originalShortCodeType', '1', 'UInt8'],
	['shortCodeRole', '1', 'UInt8'],
	['shortCodeRoleQualifier', '1', 'UInt8']
]

msgs['RG_12021_SCDM'] = [
	['eventShortCodeType', '1', 'UInt8'],
	['shortCodeRole', '1', 'UInt8'],
	['shortCodeRoleQualifier', '1', 'UInt8']
]

msgs['IAQuoteRequest'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['eventID', '8', 'UInt64'],
	['bookIN', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['darkExecutionInstruction', '1', 'UInt8'],
	['eMM', '1', 'UInt8'],
	['endClient', '11', 'Char'],
	['firmID', '8', 'Char'],
	['firmIDPublication', '1', 'UInt8'],
	['oESessionID', '8', 'UInt64'],
	['oEGINFromMember', '8', 'UInt64'],
	['oEGOUTTimeToME', '8', 'UInt64'],
	['orderID', '8', 'UInt64'],
	['orderQty', '8', 'UInt64'],
	['orderSide', '1', 'UInt8'],
	['rFQStatus', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['minOrderQty', '8', 'UInt64'],
	['sequenceTime', '8', 'UInt64'],
	['accountType', '1', 'UInt8'],
	['RG_12022_NMSC', 1, 0, 0],
	['RG_12022_SCDNM', 4, 0, 0]
]

msgs['RG_12022_NMSC'] = [
	['originalClientIDShortCode', '4', 'Int32'],
	['originalExecWFirmShortCode', '4', 'Int32'],
	['originalInvestDecisWFirmShortCode', '4', 'Int32'],
	['originalNonExecBrokerShortCode', '4', 'Int32']
]

msgs['RG_12022_SCDNM'] = [
	['originalShortCodeType', '1', 'UInt8'],
	['shortCodeRole', '1', 'UInt8'],
	['shortCodeRoleQualifier', '1', 'UInt8']
]

msgs['IATradePublication'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['eventID', '8', 'UInt64'],
	['bookIN', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['tradeTime', '8', 'UInt64'],
	['publicationTime', '8', 'UInt64'],
	['executionID', '4', 'UInt32'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['tradeUniqueIdentifier', '16', 'Char']
]

msgs['IACalendar'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['rLCeventDate', '8', 'Char'],
	['rLCeventTime', '6', 'Char'],
	['sessionTradingDay', '2', 'UInt16'],
	['marketType', '1', 'Char'],
	['dayType', '1', 'Char'],
	['atypicalSession', '1', 'Char'],
	['sequenceTime', '8', 'UInt64'],
	['dayOfWeek', '1', 'UInt8'],
	['changeReason', '100', 'Char'],
	['dayType2', '1', 'Char'],
	['batchID', '1', 'UInt8']
]

msgs['IAHeaderRefData'] = [
	['messageType', '1', 'UInt8'],
	['messageState', '1', 'UInt8'],
	['recordSize', '8', 'UInt64'],
	['produceTime', '8', 'UInt64'],
	['applicationProducer', '1', 'UInt8'],
	['sessionTradingDay', '2', 'UInt16'],
	['deltaBasedOnSessionTradingDay', '2', 'UInt16'],
	['batchID', '1', 'UInt8']
]

msgs['IAClosingPrice'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['sequenceTime', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['eventID', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['closingPriceType', '1', 'UInt8'],
	['actualClosingPriceType', '1', 'UInt8'],
	['roundedClosingPrice', '8', 'Int64'],
	['rAWClosingPrice', '8', 'Int64'],
	['lastTradedPx', '8', 'Int64'],
	['bookState', '1', 'UInt8'],
	['suspensionIndicator', '1', 'UInt8']
]

msgs['IAQuote'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['bookIn', '8', 'UInt64'],
	['bookOUTTime', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['clientOrderID', '8', 'Int64'],
	['tradingCapacity', '1', 'UInt8'],
	['accountType', '1', 'UInt8'],
	['lPRole', '1', 'UInt8'],
	['miFIDIndicators', '1', 'UInt8'],
	['rFEAnswer', '1', 'UInt8'],
	['firmID', '8', 'Char'],
	['executionInstruction', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64'],
	['orderQualifiers', '1', 'UInt8'],
	['sTPID', '2', 'UInt16'],
	['RG_12050_BQ', 1, 0, 0],
	['RG_12050_OQ', 1, 0, 0],
	['RG_12050_CD', 1, 0, 0],
	['RG_12050_NMSC', 1, 0, 0],
	['RG_12050_MSC', 1, 0, 0]
]

msgs['RG_12050_BQ'] = [
	['bidSize', '8', 'UInt64'],
	['bidPx', '8', 'Int64'],
	['bidQuotePriority', '8', 'UInt64'],
	['bidOrderID', '8', 'UInt64'],
	['buyRevisionFlag', '1', 'UInt8'],
	['bidErrorCode', '2', 'UInt16'],
	['bidOESessionID', '8', 'UInt64'],
	['rFEAnswer', '1', 'UInt8'],
	['bidLeavesQuantity', '8', 'UInt64']
]

msgs['RG_12050_OQ'] = [
	['offerSize', '8', 'UInt64'],
	['offerPx', '8', 'Int64'],
	['offerQuotePriority', '8', 'UInt64'],
	['offerOrderID', '8', 'UInt64'],
	['sellRevisionFlag', '1', 'UInt8'],
	['offerErrorCode', '2', 'UInt16'],
	['offerOESessionID', '8', 'UInt64'],
	['rFEAnswer', '1', 'UInt8'],
	['offerLeavesQuantity', '8', 'UInt64']
]

msgs['RG_12050_CD'] = [
	['clearingFirmID', '8', 'Char'],
	['clientID', '8', 'Char'],
	['accountNumber', '12', 'Char'],
	['technicalOrigin', '1', 'UInt8'],
	['openClose', '2', 'UInt16'],
	['clearingInstruction', '2', 'UInt16'],
	['freeText', '18', 'Char']
]

msgs['RG_12050_NMSC'] = [
	['originalClientIDShortCode', '4', 'Int32'],
	['originalExecWFirmShortCode', '4', 'Int32'],
	['originalInvestDecisWFirmShortCode', '4', 'Int32'],
	['originalNonExecBrokerShortCode', '4', 'Int32']
]

msgs['RG_12050_MSC'] = [
	['eventClientIDShortCode', '4', 'Int32'],
	['eventExecWFirmShortCode', '4', 'Int32']
]

msgs['IAAFQRFE'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['aFQReason', '1', 'UInt8'],
	['bookOUTTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['firmID', '8', 'Char'],
	['aFQIndicator', '1', 'UInt8'],
	['oESessionID', '8', 'UInt64'],
	['sequenceTime', '8', 'UInt64']
]

msgs['IAPriceInput'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['price', '8', 'Int64'],
	['priceDate', '8', 'UInt64'],
	['priceInputType', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64']
]

msgs['IAWarrantStatusUpdate'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['eMM', '1', 'UInt8'],
	['gBOXActionCode', '1', 'UInt8'],
	['sequenceTime', '8', 'UInt64']
]

msgs['IACountry'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['countryLabel', '100', 'Char'],
	['countryCode2', '2', 'Char'],
	['countryCode3', '3', 'Char'],
	['batchID', '1', 'UInt8']
]

msgs['IACurrency'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['currency', '3', 'Char'],
	['currencyLabel', '40', 'Char'],
	['interbankRate', '8', 'UInt64'],
	['interbankRateDecimals', '1', 'UInt8'],
	['dateOfInterbankRate', '2', 'UInt16'],
	['batchID', '1', 'UInt8'],
	['currency2', '3', 'Char'],
	['currencyLabel2', '40', 'Char']
]

msgs['IAReportingRegulator'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['reportingRegulatorTID', '8', 'UInt64'],
	['reportingRegulatorName', '50', 'Char'],
	['countryCode3', '3', 'Char'],
	['reportingRegulatorID', '3', 'Char'],
	['batchID', '1', 'UInt8']
]

msgs['IAParticipantAttributesDef'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['participantAttributeDefType', '1', 'UInt8'],
	['participantAttributeDefID', '8', 'UInt64'],
	['participantAttributeDefName', '100', 'Char'],
	['participantAttributeDefDescrip', '200', 'Char'],
	['batchID', '1', 'UInt8']
]

msgs['IAParticipantType'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['participantTypeID', '1', 'UInt8'],
	['name', '50', 'Char'],
	['participantTypeQualifiers', '1', 'UInt8'],
	['batchID', '1', 'UInt8']
]

msgs['IAMIC'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['segmentMIC', '4', 'Char'],
	['mICLabel', '60', 'Char'],
	['countryCode3', '3', 'Char'],
	['marketPlace', '3', 'Char'],
	['mICQualifiers', '1', 'UInt8'],
	['batchID', '1', 'UInt8']
]

msgs['IAParticipantCashAuthor'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['participantID', '8', 'Char'],
	['tradingGroupCode', '2', 'Char'],
	['participantCashAuthQualifiers', '1', 'UInt8'],
	['defaultCCPID', '1', 'UInt8'],
	['preferredCCPID', '1', 'UInt8'],
	['eRGCashSelfMonitoring', '1', 'UInt8'],
	['eRGCashClearerCode', '8', 'Char'],
	['sponsorFirmID', '8', 'Char'],
	['membershipRoleID', '2', 'UInt16'],
	['marketPlace', '3', 'Char'],
	['batchID', '1', 'UInt8']
]

msgs['IAParticipant'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['iD', '8', 'Char'],
	['commercialName', '100', 'Char'],
	['iMiFIDCompliant', '1', 'UInt8'],
	['eSMAIdentificationTypeID', '8', 'UInt64'],
	['iValidity', '1', 'UInt8'],
	['lEICode', '20', 'Char'],
	['positionHolderTypeID', '8', 'UInt64'],
	['positionReportingTypeID', '8', 'UInt64'],
	['reportingRegulatorTID', '8', 'UInt64'],
	['participantTypeID', '1', 'UInt8'],
	['transactionReportARMStart', '2', 'UInt16'],
	['transactionReportARMEnd', '2', 'UInt16'],
	['transactionReportENXStart', '2', 'UInt16'],
	['transactionReportENXEnd', '2', 'UInt16'],
	['aPAPreTradeStart', '2', 'UInt16'],
	['aPAPreTradeEnd', '2', 'UInt16'],
	['aPAPostTradeStart', '2', 'UInt16'],
	['aPAPostTradeEnd', '2', 'UInt16'],
	['countryRegistration', '3', 'Char'],
	['commodityPositionReportStart', '2', 'UInt16'],
	['commodityPositionReportEnd', '2', 'UInt16'],
	['lastUpdateDate', '2', 'UInt16'],
	['sponsoringFirmID', '8', 'Char'],
	['sponsoredFirmName', '100', 'Char'],
	['batchID', '1', 'UInt8']
]

msgs['IAMarketPlace'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['marketPlace', '3', 'Char'],
	['marketPlaceLabel', '60', 'Char'],
	['operatingMIC', '4', 'Char'],
	['batchID', '1', 'UInt8']
]

msgs['IAInstrument'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['aDT', '8', 'Int64'],
	['tradingCurrency', '3', 'Char'],
	['instrumentTradingCode', '15', 'Char'],
	['cFICode', '6', 'Char'],
	['instrumentGroupCode', '2', 'Char'],
	['iSIN', '12', 'Char'],
	['mIC', '4', 'Char'],
	['fullInstrumentName', '102', 'Char'],
	['liquidInstrumentIndicator', '1', 'UInt8'],
	['lISPostTrade', '8', 'UInt64'],
	['lISPreTrade', '8', 'UInt64'],
	['optiqSegment', '1', 'UInt8'],
	['priceDecimals', '1', 'UInt8'],
	['amountDecimals', '1', 'UInt8'],
	['quantityNotation', '3', 'Char'],
	['quantityDecimals', '1', 'UInt8'],
	['sSTIPostTrade', '8', 'UInt64'],
	['symbolIndex', '4', 'UInt32'],
	['underlyingName', '102', 'Char'],
	['underlyingIndexTerm', '8', 'Char'],
	['actionIndicator', '1', 'UInt8'],
	['typeOfPriceExpression', '1', 'UInt8'],
	['parValue', '8', 'UInt64'],
	['instrumentShortName', '22', 'Char'],
	['issuedSecurities', '8', 'UInt64'],
	['maturityDate', '8', 'Char'],
	['strikePrice', '8', 'Int64'],
	['instrumentShortName2', '66', 'Char'],
	['longMnemonic', '6', 'Char'],
	['officialSegment', '70', 'Char'],
	['settlementSystem', '1', 'UInt8'],
	['settlementDelay', '2', 'Char'],
	['guaranteeIndicator', '1', 'UInt8'],
	['instrumentID', '8', 'UInt64'],
	['instrumentStatus', '1', 'UInt8'],
	['issuingCountry', '3', 'Char'],
	['firstTradingDate', '2', 'UInt16'],
	['instrumentEventDate', '2', 'UInt16'],
	['messageValidityDate', '2', 'UInt16'],
	['settlementCurrency', '3', 'Char'],
	['nominalCurrency', '3', 'Char'],
	['paymentFrequency', '1', 'UInt8'],
	['instrumentTypeLabel', '50', 'Char'],
	['instrumentSubTypeLabel', '50', 'Char'],
	['endValidityDays', '1', 'UInt8'],
	['darkEligibility', '1', 'UInt8'],
	['darkMinimumQuantity', '4', 'UInt32'],
	['dateOfLastTrade', '2', 'UInt16'],
	['lastAdjustedClosingPrice', '8', 'Int64'],
	['countryOfExchange', '3', 'Char'],
	['currencyCoefficient', '4', 'UInt32'],
	['tradingCurrencyIndicator', '1', 'UInt8'],
	['strikeCurrency', '3', 'Char'],
	['typeOfCorporateEvent', '2', 'Char'],
	['issuePrice', '8', 'Int64'],
	['issuePriceDecimals', '1', 'UInt8'],
	['strikePriceDecimals', '1', 'UInt8'],
	['iCBCode', '8', 'Char'],
	['thresholdLISPostTrade60mn', '8', 'UInt64'],
	['thresholdLISPostTrade120mn', '8', 'UInt64'],
	['thresholdLISPostTradeEOD', '8', 'UInt64'],
	['icebergMinimumAmount', '8', 'UInt64'],
	['pAKOPeriod', '1', 'UInt8'],
	['maxOrderAmountCall', '8', 'UInt64'],
	['maxOrderAmountContinuous', '8', 'UInt64'],
	['maxOrderQuantityCall', '8', 'UInt64'],
	['maxOrderQuantityContinuous', '8', 'UInt64'],
	['kOBIByLPIndicator', '1', 'UInt8'],
	['marketCapitalizationClassification', '1', 'UInt8'],
	['issuerName', '80', 'Char'],
	['listingDate', '4', 'UInt32'],
	['adjustmentFactor', '8', 'UInt64'],
	['dateOfApprovalOfTheAdmissionToTrading', '2', 'UInt16'],
	['priceExpression', '4', 'Char'],
	['exerciseStyle', '1', 'UInt8'],
	['optionType', '1', 'UInt8'],
	['staticAPFTableID', '2', 'UInt16'],
	['dynamicAPFTableID', '2', 'UInt16'],
	['orderPriceControlAPFTableID', '2', 'UInt16'],
	['batchID', '1', 'UInt8'],
	['endValidityDate', '8', 'Char'],
	['legalForm', '1', 'UInt8'],
	['marketPlace', '3', 'Char'],
	['mainDepositary', '5', 'Char'],
	['underlyingMIC', '4', 'Char'],
	['instrumentDecimalsRatio', '1', 'UInt8'],
	['RG_12224_EMMPR', 0, 0, 1]
]

msgs['RG_12224_EMMPR'] = [
	['eMM', '1', 'UInt8'],
	['patternID', '2', 'UInt16'],
	['tickSizeIndexID', '2', 'UInt16'],
	['marketModel', '1', 'UInt8'],
	['lotSize', '8', 'UInt64'],
	['instUnitExp', '1', 'UInt8']
]

msgs['IATimetable'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['batchID', '1', 'UInt8'],
	['patternID', '2', 'UInt16'],
	['RG_12226_CT1', 1, 1, 0]
]

msgs['RG_12226_CT1'] = [
	['phaseTime', '8', 'UInt64'],
	['phaseId', '1', 'UInt8'],
	['phaseQualifier', '2', 'UInt16'],
	['tradingPeriod', '1', 'UInt8'],
	['orderEntryQualifier', '1', 'UInt8'],
	['session_', '1', 'UInt8'],
	['scheduledEvent', '1', 'UInt8']
]

msgs['IATicktable'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['batchID', '1', 'UInt8'],
	['tickSizeIndexID', '2', 'UInt16'],
	['RG_12227_CTSR', 1, 1, 0]
]

msgs['RG_12227_CTSR'] = [
	['minimumPrice', '8', 'Int64'],
	['minimumPriceDecimals', '1', 'UInt8'],
	['tickSize', '8', 'Int64'],
	['tickSizeDecimals', '1', 'UInt8']
]

msgs['IAAuthorizedPriceFluctuation'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['batchID', '1', 'UInt8'],
	['authorizedPriceFluctuationTableID', '2', 'UInt16'],
	['RG_12228_APFR', 1, 1, 0]
]

msgs['RG_12228_APFR'] = [
	['minimumPrice', '8', 'Int64'],
	['minimumPriceDecimals', '1', 'UInt8'],
	['authorizedPriceFluctuationValue', '8', 'UInt64'],
	['authorizedPriceFluctuationDecimals', '1', 'UInt8'],
	['authorizedPriceFluctuationType', '1', 'UInt8']
]

msgs['IAMarketMaker'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['batchID', '1', 'UInt8'],
	['firmID', '8', 'Char'],
	['iSINCode', '12', 'Char'],
	['mIC', '4', 'Char'],
	['currency', '3', 'Char'],
	['symbolIndex', '4', 'UInt32'],
	['RG_12229_MMR', 1, 0, 0]
]

msgs['RG_12229_MMR'] = [
	['eMM', '1', 'UInt8'],
	['role', '50', 'Char']
]

msgs['IAMarketMakerObligations'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['batchID', '1', 'UInt8'],
	['marketMakerContractName', '20', 'Char'],
	['iSINCode', '12', 'Char'],
	['mIC', '4', 'Char'],
	['currency', '3', 'Char'],
	['symbolIndex', '4', 'UInt32'],
	['marketMaker', '8', 'Char'],
	['startValidityDate', '8', 'Char'],
	['endValidityDate', '8', 'Char'],
	['startTrackingTime', '6', 'Char'],
	['endTrackingTime', '6', 'Char'],
	['spreadExpressionType', '1', 'UInt8'],
	['spreadMaximumValue', '8', 'UInt64'],
	['spreadMaximumPercentage', '8', 'UInt64'],
	['volumeExpressionType', '1', 'UInt8'],
	['volumeMinimumLots', '8', 'UInt64'],
	['volumeMinimumAmount', '8', 'UInt64'],
	['tradingMode', '1', 'UInt8'],
	['mMRefreshDelay', '4', 'Int32'],
	['snapshotDelay', '8', 'UInt64'],
	['warrantSegment', '1', 'UInt8'],
	['presenceTypeIndicator', '1', 'UInt8'],
	['marketMakerContractFamily', '15', 'Char'],
	['marketMakerFamilyName', '30', 'Char'],
	['role', '50', 'Char'],
	['percentageBBOPresenceTime', '8', 'UInt64'],
	['percentageBBOSetter', '8', 'UInt64'],
	['orderDurationofBBOSetterOrder', '8', 'UInt64']
]

msgs['IAIssuer'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['batchID', '1', 'UInt8'],
	['issuerCode', '12', 'Char'],
	['issuerName', '80', 'Char'],
	['lEICode', '20', 'Char'],
	['issuerICBCode', '8', 'Char']
]

msgs['IATradingGroup'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['batchID', '1', 'UInt8'],
	['instrumentGroupCode', '2', 'Char'],
	['tradingGroupName', '50', 'Char'],
	['optiqSegment', '1', 'UInt8'],
	['defaultCCPID', '1', 'UInt8'],
	['closingPriceType', '1', 'UInt8'],
	['nbofBestBidsandBestOffers', '1', 'UInt8'],
	['vWAPPeriod', '8', 'UInt64'],
	['RG_12233_TGEMMP', 0, 0, 1]
]

msgs['RG_12233_TGEMMP'] = [
	['eMM', '1', 'UInt8'],
	['marketModel', '1', 'UInt8'],
	['iMSActive', '1', 'UInt8'],
	['valuationTradeType', '1', 'UInt8'],
	['aIPType', '1', 'UInt8'],
	['dynamicCollarReferencePriceSource', '1', 'UInt8'],
	['dynamicCollarLogic', '1', 'UInt8'],
	['collarUnhaltDelay', '4', 'UInt32'],
	['collarMaxUnhaltNb', '1', 'UInt8'],
	['collarUncrossingExpansionFactor', '1', 'UInt8'],
	['staticCollarLogic', '1', 'UInt8'],
	['staticCollarReferencePriceSource', '1', 'UInt8'],
	['rFEConfirmationPeriod', '4', 'Int32'],
	['orderPriceControlReferencePriceSource', '1', 'UInt8']
]

msgs['IATradeClearing'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['postTradeActionIndicator', '1', 'UInt8'],
	['eventId', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['iSIN', '12', 'Char'],
	['mIC', '4', 'Char'],
	['tradingCurrency', '3', 'Char'],
	['settlementCurrency', '3', 'Char'],
	['settlementPeriod', '1', 'UInt8'],
	['settlementDate', '2', 'UInt16'],
	['settlementSystem', '1', 'UInt8'],
	['endValidityDate', '8', 'Char'],
	['lastTradedPx', '8', 'Int64'],
	['priceDecimals', '1', 'UInt8'],
	['lastShares', '8', 'UInt64'],
	['quantityDecimals', '1', 'UInt8'],
	['tradeQualifier', '1', 'UInt8'],
	['tradeTime', '8', 'UInt64'],
	['crossOrderIndicator', '1', 'UInt8'],
	['guaranteeIndicator', '1', 'UInt8'],
	['exchangeRate', '4', 'UInt32'],
	['exchangeRateNbDecimals', '1', 'UInt8'],
	['tradeUniqueIdentifier', '16', 'Char'],
	['marketIdentifier', '4', 'Char'],
	['RG_12234_TCOS', 1, 1, 0]
]

msgs['RG_12234_TCOS'] = [
	['orderID', '8', 'UInt64'],
	['orderSide', '1', 'UInt8'],
	['firmID', '8', 'Char'],
	['bookIn', '8', 'UInt64'],
	['tradeQualifier', '1', 'UInt8'],
	['accountCode', '1', 'UInt8'],
	['tradingCapacity', '1', 'UInt8'],
	['clientOrderID', '8', 'Int64'],
	['freeText', '18', 'Char'],
	['clearingFirmID', '8', 'Char'],
	['clientID', '8', 'Char'],
	['accountNumber', '12', 'Char'],
	['technicalOrigin', '1', 'UInt8'],
	['openClose', '2', 'UInt16'],
	['clearingInstruction', '2', 'UInt16'],
	['originalClientIDShortCode', '4', 'Int32'],
	['originalExecWFirmShortCode', '4', 'Int32'],
	['originalInvestDecisWFirmShortCode', '4', 'Int32'],
	['originalNonExecBrokerShortCode', '4', 'Int32'],
	['cCPID', '1', 'UInt8'],
	['longClientID', '16', 'Char'],
	['cCPBicID', '1', 'Char']
]

msgs['IAIndexLevel'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['rebroadcastIndicator', '1', 'UInt8'],
	['eMM', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['indexLevel', '8', 'Int64'],
	['indexLevelType', '1', 'UInt8'],
	['indexPriceCode', '1', 'UInt8'],
	['pctgOfCapitalization', '8', 'UInt64'],
	['prctVarfromPrevClose', '8', 'Int64'],
	['numTradedInstruments', '2', 'UInt16']
]

msgs['IAIndexReferential'] = [
	['produceTime', '8', 'UInt64'],
	['consumeTime', '8', 'UInt64'],
	['eMM', '1', 'UInt8'],
	['symbolIndex', '4', 'UInt32'],
	['iSIN', '12', 'Char'],
	['operatingMIC', '4', 'Char'],
	['marketPlace', '3', 'Char'],
	['tradingCurrency', '3', 'Char'],
	['indexLabel', '18', 'Char'],
	['longMnemonic', '6', 'Char'],
	['fullInstrumentName', '102', 'Char'],
	['instrumentShortName2', '66', 'Char'],
	['ratioMultiplierDecimals', '1', 'UInt8'],
	['priceDecimals', '1', 'UInt8'],
	['numberOfConstituents', '2', 'UInt16'],
	['indexCalculationFormula', '1', 'UInt8'],
	['indexCalculationFrequency', '2', 'UInt16'],
	['indexBroadcastMode', '1', 'UInt8'],
	['indexBroadcastFrequency', '2', 'UInt16'],
	['indexRoutingIndicator', '1', 'UInt8'],
	['indexMessageBroadcastIndicator', '1', 'UInt8'],
	['indexLevelBroadcastStartTime', '4', 'UInt32'],
	['indexLevelBroadcastEndTime', '4', 'UInt32'],
	['eSGProductClassification', '1', 'UInt8'],
	['mDGSetOfChannelsID', '1', 'UInt8'],
	['mDGSetOfChannelsName', '100', 'Char']
]

