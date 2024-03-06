import decimal
from decimal import Decimal
import sqlite3
import time
import datetime
import requests
import json

from Scripts_arbitrzh_Django import Class_counting_trades

exchange = 'Binance'
main_amount_currency = int(1000)


def def_allMainCurrency(exchange):
    """Основные валюты торговых бирж"""

    with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:
        #########################################################
        #  Далее, иногда более предпочтительным вариантом выходных данных является не кортеж с данными, а словарь, позволяющий обращаться к элементам по именам полей. Для этого после установления соединения с БД следует прописать вот такую строчку:
        connect_db.row_factory = sqlite3.Row
        #########################################################
        cursor = connect_db.cursor()

        cursor.execute(F"SELECT * FROM arbitrazh_{exchange}_pairs_strategy_b_s_s")  #
        get_all_pairs_inf = cursor.fetchall()

    # allMainCurrency = None

    match exchange:

        case "Binance":
            # allMainCurrency = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR',
            #                    'GBR', 'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']

            mainCurrenciesList = []
            allMainCurrencyKort = []

            for i in get_all_pairs_inf:

                if i['quoteAsset_a'] in mainCurrenciesList:
                    pass
                else:
                    mainCurrenciesList.append(i['quoteAsset_a'])

            for i in mainCurrenciesList:

                a = (i, i)
                allMainCurrencyKort.append(a)

        case "Kucoin":
            allMainCurrency = ['BTC', 'KCS', 'ETH', 'TRX', 'DOGE', 'USDT', 'TUSD', 'DAI', 'USDC']

    return allMainCurrencyKort


