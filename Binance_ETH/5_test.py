# -*- coding: utf8 -*-
import json
import time
from collections import OrderedDict  # модуль для удаления повторения

check_quote_pairs = '../Binance_ETH/1_pairs_buy_para_b_test.json'


def f_file_step_1_pairs_trade():
    with open(check_quote_pairs) as file_data:
        data_a = json.load(file_data)

    return data_a


########################################################################################################
# Определяем главную валюту
########################################################################################################

main_currency = []

for i in f_file_step_1_pairs_trade():
    main_currency = (i['main_currency'])

########################################################################################################
# Формируем основной файл
########################################################################################################

all_pairs_btc = "Run_BTC_all_main_currency_pairs_2" + ".py"

with open(all_pairs_btc, 'w') as file3:
    file3.write("")

with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
    file3.write(
        "import time \n"
        "import datetime \n"
        "import threading \n"
        "from decimal import Decimal \n"
        "import json \n"
        "import websocket \n"
        "from threading import * \n"
        "from binance.client import Client \n"
        "\n"
        # "\n"
        # "def f_minqty_size_up(kolichestvo, stepSize): \n"
        # "\n"
        # "\tdef adjust_to_step(value, step, increase=True): \n"
        # "\t\treturn ((int(value * 100000000) - int(value * 100000000) % int( \n"
        # "\t\t\tDdecimal.Decimal(step) * 100000000)) / 100000000) + (decimal.Decimal(step) if increase else 0) \n"
        # "\tsell_amount_a = adjust_to_step(kolichestvo, stepSize) \n"
        # "\treturn sell_amount_a \n"
        # "\n"
        # "\n"
        # "def f_minqty_size_down(kolichestvo, stepSize): \n"
        # "\n"
        # "\tdef adjust_to_step(value, step, increase=False): \n"
        # "\t\treturn ((int(value * 100000000) - int(value * 100000000) % int( \n"
        # "\t\t\tdecimal.Decimal(step) * 100000000)) / 100000000) + (decimal.Decimal(step) if increase else 0) \n"
        # "\tsell_amount_a = adjust_to_step(kolichestvo, stepSize) \n"
        # "\treturn sell_amount_a \n"
        # "\n"
        "\n"
        "def f_minqty_size_up(kolichestvo, stepSize): \n"
        "\n"
        "\tsell_amount_a = ((int(kolichestvo * 100000000) - int(kolichestvo * 100000000) % (stepSize * 100000000)) / 100000000) + stepSize \n"
        "\treturn sell_amount_a \n"
        "\n"
        "\n"
        "def f_minqty_size_down(kolichestvo, stepSize): \n"
        "\n"
        "\tsell_amount_a = ((int(kolichestvo * 100000000) - int(kolichestvo * 100000000) % (stepSize * 100000000)) / 100000000) \n"
        "\treturn sell_amount_a \n"
        "\n"
        "\n"
        "api_key = 'A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG' \n"
        "secret_key = 'zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA' \n"
        "\n"
        "client = Client(api_key, secret_key) \n"
        "\n"
        "usdt_count = Decimal(input('Укажите количество монет:')) \n"
        "\n"
        "all_pribil = Decimal('0.0') \n"
        "\n"
        "\n"
        "locker = threading.RLock() \n"
        "\n"
    )

########################################################################################################


main_pairs = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR', 'GBR',
              'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']

########################################################################################################
# Проверяем пары 'a','b' и 'c' в файле 'f_file_step_1_pairs_trade' и если в этих парах 'baseAsset' и 'quoteAsset' равно 'main_pairs', добавляем пару в переменную 'all_main_currency_pairs'
########################################################################################################

all_main_currency_pairs = []  # Список пар в которых 'baseAsset' и 'quoteAsset' равно 'main_pairs'
count_pairs_a = 0

all_pairs = []

for i in f_file_step_1_pairs_trade():
    if count_pairs_a == 0:
        symbol = (i['symbol_a'])
        baseAsset = (i['baseAsset_a'])
        quoteAsset = (i['quoteAsset_a'])
        stepSize = (i['stepSize_a'])
        commission = (i['commission_a'])
        all_pairs.append(
            {
                'symbol_g': symbol,
                'baseAsset_g': baseAsset,
                'quoteAsset_g': quoteAsset,
                'stepSize_g': stepSize,
                'commission_g': commission
            }
        )
        count_pairs_a += 1

