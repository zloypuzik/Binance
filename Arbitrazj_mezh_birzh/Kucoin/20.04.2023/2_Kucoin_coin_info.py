import json
import requests

from Arbitrazj_mezh_birzh import Classes

exchange = "Kucoin"
###########################################################
# API settings
###########################################################


client = Classes.apiKucoin()

###########################################################
# Сбор информации по Blockchain networks
###########################################################

print(f"\nИдет сбор информации Blockchain networks биржи {exchange} ...")

getAllCoinsInfo = []

for i in Classes.def_FileOpenGetAllSymbols(exchange):

    """
    Особенности Kucoin биржи:
    "symbol": "BCHSV-USDT",  # Уникальный код символа, он не изменится после переименования
    "name": "BSV-USDT",
    "baseCurrency": "BSV",  # Название торговых пар, оно изменится после переименования
    "quoteCurrency": "USDT",

    т.к. "baseCurrency" или "quoteCurrency" изменяемые (согласно документации к API), то нужно использовать название из "symbol" (т.к оно не изменяемо)
    """
    if i['baseCurrency'] != "USDT":

        symbol = i['symbol'].upper()
        symbol = symbol.split("-")[0]  # Вырезает все, что перед '-'

        # getAllCoinsInfo.append(requests.get(f'https://api.kucoin.com/api/v2/currencies/{symbol}').json())
        requestsAllCoinsInfo = requests.get(f'https://api.kucoin.com/api/v2/currencies/{symbol}').json()

        if requestsAllCoinsInfo['data']['chains'] is not None:
            getAllCoinsInfo.append(requestsAllCoinsInfo)

    elif i['quoteCurrency'] != "USDT":

        symbol = i['symbol'].upper()
        symbol = symbol.split("-")[1]  # Вырезает все, что после '-'
        # getAllCoinsInfo.append(requests.get(f'https://api.kucoin.com/api/v2/currencies/{symbol}').json())
        requestsAllCoinsInfo = requests.get(f'https://api.kucoin.com/api/v2/currencies/{symbol}').json()

        if requestsAllCoinsInfo['data']['chains'] is not None:
            getAllCoinsInfo.append(requestsAllCoinsInfo)
for i in getAllCoinsInfo:
    print(i)


print("\nСбор информации Blockchain networks закончен !")

# for i in getAllCoinsInfo:
#     print(i)
#     print(i)# getAllCoinsInfo.append(requests.get(f'https://api.kucoin.com/api/v2/currencies/wAXL').json())

# a = client.get_currency("BCHSV")
# print(a)

# getAllCoinsInfo.append(requests.get(f'https://api.kucoin.com/api/v2/currencies/LOKI').json())
#
# for ii in getAllCoinsInfo:
#     # print(ii['data'])
#     # print(len(ii['data']['chains']))
#     print(ii)
# print(getAllCoinsInfo)

###########################################################
# Формирование файла Json со списком сетей валют
###########################################################


binanceCoinInfoModify = []  # Список сетей валют Kucoin

# for i in getAllCoinsInfo:
#     print(i)

with open(f'{exchange}_coin_network_info.json', 'w') as file:  # Очистка файла
    json.dump([], file, indent=2)

for i_AllCoinsInfo in getAllCoinsInfo:
    for i_def_FileOpenGetAllSymbols in Classes.def_FileOpenGetAllSymbols(exchange):
        symbol = None
        if i_def_FileOpenGetAllSymbols['baseCurrency'] != "USDT":
            symbol = i_def_FileOpenGetAllSymbols['symbol'].upper()
            symbol = symbol.split("-")[0]  # Вырезает все, что перед '-'
        elif i_def_FileOpenGetAllSymbols['quoteCurrency'] != "USDT":
            symbol = i_def_FileOpenGetAllSymbols['symbol'].upper()
            symbol = symbol.split("-")[1]  # Вырезает все, что после '-'

        if i_AllCoinsInfo['data']['currency'] == symbol:

            indexNetwork = len(i_AllCoinsInfo['data']['chains'])  # Количество сетей у валюты

            listNetwork = []
            network_count = 0

            symbol = i_AllCoinsInfo['data']['name']

            while network_count < indexNetwork:
                network = str(i_AllCoinsInfo['data']['chains'][network_count]['chain']).upper()
                secondaryNameNetwork = str(i_AllCoinsInfo['data']['chains'][network_count]['chainName'])
                depositEnable = bool(i_AllCoinsInfo['data']['chains'][network_count]['isDepositEnabled'])
                withdrawEnable = bool(i_AllCoinsInfo['data']['chains'][network_count]['isWithdrawEnabled'])
                withdrawFee = float(i_AllCoinsInfo['data']['chains'][network_count]['withdrawalMinFee'])
                withdrawMin = float(i_AllCoinsInfo['data']['chains'][network_count]['withdrawalMinSize'])
                minConfirm = int(i_AllCoinsInfo['data']['chains'][network_count]['confirms'])

                listNetwork.append(
                    [
                        network,
                        secondaryNameNetwork,
                        depositEnable,
                        withdrawEnable,
                        withdrawFee,
                        withdrawMin,
                        minConfirm
                    ])
                network_count += 1

            Classes.ExchangeInfoBlockchainNetwork(exchange, symbol, listNetwork)
# # a = Classes.def_FileOpenGetAllSymbols(exchange)

# client.get_currencies()
# a = requests.get(f'https://api.kucoin.com/api/v2/currencies/AAVE').json()
# print(a["data"])
# print(client.get_currencies())
