import json
import time
import requests

from Arbitrazj_mezh_birzh import Classes


###########################################################
# Меню выбора основной валюты
###########################################################import json


from Arbitrazj_mezh_birzh import Classes

###########################################################

client = Classes.apiMexc()
"""API settings"""

getAllCoinsInfo = client.test()
"""Сбор информации по Blockchain networks"""

###########################################################
# Формирование файла Json со списком сетей валют
###########################################################

#
# exchange = "Mexc"
# addedNumberNetworks = 0  # Счетчик общего количества добавленных сетей
#
# with open(f'{exchange}_coin_network_info.json', 'w') as file:
#     json.dump([], file, indent=2)
# """Очистка файла, перед его заполнением информацией"""
#
# listAllCoinsTrading = []
#
# for i_def_FileOpenGetAllSymbols in Classes.def_FileOpenGetAllSymbols(exchange):
#
#     if i_def_FileOpenGetAllSymbols['immutableNameBaseAsset'] not in listAllCoinsTrading:
#         listAllCoinsTrading.append(i_def_FileOpenGetAllSymbols['immutableNameBaseAsset'])
#
#     elif i_def_FileOpenGetAllSymbols['immutableNameQuoteAsset'] not in listAllCoinsTrading:
#         listAllCoinsTrading.append(i_def_FileOpenGetAllSymbols['immutableNameQuoteAsset'])
#
#
# for i_AllCoinsInfo in getAllCoinsInfo:
#
#     if i_AllCoinsInfo['coin'] in listAllCoinsTrading:
#
#         symbol = i_AllCoinsInfo['coin']
#         name = i_AllCoinsInfo['coin']
#
#         indexNetwork = len(i_AllCoinsInfo['networkList'])  # Количество сетей у валюты
#
#         listNetwork = []
#         network_count = 0
#         addedNumberNetworks += 1
#
#         while network_count < indexNetwork:
#
#             network = str(i_AllCoinsInfo['networkList'][network_count]['network'])
#             secondaryNameNetwork = str(i_AllCoinsInfo['networkList'][network_count]['name'])
#             depositEnable = bool(i_AllCoinsInfo['networkList'][network_count]['depositEnable'])
#             withdrawEnable = bool(i_AllCoinsInfo['networkList'][network_count]['withdrawEnable'])
#             withdrawFee = float(i_AllCoinsInfo['networkList'][network_count]['withdrawFee'])
#             withdrawMin = float(i_AllCoinsInfo['networkList'][network_count]['withdrawMin'])
#             minConfirm = int(i_AllCoinsInfo['networkList'][network_count]['minConfirm'])
#
#             listNetwork.append(
#                 [
#                     network,
#                     secondaryNameNetwork,
#                     depositEnable,
#                     withdrawEnable,
#                     withdrawFee,
#                     withdrawMin,
#                     minConfirm
#                 ])
#
#             network_count += 1
#
#         Classes.ExchangeInfoBlockchainNetwork(exchange, symbol, name, listNetwork)
#
# print(f"Добавлена информация о '{addedNumberNetworks}' BlockchainNetworks.")


exchange = 'Mexc'
mainCurrencyTrading = Classes.MainCurrencySelectionMenu(exchange).mainCurrencyTrading

###########################################################
#
###########################################################


ListAllPairsTradingInformation = []  # Список всех торгуемых пар на бирже, со всей торговой информацией

couldPairs = int(0)
startTimeProgram = time.time()

getAllInfoSymbolFromExchange = requests.get(f'https://api.mexc.com/api/v3/exchangeInfo').json()

for i_getAllInfoSymbolFromExchange in getAllInfoSymbolFromExchange['symbols']:

    SymbolTradingStatus = i_getAllInfoSymbolFromExchange['status']

    if SymbolTradingStatus == 'ENABLED':
        if len(mainCurrencyTrading) == 1:
            if i_getAllInfoSymbolFromExchange['baseAsset'] == mainCurrencyTrading[0] or i_getAllInfoSymbolFromExchange['quoteAsset'] == mainCurrencyTrading[0]:
                ListAllPairsTradingInformation.append(i_getAllInfoSymbolFromExchange)
                couldPairs += 1
        elif len(mainCurrencyTrading) > 1:
            ListAllPairsTradingInformation.append(i_getAllInfoSymbolFromExchange)
            couldPairs += 1


##########################################################


new_ListAllPairsTradingInformation = []

for i_ListAllPairsTradingInformation in ListAllPairsTradingInformation:
    """Создаем свой Json с торгуемыми парами"""

    new_ListAllPairsTradingInformation.append({

        'symbol': i_ListAllPairsTradingInformation['symbol'],
        'immutableNameBaseAsset': i_ListAllPairsTradingInformation['baseAsset'],
        'immutableNameQuoteAsset': i_ListAllPairsTradingInformation['quoteAsset'],
        "baseAsset": i_ListAllPairsTradingInformation['baseAsset'],
        "quoteAsset": i_ListAllPairsTradingInformation['quoteAsset']

    })

##########################################################


with open(f'{exchange}_AllPairsTradingInf.json', 'w') as file:
    json.dump(new_ListAllPairsTradingInformation, file, indent=2)

print("\n")
print("#" * 79)
print("Обработка завершена.")
print(F"Обработка заняла: {(time.time() - startTimeProgram) / 60}")
print(f"Было добавлено: {couldPairs} пар.")

##########################################################
##########################################################

