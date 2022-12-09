import json

main_currency = 'USDT'

file_step_1_pairs_trade = '../Binance_ETH/1_25_step_1_pairs_trade.json'

def f_file_step_1_pairs_trade():
    with open(file_step_1_pairs_trade) as file_data:
        data_a = json.load(file_data)

    return data_a

quote_asset = 'ETH'

count_pairs_1 = 0
count_pairs_2 = 0

all_pairs_c = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR', 'GBR', 'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']  # Валюта, за которую можно купить или продать другую валюту.


for test in f_file_step_1_pairs_trade():
    if test['baseAsset'] == quote_asset:
        print(test['quoteAsset'])

        count_pairs_1 += 1
print('##############################')
print(count_pairs_1)
print('##############################')



for test2 in f_file_step_1_pairs_trade():
    #for test22 in all_pairs_c:
    if test2['quoteAsset'] == quote_asset:
        for test22 in all_pairs_c:
            if test2['baseAsset'] == test22:
                print(test2['baseAsset'])

                count_pairs_2 += 1
print('##############################')
print(count_pairs_2)
print('##############################')
