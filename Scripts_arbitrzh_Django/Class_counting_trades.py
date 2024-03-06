import sqlite3

#########################################################
""" Функция округения """
#########################################################


def f_minqty_size_up(kolichestvo, stepSize):
    def adjust_to_step(value, step, increase=False):
        return ((int(value * 100000000) - int(value * 100000000) % int(
            float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)

    sell_amount_a = adjust_to_step(kolichestvo, stepSize)

    return sell_amount_a


def f_minqty_size_down(kolichestvo, stepSize):
    def adjust_to_step(value, step, increase=False):
        return ((int(value * 100000000) - int(value * 100000000) % int(
            float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)

    sell_amount_a = adjust_to_step(kolichestvo, stepSize)

    return sell_amount_a
#########################################################

def def_allMainCurrency(exchange):
    """Основные валюты торговых бирж"""

    with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:
        #########################################################
        #  Далее, иногда более предпочтительным вариантом выходных данных является не кортеж с данными, а словарь, позволяющий обращаться к элементам по именам полей. Для этого после установления соединения с БД следует прописать вот такую строчку:
        connect_db.row_factory = sqlite3.Row
        #########################################################
        cursor = connect_db.cursor()

        cursor.execute(F"SELECT * FROM arbitrazh_{exchange}_all_pairs_trading_inf")  #
        get_all_pairs_inf = cursor.fetchall()

    allMainCurrency = None

    match exchange:

        case "Binance":
            # allMainCurrency = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR',
            #                    'GBR', 'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']

            allMainCurrency = []

            for i in get_all_pairs_inf:
                # print(i['quoteAsset_a'])

                if i['quoteAsset'] in allMainCurrency:
                    pass
                else:
                    allMainCurrency.append(i['quoteAsset'])


        case "Kucoin":
            allMainCurrency = ['BTC', 'KCS', 'ETH', 'TRX', 'DOGE', 'USDT', 'TUSD', 'DAI', 'USDC']

    return allMainCurrency
    #########################################################


    test = []



#########################################################

def aaa():
    a = 'safdgfdsgffs'
    return a


def f_makerStrategy_bss(symbol, bid_or_ask, price, stepSize, quantity_coins='None', main_amount_currency='None'):

    dict_f_aprice = {}

    try:

        if bid_or_ask == 'bidPrice':

            price = float(price)  # Цена монеты на круге А для покупки coins
            quantity_coins_without_stepSize = float(main_amount_currency) / float(price)  # Полученное количество монет после покупки
            quantity_coins_with_stepSize = f_minqty_size_up(float(quantity_coins_without_stepSize), float(stepSize))  # Округление согласно StepSize
            final_quantity_coins_without_percent = quantity_coins_with_stepSize  # Финальное количество монет с округлением и без учёта процентов

            dict_f_aprice = {
                'symbol': symbol,
                'price': price,
                'quantity_coins_with_stepSize': quantity_coins_with_stepSize,
                'quantity_coins_without_stepSize': quantity_coins_without_stepSize,
                'final_quantity_coins_without_percent': final_quantity_coins_without_percent
            }

        elif bid_or_ask == 'askPrice':

            price = float(price)  # Цена монеты для продажи
            quantity_coins_with_stepSize = f_minqty_size_down(float(quantity_coins), float(stepSize))  # Округление согласно StepSize
            quantity_coins_without_stepSize = float(quantity_coins_with_stepSize) * float(price)  # Полученное количество монет после продажи

            final_quantity_coins_without_percent = quantity_coins_without_stepSize

            dict_f_aprice = {
                'symbol': symbol,
                'price': price,
                'quantity_coins_with_stepSize': quantity_coins_with_stepSize,
                'quantity_coins_without_stepSize': quantity_coins_without_stepSize,
                'final_quantity_coins_without_percent': final_quantity_coins_without_percent
            }

    except:
        pass

    return dict_f_aprice


def f_insert_bd_profitTrade(insert_bd_profitTrade, exchange):

    with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:
        #########################################################
        #  Далее, иногда более предпочтительным вариантом выходных данных является не кортеж с данными, а словарь, позволяющий обращаться к элементам по именам полей. Для этого после установления соединения с БД следует прописать вот такую строчку:
        connect_db.row_factory = sqlite3.Row
        #########################################################
        cursor = connect_db.cursor()
        cursor.execute(F"SELECT * from arbitrazh_{exchange}_profit_trademaker_bss")
        suka = cursor.fetchall()

        if not suka:  # Если таблица пустая

            for i_insert_bd_profitTrade in insert_bd_profitTrade:  #
                # print(i_insert_bd_profitTrade['symbols'])
                cursor.execute(
                        F"INSERT INTO arbitrazh_{exchange}_profit_trademaker_bss VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), ?)",
                        (
                            i_insert_bd_profitTrade['symbols'],
                            i_insert_bd_profitTrade['symbol_a'],
                            i_insert_bd_profitTrade['baseCurrency_a'],
                            i_insert_bd_profitTrade['quoteAsset_a'],
                            i_insert_bd_profitTrade['stepSize_a'],
                            i_insert_bd_profitTrade['bidPrice_a'],
                            i_insert_bd_profitTrade['bidQty_a'],
                            i_insert_bd_profitTrade['askPrice_a'],
                            i_insert_bd_profitTrade['askQty_a'],
                            i_insert_bd_profitTrade['symbol_b'],
                            i_insert_bd_profitTrade['baseCurrency_b'],
                            i_insert_bd_profitTrade['quoteAsset_b'],
                            i_insert_bd_profitTrade['stepSize_b'],
                            i_insert_bd_profitTrade['bidPrice_b'],
                            i_insert_bd_profitTrade['bidQty_b'],
                            i_insert_bd_profitTrade['askPrice_b'],
                            i_insert_bd_profitTrade['askQty_b'],
                            i_insert_bd_profitTrade['symbol_c'],
                            i_insert_bd_profitTrade['baseCurrency_c'],
                            i_insert_bd_profitTrade['quoteAsset_c'],
                            i_insert_bd_profitTrade['stepSize_c'],
                            i_insert_bd_profitTrade['bidPrice_c'],
                            i_insert_bd_profitTrade['bidQty_c'],
                            i_insert_bd_profitTrade['askPrice_c'],
                            i_insert_bd_profitTrade['askQty_c'],
                            i_insert_bd_profitTrade['time_update']
                        ))
        elif suka:  # Если таблица не пустая

            cursor.execute(F"SELECT * from arbitrazh_{exchange}_profit_trademaker_bss")
            select_all_profit = cursor.fetchall()

            for i_select_all_profit in select_all_profit:

                exists_in_the_table_bd = None

                for i_insert_bd_profitTrade in insert_bd_profitTrade:
                    if i_select_all_profit['symbols'] == i_insert_bd_profitTrade['symbols']:  # Проверка, запись в БД есть в новых полученных данных, если есть, то обновляем данные в таблице

                        cursor.execute(f"UPDATE arbitrazh_{exchange}_profit_trademaker_bss SET "

                                               f"bidPrice_a = {i_insert_bd_profitTrade['bidPrice_a']}, "
                                               f"bidQty_a = {i_insert_bd_profitTrade['bidQty_a']}, "
                                               f"askPrice_a = {i_insert_bd_profitTrade['askPrice_a']},"
                                               f"askQty_a = {i_insert_bd_profitTrade['askQty_a']},"
                                               f"bidPrice_b = {i_insert_bd_profitTrade['bidPrice_b']},"
                                               f"bidQty_b = {i_insert_bd_profitTrade['bidQty_b']},"
                                               f"askPrice_b = {i_insert_bd_profitTrade['askPrice_b']},"
                                               f"askQty_b = {i_insert_bd_profitTrade['askQty_b']},"
                                               f"bidPrice_c = {i_insert_bd_profitTrade['bidPrice_c']},"
                                               f"bidQty_c = {i_insert_bd_profitTrade['bidQty_c']},"
                                               f"askPrice_c = {i_insert_bd_profitTrade['askPrice_c']},"
                                               f"askQty_c = {i_insert_bd_profitTrade['askQty_c']},"
                                               f"time_update = datetime('now') "

                                               f"WHERE id = {i_select_all_profit['id']}")

                        exists_in_the_table_bd = 'is not None'
                        break

                    else:

                        exists_in_the_table_bd = None

                if exists_in_the_table_bd is None:
                    cursor.execute(F"DELETE from arbitrazh_{exchange}_profit_trademaker_bss where id = {i_select_all_profit['id']}")

            ##########################################
            #Добавляем цепочку в БД если ее там нет
            ##########################################

            for i_insert_bd_profitTrade in insert_bd_profitTrade:
                exists_in_the_table_bd = None
                for i_select_all_profit in select_all_profit:
                    if i_select_all_profit['symbols'] == i_insert_bd_profitTrade['symbols']:
                        exists_in_the_table_bd = 'is not None'
                        break
                    else:
                        exists_in_the_table_bd = None

                if exists_in_the_table_bd is None:

                    cursor.execute(
                        F"INSERT INTO arbitrazh_{exchange}_profit_trademaker_bss VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), ?)",
                        (
                            i_insert_bd_profitTrade['symbols'],
                            i_insert_bd_profitTrade['symbol_a'],
                            i_insert_bd_profitTrade['baseCurrency_a'],
                            i_insert_bd_profitTrade['quoteAsset_a'],
                            i_insert_bd_profitTrade['stepSize_a'],
                            i_insert_bd_profitTrade['bidPrice_a'],
                            i_insert_bd_profitTrade['bidQty_a'],
                            i_insert_bd_profitTrade['askPrice_a'],
                            i_insert_bd_profitTrade['askQty_a'],
                            i_insert_bd_profitTrade['symbol_b'],
                            i_insert_bd_profitTrade['baseCurrency_b'],
                            i_insert_bd_profitTrade['quoteAsset_b'],
                            i_insert_bd_profitTrade['stepSize_b'],
                            i_insert_bd_profitTrade['bidPrice_b'],
                            i_insert_bd_profitTrade['bidQty_b'],
                            i_insert_bd_profitTrade['askPrice_b'],
                            i_insert_bd_profitTrade['askQty_b'],
                            i_insert_bd_profitTrade['symbol_c'],
                            i_insert_bd_profitTrade['baseCurrency_c'],
                            i_insert_bd_profitTrade['quoteAsset_c'],
                            i_insert_bd_profitTrade['stepSize_c'],
                            i_insert_bd_profitTrade['bidPrice_c'],
                            i_insert_bd_profitTrade['bidQty_c'],
                            i_insert_bd_profitTrade['askPrice_c'],
                            i_insert_bd_profitTrade['askQty_c'],
                            i_insert_bd_profitTrade['time_update']
                        ))

        #
        #     for i_select_all_profit in select_all_profit:
        #         print(i_select_all_profit['symbols'])

            # for i_suka in suka:
            #
            #     if i_suka['symbols'] == test['symbols']:
            #         # print(i_suka['id'])
            #         cursor.execute(f"UPDATE arbitrazh_binance_profit_trademaker_bss SET "
            #                        f"bidPrice_a = {test['bidPrice_a']}, "
            #                        f"bidQty_a = {test['bidQty_a']}, "
            #                        f"askPrice_a = {test['askPrice_a']},"
            #                        f"askQty_a = {test['askQty_a']},"
            #                        f"bidPrice_b = {test['bidPrice_b']},"
            #                        f"bidQty_b = {test['bidQty_b']},"
            #                        f"askPrice_b = {test['askPrice_b']},"
            #                        f"askQty_b = {test['askQty_b']},"
            #                        f"bidPrice_c = {test['bidPrice_c']},"
            #                        f"bidQty_c = {test['bidQty_c']},"
            #                        f"askPrice_c = {test['askPrice_c']},"
            #                        f"askQty_c = {test['askQty_c']},"
            #                        f"time_update = datetime('now') "
            #                        f"WHERE id = {i_suka['id']}")
            #         break
            #
            #     elif i_suka['symbols'] != test['symbols']:
            #
            #         cursor.execute(
            #             F"INSERT INTO arbitrazh_binance_profit_trademaker_bss VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), ?)",
            #             (
            #                 test['symbols'],
            #                 test['symbol_a'],
            #                 test['baseCurrency_a'],
            #                 test['quoteAsset_a'],
            #                 test['stepSize_a'],
            #                 test['bidPrice_a'],
            #                 test['bidQty_a'],
            #                 test['askPrice_a'],
            #                 test['askQty_a'],
            #                 test['symbol_b'],
            #                 test['baseCurrency_b'],
            #                 test['quoteAsset_b'],
            #                 test['stepSize_b'],
            #                 test['bidPrice_b'],
            #                 test['bidQty_b'],
            #                 test['askPrice_b'],
            #                 test['askQty_b'],
            #                 test['symbol_c'],
            #                 test['baseCurrency_c'],
            #                 test['quoteAsset_c'],
            #                 test['stepSize_c'],
            #                 test['bidPrice_c'],
            #                 test['bidQty_c'],
            #                 test['askPrice_c'],
            #                 test['askQty_c'],
            #                 test['time_update']
            #             ))



