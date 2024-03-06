from binance.client import Client

from Arbitrazj_mezh_birzh import Classes

# from typing import NamedTuple  # Именованный кортеж

###########################################################
# Для формирование файла Json со списком сетей валют Binance
#
#   Пример:
#
#   {
#    "symbol": "AGLD",
#    "networkList": [
#      {
#        "network": "ETH",                                  # Имя сети
#        "secondaryNameNetwork": "Ethereum (ERC20)",        # Альтернативное название сети
#        "depositEnable": true,                             # Возможность внесения депозита
#        "withdrawEnable": true,                            # Возможность вывода депозита
#        "withdrawFee": "10",                               # Комиссия за вывод средств (количество монет)
#        "withdrawMin": "20",                               # Минимальный вывод (количество монет)
#        "minConfirm": 12                                   # Минимальное подтверждение сети
#      }
#   }

###########################################################
# Binance API settings
###########################################################


apiKey = str("TZSHjpkEt8fEuquAaKU7rZaYIjYa2oO7xuJyAnzMZjPjVXsi74jCo76hFEtrOFFD")
secretApiKey = str("HyDXw0T6WFq55ryrdZabmWDKnyUjAJPBxzFr310o50lNTYOHC2pdnUIO64pMBGBk")

client = Client(
    apiKey,
    secretApiKey
)

getAllCoinsInfo = client.get_all_coins_info()

###########################################################
# Открытие Json со всеми валютными парами
###########################################################


# binanceGetAllSymbols = '../Binance/Binance_get_all_symbol.json'
#
#
# def def_FileOpenGetAllSymbolsBinance():
#     with open(binanceGetAllSymbols) as fileData:
#         data = json.load(fileData)
#
#     return data

###########################################################
# Именованный кортеж. Типизируем данные
# ###########################################################
#
# class ListNetworkT(NamedTuple):
#     network: str
#     # secondaryNameNetwork: str
#     # depositEnable: bool
#     # withdrawEnable: bool
#     # withdrawFee: float
#     # withdrawMin: float
#     # minConfirm: float
#
# def test() -> ListNetworkT:
#
#
#     return ListNetworkT(
#
#             network= int(3)
#         # secondaryNameNetwork: secondaryNameNetwork,
#         # depositEnable: depositEnable,
#         # withdrawEnable: withdrawEnable,
#         # withdrawFee: withdrawFee,
#         # withdrawMin: withdrawMin,
#         # minConfirm: minConfirm
#
#         )

###########################################################
# Формирование файла Json со списком сетей валют
###########################################################


# for i in Classes.def_FileOpenGetAllSymbols("Binance"):
#     print(i)

exchange = "Binance"
binanceCoinInfoModify = []  # Список сетей валют Binance

for i_AllCoinsInfo in getAllCoinsInfo:
    for i_def_FileOpenGetAllSymbolsBinance in Classes.def_FileOpenGetAllSymbols(exchange):

        if i_AllCoinsInfo['coin'] == i_def_FileOpenGetAllSymbolsBinance['baseAsset']:

            indexNetwork = len(i_AllCoinsInfo['networkList'])  # Количество сетей у валюты

            Classes.ExchangeInfoBlockchainNetwork(indexNetwork, i_AllCoinsInfo, exchange)
            # Classes.ExchangeInfoBlockchainNetwork(indexNetwork, i_AllCoinsInfo['coin'])

            # listNetwork = []
            #
            # network_count = 0
            #
            # while network_count < indexNetwork:
            #
            #     network = str(i_AllCoinsInfo['networkList'][network_count]['network'])
            #     secondaryNameNetwork = str(i_AllCoinsInfo['networkList'][network_count]['name'])
            #     depositEnable = bool(i_AllCoinsInfo['networkList'][network_count]['depositEnable'])
            #     withdrawEnable = bool(i_AllCoinsInfo['networkList'][network_count]['withdrawEnable'])
            #     withdrawFee = float(i_AllCoinsInfo['networkList'][network_count]['withdrawFee'])
            #     withdrawMin = float(i_AllCoinsInfo['networkList'][network_count]['withdrawMin'])
            #     minConfirm = int(i_AllCoinsInfo['networkList'][network_count]['minConfirm'])
            #
            #     listNetwork.append(
            #         {
            #             'network': network,
            #             'secondaryNameNetwork': secondaryNameNetwork,
            #             'depositEnable': depositEnable,
            #             'withdrawEnable': withdrawEnable,
            #             'withdrawFee': withdrawFee,
            #             'withdrawMin': withdrawMin,
            #             'minConfirm': minConfirm
            #         }
            #         )
            #
            #     network_count += 1
            #
            # binanceCoinInfoModify.append(
            #     {
            #         'symbol': i_AllCoinsInfo['coin'],
            #         'networkList': listNetwork
            #     }
            # )

###########################################################

#
# with open('Binance_coin_network_info.json', 'w') as file1:
#     json.dump(binanceCoinInfoModify, file1, indent=2)
