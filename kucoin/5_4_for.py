# -*- coding: utf8 -*-
import json
import time
from collections import OrderedDict  # модуль для удаления повторения

check_quote_pairs = '../kucoin/1_pairs_buy_para_b_test.json'


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

for_buy_buy_sell = "for_buy_buy_sell" + ".py"

with open(all_pairs_btc, 'w') as file3:
    file3.write("")


with open(for_buy_buy_sell, 'w') as file3:
    file3.write("")

with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
    file3.write(
        "import time \n"
        "import datetime \n"
        "import threading \n"
        "import requests \n"
        "from decimal import Decimal \n"
        "import json \n"
        "import websocket \n"
        "from kucoin.client import Client \n"
        "from threading import * \n"
        "\n"
        "\n"
        "def f_minqty_size_up(kolichestvo, stepSize): \n"
        "\n"
        # "\tsell_amount_a = ((int(kolichestvo * 100000000) - int(kolichestvo * 100000000) % (stepSize * 100000000)) / 100000000) + stepSize \n"
        "\tsell_amount_a = Decimal(kolichestvo) + Decimal(stepSize) \n"
        "\treturn sell_amount_a \n"
        "\n"
        "\n"
        "def f_minqty_size_down(kolichestvo, stepSize): \n"
        "\n"
        "\tsell_amount_a = ((int(kolichestvo * 100000000000000) - int(kolichestvo * 100000000000000) % (stepSize * 100000000000000)) / 100000000000000) \n"
        "\treturn sell_amount_a \n"
        "\n"
        "\n"
        "api_key = '63cc9d027675230001bba629' \n"
        "api_secret = '0e8444e7-0594-4a57-a058-92d34decd0d7' \n"
        "\n"
        "client = Client(api_key, api_secret, passphrase='4796212') \n"
        "\n"
        "usdt_count = Decimal(input('Укажите количество монет:')) \n"
        "\n"
        "all_pribil = Decimal('0.0') \n"
        "\n"
        "locker = threading.RLock() \n"
    )

########################################################################################################
# Проверяем пары 'a','b' и 'c' в файле 'f_file_step_1_pairs_trade' и если в этих парах 'baseCurrency' и 'quoteCurrency' равно 'main_pairs', добавляем пару в переменную 'all_main_currency_pairs'
########################################################################################################

all_main_currency_pairs = []  # Список пар в которых 'baseCurrency' и 'quoteCurrency' равно 'main_pairs'
count_pairs_a = 0

all_pairs = []

