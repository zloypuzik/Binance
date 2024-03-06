import json
import requests

from kucoin.client import Client


##################################################################
# API Kucoin
##################################################################


api_key = '63cc9d027675230001bba629'
api_secret = '0e8444e7-0594-4a57-a058-92d34decd0d7'

client = Client(api_key, api_secret, passphrase='4796212')

getAllCoinsInfo = client.get_currencies()
print(getAllCoinsInfo)
###########################################################
# Открытие Json со всеми валютными парами
###########################################################


KucoinGetAllSymbols = '../Kucoin/Kucoin_get_all_symbol.json'


def def_FileOpenGetAllSymbolsKucoin():
    with open(KucoinGetAllSymbols) as fileData:
        data = json.load(fileData)

    return data

###########################################################
# Формирование файла Json со списком сетей валют
###########################################################


# kucoinCoinInfoModify = []  # Список сетей валют Kucoin
#
# for i_AllCoinsInfo in getAllCoinsInfo:
#     for i_def_FileOpenGetAllSymbolsKucoin in def_FileOpenGetAllSymbolsKucoin():
#
#         if i_AllCoinsInfo['coin'] == i_def_FileOpenGetAllSymbolsBinance['baseAsset']:
#
#
a = requests.get(f'https://api.kucoin.com/api/v2/currencies/MTV').json()
print(a["data"])