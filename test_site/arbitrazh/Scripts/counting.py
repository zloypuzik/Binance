from ..models import Binance_profit_tradeMaker_bss
import sqlite3
from ..models import Binance_all_pairs_trading_inf, Bybit_all_pairs_trading_inf, Binance_profit_tradeMaker_bss
from datetime import datetime
from pytz import timezone as tz

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

def def_time_passed(old_time):

    old_time = old_time.replace(tzinfo=None) # Удалить информацию о часовом поясе в дату и время с учетом смещения
    re = datetime.strptime(f'{old_time}', "%Y-%m-%d %H:%M:%S")

    re1 = datetime.strptime(str(datetime.now()), "%Y-%m-%d %H:%M:%S.%f")
    a = re1-re
    a = str(a).split('.')[0] # Убираем миллисекунды
    # old_time = '2024-02-09 20:42:51'
    # old_time = str(old_time)
    # year = int(old_time[0]+old_time[1]+old_time[2]+old_time[3])
    # month = int(old_time[5]+old_time[6])
    # day = int(old_time[8]+old_time[9])
    # hour = int(old_time[11]+old_time[12])
    # minute = int(old_time[14]+old_time[15])
    # second = int(old_time[17]+old_time[18])
    #
    #
    # date = datetime.datetime(year, month, day, hour, minute, second)
    # today = datetime.datetime.now()
    # delta = today - date
    # a = delta.seconds
    # #dsadsa = old_time[17]+old_time[18]
    # #
    # b = datetime(year, month, day, hour, minute, second)
    # a = datetime.now()
    # #
    # # # returns a timedelta object
    # c = a - b
    # # # print('Difference: ', c)
    # #
    # # # returns (minutes, seconds)
    # # # minutes = divmod(c.total_seconds(), 60)
    # # # print('Total difference in minutes: ', minutes[0], 'minutes', minutes[1], 'seconds')
    # #
    # # # returns the difference of the time of the day (minutes, seconds)
    # # # minutes = divmod(c.seconds, 60)
    # # # print('Total difference in minutes: ', minutes[0], 'minutes', minutes[1], 'seconds')
    #
    # days = c.days
    # minutes = divmod(c.seconds, 60)
    # b = f"'Прошло:{days} Дней {minutes[0]}'Минут' {minutes[1]} 'Секунд'"
    # print(type(old_time))
    # a = old_time
    return a

def def_allMainCurrency(exchange):
    """Основные валюты торговых бирж"""

    get_all_pairs_inf = Binance_all_pairs_trading_inf.objects.all()

    # for i in get_all_pairs_inf:
    #     print(i.symbol)


    # print('dddddddddddddddddddddddddd', get_all_pairs_inf)
    # print('dddddddddddddddddddddddddd', type(get_all_pairs_inf))
    #
    allMainCurrency = None

    # for i in get_all_pairs_inf:
    #     # a = i['quoteAsset']
    #     print(i)

    match exchange:

        case "Binance":
            # allMainCurrency = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR',
            #                    'GBR', 'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']

            allMainCurrency = []
            allMainCurrencyKort = []
            for i in get_all_pairs_inf:
                # print(i['quoteAsset_a'])

                if i.quoteAsset in allMainCurrency:
                    pass
                else:
                    allMainCurrency.append(i.quoteAsset)

            for i in allMainCurrency:

                a = (i, i)
                allMainCurrencyKort.append(a)



        case "Kucoin":
            allMainCurrency = ['BTC', 'KCS', 'ETH', 'TRX', 'DOGE', 'USDT', 'TUSD', 'DAI', 'USDC']

    return allMainCurrencyKort

#########################################################


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


def f_get_bd_profitTrade_bss(allMainCurrency):

    a = Binance_profit_tradeMaker_bss.objects.all()
    listId = []

    for i_a in a:
        # print('2342342342342342', i_a.id)
        #print('444444444444444444444444444444444444444444444444', i_a.quoteAsset_a)
        for i_allMainCurrency in allMainCurrency:

            if i_a.quoteAsset_a == i_allMainCurrency:

                listId.append(i_a.id)

    return listId
    # listId = []
    #print('00000000000000000000000000000000000000', a)
    # print(a)
    # print('0' * 72)
    # for i in a.quoteAsset_a:
    #     if i in allMainCurrencyKort
    # return 'ss'
    # return print('0' * 72)