while True:

    with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:
        #########################################################
        #  Далее, иногда более предпочтительным вариантом выходных данных является не кортеж с данными, а словарь, позволяющий обращаться к элементам по именам полей. Для этого после установления соединения с БД следует прописать вот такую строчку:
        connect_db.row_factory = sqlite3.Row
        #########################################################
        cursor = connect_db.cursor()

        cursor.execute(F"SELECT * FROM arbitrazh_binance_pairs_strategy_b_s_s")  #
        get_arbitrazh_binance_pairs_strategy_b_s_s = cursor.fetchall()

        cursor.execute(F"SELECT * FROM arbitrazh_binance_bookticker")
        get_arbitrazh_binance_bookticker = cursor.fetchall()

        # (1585, 'BNBUSDT', 'BNB', 'USDT', 'BNBTUSD', 'BNB', 'TUSD', 'TUSDUSDT', 'TUSD', 'USDT')

    insert_bd_profitTrade = []

    allMainCurrency = def_allMainCurrency(exchange)

    for i_allMainCurrency in allMainCurrency:
        main_curency = i_allMainCurrency[0]

        # for main_curency in all_main_curency:

            # print(main_curency)

        for i_get_arbitrazh_binance_pairs_strategy_b_s_s in get_arbitrazh_binance_pairs_strategy_b_s_s:
            # print(i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_a'],i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_b'],i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_c'])

            if i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_a'] == main_curency:

                """ Круг Symbol - A """

                for i_get_arbitrazh_binance_bookticker_symbol_a in get_arbitrazh_binance_bookticker:

                    if i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_a'] == i_get_arbitrazh_binance_bookticker_symbol_a['symbol']:

                        """ Стратегия торговли по рынку  """

                        #

                        """ Стратегия торговли по лимитным заявка  """
                        # print(i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_a'])
                        trade_circle_a = Class_counting_trades.f_makerStrategy_bss(
                            symbol=i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_a'],
                            bid_or_ask='bidPrice',
                            price=i_get_arbitrazh_binance_bookticker_symbol_a['bidPrice'],
                            stepSize=i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_a'],
                            main_amount_currency=main_amount_currency
                        )
                        # print(trade_circle_a)

                        break

                """ Круг Symbol - B """

                for i_get_arbitrazh_binance_bookticker_symbol_b in get_arbitrazh_binance_bookticker:

                    if i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_b'] == i_get_arbitrazh_binance_bookticker_symbol_b['symbol']:

                        """ Стратегия торговли по рынку  """

                        #

                        """ Стратегия торговли по лимитным заявка  """

                        trade_circle_b = Class_counting_trades.f_makerStrategy_bss(
                            symbol=i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_b'],
                            bid_or_ask='askPrice',
                            price=i_get_arbitrazh_binance_bookticker_symbol_b['askPrice'],
                            stepSize=i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_b'],
                            quantity_coins=trade_circle_a['final_quantity_coins_without_percent'],
                        )

                        break

                """ Круг Symbol - C """

                for i_get_arbitrazh_binance_bookticker_symbol_c in get_arbitrazh_binance_bookticker:

                    if i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_c'] == i_get_arbitrazh_binance_bookticker_symbol_c['symbol']:

                        """ Стратегия торговли по рынку  """

                        #

                        """ Стратегия торговли по лимитным заявка  """

                        trade_circle_c = Class_counting_trades.f_makerStrategy_bss(
                            symbol=i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_c'],
                            bid_or_ask='askPrice',
                            price=i_get_arbitrazh_binance_bookticker_symbol_c['askPrice'],
                            stepSize=i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_c'],
                            quantity_coins=trade_circle_b['final_quantity_coins_without_percent']
                        )

                        break
                try:
                    """ Подсчет полученных данных """

                    costs_main_currency_makerStrategy = trade_circle_a['final_quantity_coins_without_percent'] * trade_circle_a['price']  # Количество потраченной основной валюты "main_currency" на круге А

                    """ Расчет комиссии Maker"""



                    percentage_for_trading = 0.1  # Комиссия биржи за одну сделку
                    c = trade_circle_c['final_quantity_coins_without_percent'] / 100 * percentage_for_trading  # Количество комиссии в валюте
                    final_quantity_coins_circle_c_with_percent_makerStrategy = trade_circle_c['final_quantity_coins_without_percent'] - c  # Финальное количество получаемых монет на последнем круге с учётом комиссии
                    # print(trade_circle_a['final_quantity_coins_without_percent'])
                    # print(final_quantity_coins_circle_c_with_percent_makerStrategy, costs_main_currency_makerStrategy)

                    profit_without_percents = trade_circle_c['final_quantity_coins_without_percent'] - costs_main_currency_makerStrategy  # Расчёт прибыли без комиссии
                    profit_with_percents = final_quantity_coins_circle_c_with_percent_makerStrategy - costs_main_currency_makerStrategy  # Расчёт прибыли с комиссией
                    profit_percent = final_quantity_coins_circle_c_with_percent_makerStrategy / costs_main_currency_makerStrategy * 100 - 100  # Формула прибыли в процентах

                    if profit_percent > 0:
                        #
                        # print('Цепочка:', trade_circle_a['symbol'], '|', trade_circle_b['symbol'], '|', trade_circle_c['symbol'])
                        # print('Купили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_a'], 'в количестве:', trade_circle_a['final_quantity_coins_without_percent'], 'по цене:', trade_circle_a['price'])
                        # print('Продали:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_b'], 'в количестве:', trade_circle_b['quantity_coins_with_stepSize'], 'по цене:', trade_circle_b['price'], 'и получили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_b'], 'в количестве:', trade_circle_b['final_quantity_coins_without_percent'])
                        # print('Продали:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_c'], 'в количестве:', trade_circle_c['quantity_coins_with_stepSize'], 'по цене:', trade_circle_c['price'], 'и получили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_c'], 'в количестве:', trade_circle_c['final_quantity_coins_without_percent'])
                        # print('Затраты:', costs_main_currency_makerStrategy, main_curency)
                        # print('Прибыль c комиссией:', profit_with_percents)
                        # print('Прибыль без комиссии:', profit_without_percents)
                        # print('Прибыль в % с учётом комиссии:', profit_percent)
                        # print('#' * 72)

                        insert_bd_profitTrade.append({
                            'symbols': trade_circle_a['symbol'] + trade_circle_b['symbol'] + trade_circle_c['symbol'],
                            'symbol_a': trade_circle_a['symbol'],
                            'baseCurrency_a': i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_a'],
                            'quoteAsset_a': i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_a'],
                            'bidPrice_a': i_get_arbitrazh_binance_bookticker_symbol_a['bidPrice'],
                            'bidQty_a': i_get_arbitrazh_binance_bookticker_symbol_a['bidQty'],
                            'askPrice_a': i_get_arbitrazh_binance_bookticker_symbol_a['askPrice'],
                            'askQty_a': i_get_arbitrazh_binance_bookticker_symbol_a['askQty'],
                            'stepSize_a': i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_a'],
                            'symbol_b': trade_circle_b['symbol'],
                            'baseCurrency_b': i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_b'],
                            'quoteAsset_b': i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_b'],
                            'bidPrice_b': i_get_arbitrazh_binance_bookticker_symbol_b['bidPrice'],
                            'bidQty_b': i_get_arbitrazh_binance_bookticker_symbol_b['bidQty'],
                            'askPrice_b': i_get_arbitrazh_binance_bookticker_symbol_b['askPrice'],
                            'askQty_b': i_get_arbitrazh_binance_bookticker_symbol_b['askQty'],
                            'stepSize_b': i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_b'],
                            'symbol_c': trade_circle_c['symbol'],
                            'baseCurrency_c': i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_c'],
                            'quoteAsset_c': i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_c'],
                            'bidPrice_c': i_get_arbitrazh_binance_bookticker_symbol_c['bidPrice'],
                            'bidQty_c': i_get_arbitrazh_binance_bookticker_symbol_c['bidQty'],
                            'askPrice_c': i_get_arbitrazh_binance_bookticker_symbol_c['askPrice'],
                            'askQty_c': i_get_arbitrazh_binance_bookticker_symbol_c['askQty'],
                            'stepSize_c': i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_c'],
                            'time_update': 'None'
                        })

                except:
                    pass

                    #a = Class_counting_trades.f_insert_bd_profitTrade(dict_insert_bd_profitTrade)

    a = Class_counting_trades.f_insert_bd_profitTrade(insert_bd_profitTrade, exchange)
    print('#' * 72)