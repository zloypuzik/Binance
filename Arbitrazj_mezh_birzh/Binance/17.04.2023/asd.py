
import json

binance_coin_info = '../Binance/test.json'


def f_file_binance_coin_info():
    with open(binance_coin_info) as file_data:
        data_a = json.load(file_data)

    return data_a

all_pairs_a = []

for i in f_file_binance_coin_info():

    if i['trading'] and i['depositAllEnable'] and i['withdrawAllEnable'] :
        print(i['networkList'][0]['network'])
        #print(i)
    #test = i['coin']
    # coin = i[0]['coin']
    # depositAllEnable = i[0]['depositAllEnable']
    # withdrawAllEnable = i[0]['withdrawAllEnable']
    # trading = i[0]['trading']
    # # print(i[0]['depositAllEnable'])
    # print(coin)

    # all_pairs_a.append(
    #     {
    #         'symbol_a': symbol_a,
    #         'baseAsset_a': baseAsset_a,
    #         'quoteAsset_a': quoteAsset_a,
    #         'stepSize_a': stepSize_a,
    #         'commission_a': commission_a
    #     }
    #print(test)
