import json

from Arbitrazj_mezh_birzh import Classes

###########################################################

client = Classes.apiBinance()
"""API settings"""

getAllCoinsInfo = client.get_all_coins_info()
"""Сбор информации по Blockchain networks"""

###########################################################
# Формирование файла Json со списком сетей валют
###########################################################


exchange = "Binance"
binanceCoinInfoModify = []  # Список сетей валют Binance
symbolNoDuplicates = []  # Список без дубликатов, чтоб не создавать дубликаты в info JSON (например USDT)
addedNumberNetworks = 0  # Счетчик общего количества добавленных сетей

with open(f'{exchange}_coin_network_info.json', 'w') as file:
    json.dump([], file, indent=2)
"""Очистка файла, перед его заполнением информацией"""

for i_AllCoinsInfo in getAllCoinsInfo:

    for i_def_FileOpenGetAllSymbols in Classes.def_FileOpenGetAllSymbols(exchange):

        if i_AllCoinsInfo['coin'] == i_def_FileOpenGetAllSymbols['baseAsset']:

            symbol = i_AllCoinsInfo['coin']

            if symbol not in symbolNoDuplicates:  # Проверка, что нет повторений Symbol (чтоб избежать дублирования в info Json)
                """
                    Проверяем что нет повторений, т.к. в отобранных парах, в файле 'FileOpenGetAllSymbols', может дублироваться 'baseAsset' или 'quoteAsset'.
                    Например: 'ETHUSDT', 'BTCUSDT' - дублируется 'USDT'
                """
                symbolNoDuplicates.append(symbol)

                indexNetwork = len(i_AllCoinsInfo['networkList'])  # Количество сетей у валюты

                listNetwork = []
                network_count = 0
                addedNumberNetworks += 1

                while network_count < indexNetwork:

                    network = str(i_AllCoinsInfo['networkList'][network_count]['network'])
                    secondaryNameNetwork = str(i_AllCoinsInfo['networkList'][network_count]['name'])
                    depositEnable = bool(i_AllCoinsInfo['networkList'][network_count]['depositEnable'])
                    withdrawEnable = bool(i_AllCoinsInfo['networkList'][network_count]['withdrawEnable'])
                    withdrawFee = float(i_AllCoinsInfo['networkList'][network_count]['withdrawFee'])
                    withdrawMin = float(i_AllCoinsInfo['networkList'][network_count]['withdrawMin'])
                    minConfirm = int(i_AllCoinsInfo['networkList'][network_count]['minConfirm'])

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

print(f"Добавлена информация о '{addedNumberNetworks}' BlockchainNetworks.")
