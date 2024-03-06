import requests
import json

get_currency_detail = requests.get('https://api.kucoin.com/api/v2/currencies/BTC').json()

symbol_list = requests.get('https://api.kucoin.com/api/v2/symbols').json()

aa = []

for get_all_info_symbol in symbol_list['data']:
    if get_all_info_symbol['enableTrading'] is True:
        aa.append(get_all_info_symbol)

with open('symbol_list.json', 'w') as file1:
    json.dump(aa, file1, indent=2)

###################################################################

kucoin_coin_info = '../Kucoin/symbol_list.json'


def f_file_binance_coin_info():
    with open(kucoin_coin_info) as file_data:
        data_a = json.load(file_data)

    return data_a

all_pairs = []

for i in f_file_binance_coin_info():
    if i['quoteCurrency'] == 'USDT':
        currency_symbol = i['baseCurrency']
        get_currency_detail = requests.get(f'https://api.kucoin.com/api/v2/currencies/{currency_symbol}').json()
        symbol = get_currency_detail['data']['currency']

        index_network = len(get_currency_detail['data']['chains'])
        list_network = []

        network_count = 0

        while network_count < index_network:
            network = get_currency_detail['data']['chains'][network_count]['chain'].upper()
            # secondary_name_network = d['networkList'][network_count]['name']
            depositEnable = get_currency_detail['data']['chains'][network_count]['isDepositEnabled']
            withdrawEnable = get_currency_detail['data']['chains'][network_count]['isWithdrawEnabled']
            withdrawFee = get_currency_detail['data']['chains'][network_count]['withdrawalMinFee']
            withdrawMin = get_currency_detail['data']['chains'][network_count]['withdrawalMinSize']
            minConfirm = get_currency_detail['data']['chains'][network_count]['confirms']

            list_network.append(
                {
                    'network': network,
                    # 'secondary_name_network': secondary_name_network,
                    'depositEnable': depositEnable,
                    'withdrawEnable': withdrawEnable,
                    'withdrawFee': withdrawFee,
                    'withdrawMin': withdrawMin,
                    'minConfirm': minConfirm
                }
            )
            network_count += 1

        all_pairs.append(
            {
                'symbol': symbol,
                'networkList': list_network

            }
        )

        # networkList = get_currency_detail['data']['chains']
        print(index_network)
        # test.append(get_currency_detail)
        #print(test)
        # print(get_currency_detail)
    if i['baseCurrency'] == 'USDT':
        # currency_symbol = i['quoteCurrency']
        # get_currency_detail = requests.get(f'https://api.kucoin.com/api/v2/currencies/{currency_symbol}').json()
        # test.append(get_currency_detail)
        # # print(test)
        # print(get_currency_detail)
        pass

with open('Kucoim_coin_info_modifi.json', 'w') as file1:
    json.dump(all_pairs, file1, indent=2)

# bb = []
#
# for get_currency_detail in get_currency_detail['data']:
#     if get_currency_detail['enableTrading'] is True:
#         aa.append(get_currency_detail)
#
# with open('../Kucoin/get_currency_detail.json', 'w') as file1:
#     json.dump(aa, file1, indent=2)
# aa = []
#
# aa.append(symbol_list)
#
# print(symbol_list)
#
#
# with open('symbol_list.json', 'w') as file1:
#     json.dump(aa, file1, indent=2)
#
# # for get_all_info_symbol in symbol_list['data']:
# #     if get_all_info_symbol['enableTrading'] is True:
# #         count += 1
# #         aa.append(get_all_info_symbol)
# #     elif get_all_info_symbol['enableTrading'] is not True:
# #         not_count += 1

# from kucoin.client import Client
# from threading import *
# import websocket
# #import comm as a
#
# #x = a.check_commissions('a_1', 'a_2')
# #print(x)
# api_key = '640d22e75324b20001225c19'
# api_secret = 'f23287fb-e36a-48a8-9fa9-80fea1401435'
#
# client = Client(api_key, api_secret, passphrase='4796212')
#
# aa = client.get_withdrawals(
#     currency='XRP'
# )
# print(aa)
# for i in aa:
#     print(i)