def testprocent(amount_main_currency, commission, selectedMainCurrency, profit_procent):
    # print(type(amount_main_currency), type(commission), type(selectedMainCurrency), type(profit_procent))
    print(amount_main_currency, commission, selectedMainCurrency, profit_procent)
    if commission >= float(0):
        # print('111111', 'sdfsdfsdfsdfsdfsdf')
        # print('111111', selectedMainCurrency)
        # print('111111', commission)
        # print('111111', profit_procent)
        test_dict = []
        # get_all_pairs_inf = Binance_all_pairs_trading_inf.objects.all()
        get_arbitrazh_binance_profit_trademaker_bss = Binance_profit_tradeMaker_bss.objects.all()
        for i_selectedMainCurrency in selectedMainCurrency:
            for i_get_arbitrazh_binance_profit_trademaker_bss in get_arbitrazh_binance_profit_trademaker_bss:
                # if i_selectedMainCurrency == i_get_arbitrazh_binance_profit_trademaker_bss.id:
                if i_selectedMainCurrency == i_get_arbitrazh_binance_profit_trademaker_bss.quoteAsset_a:

                    # print('9999999999999999')
                    # pass
                    # print(i_get_arbitrazh_binance_profit_trademaker_bss.symbol_a)
                    # print(i_get_arbitrazh_binance_profit_trademaker_bss.bidPrice_a)
                    # print(i_get_arbitrazh_binance_profit_trademaker_bss.symbols)
                    #

                    trade_circle_a = f_makerStrategy_bss(
                        symbol=i_get_arbitrazh_binance_profit_trademaker_bss.symbol_a,
                        bid_or_ask='bidPrice',
                        price=i_get_arbitrazh_binance_profit_trademaker_bss.bidPrice_a,
                        stepSize=i_get_arbitrazh_binance_profit_trademaker_bss.stepSize_a,
                        main_amount_currency=amount_main_currency
                    )

                    # print('9999999999999999', amount_main_currency)
                    trade_circle_b = f_makerStrategy_bss(
                        symbol=i_get_arbitrazh_binance_profit_trademaker_bss.symbol_b,
                        bid_or_ask='askPrice',
                        price=i_get_arbitrazh_binance_profit_trademaker_bss.askPrice_b,
                        stepSize=i_get_arbitrazh_binance_profit_trademaker_bss.stepSize_b,
                        quantity_coins=trade_circle_a['final_quantity_coins_without_percent'],
                    )
                    trade_circle_c = f_makerStrategy_bss(
                        symbol=i_get_arbitrazh_binance_profit_trademaker_bss.symbol_c,
                        bid_or_ask='askPrice',
                        price=i_get_arbitrazh_binance_profit_trademaker_bss.askPrice_c,
                        stepSize=i_get_arbitrazh_binance_profit_trademaker_bss.stepSize_c,
                        quantity_coins=trade_circle_b['final_quantity_coins_without_percent']
                    )

            # print()
            try:
                """ Подсчет полученных данных """
                # print('9999999999999999', trade_circle_a)

                costs_main_currency_makerStrategy = trade_circle_a['final_quantity_coins_without_percent'] * trade_circle_a['price']  # Количество потраченной основной валюты "main_currency" на круге А
                # print(costs_main_currency_makerStrategy)

                percentage_for_trading = commission  # Комиссия биржи за одну сделку
                c = trade_circle_c['final_quantity_coins_without_percent'] / 100 * percentage_for_trading  # Количество комиссии в валюте
                final_quantity_coins_circle_c_with_percent_makerStrategy = trade_circle_c['final_quantity_coins_without_percent'] - c  # Финальное количество получаемых монет на последнем круге с учётом комиссии
                # print(trade_circle_a['final_quantity_coins_without_percent'])
                # print(final_quantity_coins_circle_c_with_percent_makerStrategy, costs_main_currency_makerStrategy)

                profit_without_percents = trade_circle_c['final_quantity_coins_without_percent'] - costs_main_currency_makerStrategy  # Расчёт прибыли без комиссии
                profit_with_percents = final_quantity_coins_circle_c_with_percent_makerStrategy - costs_main_currency_makerStrategy  # Расчёт прибыли с комиссией
                profit_percent = final_quantity_coins_circle_c_with_percent_makerStrategy / costs_main_currency_makerStrategy * 100 - 100  # Формула прибыли в процентах
                # print(costs_main_currency_makerStrategy)
                #

                # # test_dict.append(i_selectedMainCurrency, costs_main_currency_makerStrategy, c, final_quantity_coins_circle_c_with_percent_makerStrategy, profit_without_percents, profit_with_percents, profit_percent)
                if profit_percent >= profit_procent:
                    test_dict.append({
                        # 'test': 'asdasasdasddddddddddddddddddddddasdasdasda'
                        'i_selectedMainCurrency': i_selectedMainCurrency,
                        'costs_main_currency_makerStrategy': costs_main_currency_makerStrategy,
                        'c': c,
                        'final_quantity_coins_circle_c_with_percent_makerStrategy': final_quantity_coins_circle_c_with_percent_makerStrategy,
                        'profit_without_percents': profit_without_percents,
                        'profit_with_percents': profit_with_percents,
                        # 'costs_main_currency_makerStrategy': costs_main_currency_makerStrategy,
                        'profit_percent': profit_percent
                    })
            except:
                pass
        #print('0000000000000000000000',test_dict)
            # for i in test_dict:
            #     print('44444', i)
        print('3333333333', test_dict)
        return test_dict