for i in f_file_step_1_pairs_trade():
    a = False
    for ii in all_pairs:

        if i['symbol_a'] == ii['symbol_g']:
            a = True
            break

    if not a:

        symbol = (i['symbol_a'])
        baseAsset = (i['baseAsset_a'])
        quoteAsset = (i['quoteAsset_a'])
        stepSize = (i['stepSize_a'])
        commission = (i['commission_a'])
        all_pairs.append(
            {
                'symbol_g': symbol,
                'baseAsset_g': baseAsset,
                'quoteAsset_g': quoteAsset,
                'stepSize_g': stepSize,
                'commission_g': commission
            }
        )

        count_pairs_a += 1

for i in f_file_step_1_pairs_trade():
    a = False
    for ii in all_pairs:

        if i['symbol_b'] == ii['symbol_g']:
            a = True
            break

    if not a:

        symbol = (i['symbol_b'])
        baseAsset = (i['baseAsset_b'])
        quoteAsset = (i['quoteAsset_b'])
        stepSize = (i['stepSize_b'])
        commission = (i['commission_b'])
        all_pairs.append(
            {
                'symbol_g': symbol,
                'baseAsset_g': baseAsset,
                'quoteAsset_g': quoteAsset,
                'stepSize_g': stepSize,
                'commission_g': commission
            }
        )

        count_pairs_a += 1

for i in f_file_step_1_pairs_trade():
    a = False
    for ii in all_pairs:

        if i['symbol_c'] == ii['symbol_g']:
            a = True
            break

    if not a:

        symbol = (i['symbol_c'])
        baseAsset = (i['baseAsset_c'])
        quoteAsset = (i['quoteAsset_c'])
        stepSize = (i['stepSize_c'])
        commission = (i['commission_c'])
        all_pairs.append(
            {
                'symbol_g': symbol,
                'baseAsset_g': baseAsset,
                'quoteAsset_g': quoteAsset,
                'stepSize_g': stepSize,
                'commission_g': commission
            }
        )

        count_pairs_a += 1

########################################################################################################
# Формируем функции для основных валют (пара 'с')
########################################################################################################
for i in all_pairs:
    symbol_gg = i['symbol_g']
    symbol_gg = symbol_gg.lower()
    with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
        file3.write(
            f"symbol_g_{i['symbol_g']} = '{i['symbol_g']}' \n"
            f"price_bids_g_{i['symbol_g']} = Decimal('0.0') \n"
            f"qty_bids_g_{i['symbol_g']} = Decimal('0.0') \n"
            f"price_asks_g_{i['symbol_g']} = Decimal('0.0') \n"
            f"qty_asks_g_{i['symbol_g']} = Decimal('0.0') \n"
            f"stepSize_g_{i['symbol_g']} = Decimal('{i['stepSize_g']}') \n"
            "\n"
            "\n"
            f"def on_message_{i['symbol_g']}(ws, message): \n"
            "\n"
            "\tdata = json.loads(message) \n"
            "\n"
            f"\tsymbol_c_l_{i['symbol_g']} = '{i['symbol_g']}' \n"
            f"\tprice_bids_c_l_{i['symbol_g']} = data['bids'][0][0] \n"
            f"\tqty_bids_c_l_{i['symbol_g']} = data['bids'][0][1] \n"
            f"\tprice_asks_c_l_{i['symbol_g']} = data['asks'][0][0] \n"
            f"\tqty_asks_c_l_{i['symbol_g']} = data['asks'][0][1] \n"
            "\n"
            f"\tglobal symbol_g_{i['symbol_g']} \n"
            f"\tglobal price_bids_g_{i['symbol_g']} \n"
            f"\tglobal qty_bids_g_{i['symbol_g']} \n"
            f"\tglobal price_asks_g_{i['symbol_g']} \n"
            f"\tglobal qty_asks_g_{i['symbol_g']} \n"
            "\n"
            f"\tsymbol_g_{i['symbol_g']} = symbol_c_l_{i['symbol_g']} \n"
            f"\tprice_bids_g_{i['symbol_g']} = Decimal(price_bids_c_l_{i['symbol_g']}) \n"
            f"\tqty_bids_g_{i['symbol_g']} = Decimal(qty_bids_c_l_{i['symbol_g']}) \n"
            f"\tprice_asks_g_{i['symbol_g']} = Decimal(price_asks_c_l_{i['symbol_g']}) \n"
            f"\tqty_asks_g_{i['symbol_g']} = Decimal(qty_asks_c_l_{i['symbol_g']}) \n"
            "\n"
            "\n"
            f"def loop_{i['symbol_g']}(): \n"
            "\n"
            f"\tsocket1 = f'wss://stream.binance.com:9443/ws/{symbol_gg}@depth5@100ms' \n"
            f"\tws = websocket.WebSocketApp(socket1, on_message=on_message_{i['symbol_g']}) \n"
            "\tws.run_forever() \n"
            "\n"
            "\n"
            f"Thread(target=loop_{i['symbol_g']}).start() \n"
            "\n"
        )
