import decimal
from decimal import Decimal
import sqlite3
import time
import datetime
import requests
import json

from Scripts_arbitrzh_Django import Class_counting_trades

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


# def f_insertBD_profit_trade():
#
#     cursor.execute(
#         F"INSERT INTO arbitrazh_binance_profit_trademaker_bss VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'))",
#         (
#                     symbols_profit_trade,
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf',
#                     'sdfsdf'))


main_curency = 'USDT'
main_amount_currency = int(10)

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

    for i_get_arbitrazh_binance_pairs_strategy_b_s_s in get_arbitrazh_binance_pairs_strategy_b_s_s:

        if i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_a'] == main_curency:

            """ Круг Symbol - A """

            for i_get_arbitrazh_binance_bookticker in get_arbitrazh_binance_bookticker:

                if i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_a'] == i_get_arbitrazh_binance_bookticker['symbol']:

                    """ Стратегия торговли по рынку  """

                    symbol_a_askPrice_takerStrategy = i_get_arbitrazh_binance_bookticker['askPrice']

                    currency_a_without_change_stepSize_takerStrategy = main_amount_currency / float(symbol_a_askPrice_takerStrategy)
                    currency_a_with_change_stepSize_takerStrategy = f_minqty_size_up(currency_a_without_change_stepSize_takerStrategy, i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_a'])

                    final_quantity_coins_circle_a_takerStrategy = currency_a_with_change_stepSize_takerStrategy

                    """ Стратегия торговли по лимитным заявка  """

                    symbol_a_askPrice_makerStrategy = i_get_arbitrazh_binance_bookticker['bidPrice']  # Самая выгодная цена на покупку

                    currency_a_without_change_stepSize_makerStrategy = main_amount_currency / float(symbol_a_askPrice_makerStrategy)  # Количество монет которые можем купить по цене "symbol_a_askPrice_makerStrategy" за количество "main_amount_currency"
                    currency_a_with_change_stepSize_makerStrategy = f_minqty_size_up(currency_a_without_change_stepSize_makerStrategy, i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_a'])  # Округления количества монет которые можем купить

                    final_quantity_coins_circle_a_makerStrategy = currency_a_with_change_stepSize_makerStrategy  # Окончательное количество монет, вместе с округлением, которое можем купить за "main_amount_currency"

                    break

            """ Круг Symbol - B """

            for i_get_arbitrazh_binance_bookticker in get_arbitrazh_binance_bookticker:

                if i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_b'] == i_get_arbitrazh_binance_bookticker['symbol']:

                    """ Стратегия торговли по рынку  """

                    symbol_b_bidPrice_takerStrategy = i_get_arbitrazh_binance_bookticker['bidPrice']

                    currency_b_with_change_stepSize_takerStrategy = f_minqty_size_down(final_quantity_coins_circle_a_takerStrategy, i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_b'])
                    currency_b_without_change_stepSize_takerStrategy = currency_b_with_change_stepSize_takerStrategy * float(symbol_b_bidPrice_takerStrategy)

                    final_quantity_coins_circle_b_takerStrategy = currency_b_without_change_stepSize_takerStrategy

                    """ Стратегия торговли по лимитным заявка  """

                    symbol_b_askPrice_makerStrategy = i_get_arbitrazh_binance_bookticker['askPrice']  # Самая выгодная цена на продажу

                    currency_b_with_change_stepSize_makerStrategy = f_minqty_size_down(final_quantity_coins_circle_a_makerStrategy, i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_b'])
                    currency_b_without_change_stepSize_makerStrategy = currency_b_with_change_stepSize_makerStrategy * float(symbol_b_askPrice_makerStrategy)

                    final_quantity_coins_circle_b_makerStrategy = currency_b_without_change_stepSize_makerStrategy

                    """ Тест """

                    bbbb = Class_counting_trades.f_askPrice_makerStrategy(i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_b'], i_get_arbitrazh_binance_bookticker['askPrice'], final_quantity_coins_circle_a_makerStrategy , i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_b'])

                    break

            """ Круг Symbol - C """

            for i_get_arbitrazh_binance_bookticker in get_arbitrazh_binance_bookticker:

                if i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_c'] == i_get_arbitrazh_binance_bookticker['symbol']:

                    """ Стратегия торговли по рынку  """

                    symbol_c_bidPrice_takerStrategy = i_get_arbitrazh_binance_bookticker['bidPrice']

                    currency_c_with_change_stepSize_takerStrategy = f_minqty_size_down(final_quantity_coins_circle_b_takerStrategy, i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_c'])
                    currency_c_without_change_stepSize_takerStrategy = currency_c_with_change_stepSize_takerStrategy * float(symbol_c_bidPrice_takerStrategy)

                    final_quantity_coins_circle_c_without_procent_takerStrategy = currency_c_without_change_stepSize_takerStrategy

                    """ Стратегия торговли по лимитным заявка  """

                    symbol_c_askPrice_makerStrategy = i_get_arbitrazh_binance_bookticker['askPrice']

                    currency_c_with_change_stepSize_makerStrategy = f_minqty_size_down(final_quantity_coins_circle_b_makerStrategy, i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_c'])
                    currency_c_without_change_stepSize_makerStrategy = currency_c_with_change_stepSize_makerStrategy * float(symbol_c_askPrice_makerStrategy)

                    final_quantity_coins_circle_c_without_procent_makerStrategy = currency_c_without_change_stepSize_makerStrategy

                    """ Тест """

                    cccc = Class_counting_trades.f_askPrice_makerStrategy(i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_c'], i_get_arbitrazh_binance_bookticker['askPrice'], final_quantity_coins_circle_b_makerStrategy, i_get_arbitrazh_binance_pairs_strategy_b_s_s['stepSize_c'])

                    break

            """ Подсчет полученных данных """

            costs_main_currency_takerStrategy = final_quantity_coins_circle_a_takerStrategy * float(symbol_a_askPrice_takerStrategy)  # Количество потраченной основной валюты "main_currency" на круге А
            costs_main_currency_makerStrategy = final_quantity_coins_circle_a_makerStrategy * float(symbol_a_askPrice_makerStrategy)  # Количество потраченной основной валюты "main_currency" на круге А

            """ Расчет комиссии Taker"""
            percentage_for_trading = 0.225 # Комиссия биржи за одну сделку
            c = final_quantity_coins_circle_c_without_procent_takerStrategy / 100 * percentage_for_trading  # Количество комиссии в валюте
            final_quantity_coins_circle_c_with_procent_takerStrategy = final_quantity_coins_circle_c_without_procent_takerStrategy - c  # Финальное количество получаемых монет на последнем круге с учётом комиссии

            """ Расчет комиссии Maker"""
            percentage_for_trading = 0.0  # Комиссия биржи за одну сделку
            c = final_quantity_coins_circle_c_without_procent_makerStrategy / 100 * percentage_for_trading  # Количество комиссии в валюте
            final_quantity_coins_circle_c_with_procent_makerStrategy = final_quantity_coins_circle_c_without_procent_makerStrategy - c  # Финальное количество получаемых монет на последнем круге с учётом комиссии

            """ Если количество получаемых монет на последнем круге больше, чем затраченных монет на первом круге """
            # if final_quantity_coins_circle_c_with_procent_takerStrategy < costs_main_currency:
            #
            #     profit_without_percents = Decimal(final_quantity_coins_circle_c_without_procent_takerStrategy) - Decimal(costs_main_currency)
            #
            #     print('Цепочка:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_a'], '|', i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_b'], '|', i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_c'])
            #     print('Купили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_a'], 'в количестве:', final_quantity_coins_circle_a_takerStrategy, 'по цене:', symbol_a_askPrice_takerStrategy)
            #     print('Продали:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_b'], 'в количестве:', final_quantity_coins_circle_a_takerStrategy, 'по цене:', symbol_b_bidPrice_takerStrategy, 'и получили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_b'], 'в количестве:', final_quantity_coins_circle_b_takerStrategy)
            #     print('Продали:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_c'], 'в количестве:', final_quantity_coins_circle_b_takerStrategy, 'по цене:', symbol_c_bidPrice_takerStrategy, 'и получили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_c'], 'в количестве:', final_quantity_coins_circle_c_without_procent_takerStrategy)
            #     print('Затраты:', costs_main_currency, main_curency)
            #     print('Прибыль без комиссии:', profit_without_percents)
            #     print('Прибыль с комиссией:', final_quantity_coins_circle_c_with_procent_takerStrategy, final_quantity_coins_circle_c_without_procent_takerStrategy)
            #     print('#' * 72)

            profit_without_percents = final_quantity_coins_circle_c_without_procent_makerStrategy - costs_main_currency_makerStrategy
            profit_with_percents = final_quantity_coins_circle_c_with_procent_makerStrategy - costs_main_currency_makerStrategy

            profit_percent = final_quantity_coins_circle_c_with_procent_makerStrategy / costs_main_currency_makerStrategy * 100 - 100  # Формула прибыли в процентах

            if profit_percent < 0:
            # if final_quantity_coins_circle_c_with_procent_makerStrategy > costs_main_currency_makerStrategy:

                # profit_without_percents = final_quantity_coins_circle_c_without_procent_makerStrategy - costs_main_currency_makerStrategy
                # profit_with_percents = final_quantity_coins_circle_c_with_procent_makerStrategy - costs_main_currency_makerStrategy
                #symbols_profit_trade = i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_a'] + i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_b'] + i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_c']


                print('Цепочка:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_a'], '|', i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_b'], '|', i_get_arbitrazh_binance_pairs_strategy_b_s_s['symbol_c'])
                print('Купили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_a'], 'в количестве:', final_quantity_coins_circle_a_makerStrategy, 'по цене:', symbol_a_askPrice_makerStrategy)
                print(bbbb)
                print('Продали:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_b'], 'в количестве:', currency_b_with_change_stepSize_makerStrategy, 'по цене:', symbol_b_askPrice_makerStrategy, 'и получили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_b'], 'в количестве:', final_quantity_coins_circle_b_makerStrategy)
                print(cccc)
                print('Продали:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['baseCurrency_c'], 'в количестве:', currency_c_with_change_stepSize_makerStrategy, 'по цене:', symbol_c_askPrice_makerStrategy, 'и получили:', i_get_arbitrazh_binance_pairs_strategy_b_s_s['quoteAsset_c'], 'в количестве:', final_quantity_coins_circle_c_without_procent_makerStrategy)
                print('Затраты:', costs_main_currency_makerStrategy, main_curency)
                print('Прибыль без комиссии:', profit_without_percents)
                print('Прибыль c комиссии:', profit_with_percents)
                print('Прибыль с комиссией:', final_quantity_coins_circle_c_with_procent_makerStrategy, final_quantity_coins_circle_c_without_procent_makerStrategy)
                print('Прибыль в %Ж', profit_percent)
                print(symbol_b_askPrice_makerStrategy)
                print('#' * 72)