for i in f_file_step_1_pairs_trade():
    if count_pairs_a == 0:
        symbol_original = (i['symbol_a_original'])
        symbol = (i['symbol_a'])
        baseCurrency = (i['baseCurrency_a'])
        quoteCurrency = (i['quoteCurrency_a'])
        stepSize_base = (i['stepSize_base_a'])
        stepSize_quote = (i['stepSize_quote_a'])
        commission = (i['commission_a'])
        all_pairs.append(
            {
                'symbol_original_g': symbol_original,
                'symbol_g': symbol,
                'baseCurrency_g': baseCurrency,
                'quoteCurrency_g': quoteCurrency,
                'stepSize_base_g': stepSize_base,
                'stepSize_quote_g': stepSize_quote,
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
        symbol_original = (i['symbol_a_original'])
        symbol = (i['symbol_a'])
        baseCurrency = (i['baseCurrency_a'])
        quoteCurrency = (i['quoteCurrency_a'])
        stepSize_base = (i['stepSize_base_a'])
        stepSize_quote = (i['stepSize_quote_a'])
        commission = (i['commission_a'])
        all_pairs.append(
            {
                'symbol_original_g': symbol_original,
                'symbol_g': symbol,
                'baseCurrency_g': baseCurrency,
                'quoteCurrency_g': quoteCurrency,
                'stepSize_base_g': stepSize_base,
                'stepSize_quote_g': stepSize_quote,
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
        symbol_original = (i['symbol_b_original'])
        symbol = (i['symbol_b'])
        baseCurrency = (i['baseCurrency_b'])
        quoteCurrency = (i['quoteCurrency_b'])
        stepSize_base = (i['stepSize_base_b'])
        stepSize_quote = (i['stepSize_quote_b'])
        commission = (i['commission_b'])
        all_pairs.append(
            {
                'symbol_original_g': symbol_original,
                'symbol_g': symbol,
                'baseCurrency_g': baseCurrency,
                'quoteCurrency_g': quoteCurrency,
                'stepSize_base_g': stepSize_base,
                'stepSize_quote_g': stepSize_quote,
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
        symbol_original = (i['symbol_c_original'])
        symbol = (i['symbol_c'])
        baseCurrency = (i['baseCurrency_c'])
        quoteCurrency = (i['quoteCurrency_c'])
        stepSize_base = (i['stepSize_base_c'])
        stepSize_quote = (i['stepSize_quote_c'])
        commission = (i['commission_c'])
        all_pairs.append(
            {
                'symbol_original_g': symbol_original,
                'symbol_g': symbol,
                'baseCurrency_g': baseCurrency,
                'quoteCurrency_g': quoteCurrency,
                'stepSize_base_g': stepSize_base,
                'stepSize_quote_g': stepSize_quote,
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
            # f"symbol_original_g_{i['symbol_g']} = '{i['symbol_original_g']}' \n"
            f"symbol_g_{i['symbol_g']} = '{i['symbol_g']}' \n"
            f"price_bids_g_{i['symbol_g']} = Decimal('0.0') \n"
            f"qty_bids_g_{i['symbol_g']} = Decimal('0.0') \n"
            f"price_asks_g_{i['symbol_g']} = Decimal('0.0') \n"
            f"qty_asks_g_{i['symbol_g']} = Decimal('0.0') \n"
            f"stepSize_base_g_{i['symbol_g']} = Decimal('{i['stepSize_base_g']}') \n"
            f"stepSize_quote_g_{i['symbol_g']} = Decimal('{i['stepSize_quote_g']}') \n"
            "\n"

        )

for i in f_file_step_1_pairs_trade():

    symbol_a = i['symbol_a']
    symbol_a_original = i['symbol_a_original']
    symbol_aa = symbol_a.lower()
    stepSize_base_a = i['stepSize_base_a']
    stepSize_quote_a = i['stepSize_quote_a']
    commission_a = i['commission_a']
    symbol_b = i['symbol_b']
    symbol_b_original = i['symbol_b_original']
    symbol_bb = symbol_b.lower()
    stepSize_base_b = i['stepSize_base_b']
    stepSize_quote_b = i['stepSize_quote_b']
    commission_b = i['commission_b']

    symbol_c = i['symbol_c']
    symbol_c_original = i['symbol_c_original']
    symbol_cc = symbol_c.lower()
    stepSize_base_c = i['stepSize_base_c']
    stepSize_quote_c = i['stepSize_quote_c']
    commission_c = i['commission_c']

    if i['quoteCurrency_a'] == main_currency:
        trade_a_pair = 'buy'
        tr_a_pair_a_1 = i['baseCurrency_a']
        tr_a_pair_a_2 = main_currency
        tr_n_a = 'asks'

        if i['baseCurrency_a'] == i['quoteCurrency_b']:
            trade_b_pair = 'buy'
            tr_n_b = 'asks'
            tr_a_pair_b_1 = i['baseCurrency_b']
            tr_a_pair_b_2 = i['quoteCurrency_b']

            if i['baseCurrency_b'] == i['quoteCurrency_c']:
                trade_c_pair = 'buy'
                tr_n_c = 'asks'
                trade_all = 'buy -> buy -> buy'
                tr_a = 'Покупаем'
                tr_b = 'Покупаем'
                tr_c = 'Покупаем'
                tr_a_side = ''
                tr_b_side = ''
                tr_c_side = ''

            elif i['baseCurrency_b'] == i['baseCurrency_c']:
                trade_c_pair = 'sell'
                tr_a_pair_c_1 = i['baseCurrency_c']
                tr_a_pair_c_2 = i['quoteCurrency_c']
                tr_n_c = 'bids'
                trade_all = 'buy -> buy -> sell'
                tr_a = 'Покупаем'
                tr_b = 'Покупаем'
                tr_c = 'Продаем'
                tr_a_side = 'buy'
                tr_b_side = 'buy'
                tr_c_side = 'sell'
                with open(for_buy_buy_sell, 'a') as file3:
                    file3.write(f'tr_a_pair_c_1 = {tr_a_pair_c_1}')

            else:
                print("1 Проверьте пару 'C', в ней отсутствует монета:", i['baseCurrency_b'])

        elif i['baseCurrency_a'] == i['baseCurrency_b']:
            trade_b_pair = 'sell'
            tr_n_b = 'bids'
            tr_a_pair_b_1 = i['baseCurrency_b']
            tr_a_pair_b_2 = i['quoteCurrency_b']

            if i['quoteCurrency_b'] == i['quoteCurrency_c']:
                trade_c_pair = 'buy'
                tr_n_c = 'asks'
                trade_all = 'buy -> sell -> buy'
                tr_a = 'Покупаем'
                tr_b = 'Продаем'
                tr_c = 'Покупаем'
                tr_a_pair_c_1 = i['baseCurrency_c']
                tr_a_pair_c_2 = i['quoteCurrency_c']
                tr_a_side = ''
                tr_b_side = ''
                tr_c_side = ''

            elif i['quoteCurrency_b'] == i['baseCurrency_c']:
                trade_c_pair = 'sell'
                tr_n_c = 'bids'
                trade_all = 'buy -> sell -> sell'
                tr_a = 'Покупаем'
                tr_b = 'Продаем'
                tr_c = 'Продаем'
                tr_a_pair_c_1 = i['baseCurrency_c']
                tr_a_pair_c_2 = i['quoteCurrency_c']
                tr_a_side = 'buy'
                tr_b_side = 'sell'
                tr_c_side = 'sell'
            else:
                print("2 Проверьте пару 'C', в ней отсутствует монета:", i['quoteCurrency_b'])

        else:
            print("Проверьте пару 'Б', в ней отсутствует монета:", i['baseCurrency'])
    #####################################################################################################################
    elif i['baseCurrency_a'] == main_currency:
        trade_a_pair = 'sell'
        tr_n_a = 'bids'
        tr_a_pair_a_1 = main_currency
        tr_a_pair_a_2 = i['quoteCurrency_a']

        if i['quoteCurrency_a'] == i['quoteCurrency_b']:
            trade_b_pair = 'buy'
            tr_n_b = 'asks'

            if i['baseCurrency_b'] == i['quoteCurrency_c']:
                trade_c_pair = 'buy'
                tr_n_c = 'asks'
                trade_all = 'sell -> buy -> buy'
                tr_a = 'Продаем'
                tr_b = 'Покупаем'
                tr_c = 'Покупаем'
                tr_a_side = ''
                tr_b_side = ''
                tr_c_side = ''

            elif i['baseCurrency_b'] == i['baseCurrency_c']:
                trade_c_pair = 'sell'
                tr_n_c = 'bids'
                trade_all = 'sell -> buy -> sell'
                tr_a = 'Продаем'
                tr_b = 'Покупаем'
                tr_c = 'Продаем'
                tr_a_side = ''
                tr_b_side = ''
                tr_c_side = ''
            else:
                print("1 Проверьте пару 'C', в ней отсутствует монета:", i['baseCurrency_b'])

        elif i['quoteCurrency_a'] == i['baseCurrency_b']:
            trade_b_pair = 'sell'
            tr_n_b = 'bids'

            if i['quoteCurrency_b'] == i['quoteCurrency_c']:
                trade_c_pair = 'buy'
                tr_n_c = 'asks'
                trade_all = 'sell -> sell -> buy'
                tr_a = 'Продаем'
                tr_b = 'Продаем'
                tr_c = 'Покупаем'
                tr_a_side = ''
                tr_b_side = ''
                tr_c_side = ''

            elif i['quoteCurrency_b'] == i['baseCurrency_c']:
                trade_c_pair = 'sell'
                tr_n_c = 'bids'
                trade_all = 'sell -> sell -> sell'
                tr_a = 'Продаем'
                tr_b = 'Продаем'
                tr_c = 'Продаем'
                tr_a_side = ''
                tr_b_side = ''
                tr_c_side = ''

            else:
                print("2 Проверьте пару 'C', в ней отсутствует монета:", i['quoteCurrency_b'])

        else:
            print("Проверьте пару 'Б', в ней отсутствует монета:", i['quoteCurrency'])

    else:
        print("Проверьте пару 'А', в ней отсутствует монета:", main_currency)
#####################################################################################################################
#####################################################################################################################
    quantity_pair_c_raschet_buy = [
        f"\t\t\tquantity_pair_c_raschet = Decimal(usdt_count) * Decimal(price_asks_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
        f"\t\t\tquantity_pair_c_raschet = Decimal(f_minqty_size_down(quantity_pair_c_raschet, stepSize_g_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
        f"\t\t\t# quantity_pair_c_raschet = количество '{i['quoteCurrency_c']}' \n"
        ]
    quantity_pair_c_raschet_sell = [
        f"\t\t\tquantity_pair_c_raschet = Decimal(usdt_count) / Decimal(price_bids_g_{symbol_c}) \n"
        f"\t\t\tquantity_pair_c_raschet = Decimal(f_minqty_size_down(quantity_pair_c_raschet, stepSize_base_g_{symbol_c})) \n"
        f"\t\t\ttest3 = quantity_pair_c_raschet \n"
    ]
    #####################################################################################################################
    quantity_pair_b_raschet_buy = [
        f"\t\t\tfloat_qty_bids_g_{symbol_c} = float(qty_bids_g_{symbol_c}) \n"
        f"\t\t\tif float_qty_bids_g_{symbol_c} > test3: \n"
        f"\t\t\t\tdd = Decimal(f_minqty_size_down(test3, stepSize_base_g_{symbol_b})) \n"
        f"\t\t\t\twhile dd < test3: \n"
        f"\t\t\t\t\tdd = (f_minqty_size_up(dd, stepSize_base_g_{symbol_b})) \n"
        f"\t\t\t\ttest3 = dd \n"
        f"\t\t\t\tquantity_pair_b_raschet = Decimal(test3) * Decimal(price_asks_g_{symbol_b}) \n"
        f"\t\t\t\ttest2 = quantity_pair_b_raschet \n"
        f"\t\t\t\tfloat_qty_asks_g_{symbol_b} = float(qty_asks_g_{symbol_b}) \n"
        f"\t\t\t\tif float_qty_asks_g_{symbol_b} > test3: \n"
        "\n"
        f"\t\t\t\t\tddd = Decimal(f_minqty_size_down(test2, stepSize_base_g_{symbol_a})) \n"
        f"\t\t\t\t\twhile ddd < test2: \n"
        f"\t\t\t\t\t\tddd = Decimal(f_minqty_size_up(ddd, stepSize_base_g_{symbol_a})) \n"
        f"\t\t\t\t\ttest2 = ddd \n"
        "\n"
        f"\t\t\t\t\ttest1 = ddd \n"
        f"\t\t\t\t\tfloat_qty_asks_g_{symbol_a} = float(qty_asks_g_{symbol_a}) \n"
        f"\t\t\t\t\tif float_qty_asks_g_{symbol_a} > test1:\n"
        f"\t\t\t\t\t\tquantity_pair_a = test1 \n"
        f"\t\t\t\t\t\tquantity_pair_b = test3 \n"
        f"\t\t\t\t\t\tquantity_pair_c = test3 \n"
    ]
    quantity_pair_b_raschet_sell = [
        f"\t\t\tfloat_qty_bids_g_{symbol_c} = float(qty_bids_g_{symbol_c}) \n"
        f"\t\t\tif float_qty_bids_g_{symbol_c} > test3: \n"
        f"\t\t\t\tquantity_pair_b_raschet = Decimal(test3) / Decimal(price_bids_g_{symbol_b}) \n"
        f"\t\t\t\tff = Decimal(f_minqty_size_down(quantity_pair_b_raschet, stepSize_base_g_{symbol_b})) \n"
        f"\t\t\t\twhile ff < quantity_pair_b_raschet: \n"
        f"\t\t\t\t\tff = Decimal(f_minqty_size_up(ff, stepSize_base_g_{symbol_b})) \n"
        f"\t\t\t\ttest2 = ff \n"
        f"\t\t\t\tfloat_qty_bids_g_{symbol_b} = float(qty_bids_g_{symbol_b}) \n"
        f"\t\t\t\tif float_qty_bids_g_{symbol_b} > test2: \n"
        f"\t\t\t\t\tfff = Decimal(f_minqty_size_down(test2, stepSize_base_g_{symbol_a})) \n"
        f"\t\t\t\t\twhile fff < test2: \n"
        f"\t\t\t\t\t\tfff = Decimal(f_minqty_size_up(fff, stepSize_base_g_{symbol_a})) \n"
        f"\t\t\t\t\ttest1 = fff \n"
        f"\t\t\t\t\tfloat_qty_asks_g_{symbol_a} = float(qty_asks_g_{symbol_a}) \n"
        f"\t\t\t\t\tif float_qty_asks_g_{symbol_a} > test1: \n"
        # 
        # f"\t\t\tquantity_pair_b_raschet = Decimal(test3) / Decimal(price_bids_g_{symbol_b}) \n"
        # f"\t\t\ttest2 = Decimal(f_minqty_size_down(quantity_pair_b_raschet, stepSize_g_{symbol_b})) \n"
        # f"\t\t\twhile test2 < quantity_pair_b_raschet: \n"
        # f"\t\t\t\ttest2 = Decimal(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b})) \n"
        # f"\t\t\ttest1 = Decimal(f_minqty_size_down(test2, stepSize_g_{symbol_a})) \n"
        # f"\t\t\twhile test1 < test2: \n"
        # f"\t\t\t\ttest1 = Decimal(f_minqty_size_up(test1, stepSize_g_{symbol_a})) \n"
        f"\t\t\t\t\t\tquantity_pair_a = test1 \n"
        f"\t\t\t\t\t\tquantity_pair_b = test2 \n"
        f"\t\t\t\t\t\tquantity_pair_c = test3 \n"
    ]
    #####################################################################################################################
    trade_pair_a_buy = [
        f"\t\t\t\t\t\tprice_a = Decimal(quantity_pair_a) * Decimal(price_asks_g_{symbol_a}) \n"
    ]
    trade_pair_a_sell = [
        f"\t\t\t\t\t\tprice_a = Decimal(quantity_pair_b_raschet) / Decimal(price_bids_g_{symbol_a}) \n"
        f"\t\t\t\t\t\t# price_a = сколько потребуется '{i['baseCurrency_a']}' \n"
    ]
    #####################################################################################################################
    trade_pair_b_buy = [
        f"\t\t\t\t\t\tprice_b = Decimal(quantity_pair_b) * Decimal(price_asks_g_{symbol_b}) \n"
    ]
    trade_pair_b_sell = [
        f"\t\t\t\t\t\tprice_b = Decimal(quantity_pair_b) * Decimal(price_bids_g_{symbol_b}) \n"
    ]
    #####################################################################################################################
    trade_pair_c_buy = [
        f"\t\t\t\t\t\tprice_c = Decimal(price_b) * Decimal(price_asks_g_{symbol_c}) \n"
        f"\t\t\t# price_c = сколько получим '{i['baseCurrency_c']}' \n"
    ]
    trade_pair_c_sell = [
        f"\t\t\t\t\t\tprice_c = Decimal(quantity_pair_c) * Decimal(price_bids_g_{symbol_c}) \n"
    ]
    #####################################################################################################################

    test_op = [
        "\n"
        "\n"
        f"def loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade(): \n"
        "\n"
        "\twhile True: \n"
        "\t\ttime.sleep(0.1)\n"
        #"\t\tlocker.acquire()\n"
        "\n"
        f"\t\tif price_bids_g_{symbol_a} != 0.0 and qty_bids_g_{symbol_a} != 0.0 and price_asks_g_{symbol_a} != 0.0 and qty_asks_g_{symbol_a} != 0.0 and price_bids_g_{symbol_b} != 0.0 and qty_bids_g_{symbol_b} != 0.0 and price_asks_g_{symbol_b} != 0.0 and qty_asks_g_{symbol_b} != 0.0 and price_bids_g_{symbol_c} != 0.0 and qty_bids_g_{symbol_c} != 0.0 and price_asks_g_{symbol_c} != 0.0 and qty_asks_g_{symbol_c} != 0.0: \n"
        #######################################################################################################################
        "\n"
    ]
    test_bribil = [
        f"\t\t\t\t\t\tpribil = Decimal(price_c) - Decimal(price_a) \n"
        "\n"
        f"\t\t\t\t\t\ttime_test = datetime.datetime.now() \n"
        f"\t\t\t\t\t\ta = Decimal(price_c) \n"
        f"\t\t\t\t\t\tb = Decimal(price_a) \n"
        f"\t\t\t\t\t\tc = Decimal((a / b - 1) * 100) \n"
        f"\t\t\t\t\t\tcommission_a = Decimal('{commission_a}') \n"
        f"\t\t\t\t\t\tcommission_b = Decimal('{commission_b}') \n"
        f"\t\t\t\t\t\tcommission_c = Decimal('{commission_c}') \n"
        f"\t\t\t\t\t\tcommission_all = Decimal(commission_a) + Decimal(commission_b) + Decimal(commission_c) \n"
        f"\t\t\t\t\t\tif c > commission_all: \n"
    ]
    trade_buy_buy_sell = [
        # f"\t\t\t\t\t\t\torder_a = client.create_market_order(symbol='{symbol_a_original}', side='{tr_a_side}', size=str(quantity_pair_a)) \n"
        # f"\t\t\t\t\t\t\torder_b_Id = '' \n"
        # f"\t\t\t\t\t\t\torder_b = client.create_market_order(symbol='{symbol_b_original}', side='{tr_b_side}', size=str(quantity_pair_b)) \n"
        # f"\t\t\t\t\t\t\torder_b_Id = order_b['orderId'] \n"
        # f"\t\t\t\t\t\t\ttry: \n"
        # f"\t\t\t\t\t\t\t\torder_c = client.create_market_order(symbol='{symbol_c_original}', side='{tr_c_side}', size=str(quantity_pair_c)) \n"
        # f"\t\t\t\t\t\t\texcept: \n"
        # f"\t\t\t\t\t\t\t\tfills_totalNum = 0 \n"
        # f"\t\t\t\t\t\t\t\twhile fills_totalNum == 0: \n"
        # f"\t\t\t\t\t\t\t\t\ttime.sleep(0.1) \n"
        # f"\t\t\t\t\t\t\t\t\tfills = client.get_fills(order_id=order_b_Id) \n"
        # f"\t\t\t\t\t\t\t\t\tfills_totalNum = fills['totalNum'] \n"
        # f"\t\t\t\t\t\t\t\tdeposits = client.get_accounts(currency='{tr_a_pair_c_1}') \n"
        # f"\t\t\t\t\t\t\t\titog = Decimal(deposits[0]['balance']) \n"
        # f"\t\t\t\t\t\t\t\tff = Decimal(f_minqty_size_down(itog, stepSize_base_g_{symbol_c})) \n"
        # f"\t\t\t\t\t\t\t\torder_c = client.create_market_order(symbol='{symbol_c_original}', side='{tr_c_side}', size=str(ff)) \n"
        f"\t\t\t\t\t\t\tlocker.release() \n"




        # f"\t\t\t\t\t\t\t\titog = Decimal(fills['items'][0]['size']) \n"
        # f"\t\t\t\t\t\t\t\tprint(itog) \n"
        # f"\t\t\t\t\t\t\t\tprint(fills) \n"
        # f"\t\t\t\t\t\t\t\tff = Decimal(f_minqty_size_down(itog, stepSize_base_g_{symbol_c})) \n"
        # f"\t\t\t\t\t\t\t\tprint(ff) \n"
        # f"\t\t\t\t\t\t\t\torder_c = client.create_market_order(symbol='{symbol_c_original}', side='{tr_c_side}', size=str(ff)) \n"
        # f"\t\t\t\t\t\t\tlocker.release() \n"
    ]
    trade_buy_sell_sell = [
        # f"\t\t\t\t\t\t\torder_a = client.create_market_order(symbol='{symbol_a_original}', side='{tr_a_side}', size=str(quantity_pair_a)) \n"
        # f"\t\t\t\t\t\t\torder_b_Id = '' \n"
        # f"\t\t\t\t\t\t\torder_b = client.create_market_order(symbol='{symbol_b_original}', side='{tr_b_side}', size=str(quantity_pair_b)) \n"
        # f"\t\t\t\t\t\t\torder_b_Id = order_b['orderId'] \n"
        # f"\t\t\t\t\t\t\ttry: \n"
        # f"\t\t\t\t\t\t\t\torder_c = client.create_market_order(symbol='{symbol_c_original}', side='{tr_c_side}', size=str(quantity_pair_c)) \n"
        # f"\t\t\t\t\t\t\texcept: \n"
        # f"\t\t\t\t\t\t\t\tfills_totalNum = 0 \n"
        # f"\t\t\t\t\t\t\t\twhile fills_totalNum == 0: \n"
        # f"\t\t\t\t\t\t\t\t\ttime.sleep(0.1) \n"
        # f"\t\t\t\t\t\t\t\t\tfills = client.get_fills(order_id=order_b_Id) \n"
        # f"\t\t\t\t\t\t\t\t\tfills_totalNum = fills['totalNum'] \n"
        # f"\t\t\t\t\t\t\t\tdeposits = client.get_accounts(currency='{tr_a_pair_c_1}') \n"
        # f"\t\t\t\t\t\t\t\titog = Decimal(deposits[0]['balance']) \n"
        # f"\t\t\t\t\t\t\t\tff = Decimal(f_minqty_size_down(itog, stepSize_base_g_{symbol_c})) \n"
        # f"\t\t\t\t\t\t\t\torder_c = client.create_market_order(symbol='{symbol_c_original}', side='{tr_c_side}', size=str(ff)) \n"
        f"\t\t\t\t\t\t\tlocker.release() \n"
    ]
    test_buy = [
        "\n"
        "\t\t\t\tlocker.acquire()\n"
        f"\t\t\t\ta = client.order_market_buy( \n"
            f"\t\t\t\t\tsymbol='{symbol_a}', \n"
            f"\t\t\t\t\tquantity=float(quantity_pair_a) \n"
        f"\t\t\t\t) \n"
        f"\t\t\t\tb = client.order_market_sell( \n"
            f"\t\t\t\t\tsymbol='{symbol_b}', \n"
            f"\t\t\t\t\tquantity=float(quantity_pair_b) \n"
        f"\t\t\t\t) \n"
        f"\t\t\t\tc = client.order_market_sell( \n"
            f"\t\t\t\t\tsymbol='{symbol_c}', \n"
            f"\t\t\t\t\tquantity=float(quantity_pair_c) \n"
        f"\t\t\t\t) \n"
    ]
    testtest = [

        # f"\t\t\t\tprint_all = print_itog(time_test, commission_all, quantity_pair_a, quantity_pair_b, quantity_pair_c, price_a, price_b, price_c, pribil, c) \n"
        # f"\t\t\t\tprint(print_all) \n"
        #"\n"
        "\t\t\t\t\t\t\tlocker.acquire()\n"
        f"\t\t\t\t\t\t\tprint('################################################################################################################') \n"
        f"\t\t\t\t\t\t\tprint(time_test) \n"
        f"\t\t\t\t\t\t\tprint('Общая коммисия:', commission_all) \n"
        f"\t\t\t\t\t\t\tprint('Пара_А:', symbol_g_{symbol_a}, '#', '{tr_a}', quantity_pair_a, '{tr_a_pair_a_1}', 'за', price_a, '{tr_a_pair_a_2}', 'по цене', price_{tr_n_a}_g_{symbol_a}) \n"
        f"\t\t\t\t\t\t\tprint('Пара_B:', symbol_g_{symbol_b}, '#', '{tr_b}', quantity_pair_b, '{tr_a_pair_b_1}', 'за', price_b, '{tr_a_pair_b_2}', 'по цене', price_{tr_n_b}_g_{symbol_b}) \n"
        f"\t\t\t\t\t\t\tprint('Пара_C:', symbol_g_{symbol_c}, '#', '{tr_c}', quantity_pair_c, '{tr_a_pair_c_1}', 'за', price_c, '{tr_a_pair_c_2}', 'по цене', price_{tr_n_c}_g_{symbol_c}) \n"
        f"\t\t\t\t\t\t\tprint('Прибыль:', pribil, 'Прибыль в %:', c, '%') \n"
        # f"\treturn a \n"
        # f"\t\t\t\t\t\t\t{tr_a_side} \n"
        # f"\t\t\t\t\t\t\t{tr_b_side} \n"
        # f"\t\t\t\t\t\t\tasdasd= '{tr_c_side}' \n"
        f"\t\t\t\t\t\t\ttime.sleep(1.0) \n"
        # f"\t\t\t\t\t\t\tlocker.release() \n"
        
        # f"###################################################################### \n"
    ]
    fff = [
        "def get_ticker_all(ws, message): \n"
    ]
    # opa_nihuya = [
    #     tr_a_pair_c_1 = i['baseCurrency_c'],
    #     tr_a_pair_c_2 = i['quoteCurrency_c']
    # ]
    # get_ticker_all = [
    #     "\n"
    #     f"count_message = 0 \n"
    #     f"start_time = time.time() \n"
    #     "\n"
    #     "\n"
    #     f"def get_ticker_all(ws, message): \n"
    #     "\n"
    #     f"\tglobal pingInterval, pingTime, id_channel, count_message, start_time \n"
    #     f"\tdata = json.loads(message) \n"
    #     "\n"
    #     f"\tif 'type' in data: \n"
    #     f"\t\tif data['type'] == 'welcome': \n"
    #     "\t\t\tid_channel = data['id'] \n"
    #     "\t\t\tws.send(json.dumps({'id': data['id'],'type': 'subscribe','topic': '/market/ticker:all','response': 'true'})) \n"
    #     f"\t\telif data['type'] == 'message': \n"
    #     f"\t\t\tcount_message += 1 \n"
    #     "\n"
    #     f"\t\t\tsymbol = data['subject'] \n"
    #     f"\t\t\tprice_bids_g = data['data']['bestBid'] \n"
    #     f"\t\t\tqty_bids_g = data['data']['bestBidSize'] \n"
    #     f"\t\t\tprice_asks_g = data['data']['bestAsk'] \n"
    #     f"\t\t\tqty_asks_g = data['data']['bestAskSize'] \n"
    #     "\n"
    #     f"\t\t\tchars = '.-!' \n"
    #     f"\t\t\tsymbol = symbol.translate(str.maketrans('', '', chars)) \n"
    #     f"\t\t\ttry: \n"
    #     "\t\t\t\tprice_bids_g_ = 'price_bids_g_' + symbol \n"
    #     "\t\t\t\tglobals()[price_bids_g_] = price_bids_g \n"
    #     "\n"
    #     "\t\t\t\tqty_bids_g_ = 'qty_bids_g_' + symbol \n"
    #     "\t\t\t\tglobals()[qty_bids_g_] = qty_bids_g \n"
    #     "\n"
    #     "\t\t\t\tprice_asks_g_ = 'price_asks_g_' + symbol \n"
    #     "\t\t\t\tglobals()[price_asks_g_] = price_asks_g \n"
    #     "\n"
    #     "\t\t\t\tqty_asks_g_ = 'qty_asks_g_' + symbol \n"
    #     "\t\t\t\tglobals()[qty_asks_g_] = qty_asks_g \n"
    #     f"\t\t\texcept: \n"
    #     "\t\t\t\tpass \n"
    #     f"\t\telse: \n"
    #     f"\t\t\tprint(data) \n"
    #     f"\telse: \n"
    #     f"\t\tprint(data) \n"
    #     "\n"
    #     f"\tif (pingTime + pingInterval) <= round(time.time()): \n"
    #     "\t\tws.send(json.dumps({'id':id_channel, 'type':'ping'})) \n"
    #     f"\t\tpingTime = round(time.time())  # Запомним новое время для сообщения \n"
    #     f"\t\tcount_message = 0  # Обнуляем счетчик сообщений \n"
    #     f"\t\tstart_time = time.time()  # Сбросим счетчик времени \n"
    #     "\n"
    #     f"def on_close(ws): \n"
    #     f"\tprint(message) \n"
    #     "\n"
    #     f"def loadSetting(): \n"
    #     f"\treturn requests.post('https://api.kucoin.com/api/v1/bullet-public').json() \n"
    #     "\n"
    #     f"settings = loadSetting() \n"
    #     f"pingInterval = round((settings['data']['instanceServers'][0]['pingInterval'] / 1000) / 2) - 1 \n"
    #     f"pingTime = round(time.time()) \n"
    #     f"id_channel = '' \n"
    #     "\n"
    #     "ws = websocket.WebSocketApp(f'{settings['data']['instanceServers'][0]['endpoint']}?token={settings['data']['token']}',on_message=get_ticker_all,on_close=on_close,on_error=on_error) \n"
    #     f"ws.run_forever() \n"
    # ]
    # with open(all_pairs_btc, 'a') as file3:
    #     file3.write(
    #         "\n"
    #         "\n"
    #         "def print_itog(time_test, commission_all, quantity_pair_a, quantity_pair_b, quantity_pair_c, price_a, price_b, price_c, pribil, c): \n"
    #         # "\tlocker.acquire()\n"
    #         f"\ta = '################################################################################################################' \n"
    #         f"\tprint(time_test) \n"
    #         f"\tprint('Общая коммисия:', commission_all) \n"
    #         f"\tprint('Пара_А:', symbol_g_{symbol_a}, '#', '{tr_a}', quantity_pair_a, '{tr_a_pair_a_1}', 'за', price_a, '{tr_a_pair_a_2}', 'по цене', price_{tr_n_a}_g_{symbol_a}) \n"
    #         f"\tprint('Пара_B:', symbol_g_{symbol_b}, '#', '{tr_b}', quantity_pair_b, '{tr_a_pair_b_1}', 'за', price_b, '{tr_a_pair_b_2}', 'по цене', price_{tr_n_b}_g_{symbol_b}) \n"
    #         f"\tprint('Пара_C:', symbol_g_{symbol_c}, '#', '{tr_c}', quantity_pair_c, '{tr_a_pair_c_1}', 'за', price_c, '{tr_a_pair_c_2}', 'по цене', price_{tr_n_c}_g_{symbol_c}) \n"
    #         f"\tprint('Прибыль:', pribil, 'Прибыль в %:', c, '%') \n"
    #         f"\treturn a \n"
    #         # f"\ttime.sleep(1.0) \n"
    #         # f"\tlocker.release() \n"
    # )
    end_def = [
        "\n"
        "\n"
        f"Thread(target=loop_{symbol_a}_{symbol_b}_{symbol_c}_Trade).start() \n"
    ]
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

        for p in test_bribil:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in testtest:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in trade_buy_buy_sell:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in end_def:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
    #####################################################################################################################
    if trade_all == "buy -> sell -> sell":

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



        for p in test_bribil:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        # for p in test_buy:
        #     with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
        #         file3.write(p)
        for p in testtest:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in trade_buy_sell_sell:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)
        for p in end_def:
            with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
                file3.write(p)

with open(all_pairs_btc, 'a', encoding="cp1251") as file3:
        file3.write(
            "\n"
            f"count_message = 0 \n"
            f"start_time = time.time() \n"
            "\n"
            "\n"
            f"def get_ticker_all(ws, message): \n"
            "\n"
            f"\tglobal pingInterval, pingTime, id_channel, count_message, start_time \n"
            f"\tdata = json.loads(message) \n"
            "\n"
            f"\tif 'type' in data: \n"
            f"\t\tif data['type'] == 'welcome': \n"
            "\t\t\tid_channel = data['id'] \n"
            "\t\t\tws.send(json.dumps({'id': data['id'], 'type': 'subscribe', 'topic': '/market/ticker:all', 'response': 'true'})) \n"
            f"\t\telif data['type'] == 'message': \n"
            f"\t\t\tcount_message += 1 \n"
            "\n"
            f"\t\t\tsymbol = data['subject'] \n"
            f"\t\t\tprice_bids_g = data['data']['bestBid'] \n"
            f"\t\t\tqty_bids_g = data['data']['bestBidSize'] \n"
            f"\t\t\tprice_asks_g = data['data']['bestAsk'] \n"
            f"\t\t\tqty_asks_g = data['data']['bestAskSize'] \n"
            "\n"
            f"\t\t\tchars = '.-!' \n"
            f"\t\t\tsymbol = symbol.translate(str.maketrans('', '', chars)) \n"
            #f"\t\t\ttry: \n"
            "\t\t\tprice_bids_g_ = 'price_bids_g_' + symbol \n"
            "\t\t\tglobals()[price_bids_g_] = price_bids_g \n"
            # "\n"
            "\t\t\tqty_bids_g_ = 'qty_bids_g_' + symbol \n"
            "\t\t\tglobals()[qty_bids_g_] = qty_bids_g \n"
            "\n"
            "\t\t\tprice_asks_g_ = 'price_asks_g_' + symbol \n"
            "\t\t\tglobals()[price_asks_g_] = price_asks_g \n"
            "\n"
            "\t\t\tqty_asks_g_ = 'qty_asks_g_' + symbol \n"
            "\t\t\tglobals()[qty_asks_g_] = qty_asks_g \n"
            # f"\t\t\texcept: \n"
            # "\t\t\t\tpass \n"
            f"\t\telse: \n"
            f"\t\t\tpass \n"
            # f"\t\t\tprint('2222222',data) \n"
            f"\telse: \n"
            f"\t\tprint(data) \n"
            "\n"
            f"\tif (pingTime + pingInterval) <= round(time.time()): \n"
            "\t\tws.send(json.dumps({'id': id_channel, 'type': 'ping'})) \n"
            f"\t\tpingTime = round(time.time())  # Запомним новое время для сообщения \n"
            f"\t\tcount_message = 0  # Обнуляем счетчик сообщений \n"
            f"\t\tstart_time = time.time()  # Сбросим счетчик времени \n"
            "\n"
            "\n"
            f"def on_close(ws): \n"
            f"\tprint('### closed ###') \n"
            "\n"
            "\n"
            f"def on_error(ws, message): \n"
            f"\tprint(message) \n"
            "\n"
            "\n"
            f"def loadSetting(): \n"
            f"\treturn requests.post('https://api.kucoin.com/api/v1/bullet-public').json() \n"
            "\n"
            "\n"
            f"settings = loadSetting() \n"
            f"pingInterval = round((settings['data']['instanceServers'][0]['pingInterval'] / 1000) / 2) - 1 \n"
            f"pingTime = round(time.time()) \n"
            f"id_channel = '' \n"
            "\n"
            "ws = websocket.WebSocketApp(f\"{settings['data']['instanceServers'][0]['endpoint']}?token={settings['data']['token']}\", on_message=get_ticker_all, on_close=on_close, on_error=on_error) \n"
            f"ws.run_forever() \n"
        )