# ########################################################################################################
# # Только для визуального отделения (#)
# ########################################################################################################
#
# with open(all_pairs_btc, 'a') as file3:
#     file3.write(
#         "\n"
#         "########################################################################################################"
#         "\n"
#     )
# ########################################################################################################

for i in f_file_step_1_pairs_trade():

    symbol_a = i['symbol_a']
    symbol_aa = symbol_a.lower()
    stepSize_a = i['stepSize_a']
    commission_a = i['commission_a']

    symbol_b = i['symbol_b']
    symbol_bb = symbol_b.lower()
    stepSize_b = i['stepSize_b']
    commission_b = i['commission_b']

    symbol_c = i['symbol_c']
    symbol_cc = symbol_c.lower()
    stepSize_c = i['stepSize_c']
    commission_c = i['commission_c']

    if i['quoteAsset_a'] == main_currency:
        trade_a_pair = 'buy'
        tr_a_pair_a_1 = i['baseAsset_a']
        tr_a_pair_a_2 = main_currency
        tr_n_a = 'asks'

        if i['baseAsset_a'] == i['quoteAsset_b']:
            trade_b_pair = 'buy'
            tr_n_b = 'asks'
            tr_a_pair_b_1 = i['baseAsset_b']
            tr_a_pair_b_2 = i['quoteAsset_b']

            if i['baseAsset_b'] == i['quoteAsset_c']:
                trade_c_pair = 'buy'
                tr_n_c = 'asks'
                trade_all = 'buy -> buy -> buy'
                tr_a = 'Покупаем'
                tr_b = 'Покупаем'
                tr_c = 'Покупаем'

            elif i['baseAsset_b'] == i['baseAsset_c']:
                trade_c_pair = 'sell'
                tr_a_pair_c_1 = i['baseAsset_c']
                tr_a_pair_c_2 = i['quoteAsset_c']
                tr_n_c = 'bids'
                trade_all = 'buy -> buy -> sell'
                tr_a = 'Покупаем'
                tr_b = 'Покупаем'
                tr_c = 'Продаем'

            else:
                print("1 Проверьте пару 'C', в ней отсутствует монета:", i['baseAsset_b'])

        elif i['baseAsset_a'] == i['baseAsset_b']:
            trade_b_pair = 'sell'
            tr_n_b = 'bids'
            tr_a_pair_b_1 = i['baseAsset_b']
            tr_a_pair_b_2 = i['quoteAsset_b']

            if i['quoteAsset_b'] == i['quoteAsset_c']:
                trade_c_pair = 'buy'
                tr_n_c = 'asks'
                trade_all = 'buy -> sell -> buy'
                tr_a = 'Покупаем'
                tr_b = 'Продаем'
                tr_c = 'Покупаем'
                tr_a_pair_c_1 = i['baseAsset_c']
                tr_a_pair_c_2 = i['quoteAsset_c']

            elif i['quoteAsset_b'] == i['baseAsset_c']:
                trade_c_pair = 'sell'
                tr_n_c = 'bids'
                trade_all = 'buy -> sell -> sell'
                tr_a = 'Покупаем'
                tr_b = 'Продаем'
                tr_c = 'Продаем'
                tr_a_pair_c_1 = i['baseAsset_c']
                tr_a_pair_c_2 = i['quoteAsset_c']
            else:
                print("2 Проверьте пару 'C', в ней отсутствует монета:", i['quoteAsset_b'])

        else:
            print("Проверьте пару 'Б', в ней отсутствует монета:", i['baseAsset'])
    #####################################################################################################################
    elif i['baseAsset_a'] == main_currency:
        trade_a_pair = 'sell'
        tr_n_a = 'bids'
        tr_a_pair_a_1 = main_currency
        tr_a_pair_a_2 = i['quoteAsset_a']

        if i['quoteAsset_a'] == i['quoteAsset_b']:
            trade_b_pair = 'buy'
            tr_n_b = 'asks'

            if i['baseAsset_b'] == i['quoteAsset_c']:
                trade_c_pair = 'buy'
                tr_n_c = 'asks'
                trade_all = 'sell -> buy -> buy'
                tr_a = 'Продаем'
                tr_b = 'Покупаем'
                tr_c = 'Покупаем'

            elif i['baseAsset_b'] == i['baseAsset_c']:
                trade_c_pair = 'sell'
                tr_n_c = 'bids'
                trade_all = 'sell -> buy -> sell'
                tr_a = 'Продаем'
                tr_b = 'Покупаем'
                tr_c = 'Продаем'
            else:
                print("1 Проверьте пару 'C', в ней отсутствует монета:", i['baseAsset_b'])

        elif i['quoteAsset_a'] == i['baseAsset_b']:
            trade_b_pair = 'sell'
            tr_n_b = 'bids'

            if i['quoteAsset_b'] == i['quoteAsset_c']:
                trade_c_pair = 'buy'
                tr_n_c = 'asks'
                trade_all = 'sell -> sell -> buy'
                tr_a = 'Продаем'
                tr_b = 'Продаем'
                tr_c = 'Покупаем'

            elif i['quoteAsset_b'] == i['baseAsset_c']:
                trade_c_pair = 'sell'
                tr_n_c = 'bids'
                trade_all = 'sell -> sell -> sell'
                tr_a = 'Продаем'
                tr_b = 'Продаем'
                tr_c = 'Продаем'

            else:
                print("2 Проверьте пару 'C', в ней отсутствует монета:", i['quoteAsset_b'])

        else:
            print("Проверьте пару 'Б', в ней отсутствует монета:", i['quoteAsset'])

    else:
        print("Проверьте пару 'А', в ней отсутствует монета:", main_currency)
