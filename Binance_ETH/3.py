import json
from collections import OrderedDict  # модуль для удаления повторения

check_quote_pairs = '../Binance_ETH/1_pairs_buy_para_b_test.json'


def f_file_step_1_pairs_trade():
    with open(check_quote_pairs) as file_data:
        data_a = json.load(file_data)

    return data_a


########################################################################################################
# Определяем главную валюту
########################################################################################################

for main_currency in f_file_step_1_pairs_trade():
    if main_currency['quoteAsset_a'] != '':
        main_currency = main_currency['quoteAsset_a']
        break

########################################################################################################
# Ищем все валюты (котируемые) для третьего круга (пара 'c')
########################################################################################################

all_symbols_c = []

for i in f_file_step_1_pairs_trade():
    all_symbols_c.append(i['symbol_c'])

all_symbols_c = list(OrderedDict.fromkeys(all_symbols_c))  # удаляем повторения в 'all_symbols_c'

########################################################################################################
# Формируем основной файл
########################################################################################################

all_pairs_btc = "Run_BTC_test_2" + ".py"

with open(all_pairs_btc, 'w') as file3:
    file3.write("")

with open(all_pairs_btc, 'a') as file3:
    file3.write(
        "import time \n"
        "import datetime \n"
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
        "\n"
        "\tsell_amount_a = adjust_to_step(kolichestvo, stepSize) \n"
        "\n"
        "\treturn sell_amount_a \n"
        "\n"
        "\n"
        "api_key = 'A6Bc2FXbmn2dreyATiWkHMVFP3HTXNgTJTkKfVHihMuTb907wgHHkfqYHE8LGLdG' \n"
        "secret_key = 'zvP6vTEroLyMwoFut4pQKf4K2s05baZeQhXzVSC4wSiYB0G3l45dpt0EDcQGsQMA' \n"
        "\n"
        "client = Client(api_key, secret_key) \n"
        "\n"
        "usdt_count = float(0.01) \n"
        "\n"
        "all_pribil = float(0.0) \n"
        "\n"
    )

########################################################################################################
# Вычесляем 'stepSize' для пары 'c'
########################################################################################################

for i in all_symbols_c:
    symbol_c = i
    symbol_cc = symbol_c.lower()
    for ii in f_file_step_1_pairs_trade():
        if ii['symbol_c'] == symbol_c:
            stepSize_c = ii['stepSize_c']

########################################################################################################
# Формируем функции для основных валют (пара 'с')
########################################################################################################

    with open(all_pairs_btc, 'a') as file3:
        file3.write(
            f"symbol_c_g_{symbol_c} = '{symbol_c}' \n"
            f"price_bids_c_g_{symbol_c} = float(0.0) \n"
            f"qty_bids_c_g_{symbol_c} = float(0.0) \n"
            f"price_asks_c_g_{symbol_c} = float(0.0) \n"
            f"qty_asks_c_g_{symbol_c} = float(0.0) \n"
            f"stepSize_{symbol_c} = '{stepSize_c}' \n"
            "\n"
            "\n"
            f"def on_message_{symbol_c}(ws, message): \n"
            "\n"
            "\tdata = json.loads(message) \n"
            "\n"
            f"\tsymbol_c_l_{symbol_c} = '{symbol_c}' \n"
            f"\tprice_bids_c_l_{symbol_c} = data['bids'][0][0] \n"
            f"\tqty_bids_c_l_{symbol_c} = data['bids'][0][1] \n"
            f"\tprice_asks_c_l_{symbol_c} = data['asks'][0][0] \n"
            f"\tqty_asks_c_l_{symbol_c} = data['asks'][0][1] \n"
            "\n"
            f"\tglobal symbol_c_g_{symbol_c} \n"
            f"\tglobal price_bids_c_g_{symbol_c} \n"
            f"\tglobal qty_bids_c_g_{symbol_c} \n"
            f"\tglobal price_asks_c_g_{symbol_c} \n"
            f"\tglobal qty_asks_c_g_{symbol_c} \n"
            "\n"
            f"\tsymbol_c_g_{symbol_c} = symbol_c_l_{symbol_c} \n"
            f"\tprice_bids_c_g_{symbol_c} = price_bids_c_l_{symbol_c} \n"
            f"\tqty_bids_c_g_{symbol_c} = qty_bids_c_l_{symbol_c} \n"
            f"\tprice_asks_c_g_{symbol_c} = price_asks_c_l_{symbol_c} \n"
            f"\tqty_asks_c_g_{symbol_c} = qty_asks_c_l_{symbol_c} \n"
            "\n"
            "\n"
            f"def loop_{symbol_c}(): \n"
            "\n"
            f"\tsocket1 = f'wss://stream.binance.com:9443/ws/{symbol_cc}@depth5@100ms' \n"
            f"\tws = websocket.WebSocketApp(socket1, on_message=on_message_{symbol_c}) \n"
            "\tws.run_forever() \n"
            "\n"
            "\n"
            f"Thread(target=loop_{symbol_c}).start() \n"
            "\n"
        )

