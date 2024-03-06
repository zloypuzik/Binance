import json
from binance.client import Client
import requests


#######################################################################################
def f_get_orderbook_kucoin(symbol, get_price):

    kucoin_get_orderbook = requests.get(f'https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol={symbol}').json()
    if get_price == 'ask':
        price = kucoin_get_orderbook['data']['asks'][0][0]
    if get_price == 'bid':
        price = kucoin_get_orderbook['data']['bids'][0][0]
    return price

# print(symbol_list)

#######################################################################################
api_key = "A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG"
secret_key = "zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA"

client = Client(
    api_key,
    secret_key
)

def f_get_orderbook_binance(symbol, get_price):

    binance_get_orderbook = client.get_orderbook_ticker(
        symbol=symbol
    )
    if get_price == 'ask':
        price = binance_get_orderbook['askPrice']
    if get_price == 'bid':
        price = binance_get_orderbook['bidPrice']
    return price
#######################################################################################


binance_coin_info = '../Arbitrazj_mezh_birzh/Binance/Binance_coin_info_modifi.json'
kucoin_coin_info = '../Arbitrazj_mezh_birzh/Kucoin/Kucoim_coin_info_modifi.json'

def f_file_binance_coin_info():
    with open(binance_coin_info) as file_data:
        data_a = json.load(file_data)

    return data_a

def f_file_kucoin_coin_info():
    with open(kucoin_coin_info) as file_data:
        data_a = json.load(file_data)

    return data_a
#######################################################################################






count = 0
count_2 = 0
for binance in f_file_binance_coin_info():
    for kucoin in f_file_kucoin_coin_info():
        if binance['symbol'] == kucoin['symbol']:

            index_network_binance = len(binance['networkList'])
            list_network_binance = []
            network_count_binance = 0

            while network_count_binance < index_network_binance:
                # print(binance['networkList'][network_count_binance])
                #print(binance['networkList'][network_count_binance]['network'])
                binance_network = binance['networkList'][network_count_binance]['network']
                binance_withdrawEnable = binance['networkList'][network_count_binance]['withdrawEnable']
                binance_depositEnable = binance['networkList'][network_count_binance]['depositEnable']
                binance_withdrawFee = binance['networkList'][network_count_binance]['withdrawFee']



                index_network_kucoin = len(kucoin['networkList'])
                list_network_kucoin = []
                network_count_kucoin = 0

                while network_count_kucoin < index_network_kucoin:
                    # print(kucoin['networkList'][network_count_kucoin]['network'])
                    kucoin_network = kucoin['networkList'][network_count_kucoin]['network']
                    kucoin_withdrawEnable = kucoin['networkList'][network_count_kucoin]['withdrawEnable']
                    kucoin_depositEnable = kucoin['networkList'][network_count_kucoin]['depositEnable']
                    kucoin_withdrawFee = kucoin['networkList'][network_count_kucoin]['withdrawFee']
                    network_count_kucoin += 1

                    if kucoin_network == binance_network:

                        if binance_withdrawEnable and kucoin_depositEnable:
                            binance_price_ask = float(f_get_orderbook_binance(binance['symbol'] + 'USDT', 'ask'))
                            kucoin_price_bid = float(f_get_orderbook_kucoin(kucoin['symbol'] + '-USDT', 'bid'))
                            # price_binance = a['askPrice']
                            # print(binance)
                            # print(kucoin)
                            # print('########################################################')
                            binance_kolichestvo_coin = 1000 / binance_price_ask

                            binance_kolichestcvo_coin_posle_vivoda = binance_kolichestvo_coin - float(binance_withdrawFee)

                            kucoin_usdt_posle_prodazhi = binance_kolichestcvo_coin_posle_vivoda * kucoin_price_bid

                            itog = kucoin_usdt_posle_prodazhi - 1000

                            if itog > 2:
                                    print('##############################################################')
                                    print('binance')
                                    print('##############################################################')
                                    print(binance['symbol'], binance_network, '|', 'Komissiya:', binance_withdrawFee, itog)
                                    # pass
                        if kucoin_withdrawEnable == True and binance_depositEnable == True:
                            kucoin_price_ask = float(f_get_orderbook_kucoin(kucoin['symbol'] + '-USDT', 'ask')) # Узнаем цену продажи
                            binance_price_bid = float(f_get_orderbook_binance(binance['symbol'] + 'USDT', 'bid'))

                            kucoin_kolichestvo_coin = 1000 / kucoin_price_ask

                            kucoin_kolichestcvo_coin_posle_vivoda = kucoin_kolichestvo_coin - float(kucoin_withdrawFee)

                            binance_usdt_posle_prodazhi = kucoin_kolichestcvo_coin_posle_vivoda * binance_price_bid

                            itog = binance_usdt_posle_prodazhi - 1000
                            if itog > 2:
                                print('##############################################################')
                                print('kucoin')
                                print('##############################################################')
                                print(kucoin['symbol'], kucoin_network, '|', 'Komissiya:', kucoin_withdrawFee , itog)
                            # pass



                network_count_binance += 1


            # if binance['withdrawEnable'] and kucoin['depositEnable']:
            #     count_2 += 1
        count += 1

    # break

# print(count)
# print(count_2)
# for i in f_file_kucoin_coin_info():
#     print(i['data']['currency'])