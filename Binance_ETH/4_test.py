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

for check_main_currency in f_file_step_1_pairs_trade():
    if check_main_currency['quoteAsset_a'] != '':
        main_currency = check_main_currency['quoteAsset_a']
        break

########################################################################################################
# Формируем основной файл
########################################################################################################

all_pairs_btc = "Run_BTC_all_main_currency_pairs_2" + ".py"

with open(all_pairs_btc, 'w') as file3:
    file3.write("")

with open(all_pairs_btc, 'a') as file3:
    file3.write(
        "import time \n"
        "import datetime \n"
        "import threading \n"
        "import json \n"
        "import websocket \n"
        "from threading import * \n"
        "from binance.client import Client \n"
        "\n"
        "\n"
        "def f_minqty_size_up(kolichestvo, stepSize): \n"
        "\n"
        "\tdef adjust_to_step(value, step, increase=True): \n"
        "\t\treturn ((int(value * 100000000) - int(value * 100000000) % int( \n"
        "\t\t\tfloat(step) * 100000000)) / 100000000) + (float(step) if increase else 0) \n"
        "\tsell_amount_a = adjust_to_step(kolichestvo, stepSize) \n"
        "\treturn sell_amount_a \n"
        "\n"
        "\n"
        "def f_minqty_size_down(kolichestvo, stepSize): \n"
        "\n"
        "\tdef adjust_to_step(value, step, increase=False): \n"
        "\t\treturn ((int(value * 100000000) - int(value * 100000000) % int( \n"
        "\t\t\tfloat(step) * 100000000)) / 100000000) + (float(step) if increase else 0) \n"
        "\tsell_amount_a = adjust_to_step(kolichestvo, stepSize) \n"
        "\treturn sell_amount_a \n"
        "\n"
        "\n"
        "api_key = 'A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG' \n"
        "secret_key = 'zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA' \n"
        "\n"
        "client = Client(api_key, secret_key) \n"
        "\n"
        "usdt_count = float(input('Укажите количество монет:')) \n"
        "\n"
        "all_pribil = float(0.0) \n"
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
    with open(all_pairs_btc, 'a') as file3:
        file3.write(
            f"symbol_g_{i['symbol_g']} = '{i['symbol_g']}' \n"
            f"price_bids_g_{i['symbol_g']} = float(0.0) \n"
            f"qty_bids_g_{i['symbol_g']} = float(0.0) \n"
            f"price_asks_g_{i['symbol_g']} = float(0.0) \n"
            f"qty_asks_g_{i['symbol_g']} = float(0.0) \n"
            f"stepSize_g_{i['symbol_g']} = '{i['stepSize_g']}' \n"
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
            f"\tprice_bids_g_{i['symbol_g']} = price_bids_c_l_{i['symbol_g']} \n"
            f"\tqty_bids_g_{i['symbol_g']} = qty_bids_c_l_{i['symbol_g']} \n"
            f"\tprice_asks_g_{i['symbol_g']} = price_asks_c_l_{i['symbol_g']} \n"
            f"\tqty_asks_g_{i['symbol_g']} = qty_asks_c_l_{i['symbol_g']} \n"
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

        if i['baseAsset_a'] == i['quoteAsset_b']:
            trade_b_pair = 'buy'

            if i['baseAsset_b'] == i['quoteAsset_c']:
                trade_c_pair = 'buy'
            elif i['baseAsset_b'] == i['baseAsset_c']:
                trade_c_pair = 'sell'
            else:
                print("1 Проверьте пару 'C', в ней отсутствует монета:", i['baseAsset_b'])

        elif i['baseAsset_a'] == i['baseAsset_b']:
            trade_b_pair = 'sell'

            if i['quoteAsset_b'] == i['quoteAsset_c']:
                trade_c_pair = 'buy'
            elif i['quoteAsset_b'] == i['baseAsset_c']:
                trade_c_pair = 'sell'
            else:
                print("2 Проверьте пару 'C', в ней отсутствует монета:", i['quoteAsset_b'])

        else:
            print("Проверьте пару 'Б', в ней отсутствует монета:", i['baseAsseta'])
#####################################################################################################################
    elif i['baseAsset_a'] == main_currency:
        trade_a_pair = 'sell'

        if i['quoteAsset_a'] == i['quoteAsset_b']:
            trade_b_pair = 'buy'

            if i['baseAsset_b'] == i['quoteAsset_c']:
                trade_c_pair = 'buy'
            elif i['baseAsset_b'] == i['baseAsset_c']:
                trade_c_pair = 'sell'
            else:
                print("1 Проверьте пару 'C', в ней отсутствует монета:", i['baseAsset_b'])

        elif i['quoteAsset_a'] == i['baseAsset_b']:
            trade_b_pair = 'sell'

            if i['quoteAsset_b'] == i['quoteAsset_c']:
                trade_c_pair = 'buy'
            elif i['quoteAsset_b'] == i['baseAsset_c']:
                trade_c_pair = 'sell'
            else:
                print("2 Проверьте пару 'C', в ней отсутствует монета:", i['quoteAsset_b'])

        else:
            print("Проверьте пару 'Б', в ней отсутствует монета:", i['quoteAsset'])

    else:
        print("Проверьте пару 'А', в ней отсутствует монета:", main_currency)

#####################################################################################################################
    with open(all_pairs_btc, 'a') as file3:
        file3.write(
            f"def loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade(): \n"
            "\n"
            "\twhile True: \n"
            "\t\ttime.sleep(0.1)\n"
            "\t\tlocker.acquire()\n"
            "\n"
            f"\t\tif price_bids_g_{symbol_a} != 0.0 and qty_bids_g_{symbol_a} != 0.0 and price_asks_g_{symbol_a} != 0.0 and qty_asks_g_{symbol_a} != 0.0 and price_bids_g_{symbol_b} != 0.0 and qty_bids_g_{symbol_b} != 0.0 and price_asks_g_{symbol_b} != 0.0 and qty_asks_g_{symbol_b} != 0.0 and price_bids_g_{symbol_c} != 0.0 and qty_bids_g_{symbol_c} != 0.0 and price_asks_g_{symbol_c} != 0.0 and qty_asks_g_{symbol_c} != 0.0: \n"
            #######################################################################################################################
            "\n"
        )

    if trade_c_pair == 'buy':
        #print("Проверьте пару 1 !!!")
        with open(all_pairs_btc, 'a') as file3:
            file3.write(
                f"\t\t\t# Цепочка: {symbol_a} -> {symbol_b} -> {symbol_c} \n"
                f"\t\t\t# Цепочка: {trade_a_pair} -> {trade_b_pair} -> {trade_c_pair} \n"
                f"\t\t\t# Покупаем {i['baseAsset_c']} продаем {i['quoteAsset_c']} \n"
                f"\t\t\tquantity_pair_c_raschet = usdt_count * float(price_asks_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
                f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\tquantity_pair_c_raschet = float(f_minqty_size_down(quantity_pair_c_raschet, stepSize_g_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
                f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['quoteAsset_c']}' \n"
            )

        if trade_b_pair == 'buy':
            print("Проверьте пару 2 !!!")
            # with open(all_pairs_btc, 'a') as file3:
            #     file3.write(
            #
            #     f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) * float(price_asks_g_{symbol_b})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
            #     f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
            #     f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
            #     f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
            #     f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
            #     "\n"
            #     f"\t\t\tquantity_pair_a_raschet = float(f_minqty_size_down(quantity_pair_b_raschet, stepSize_g_{symbol_a})) \n"
            #     f"\t\t\tquantity_pair_a_raschet = round(quantity_pair_a_raschet, 14) \n"
            #     "\n"
            # )

            if trade_a_pair == 'buy':
                print("Проверьте пару 3 !!!")
                # with open(all_pairs_btc, 'a') as file3:
                #     file3.write(
                #         f"\t\t\tprice_a = float(quantity_pair_a_raschet) * float(price_asks_g_{symbol_a}) \n"
                #         f"\t\t\tprice_a = round(price_a, 14) \n"
                #         f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                #         "\n"
                #         f"\t\t\tprice_b = float(price_asks_g_{symbol_b}) * float(quantity_pair_a_raschet) \n"
                #         f"\t\t\tprice_b = round(price_b, 14) \n"
                #         f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                #         "\n"
                #         f"\t\t\tprice_c = float(price_b) * float(price_asks_g_{symbol_c}) \n"
                #         f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
                #         f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                #         "\n"
                #         f"\t\tlocker.release() \n"
                #         f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
                #         f"\t\t\t ###################################################################### \n"
                #     )
            elif trade_a_pair == 'sell':
                print("Проверьте пару 4 !!!")
                # with open(all_pairs_btc, 'a') as file3:
                #     file3.write(
                #         f"\t\t\tprice_a = float(quantity_pair_a_raschet) / float(price_bids_g_{symbol_a}) \n"
                #         f"\t\t\tprice_a = round(price_a, 14) \n"
                #         f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                #         "\n"
                #         f"\t\t\tprice_b = float(price_asks_g_{symbol_b}) * float(quantity_pair_a_raschet) \n"
                #         f"\t\t\tprice_b = round(price_b, 14) \n"
                #         f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                #         "\n"
                #         f"\t\t\tprice_c = float(price_b) * float(price_asks_g_{symbol_c}) \n"
                #         f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
                #         f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                #         "\n"
                #         f"\t\tlocker.release() \n"
                #         f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
                #         f"\t\t\t ###################################################################### \n"
                #     )

        elif trade_b_pair == 'sell':
            # print("Проверьте пару 5 !!!")
            with open(all_pairs_btc, 'a') as file3:
                file3.write(

                f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) / float(price_bids_g_{symbol_b})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
                "\n"
                f"\t\t\tquantity_pair_a_raschet = float(f_minqty_size_down(quantity_pair_b_raschet, stepSize_g_{symbol_a})) \n"
                f"\t\t\tquantity_pair_a_raschet = round(quantity_pair_a_raschet, 14) \n"
                "\n"
            )

            if trade_a_pair == 'buy':
                # print("Проверьте пару 6 !!!")
                with open(all_pairs_btc, 'a') as file3:
                    file3.write(
                        f"\t\t\tprice_a = float(quantity_pair_a_raschet) * float(price_asks_g_{symbol_a}) \n"
                        f"\t\t\tprice_a = round(price_a, 14) \n"
                        f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                        "\n"
                        f"\t\t\tprice_b = float(price_bids_g_{symbol_b}) / float(quantity_pair_a_raschet) \n"
                        f"\t\t\tprice_b = round(price_b, 14) \n"
                        f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                        "\n"
                        f"\t\t\tprice_c = float(price_b) * float(price_asks_g_{symbol_c}) \n"
                        f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
                        f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                        "\n"
                        f"\t\tlocker.release() \n"
                        f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
                        f"\t\t\t ###################################################################### \n"
                    )
            elif trade_a_pair == 'sell':
                print("Проверьте пару 7 !!!")
                # with open(all_pairs_btc, 'a') as file3:
                #     file3.write(
                #         f"\t\t\tprice_a = float(quantity_pair_a_raschet) / float(price_bids_g_{symbol_a}) \n"
                #         f"\t\t\tprice_a = round(price_a, 14) \n"
                #         f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                #         "\n"
                #         f"\t\t\tprice_b = float(price_bids_g_{symbol_b}) / float(quantity_pair_a_raschet) \n"
                #         f"\t\t\tprice_b = round(price_b, 14) \n"
                #         f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                #         "\n"
                #         f"\t\t\tprice_c = float(price_b) * float(price_asks_g_{symbol_c}) \n"
                #         f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
                #         f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                #         "\n"
                #         f"\t\tlocker.release() \n"
                #         f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
                #         f"\t\t\t ###################################################################### \n"
                #     )

        else:
            print("Не возможно расчитать объем пары 'Б'. В паре 'Б' нет основной монеты ")

#######################################################################################################################
#######################################################################################################################

    elif trade_c_pair == 'sell':
        with open(all_pairs_btc, 'a') as file3:
            file3.write(
                f"\t\t\t# Цепочка: {symbol_a} -> {symbol_b} -> {symbol_c} \n"
                f"\t\t\t# Цепочка: {trade_a_pair} -> {trade_b_pair} -> {trade_c_pair} \n"
                f"\t\t\t# Продаем {i['baseAsset_c']} покупаем {i['quoteAsset_c']} \n"
                f"\t\t\tquantity_pair_c_raschet = usdt_count / float(price_bids_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
                f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\tquantity_pair_c_raschet = float(f_minqty_size_down(quantity_pair_c_raschet, stepSize_g_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
                f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['quoteAsset_c']}' \n"
            )
        if trade_b_pair == 'buy':
            print("Проверьте пару 8 !!!")
            # with open(all_pairs_btc, 'a') as file3:
            #     file3.write(
            #
            #     f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) * float(price_asks_g_{symbol_b})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
            #     f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
            #     f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
            #     f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
            #     f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
            #     "\n"
            #     f"\t\t\tquantity_pair_a_raschet = float(f_minqty_size_down(quantity_pair_b_raschet, stepSize_g_{symbol_a})) \n"
            #     f"\t\t\tquantity_pair_a_raschet = round(quantity_pair_a_raschet, 14) \n"
            #     "\n"
            # )

            if trade_a_pair == 'buy':
                print("Проверьте пару 9 !!!")
                # with open(all_pairs_btc, 'a') as file3:
                #     file3.write(
                #         f"\t\t\tprice_a = float(quantity_pair_a_raschet) * float(price_asks_g_{symbol_a}) \n"
                #         f"\t\t\tprice_a = round(price_a, 14) \n"
                #         f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                #         "\n"
                #         f"\t\t\tprice_b = float(price_asks_g_{symbol_b}) * float(quantity_pair_a_raschet) \n"
                #         f"\t\t\tprice_b = round(price_b, 14) \n"
                #         f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                #         "\n"
                #         f"\t\t\tprice_c = float(price_b) / float(price_bids_g_{symbol_c}) \n"
                #         f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
                #         f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                #         "\n"
                #         f"\t\tlocker.release() \n"
                #         f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
                #         f"\t\t\t ###################################################################### \n"
                #     )
            elif trade_a_pair == 'sell':
                print("Проверьте пару 10 !!!")
                # with open(all_pairs_btc, 'a') as file3:
                #     file3.write(
                #         f"\t\t\tprice_a = float(quantity_pair_a_raschet) / float(price_bids_g_{symbol_a}) \n"
                #         f"\t\t\tprice_a = round(price_a, 14) \n"
                #         f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                #         "\n"
                #         f"\t\t\tprice_b = float(price_asks_g_{symbol_b}) * float(quantity_pair_a_raschet) \n"
                #         f"\t\t\tprice_b = round(price_b, 14) \n"
                #         f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                #         "\n"
                #         f"\t\t\tprice_c = float(price_b) / float(price_bids_g_{symbol_c}) \n"
                #         f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
                #         f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                #         "\n"
                #         f"\t\tlocker.release() \n"
                #         f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
                #         f"\t\t\t ###################################################################### \n"
                #     )
        elif trade_b_pair == 'sell':
            with open(all_pairs_btc, 'a') as file3:
                file3.write(

                f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) / float(price_bids_g_{symbol_b})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
                "\n"
                # f"\t\t\tquantity_pair_a_raschet = float(f_minqty_size_down(quantity_pair_b_raschet, stepSize_g_{symbol_a})) \n"
                # f"\t\t\tquantity_pair_a_raschet = round(quantity_pair_a_raschet, 14) \n"
                # "\n"
            )
            if trade_a_pair == 'buy':
                with open(all_pairs_btc, 'a') as file3:
                    file3.write(
                        f"\t\t\tprice_a = float(quantity_pair_b_raschet) * float(price_asks_g_{symbol_a}) \n"
                        f"\t\t\tprice_a = round(price_a, 14) \n"
                        f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                        "\n"
                        f"\t\t\tprice_b = float(price_bids_g_{symbol_b}) * float(quantity_pair_b_raschet) \n"
                        f"\t\t\tprice_b = round(price_b, 14) \n"
                        f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                        "\n"
                        f"\t\t\tprice_b_size = float(f_minqty_size_down(price_b, stepSize_g_{symbol_c})) \n"
                        f"\t\t\tprice_c = float(price_b_size) / float(price_bids_g_{symbol_c}) \n"
                        # f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
                        f"\t\t\t# price_c = сколько получим '{i['quoteAsset_c']}' \n"
                        "\n"
                         f"\t\t\tpribil = float(price_c) - float(price_a) \n"
                        "\n"
                        f"\t\t\ttime_test = datetime.datetime.now() \n"
                        f"\t\t\ta = float(price_c) \n"
                        f"\t\t\tb = float(price_a) \n"
                        f"\t\t\tc = (a / b - 1) * 100 \n"
                        f"\t\t\tcommission_a = {commission_a} \n"
                        f"\t\t\tcommission_b = {commission_b} \n"
                        f"\t\t\tcommission_c = {commission_c} \n"
                        f"\t\t\tcommission_all = commission_a + commission_b + commission_c \n"
                        f"\t\t\tif c > commission_all: \n"
                        "\n"
                        f"\t\t\t\tprint('################################################################################################################', time_test) \n"
                        f"\t\t\t\tprint('Общая коммисия:', commission_all) \n"
                        f"\t\t\t\tprint('Пара_А:', symbol_g_{symbol_a}, '# Покупаем', quantity_pair_b_raschet, '{i['baseAsset_a']}', 'за', price_a, '{i['quoteAsset_a']}', 'по цене', price_asks_g_{symbol_a}) \n"
                        f"\t\t\t\tprint('Пара_B:', symbol_g_{symbol_b}, '# Продаем', quantity_pair_b_raschet, '{i['baseAsset_b']}', 'за', price_b, '{i['quoteAsset_b']}', 'по цене', price_bids_g_{symbol_b}) \n"
                        f"\t\t\t\tprint('Пара_C:', symbol_g_{symbol_c}, '# Продаем', price_b_size, '{i['baseAsset_c']}', 'за', price_c, '{i['quoteAsset_c']}', 'по цене', price_bids_g_{symbol_c}) \n"
                        f"\t\t\t\tprint('Прибыль:', pribil, 'Прибыль в %:', c, '%') \n"
                        "\n"
                        f"\t\tlocker.release() \n"
                        "\n"
                        f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
                        "\n"
                        f"###################################################################### \n"
                        "\n"
                    )
            elif trade_a_pair == 'sell':
                print("Проверьте пару 11 !!!")
                # with open(all_pairs_btc, 'a') as file3:
                #     file3.write(
                #         f"\t\t\tprice_a = float(quantity_pair_a_raschet) / float(price_bids_g_{symbol_a}) \n"
                #         f"\t\t\tprice_a = round(price_a, 14) \n"
                #         f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                #         "\n"
                #         f"\t\t\tprice_b = float(price_bids_g_{symbol_b}) / float(quantity_pair_a_raschet) \n"
                #         f"\t\t\tprice_b = round(price_b, 14) \n"
                #         f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                #         "\n"
                #         f"\t\t\tprice_c = float(price_b) / float(price_bids_g_{symbol_c}) \n"
                #         f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
                #         f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                #         "\n"
                #         f"\t\tlocker.release() \n"
                #         f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
                #         f"\t\t\t ######################################################################asdasdasd \n"
                #     )
        else:
            print("Не возможно расчитать объем пары 'Б'. В паре 'Б' нет основной монеты ")
    else:
        print("Не возможно расчитать объем пары 'С'. В паре 'С' нет основной монеты ", main_currency)
    # with open(all_pairs_btc, 'a') as file3:
    #     file3.write(
    #         f"\t\t\t# Цепочка: {symbol_a} -> {symbol_b} -> {symbol_c} \n"
    #         f"\t\t\t# Цепочка: {trade_a_pair} -> {trade_b_pair} -> {trade_c_pair} \n"
    #     )
    # print(trade_a_pair, trade_b_pair, trade_c_pair)
    # print(i)


