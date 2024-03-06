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
addedNumberNetworks = 0  # Счетчик общего количества добавленных сетей

with open(f'{exchange}_coin_network_info.json', 'w') as file:
    json.dump([], file, indent=2)
"""Очистка файла, перед его заполнением информацией"""

listAllCoinsTrading = []

for i_def_FileOpenGetAllSymbols in Classes.def_FileOpenGetAllSymbols(exchange):

    if i_def_FileOpenGetAllSymbols['immutableNameBaseAsset'] not in listAllCoinsTrading:
        listAllCoinsTrading.append(i_def_FileOpenGetAllSymbols['immutableNameBaseAsset'])

    elif i_def_FileOpenGetAllSymbols['immutableNameQuoteAsset'] not in listAllCoinsTrading:
        listAllCoinsTrading.append(i_def_FileOpenGetAllSymbols['immutableNameQuoteAsset'])


for i_AllCoinsInfo in getAllCoinsInfo:

    if i_AllCoinsInfo['coin'] in listAllCoinsTrading:

        symbol = i_AllCoinsInfo['coin']
        name = i_AllCoinsInfo['coin']

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

        Classes.ExchangeInfoBlockchainNetwork(exchange, symbol, name, listNetwork)

print(f"Добавлена информация о '{addedNumberNetworks}' BlockchainNetworks.")
