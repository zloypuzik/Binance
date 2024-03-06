import json
import requests

from Arbitrazj_mezh_birzh import Classes

###########################################################

client = Classes.apiKucoin()
"""API settings"""


getAllCoinsInfo = []
"""Сбор информации по Blockchain networks"""


def def_getAllCoinsInfo(listAllCoins):

    for i_listAllCoins in listAllCoins:
        requestsAllCoinsInfo = requests.get(f'https://api.kucoin.com/api/v2/currencies/{i_listAllCoins}').json()
        if requestsAllCoinsInfo['data']['chains'] is not None:
            getAllCoinsInfo.append(requestsAllCoinsInfo)

###########################################################
# Формирование файла Json со списком сетей валют
###########################################################


exchange = "Kucoin"
addedNumberNetworks = 0  # Общее количество добавленных сетей

with open(f'{exchange}_coin_network_info.json', 'w') as file:  # Очистка файла
    json.dump([], file, indent=2)

listAllCoinsTrading = []

for i_def_FileOpenGetAllSymbols in Classes.def_FileOpenGetAllSymbols(exchange):

    if i_def_FileOpenGetAllSymbols['immutableNameBaseAsset'] not in listAllCoinsTrading:
        listAllCoinsTrading.append(i_def_FileOpenGetAllSymbols['immutableNameBaseAsset'])

    elif i_def_FileOpenGetAllSymbols['immutableNameQuoteAsset'] not in listAllCoinsTrading:
        listAllCoinsTrading.append(i_def_FileOpenGetAllSymbols['immutableNameQuoteAsset'])

def_getAllCoinsInfo(listAllCoinsTrading)

for i_AllCoinsInfo in getAllCoinsInfo:

    if i_AllCoinsInfo['data']['currency'] in listAllCoinsTrading:

        symbol = i_AllCoinsInfo['data']['currency']
        name = i_AllCoinsInfo['data']['name']

        indexNetwork = len(i_AllCoinsInfo['data']['chains'])  # Количество сетей у валюты

        listNetwork = []
        network_count = 0
        addedNumberNetworks += 1

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

        Classes.ExchangeInfoBlockchainNetwork(exchange, symbol, name, listNetwork)

print(f"Добавлена информация о '{addedNumberNetworks}' BlockchainNetworks.")