#####################################################################################################################
#####################################################################################################################
    quantity_pair_c_raschet_buy = [
        f"\t\t\tquantity_pair_c_raschet = Decimal(usdt_count) * Decimal(price_asks_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
        # f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
        f"\t\t\tquantity_pair_c_raschet = Decimal(f_minqty_size_down(quantity_pair_c_raschet, stepSize_g_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
        # f"\t\t\tquantity_pair_c_raschet = quantity_pair_c_raschet.quantize(Decimal(stepSize_g_{symbol_c}), ROUND_DOWN)  # Округляем согласно шагу Binance 'stepSize' \n"
        #quantity_pair_c_raschet = quantity_pair_c_raschet.quantize(Decimal(stepSize_g_{symbol_c}), ROUND_DOWN)
        # sell_amount_a = kolichestvo.quantize(Decimal(stepSize), ROUND_DOWN)
        # f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
        f"\t\t\t# quantity_pair_c_raschet = количество '{i['quoteAsset_c']}' \n"
        #f"\t\t\ttest2 = Decimal('0') \n"
        ]
    quantity_pair_c_raschet_sell = [
        # f"\t\t\tquantity_pair_c_raschet = Decimal(usdt_count) / Decimal(price_bids_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
        # # f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
        # #f"\t\t\tquantity_pair_c_raschet = Decimal(f_minqty_size_down(quantity_pair_c_raschet, stepSize_g_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
        # # f"\t\t\tquantity_pair_c_raschet = quantity_pair_c_raschet.quantize(Decimal(stepSize_g_{symbol_c}), ROUND_DOWN)  # Округляем согласно шагу Binance 'stepSize' \n"
        # # f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
        # f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_c']}' \n"
        f"\t\t\tquantity_pair_c_raschet = Decimal(usdt_count) / Decimal(price_bids_g_{symbol_c}) \n"
        # Определяем, сколько нужно валюты 'c', для торговли в паре 'b'
        f"\t\t\tquantity_pair_c_raschet = Decimal(f_minqty_size_down(quantity_pair_c_raschet, stepSize_g_{symbol_c})) \n"
        # quantity_pair_c_raschet = количество 'TRX'
        f"\t\t\ttest3 = quantity_pair_c_raschet \n"
        # Округляем 'quantity_pair_c_raschet' в паре Б (количество валюты, которую должны купить в паре Б)
    ]
    #####################################################################################################################
    quantity_pair_b_raschet_buy = [
        # f"\t\t\tquantity_pair_b_raschet = Decimal(quantity_pair_c_raschet) * Decimal(price_asks_g_{symbol_b})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
        # # f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
        # # f"\t\t\tquantity_pair_b_raschet = Decimal(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
        # # f"\t\t\tquantity_pair_c_raschet = quantity_pair_c_raschet.quantize(Decimal(stepSize_g_{symbol_c}), ROUND_UP)  # Округляем согласно шагу Binance 'stepSize' \n"
        # # f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
        # f"\t\t\t# quantity_pair_b_raschet = количество '{i['quoteAsset_b']}' \n"
        #f"\t\t\tif quantity_pair_c_raschet == test: \n"
        # и если получаемая валюта в паре С, ровна этой валюте в паре Б после округления
        # f"\t\t\tif quantity_pair_c_raschet != test: \n"
        # f"\t\t\t\twhile test < quantity_pair_c_raschet: \n"
        # f"\t\t\t\t\ttest = Decimal(f_minqty_size_up(quantity_pair_c_raschet, stepSize_g_{symbol_b})) \n"
        # f"\t\t\tquantity_pair_b_raschet = Decimal(test) * Decimal(price_asks_g_{symbol_b}) \n"
        # # Определяем, сколько нужно валюты 'b', для торговли в паре 'a'
        # f"\t\t\ttest2 = Decimal(f_minqty_size_down(quantity_pair_b_raschet, stepSize_g_{symbol_a})) \n"
        # f"\t\t\tif test2 < quantity_pair_b_raschet: \n"
        # f"\t\t\t\twhile test2 < quantity_pair_b_raschet: \n"
        # f"\t\t\t\t\ttest2 = Decimal(f_minqty_size_up(test2, stepSize_g_{symbol_a})) \n"
        # f"\t\t\tquantity_pair_a = test2 \n"
        # f"\t\t\tquantity_pair_b = test \n"
        # f"\t\t\tquantity_pair_c = test \n"
        f"\t\t\tdd = Decimal(f_minqty_size_down(test3, stepSize_g_{symbol_b})) \n"
        f"\t\t\twhile dd < test3: \n"
        f"\t\t\t\tdd = (f_minqty_size_up(dd, stepSize_g_{symbol_b})) \n"
        f"\t\t\ttest3 = dd \n"
        f"\t\t\tquantity_pair_b_raschet = Decimal(test3) * Decimal(price_asks_g_{symbol_b}) \n"
        f"\t\t\ttest2 = quantity_pair_b_raschet \n"
        "\n"
        f"\t\t\tddd = Decimal(f_minqty_size_down(test2, stepSize_g_{symbol_a})) \n"
        f"\t\t\twhile ddd < test2: \n"
        f"\t\t\t\tddd = Decimal(f_minqty_size_up(ddd, stepSize_g_{symbol_a})) \n"
        f"\t\t\ttest2 = ddd \n"
        "\n"
        f"\t\t\ttest1 = ddd \n"
        f"\t\t\tquantity_pair_a = test1 \n"
        f"\t\t\tquantity_pair_b = test3 \n"
        f"\t\t\tquantity_pair_c = test3 \n"
    ]
    quantity_pair_b_raschet_sell = [
        # f"\t\t\tquantity_pair_b_raschet = Decimal(quantity_pair_c_raschet) / Decimal(price_bids_g_{symbol_b})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
        # # f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
        # # f"\t\t\tquantity_pair_b_raschet = Decimal(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
        # # f"\t\t\tquantity_pair_c_raschet = quantity_pair_c_raschet.quantize(Decimal(stepSize_g_{symbol_c}), ROUND_UP)  # Округляем согласно шагу Binance 'stepSize' \n"
        # # f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
        # f"\t\t\t# quantity_pair_b_raschet = количество '{i['baseAsset_b']}' \n"
        f"\t\t\tquantity_pair_b_raschet = Decimal(test3) / Decimal(price_bids_g_{symbol_b}) \n"
        f"\t\t\ttest2 = Decimal(f_minqty_size_down(quantity_pair_b_raschet, stepSize_g_{symbol_b})) \n"
        f"\t\t\twhile test2 < quantity_pair_b_raschet: \n"
        f"\t\t\t\ttest2 = Decimal(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b})) \n"
        f"\t\t\ttest1 = Decimal(f_minqty_size_down(test2, stepSize_g_{symbol_a})) \n"
        f"\t\t\twhile test1 < test2: \n"
        f"\t\t\t\ttest1 = Decimal(f_minqty_size_up(test1, stepSize_g_{symbol_a})) \n"
        # f"\t\t\ttest2 = Decimal(f_minqty_size_down(quantity_pair_b_raschet, stepSize_g_{symbol_b})) \n"
        # #f"\t\t\tif test2 < quantity_pair_b_raschet: \n"
        # f"\t\t\twhile test2 < quantity_pair_b_raschet: \n"
        # f"\t\t\t\ttest2 = Decimal(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b})) \n"
        f"\t\t\tquantity_pair_a = test1 \n"
        f"\t\t\tquantity_pair_b = test2 \n"
        f"\t\t\tquantity_pair_c = test3 \n"
    ]
    #####################################################################################################################
    # quantity_pair_a_raschet_buy = [
    #     f"\t\t\tprice_a = Decimal(quantity_pair_b_raschet) * Decimal(price_asks_g_{symbol_a}) \n"
    #     # f"\t\t\tprice_a = round(price_a, 14) \n"
    #     f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
    # ]
    # quantity_pair_a_raschet_sell = [
    #     f"\t\t\tprice_a = Decimal(quantity_pair_b_raschet) / Decimal(price_bids_g_{symbol_a}) \n"
    #     # f"\t\t\tprice_a = round(price_a, 14) \n"
    #     f"\t\t\t# price_a = сколько потребуется '{i['baseAsset_a']}' \n"
    # ]
    #####################################################################################################################
    trade_pair_a_buy = [
        # f"\t\t\tprice_a = Decimal(quantity_pair_b_raschet) * Decimal(price_asks_g_{symbol_a}) \n"
        # # f"\t\t\tprice_a = round(price_a, 14) \n"
        # f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
        f"\t\t\tprice_a = Decimal(quantity_pair_a) * Decimal(price_asks_g_{symbol_a}) \n"
    ]
    trade_pair_a_sell = [
        f"\t\t\tprice_a = Decimal(quantity_pair_b_raschet) / Decimal(price_bids_g_{symbol_a}) \n"
        # f"\t\t\tprice_a = round(price_a, 14) \n"
        f"\t\t\t# price_a = сколько потребуется '{i['baseAsset_a']}' \n"
    ]
    #####################################################################################################################
    trade_pair_b_buy = [
        # f"\t\t\tprice_b = Decimal(quantity_pair_b_raschet) * Decimal(price_asks_g_{symbol_b}) \n"
        # # f"\t\t\tprice_b = round(price_b, 14) \n"
        # f"\t\t\t# price_b = сколько получим '{i['baseAsset_b']}' \n"
        f"\t\t\tprice_b = Decimal(quantity_pair_b) * Decimal(price_asks_g_{symbol_b}) \n"
    ]
    trade_pair_b_sell = [
        # f"\t\t\tprice_b = Decimal(quantity_pair_b_raschet) / Decimal(price_bids_g_{symbol_b}) \n"
        # # f"\t\t\tprice_b = round(price_b, 14) \n"
        # f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
        f"\t\t\tprice_b = Decimal(quantity_pair_b) * Decimal(price_bids_g_{symbol_b}) \n"
    ]
    #####################################################################################################################
    trade_pair_c_buy = [
        # f"\t\t\tprice_b_size = Decimal(f_minqty_size_down(price_b, stepSize_g_{symbol_c})) \n"
        # f"\t\t\tprice_b_size = price_b.quantize(Decimal(stepSize_g_{symbol_c}), ROUND_DOWN) \n"
        f"\t\t\tprice_c = Decimal(price_b) * Decimal(price_asks_g_{symbol_c}) \n"
        # f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
        f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
    ]
    trade_pair_c_sell = [
        # # f"\t\t\tprice_b_size = Decimal(f_minqty_size_down(price_b, stepSize_g_{symbol_c})) \n"
        # # f"\t\t\tprice_b_size = price_b.quantize(Decimal(stepSize_g_{symbol_c}), ROUND_DOWN) \n"
        # f"\t\t\tprice_c = Decimal(price_b) / Decimal(price_bids_g_{symbol_c}) \n"
        # # f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
        # f"\t\t\t# price_c = сколько получим '{i['quoteAsset_c']}' \n"
        f"\t\t\tprice_c = Decimal(quantity_pair_c) * Decimal(price_bids_g_{symbol_c}) \n"
    ]
    #####################################################################################################################

    test_op = [
        f"def loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade(): \n"
        "\n"
        "\twhile True: \n"
        "\t\ttime.sleep(0.1)\n"
        "\t\tlocker.acquire()\n"
        "\n"
        f"\t\tif price_bids_g_{symbol_a} != 0.0 and qty_bids_g_{symbol_a} != 0.0 and price_asks_g_{symbol_a} != 0.0 and qty_asks_g_{symbol_a} != 0.0 and price_bids_g_{symbol_b} != 0.0 and qty_bids_g_{symbol_b} != 0.0 and price_asks_g_{symbol_b} != 0.0 and qty_asks_g_{symbol_b} != 0.0 and price_bids_g_{symbol_c} != 0.0 and qty_bids_g_{symbol_c} != 0.0 and price_asks_g_{symbol_c} != 0.0 and qty_asks_g_{symbol_c} != 0.0: \n"
        #######################################################################################################################
        "\n"
    ]
    testtest = [
        f"\t\t\tpribil = Decimal(price_c) - Decimal(price_a) \n"
        "\n"
        f"\t\t\ttime_test = datetime.datetime.now() \n"
        f"\t\t\ta = Decimal(price_c) \n"
        f"\t\t\tb = Decimal(price_a) \n"
        f"\t\t\tc = Decimal((a / b - 1) * 100) \n"
        f"\t\t\tcommission_a = Decimal('{commission_a}') \n"
        f"\t\t\tcommission_b = Decimal('{commission_b}') \n"
        f"\t\t\tcommission_c = Decimal('{commission_c}') \n"
        f"\t\t\tcommission_all = Decimal(commission_a) + Decimal(commission_b) + Decimal(commission_c) \n"
        # f"\t\t\tcommission_all = commission_all.quantize(Decimal('0.0001')) \n"
        f"\t\t\tif c > commission_all: \n"
        "\n"
        f"\t\t\t\tprint('################################################################################################################') \n"
        f"\t\t\t\tprint(time_test) \n"
        f"\t\t\t\tprint('Общая коммисия:', commission_all) \n"
        # f"\t\t\t\tprint('Пара_А:', symbol_g_{symbol_a}, '# Покупаем', quantity_pair_b_raschet, '{i['baseAsset_a']}', 'за', price_a, '{i['quoteAsset_a']}', 'по цене', price_asks_g_{symbol_a}) \n"
        # f"\t\t\t\tprint('Пара_B:', symbol_g_{symbol_b}, '# Продаем', quantity_pair_b_raschet, '{i['baseAsset_b']}', 'за', price_b, '{i['quoteAsset_b']}', 'по цене', price_bids_g_{symbol_b}) \n"
        # f"\t\t\t\tprint('Пара_C:', symbol_g_{symbol_c}, '# Продаем', price_b, '{i['baseAsset_c']}', 'за', price_c, '{i['quoteAsset_c']}', 'по цене', price_bids_g_{symbol_c}) \n"
        # f"\t\t\t\tprint('Прибыль:', pribil, 'Прибыль в %:', c, '%') \n"
        f"\t\t\t\tprint('Пара_А:', symbol_g_{symbol_a}, '#', '{tr_a}', quantity_pair_a, '{tr_a_pair_a_1}', 'за', price_a, '{tr_a_pair_a_2}', 'по цене', price_{tr_n_a}_g_{symbol_a}) \n"
        f"\t\t\t\tprint('Пара_B:', symbol_g_{symbol_b}, '#', '{tr_b}', quantity_pair_b, '{tr_a_pair_b_1}', 'за', price_b, '{tr_a_pair_b_2}', 'по цене', price_{tr_n_b}_g_{symbol_b}) \n"
        f"\t\t\t\tprint('Пара_C:', symbol_g_{symbol_c}, '#', '{tr_c}', quantity_pair_c, '{tr_a_pair_c_1}', 'за', price_c, '{tr_a_pair_c_2}', 'по цене', price_{tr_n_c}_g_{symbol_c}) \n"
        f"\t\t\t\tprint('Прибыль:', pribil, 'Прибыль в %:', c, '%') \n"
        "\n"
        f"\t\tlocker.release() \n"
        "\n"
        f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
        "\n"
        f"###################################################################### \n"
        "\n"
    ]
    # with open(all_pairs_btc, 'a') as file3:
    #     file3.write(
    #         f"def loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade(): \n"
    #         "\n"
    #         "\twhile True: \n"
    #         "\t\ttime.sleep(0.1)\n"
    #         "\t\tlocker.acquire()\n"
    #         "\n"
    #         f"\t\tif price_bids_g_{symbol_a} != 0.0 and qty_bids_g_{symbol_a} != 0.0 and price_asks_g_{symbol_a} != 0.0 and qty_asks_g_{symbol_a} != 0.0 and price_bids_g_{symbol_b} != 0.0 and qty_bids_g_{symbol_b} != 0.0 and price_asks_g_{symbol_b} != 0.0 and qty_asks_g_{symbol_b} != 0.0 and price_bids_g_{symbol_c} != 0.0 and qty_bids_g_{symbol_c} != 0.0 and price_asks_g_{symbol_c} != 0.0 and qty_asks_g_{symbol_c} != 0.0: \n"
    #         #######################################################################################################################
    #         "\n"
    #     )
    #####################################################################################################################
    if trade_all == "buy -> buy -> sell":

        for p in test_op:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)



        for p in quantity_pair_c_raschet_sell:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in quantity_pair_b_raschet_buy:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)

        for p in trade_pair_a_buy:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in trade_pair_b_buy:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in trade_pair_c_sell:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)

        for p in testtest:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
    #####################################################################################################################
    elif trade_all == "buy -> sell -> sell":

        for p in test_op:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)



        for p in quantity_pair_c_raschet_sell:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in quantity_pair_b_raschet_sell:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)

        for p in trade_pair_a_buy:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in trade_pair_b_sell:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in trade_pair_c_sell:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)

        for p in testtest:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
    #####################################################################################################################
    # elif trade_all == "buy -> sell -> buy":
    #     for p in quantity_pair_c_raschet_buy:
    #         with open(all_pairs_btc, 'a') as file3:
    #             file3.write(p)
    #     for p in quantity_pair_b_raschet_sell:
    #         with open(all_pairs_btc, 'a') as file3:
    #             file3.write(p)
    #
    #     for p in trade_pair_a_buy:
    #         with open(all_pairs_btc, 'a') as file3:
    #             file3.write(p)
    #     for p in trade_pair_b_sell:
    #         with open(all_pairs_btc, 'a') as file3:
    #             file3.write(p)
    #     for p in trade_pair_c_buy:
    #         with open(all_pairs_btc, 'a') as file3:
    #             file3.write(p)

    # with open(all_pairs_btc, 'a') as file3:
    #     file3.write(
    #         f"\t\t\tpribil = Decimal(price_c) - Decimal(price_a) \n"
    #         "\n"
    #         f"\t\t\ttime_test = datetime.datetime.now() \n"
    #         f"\t\t\ta = Decimal(price_c) \n"
    #         f"\t\t\tb = Decimal(price_a) \n"
    #         f"\t\t\tc = Decimal((a / b - 1) * 100) \n"
    #         f"\t\t\tcommission_a = Decimal('{commission_a}') \n"
    #         f"\t\t\tcommission_b = Decimal('{commission_b}') \n"
    #         f"\t\t\tcommission_c = Decimal('{commission_c}') \n"
    #         f"\t\t\tcommission_all = Decimal(commission_a) + Decimal(commission_b) + Decimal(commission_c) \n"
    #         # f"\t\t\tcommission_all = commission_all.quantize(Decimal('0.0001')) \n"
    #         f"\t\t\tif c > commission_all: \n"
    #         "\n"
    #         f"\t\t\t\tprint('################################################################################################################', time_test) \n"
    #         f"\t\t\t\tprint('Общая коммисия:', commission_all) \n"
    #         # f"\t\t\t\tprint('Пара_А:', symbol_g_{symbol_a}, '# Покупаем', quantity_pair_b_raschet, '{i['baseAsset_a']}', 'за', price_a, '{i['quoteAsset_a']}', 'по цене', price_asks_g_{symbol_a}) \n"
    #         # f"\t\t\t\tprint('Пара_B:', symbol_g_{symbol_b}, '# Продаем', quantity_pair_b_raschet, '{i['baseAsset_b']}', 'за', price_b, '{i['quoteAsset_b']}', 'по цене', price_bids_g_{symbol_b}) \n"
    #         # f"\t\t\t\tprint('Пара_C:', symbol_g_{symbol_c}, '# Продаем', price_b, '{i['baseAsset_c']}', 'за', price_c, '{i['quoteAsset_c']}', 'по цене', price_bids_g_{symbol_c}) \n"
    #         # f"\t\t\t\tprint('Прибыль:', pribil, 'Прибыль в %:', c, '%') \n"
    #         f"\t\t\t\tprint('Пара_А:', symbol_g_{symbol_a}, '#', '{tr_a}', quantity_pair_a, '{tr_a_pair_a_1}', 'за', price_a, '{tr_a_pair_a_2}', 'по цене', price_{tr_n_a}_g_{symbol_a}) \n"
    #         f"\t\t\t\tprint('Пара_B:', symbol_g_{symbol_b}, '#', '{tr_b}', quantity_pair_b, '{tr_a_pair_b_1}', 'за', price_b, '{tr_a_pair_b_2}', 'по цене', price_{tr_n_b}_g_{symbol_b}) \n"
    #         f"\t\t\t\tprint('Пара_C:', symbol_g_{symbol_c}, '#', '{tr_c}', quantity_pair_c, '{tr_a_pair_c_1}', 'за', price_c, '{tr_a_pair_c_2}', 'по цене', price_{tr_n_c}_g_{symbol_c}) \n"
    #         f"\t\t\t\tprint('Прибыль:', pribil, 'Прибыль в %:', c, '%') \n"
    #         "\n"
    #         f"\t\tlocker.release() \n"
    #         "\n"
    #         f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
    #         "\n"
    #         f"###################################################################### \n"
    #         "\n"
    #     )