########################################################################################################
# Только для визуального отделения (#) основных валют от других.
########################################################################################################

with open(all_pairs_btc, 'a') as file3:
    file3.write(
        "\n"
        "########################################################################################################"
        "\n"
    )

########################################################################################################
# Формируем функции для остальных пар
########################################################################################################

check_quote_pairs = '../Binance_ETH/1_pairs_buy_para_b_test.json'


def f_test():
    with open(check_quote_pairs) as file_data:
        data_a = json.load(file_data)

    return data_a

########################################################################################################

for i in f_test():
    symbol_a = i['symbol_a']
    symbol_aa = symbol_a.lower()
    stepSize_a = i['stepSize_a']

    symbol_b = i['symbol_b']
    symbol_bb = symbol_b.lower()
    stepSize_b = i['stepSize_b']

    symbol_c = i['symbol_c']
    symbol_cc = symbol_c.lower()
    stepSize_c = i['stepSize_c']


    with open(all_pairs_btc, 'a') as file3:
        file3.write(
            f"stream{symbol_aa}{symbol_bb} = '{symbol_aa}@bookTicker'\n"
            f"stream{symbol_bb}{symbol_aa} = '{symbol_bb}@bookTicker'\n"
            "\n"
            f"symbol_a_g_{symbol_a}_{symbol_b} = '{symbol_a}' \n"
            f"price_bids_a_g_{symbol_a}_{symbol_b} = float(0.0) \n"
            f"qty_bids_a_g_{symbol_a}_{symbol_b} = float(0.0) \n"
            f"price_asks_a_g_{symbol_a}_{symbol_b} = float(0.0) \n"
            f"qty_asks_a_g_{symbol_a}_{symbol_b} = float(0.0) \n"
            "\n"
            f"stepSize_{symbol_a}_{symbol_b} = {stepSize_a} \n"
            "\n"
            f"symbol_b_g_{symbol_b}_{symbol_a} = '{symbol_b}' \n"
            f"price_bids_b_g_{symbol_b}_{symbol_a} = float(0.0) \n"
            f"qty_bids_b_g_{symbol_b}_{symbol_a} = float(0.0) \n"
            f"price_asks_b_g_{symbol_b}_{symbol_a} = float(0.0) \n"
            f"qty_asks_b_g_{symbol_b}_{symbol_a} = float(0.0) \n"
            "\n"
            f"stepSize_{symbol_b}_{symbol_a} = {stepSize_b} \n"
            "\n"
            "\n"
            f"def on_message_{symbol_a}_{symbol_b}(ws, message): \n"
            "\n"
            "\tdata = json.loads(message) \n"
            "\n"
            f"\tif data['stream'] == stream{symbol_aa}{symbol_bb}:\n"
            f"\t\tsymbol_a_l_{symbol_a} = data['data']['s'] \n"
            f"\t\tprice_bids_a_l_{symbol_a} = data['data']['b'] \n"
            f"\t\tqty_bids_a_l_{symbol_a} = data['data']['B'] \n"
            f"\t\tprice_asks_a_l_{symbol_a} = data['data']['a'] \n"
            f"\t\tqty_asks_a_l_{symbol_a} = data['data']['A'] \n"
            "\n"
            f"\t\tglobal symbol_a_g_{symbol_a}_{symbol_b} \n"
            f"\t\tglobal price_bids_a_g_{symbol_a}_{symbol_b} \n"
            f"\t\tglobal qty_bids_a_g_{symbol_a}_{symbol_b} \n"
            f"\t\tglobal price_asks_a_g_{symbol_a}_{symbol_b} \n"
            f"\t\tglobal qty_asks_a_g_{symbol_a}_{symbol_b} \n"
            "\n"
            f"\t\tsymbol_a_g_{symbol_a}_{symbol_b} = symbol_a_l_{symbol_a} \n"
            f"\t\tprice_bids_a_g_{symbol_a}_{symbol_b} = price_bids_a_l_{symbol_a} \n"
            f"\t\tqty_bids_a_g_{symbol_a}_{symbol_b} = qty_bids_a_l_{symbol_a} \n"
            f"\t\tprice_asks_a_g_{symbol_a}_{symbol_b} = price_asks_a_l_{symbol_a} \n"
            f"\t\tqty_asks_a_g_{symbol_a}_{symbol_b} = qty_asks_a_l_{symbol_a} \n"
            "\n"
            f"\tif data['stream'] == stream{symbol_bb}{symbol_aa}:\n"

            "\t\tdata = json.loads(message) \n"
            "\n"
            f"\t\tsymbol_b_l_{symbol_b} = data['data']['s'] \n"
            f"\t\tprice_bids_b_l_{symbol_b} = data['data']['b'] \n"
            f"\t\tqty_bids_b_l_{symbol_b} = data['data']['B']\n"
            f"\t\tprice_asks_b_l_{symbol_b} = data['data']['a'] \n"
            f"\t\tqty_asks_b_l_{symbol_b} = data['data']['A'] \n"
            "\n"
            f"\t\tglobal symbol_b_g_{symbol_b}_{symbol_a} \n"
            f"\t\tglobal price_bids_b_g_{symbol_b}_{symbol_a} \n"
            f"\t\tglobal qty_bids_b_g_{symbol_b}_{symbol_a} \n"
            f"\t\tglobal price_asks_b_g_{symbol_b}_{symbol_a} \n"
            f"\t\tglobal qty_asks_b_g_{symbol_b}_{symbol_a} \n"
            "\n"
            f"\t\tsymbol_b_g_{symbol_b}_{symbol_a} = symbol_b_l_{symbol_b} \n"
            f"\t\tprice_bids_b_g_{symbol_b}_{symbol_a} = price_bids_b_l_{symbol_b} \n"
            f"\t\tqty_bids_b_g_{symbol_b}_{symbol_a} = qty_bids_b_l_{symbol_b} \n"
            f"\t\tprice_asks_b_g_{symbol_b}_{symbol_a} = price_asks_b_l_{symbol_b} \n"
            f"\t\tqty_asks_b_g_{symbol_b}_{symbol_a} = qty_asks_b_l_{symbol_b} \n"
            "\n"
            "\n"
            f"def loop_{symbol_a}_{symbol_b}():\n"
            "\tsocket1 = f'wss://stream.binance.com:9443/stream?streams={stream"f"{symbol_aa}{symbol_bb}""}""/""{stream"f"{symbol_bb}{symbol_aa}""}""' \n"
            "\n"
            f"\tws = websocket.WebSocketApp(socket1, on_message=on_message_{symbol_a}_{symbol_b})\n"
            "\n"
            "\tws.run_forever() \n"
            "\n"
            "\n"
            f"Thread(target=loop_{symbol_a}_{symbol_b}).start()\n"
            "\n"
            "\n"
            f"def loop_{symbol_a}_{symbol_b}_Trade(): \n"
            "\n"
            "\twhile True: \n"
            "\t\ttime.sleep(0.1)\n"
            "\n"
            f"\t\tif price_bids_c_g_{symbol_c} != 0.0 and qty_bids_c_g_{symbol_c} != 0.0 and price_asks_c_g_{symbol_c} != 0.0 and qty_asks_c_g_{symbol_c} != 0.0 and price_bids_a_g_{symbol_a}_{symbol_b} != 0.0 and qty_bids_a_g_{symbol_a}_{symbol_b} != 0.0 and price_asks_a_g_{symbol_a}_{symbol_b} != 0.0 and qty_asks_a_g_{symbol_a}_{symbol_b} != 0.0 and price_bids_b_g_{symbol_b}_{symbol_a} != 0.0 and qty_bids_b_g_{symbol_b}_{symbol_a} != 0.0 and price_asks_b_g_{symbol_b}_{symbol_a} != 0.0 and qty_asks_b_g_{symbol_b}_{symbol_a} != 0.0: \n"
            #######################################################################################################################
            "\n"
        )
    ########################################################################################################
    # Если в паре 'c' baseAsset_c равно основной валюте (main_currency)
    ########################################################################################################
    if i['baseAsset_c'] == main_currency:
        with open(all_pairs_btc, 'a') as file3:
            file3.write(

                # Вычисляем сколько нужно продать в конце (пара С) BTC при депозите main_currency.
                f"\t\t\t# Цепочка: {symbol_a} -> {symbol_b} -> {symbol_c} \n"
                "\n"
                f"\t\t\t# Покупаем {i['baseAsset_c']} продаем {i['quoteAsset_c']} \n"
                f"\t\t\tquantity_pair_c_raschet = usdt_count * float(price_asks_c_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
                f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                #f"\t\t\tquantity_pair_c_raschet = float(f_minqty_size_up(quantity_pair_c_raschet, stepSize_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
                #f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['quoteAsset_c']}' \n"
                f"\t\t\ttrade_pair_c = 'buy' \n"
                "\n"
                f"\t\t\t# Продаем {i['baseAsset_b']} покупаем {i['quoteAsset_b']} \n"

                f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) / float(price_bids_b_g_{symbol_b}_{symbol_a})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_{symbol_b}_{symbol_a}))  # Округляем согласно шагу Binance 'stepSize' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
                f"\t\t\ttrade_pair_b = 'sell' \n"
                "\n"
                f"\t\t\tquantity_pair_a_raschet = float(f_minqty_size_down(quantity_pair_b_raschet, stepSize_{symbol_a}_{symbol_b})) \n"
			    f"\t\t\tquantity_pair_a_raschet = round(quantity_pair_a_raschet, 14) \n"
                "\n"
                f"\t\t\tprice_a = float(quantity_pair_a_raschet) * float(price_asks_a_g_{symbol_a}_{symbol_b}) \n"
                f"\t\t\tprice_a = round(price_a, 14) \n"
                f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                "\n"
                f"\t\t\tprice_b = float(price_bids_b_g_{symbol_b}_{symbol_a}) * float(quantity_pair_a_raschet) \n"
                f"\t\t\tprice_b = round(price_b, 14) \n"
                f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                "\n"
                f"\t\t\tprice_c = float(price_b) / float(price_asks_c_g_{symbol_c}) \n"
                f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_{symbol_c})) \n"
                f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                "\n"
                f"\t\t\tpribil = float(price_cc) - float(price_a) \n"
                "\n"
                f"\t\t\ttime_test = datetime.datetime.now() \n"
                f"\t\t\ta = float(price_cc) \n"
                f"\t\t\tb = float(price_a) \n"
                f"\t\t\tc = (a / b - 1) * 100 \n"
                f"\t\t\tif c > 0.225: \n"
                "\n"
                f"\t\t\t\tprint('################################################################################################################', time_test) \n"
                f"\t\t\t\tprint('Пара_А:', symbol_a_g_{symbol_a}_{symbol_b}) \n"
                f"\t\t\t\tprint('Покупаем', quantity_pair_b_raschet, '{i['baseAsset_a']}', 'за', price_a, '{i['quoteAsset_a']}', 'по цене', price_asks_a_g_{symbol_a}_{symbol_b}) \n"
                f"\t\t\t\tprint('Пара_B:', symbol_b_g_{symbol_b}_{symbol_a}) \n"
                f"\t\t\t\tprint('Продаем', quantity_pair_b_raschet, '{i['baseAsset_b']}', 'за', price_b, '{i['quoteAsset_b']}', 'по цене', price_bids_b_g_{symbol_b}_{symbol_a}) \n"
                f"\t\t\t\tprint('Пара_C:', symbol_c_g_{symbol_c}) \n"
                f"\t\t\t\tprint('Покупаем', price_c, '{i['baseAsset_c']}', 'за', price_b, '{i['quoteAsset_c']}', 'по цене', price_asks_c_g_{symbol_c}) \n"
                f"\t\t\t\tprint(price_cc, c, '%') \n"
                "\n"
                f"\t\t\t\ttime.sleep(1) \n"
                f"Thread(target=loop_{symbol_a}_{symbol_b}_Trade).start() \n"
                "\n"
            )

    if i['quoteAsset_c'] == main_currency:
        with open(all_pairs_btc, 'a') as file3:
            file3.write(

                # Вычисляем сколько нужно продать в конце (пара С) BTC при депозите main_currency.
                f"\t\t\t# Цепочка: {symbol_a} -> {symbol_b} -> {symbol_c} \n"
                "\n"
                f"\t\t\t# Продаем {i['baseAsset_c']} покупаем {i['quoteAsset_c']} \n"
                f"\t\t\tquantity_pair_c_raschet = usdt_count / float(price_bids_c_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
                f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\tquantity_pair_c_raschet = float(f_minqty_size_up(quantity_pair_c_raschet, stepSize_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
                f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['quoteAsset_c']}' \n"
                f"\t\t\ttrade_pair_c = 'sell' \n"
                "\n"
                f"\t\t\t# Продаем {i['baseAsset_b']} покупаем {i['quoteAsset_b']} \n"

                f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) / float(price_bids_b_g_{symbol_b}_{symbol_a})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_{symbol_b}_{symbol_a}))  # Округляем согласно шагу Binance 'stepSize' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
                f"\t\t\ttrade_pair_b = 'sell' \n"
                "\n"
                f"\t\t\tprice_a = float(quantity_pair_b_raschet) * float(price_asks_a_g_{symbol_a}_{symbol_b}) \n"
                f"\t\t\tprice_a = round(price_a, 14) \n"
                f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
                "\n"
                f"\t\t\tprice_b = float(price_bids_b_g_{symbol_b}_{symbol_a}) * float(quantity_pair_b_raschet) \n"
                f"\t\t\tprice_b = round(price_b, 14) \n"
                f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
                "\n"
                f"\t\t\tprice_c = float(price_b) * float(price_bids_c_g_{symbol_c}) \n"
                f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_{symbol_c})) \n"
                f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
                "\n"
                f"\t\t\tpribil = float(price_cc) - float(price_a) \n"
                "\n"
                f"\t\t\tif pribil > 0: \n"
                "\n"
                f"\t\t\t\tprint('################################################################################################################') \n"
                f"\t\t\t\tprint('Пара_А:', symbol_a_g_{symbol_a}_{symbol_b}) \n"
                f"\t\t\t\tprint('Покупаем', quantity_pair_b_raschet, '{i['baseAsset_a']}', 'за', price_a, '{i['quoteAsset_a']}', 'по цене', price_asks_a_g_{symbol_a}_{symbol_b}) \n"
                f"\t\t\t\tprint('Пара_B:', symbol_b_g_{symbol_b}_{symbol_a}) \n"
                f"\t\t\t\tprint('Продаем', quantity_pair_b_raschet, '{i['baseAsset_b']}', 'за', price_b, '{i['quoteAsset_b']}', 'по цене', price_bids_b_g_{symbol_b}_{symbol_a}) \n"
                f"\t\t\t\tprint('Пара_C:', symbol_c_g_{symbol_c}) \n"
                f"\t\t\t\tprint('Продаем', price_b, '{i['baseAsset_c']}', 'за', price_c, '{i['quoteAsset_c']}', 'по цене', price_bids_c_g_{symbol_c}) \n"
                f"\t\t\t\tprint('Потратили', price_a, 'получили', price_cc) \n"
                f"\t\t\t\ttime.sleep(1) \n"
                f"Thread(target=loop_{symbol_a}_{symbol_b}_Trade).start() \n"
                "\n"

            )

    # if i['quoteAsset_a'] == main_currency and i['baseAsset_a'] == i['baseAsset_b'] :
    #     with open(all_pairs_btc, 'a') as file3:
    #         file3.write(
    #
    #             #Вычесляем сколько нужно продать в конце (пара B) ETH при quantity_pair_c_raschet
    #             f"\t\t\t# Продаем {i['baseAsset_b']} покупаем {i['quoteAsset_b']} \n"
    #
    #             f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) / float(price_bids_b_g_{symbol_b}_{symbol_a})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
    #             f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
    #             f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_{symbol_b}_{symbol_a}))  # Округляем согласно шагу Binance 'stepSize' \n"
    #             f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
    #             f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
    #             f"\t\t\ttrade_pair_b = 'sell' \n"
    #             "\n"
    #             f"\t\t\tprice_a = float(quantity_pair_b_raschet) * float(price_asks_a_g_{symbol_a}_{symbol_b}) \n"
    #             f"\t\t\tprice_a = round(price_a, 14) \n"
    #             f"\t\t\t# price_a = сколько потребуется '{i['quoteAsset_a']}' \n"
    #             "\n"
    #             f"\t\t\tprice_b = float(price_bids_b_g_{symbol_b}_{symbol_a}) * float(quantity_pair_b_raschet) \n"
	# 		    f"\t\t\tprice_b = round(price_b, 14) \n"
	# 		    f"\t\t\t# price_b = сколько получим '{i['quoteAsset_b']}' \n"
    #             "\n"
    #             f"\t\t\tprice_c = float(price_b) / float(price_asks_c_g_{symbol_c}) \n"
    #             f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_{symbol_c})) \n"
	# 		    f"\t\t\t# price_c = сколько получим '{i['baseAsset_c']}' \n"
    #             "\n"
    #             f"\t\t\tprint('################################################################################################################') \n"
    #             f"\t\t\tprint('Пара_А:', symbol_a_g_{symbol_a}_{symbol_b}) \n"
    #             f"\t\t\tprint('Покупаем', quantity_pair_b_raschet, '{i['baseAsset_a']}', 'за', price_a, '{i['quoteAsset_a']}', 'по цене', price_asks_a_g_{symbol_a}_{symbol_b}) \n"
    #             f"\t\t\tprint('Пара_B:', symbol_b_g_{symbol_b}_{symbol_a}) \n"
    #             f"\t\t\tprint('Продаем', quantity_pair_b_raschet, '{i['baseAsset_b']}', 'за', price_b, '{i['quoteAsset_b']}', 'по цене', price_bids_b_g_{symbol_b}_{symbol_a}) \n"
    #             f"\t\t\tprint('Пара_C:', symbol_c_g_{symbol_c}) \n"
    #             f"\t\t\tprint('Покупаем', price_c, '{i['baseAsset_c']}', 'за', price_b, '{i['quoteAsset_c']}', 'по цене', price_asks_c_g_{symbol_c}) \n"
    #             f"\t\t\tprint(price_cc ) \n"
    #             # Вычесляем сколько нужно купить в конце (пара А) ETH при quantity_pair_b_raschet
    #             #f"\t\t\t# Покупаем {i['baseAsset_a']} продаем {i['quoteAsset_a']} \n"
    #             #f"\t\t\tquantity_pair_a_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_{symbol_a}_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
    #             #f"\t\t\tquantity_pair_a_raschet = round(quantity_pair_a_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
    #             #f"\t\t\tquantity_pair_a_raschet = float(quantity_pair_a_raschet * float(price_asks_a_g_{symbol_a}_{symbol_b})) \n"
    #             #f"\t\t\tquantity_pair_a_raschet = float(f_minqty_size_up(quantity_pair_a_raschet, stepSize_{symbol_a}_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
    #             #f"\t\t\tquantity_pair_a_raschet = round(quantity_pair_a_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
    #             #f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_a']}' \n"
    #             #f"\t\t\ttrade_pair_a = 'buy' \n"
    #             #"\n"
    #             f"Thread(target=loop_{symbol_a}_{symbol_b}_Trade).start() \n"
    #             "\n"
    #         )

    if i['quoteAsset_a'] == main_currency and i['baseAsset_a'] == i['quoteAsset_b']:
        print("Есть проблема, проверить: if i['quoteAsset_a'] == main_currency and i['baseAsset_a'] == i['quoteAsset_b']:")


