# -*- coding: utf8 -*-
import json

########################################################################################################

file_step_1_pairs_trade = '../Binance_ETH/1_25_step_1_pairs_trade.json'


def f_file_step_1_pairs_trade():
    with open(file_step_1_pairs_trade) as file_data:
        data_a = json.load(file_data)

    return data_a


########################################################################################################
# Пары с нулевой комисcией (Binance)
#######################################################################################################

zero_commission = ['BTCUSDT', 'BTCAUD', 'BTCBIDR', 'BTCBRL', 'BTCBUSD', 'BTCEUR', 'BTCGBP', 'BTCRUB', 'BTCTRY',
                   'BTCTUSD', 'BTCUAH', 'BTCUSDC', 'BTCUSDP', 'BTCUSD', 'BUSDUSDT', 'TUSDBUSD', 'TUSDUSDT', 'USDCBUSD',
                   'USDCUSDT', 'USDPBUSD', 'USDPUSDT']

########################################################################################################
# Валюта, за которую можно купить или продать другие валюты.
########################################################################################################

all_pairs_c = ['BUSD', 'USDT', 'BNB', 'BTC', 'ETH', 'XRP', 'TRX', 'DOGE', 'DOT', 'AUD', 'BIDR', 'BRL', 'EUR', 'GBR',
               'RUB', 'TRY', 'DAI', 'UAH', 'ZAR', 'VAI', 'IDRT', 'NGN', 'PLN']

########################################################################################################
# Для выбора основной валюты
########################################################################################################

main_currency = input('Введите базовую валюту (Например "ETH"):')

check_main_currency = False

for check_currency in all_pairs_c:  # Проверка на правильность ввода основной валюты (main_currency)
    if main_currency == check_currency:
        check_main_currency = True
        break  # Если вводимая валюта совпадает с валютой из списка 'all_pairs_c', то прекращаем проверку.
    else:
        check_main_currency = False

########################################################################################################
# Для выбора комиссии на Бирже
########################################################################################################

main_commission = float(input('Укажите вашу комиссию в процентах (Например "0,075"):'))

########################################################################################################
# Убрать вторую валюту из первого круга
########################################################################################################

not_pair_a = str(input('Укажите вашу для исключения из первого круга:'))

########################################################################################################
# Функция, чтоб убрать нули после 1
########################################################################################################


def f_step_size(stepSize):

    for check_stepSize in range(len(stepSize) - 1, 0, -1):
        if stepSize[check_stepSize] != str(0):
            stepSize = (stepSize[0:check_stepSize + 1])
            break

    if stepSize == '1.':
        stepSize = '1.0'

    return stepSize
########################################################################################################


if check_main_currency:  # если основная валюта (main_currency) ровна 'True'

    ########################################################################################################
    # Проверяем кем является 'main_currency' относительно других основных монет
    ########################################################################################################

    # main_currency_quoteAsset_b = []
    # quoteAsset_b_main_currency = []
    #
    # for test in f_file_step_1_pairs_trade():
    #     if test['baseAsset'] == main_currency:
    #         main_currency_quoteAsset_b.append(test['quoteAsset'])
    #
    # # Пример: ETH/UAH
    #
    # for test2 in f_file_step_1_pairs_trade():
    #     if test2['quoteAsset'] == main_currency:
    #         for test22 in all_pairs_c:
    #             if test2['baseAsset'] == test22:
    #                 quoteAsset_b_main_currency.append(test2['baseAsset'])
    # print(quoteAsset_b_main_currency)
    #
    # # Пример: BNB/ETH

    ########################################################################################################
    # Если в общем словаре "file_step_1_pairs_trade" вторая валюта это 'main_currency', то добавляем пару 'A' в список 'all_pairs_a'
    ########################################################################################################

    quoteAsset_main_currency = False
    baseAsset_main_currency = False

    count_pairs_a_quoteAsset_mc = 0
    count_pairs_a_baseAsset_mc = 0
    all_pairs_a = []

    for i in f_file_step_1_pairs_trade():
        if i['quoteAsset'] == main_currency and i['baseAsset'] != not_pair_a:
            symbol_a = (i['symbol'])
            baseAsset_a = (i['baseAsset'])
            quoteAsset_a = (i['quoteAsset'])
            for ch_stepsize in i['filters']:
                if ch_stepsize['filterType'] == 'LOT_SIZE':
                    stepSize_a = ch_stepsize['stepSize']
                    break
            #stepSize_a = (i['filters'][1]['stepSize'])
            commission_a = main_commission
            for commission in zero_commission:

                if symbol_a == commission:
                    commission_a = float(0.0)
                    break
                else:
                    commission_a = main_commission

            all_pairs_a.append(
                {
                    'symbol_a': symbol_a,
                    'baseAsset_a': baseAsset_a,
                    'quoteAsset_a': quoteAsset_a,
                    'stepSize_a': stepSize_a,
                    'commission_a': commission_a
                }
            )
            count_pairs_a_quoteAsset_mc += 1
        # elif i['baseAsset'] == main_currency and i['quoteAsset'] != not_pair_a:
        #     symbol_a = (i['symbol'])
        #     baseAsset_a = (i['baseAsset'])
        #     quoteAsset_a = (i['quoteAsset'])
        #     for ch_stepsize in i['filters']:
        #         if ch_stepsize['filterType'] == 'LOT_SIZE':
        #             stepSize_a = ch_stepsize['stepSize']
        #             break
        #     #stepSize_a = (i['filters'][1]['stepSize'])
        #     commission_a = main_commission
        #     for commission in zero_commission:
        #
        #         if symbol_a == commission:
        #             commission_a = float(0.0)
        #             break
        #         else:
        #             commission_a = main_commission
        #
        #     all_pairs_a.append(
        #         {
        #             'symbol_a': symbol_a,
        #             'baseAsset_a': baseAsset_a,
        #             'quoteAsset_a': quoteAsset_a,
        #             'stepSize_a': stepSize_a,
        #             'commission_a': commission_a
        #         }
        #     )
        #     count_pairs_a_baseAsset_mc += 1
        # elif (i['baseAsset']) == main_currency:
        #     count_pairs_a_baseAsset_mc += 1
        #     print(i)

    all_count_pairs_a = count_pairs_a_quoteAsset_mc + count_pairs_a_baseAsset_mc

    print('Найдено:', count_pairs_a_quoteAsset_mc, 'валют,', 'торгуемые с', main_currency,
          ', где основная валюта "quoteAsset"')
    print('Найдено:', count_pairs_a_baseAsset_mc, 'валют,', 'торгуемые с', main_currency,
          ', где основная валюта "baseAsset"')
    print('Найдено всего:', all_count_pairs_a, 'валют,', 'торгуемые с', main_currency,
          ', (и "baseAsset", и "quoteAsset")')

    # for i in all_pairs_a:
    #     print(i)
    ########################################################################################################
    # Ищем все пары которые торгуются с 'main_currency' (из первого круга) и добавляем пару 'B' в список 'all_pairs_b'
    ########################################################################################################

    count_pairs_b = 0
    all_pairs_b = []

    for ii in f_file_step_1_pairs_trade():
        for iii in all_pairs_a:
            if ii['quoteAsset'] != main_currency and ii['baseAsset'] != main_currency:

                if iii['baseAsset_a'] == ii['baseAsset'] or iii['baseAsset_a'] == ii['quoteAsset']:
                    symbol_b = (ii['symbol'])
                    baseAsset_b = (ii['baseAsset'])
                    quoteAsset_b = (ii['quoteAsset'])
                    for ch_stepsize in ii['filters']:
                        if ch_stepsize['filterType'] == 'LOT_SIZE':
                            stepSize_b = ch_stepsize['stepSize']
                            break
                    #stepSize_b = (ii['filters'][1]['stepSize'])
                    commission_b = main_commission
                    for commission in zero_commission:

                        if symbol_b == commission:
                            commission_b = float(0.0)
                            break
                        else:
                            commission_b = main_commission

                    all_pairs_b.append(
                        {
                            'symbol_b': symbol_b,
                            'baseAsset_b': baseAsset_b,
                            'quoteAsset_b': quoteAsset_b,
                            'stepSize_b': stepSize_b,
                            'commission_b': commission_b
                        }
                    )
                    count_pairs_b += 1
                    break
                elif iii['quoteAsset_a'] == ii['baseAsset'] or iii['quoteAsset_a'] == ii['quoteAsset']:
                    symbol_b = (ii['symbol'])
                    baseAsset_b = (ii['baseAsset'])
                    quoteAsset_b = (ii['quoteAsset'])
                    for ch_stepsize in ii['filters']:
                        if ch_stepsize['filterType'] == 'LOT_SIZE':
                            stepSize_b = ch_stepsize['stepSize']
                            break
                    #stepSize_b = (ii['filters'][1]['stepSize'])
                    commission_b = main_commission
                    for commission in zero_commission:

                        if symbol_b == commission:
                            commission_b = float(0.0)
                            break
                        else:
                            commission_b = main_commission

                    all_pairs_b.append(
                        {
                            'symbol_b': symbol_b,
                            'baseAsset_b': baseAsset_b,
                            'quoteAsset_b': quoteAsset_b,
                            'stepSize_b': stepSize_b,
                            'commission_b': commission_b
                        }
                    )
                    count_pairs_b += 1
                    break
    print('Найдено:', count_pairs_b, 'возможных пар, для торговли второго круга')
    # for i in all_pairs_b:
    #     print(i)

    ########################################################################################################

    count_pairs_c = 0
    pairs_buy_para_b = []

    for t in all_pairs_a:
        for tt in all_pairs_b:
            if t['quoteAsset_a'] == main_currency:
                if t['baseAsset_a'] == tt['baseAsset_b']:
                    pairs_buy_para_b.append(
                        {
                            'symbol_a': t['symbol_a'],
                            'baseAsset_a': t['baseAsset_a'],
                            'quoteAsset_a': t['quoteAsset_a'],
                            'stepSize_a': t['stepSize_a'],
                            'commission_a': t['commission_a'],

                            'symbol_b': tt['symbol_b'],
                            'baseAsset_b': tt['baseAsset_b'],
                            'quoteAsset_b': tt['quoteAsset_b'],
                            'stepSize_b': tt['stepSize_b'],
                            'commission_b': tt['commission_b'],
                            'trade_pair_c': tt['quoteAsset_b']
                        }
                    )
                    count_pairs_c += 1

                elif t['baseAsset_a'] == tt['quoteAsset_b']:
                    pairs_buy_para_b.append(
                        {
                            'symbol_a': t['symbol_a'],
                            'baseAsset_a': t['baseAsset_a'],
                            'quoteAsset_a': t['quoteAsset_a'],
                            'stepSize_a': t['stepSize_a'],
                            'commission_a': t['commission_a'],

                            'symbol_b': tt['symbol_b'],
                            'baseAsset_b': tt['baseAsset_b'],
                            'quoteAsset_b': tt['quoteAsset_b'],
                            'stepSize_b': tt['stepSize_b'],
                            'commission_b': tt['commission_b'],
                            'trade_pair_c': tt['baseAsset_b']
                        }
                    )
                    count_pairs_c += 1

                # elif t['baseAsset_a'] == tt['quoteAsset_b']:
                # print(t, tt)

            if t['baseAsset_a'] == main_currency:
                if t['quoteAsset_a'] == tt['quoteAsset_b']:
                    pairs_buy_para_b.append(
                        {
                            'symbol_a': t['symbol_a'],
                            'baseAsset_a': t['baseAsset_a'],
                            'quoteAsset_a': t['quoteAsset_a'],
                            'stepSize_a': t['stepSize_a'],
                            'commission_a': t['commission_a'],

                            'symbol_b': tt['symbol_b'],
                            'baseAsset_b': tt['baseAsset_b'],
                            'quoteAsset_b': tt['quoteAsset_b'],
                            'stepSize_b': tt['stepSize_b'],
                            'commission_b': tt['commission_b'],
                            'trade_pair_c': tt['baseAsset_b']
                        }
                    )
                    count_pairs_c += 1

                elif t['quoteAsset_a'] == tt['baseAsset_b']:
                    pairs_buy_para_b.append(
                        {
                            'symbol_a': t['symbol_a'],
                            'baseAsset_a': t['baseAsset_a'],
                            'quoteAsset_a': t['quoteAsset_a'],
                            'stepSize_a': t['stepSize_a'],
                            'commission_a': t['commission_a'],

                            'symbol_b': tt['symbol_b'],
                            'baseAsset_b': tt['baseAsset_b'],
                            'quoteAsset_b': tt['quoteAsset_b'],
                            'stepSize_b': tt['stepSize_b'],
                            'commission_b': tt['commission_b'],
                            'trade_pair_c': tt['quoteAsset_b']
                        }
                    )
                    count_pairs_c += 1

            # print(t, tt)
    test = 0
    # print(count_pairs_c)
    # for i in pairs_buy_para_b:
    #     test += 1
    #     print(i)
    # print(test)
    ########################################################################################################

    count_pairs_cc = 0
    pairs_buy_para_c = []

    for y in pairs_buy_para_b:
        for u in f_file_step_1_pairs_trade():
            if u['baseAsset'] == main_currency and u['quoteAsset'] == y['trade_pair_c']:
                for ch_stepsize in u['filters']:
                    if ch_stepsize['filterType'] == 'LOT_SIZE':
                        stepSize_c = ch_stepsize['stepSize']
                        break
                #stepSize_c = u['filters'][1]['stepSize']
                commission_c = main_commission

                for commission in zero_commission:

                    if u['symbol'] == commission:
                        commission_c = float(0.0)
                        break
                    else:
                        commission_c = main_commission

                pairs_buy_para_c.append(
                    {
                        'main_currency': main_currency,
                        'symbol_a': y['symbol_a'],
                        'baseAsset_a': y['baseAsset_a'],
                        'quoteAsset_a': y['quoteAsset_a'],
                        'stepSize_a': f_step_size(y['stepSize_a']),
                        'commission_a': y['commission_a'],

                        'symbol_b': y['symbol_b'],
                        'baseAsset_b': y['baseAsset_b'],
                        'quoteAsset_b': y['quoteAsset_b'],
                        'stepSize_b': f_step_size(y['stepSize_b']),
                        'commission_b': y['commission_b'],

                        'symbol_c': u['symbol'],
                        'baseAsset_c': u['baseAsset'],
                        'quoteAsset_c': u['quoteAsset'],
                        'stepSize_c': f_step_size(stepSize_c),
                        'commission_c': commission_c
                    }
                )

                count_pairs_cc += 1

    for y in pairs_buy_para_b:
        for u in f_file_step_1_pairs_trade():
            if u['quoteAsset'] == main_currency and u['baseAsset'] == y['trade_pair_c']:
                for ch_stepsize in u['filters']:
                    if ch_stepsize['filterType'] == 'LOT_SIZE':
                        stepSize_c = ch_stepsize['stepSize']
                        break
                #stepSize_c = u['filters'][1]['stepSize']
                commission_c = main_commission

                for commission in zero_commission:

                    if u['symbol'] == commission:
                        commission_c = float(0.0)
                        break
                    else:
                        commission_c = main_commission

                pairs_buy_para_c.append(
                    {
                        'main_currency': main_currency,
                        'symbol_a': y['symbol_a'],
                        'baseAsset_a': y['baseAsset_a'],
                        'quoteAsset_a': y['quoteAsset_a'],
                        'stepSize_a': f_step_size(y['stepSize_a']),
                        'commission_a': y['commission_a'],

                        'symbol_b': y['symbol_b'],
                        'baseAsset_b': y['baseAsset_b'],
                        'quoteAsset_b': y['quoteAsset_b'],
                        'stepSize_b': f_step_size(y['stepSize_b']),
                        'commission_b': y['commission_b'],

                        'symbol_c': u['symbol'],
                        'baseAsset_c': u['baseAsset'],
                        'quoteAsset_c': u['quoteAsset'],
                        'stepSize_c': f_step_size(stepSize_c),
                        'commission_c': commission_c
                    }
                )

                count_pairs_cc += 1

    # for y in pairs_buy_para_b:
    #     for yy in main_currency_quoteAsset_b:
    #         if y['quoteAsset_b'] == yy:
    #             #print(y, yy)
    #             symbol_c = main_currency + y['quoteAsset_b']
    #             #print(symbol_c)
    #             for u in f_file_step_1_pairs_trade():
    #                 if u['symbol'] == symbol_c:
    #                     stepSize_c = u['filters'][1]['stepSize']
    #                     commission_c = main_commission
    #
    #                     for commission in zero_commission:
    #
    #                         if symbol_c == commission:
    #                             commission_c = float(0.0)
    #                             break
    #                         else:
    #                             commission_c = main_commission
    #
    #                     pairs_buy_para_c.append(
    #                         {
    #                             'symbol_a': y['symbol_a'],
    #                             'baseAsset_a': y['baseAsset_a'],
    #                             'quoteAsset_a': y['quoteAsset_a'],
    #                             'stepSize_a': y['stepSize_a'],
    #                             'commission_a': y['commission_a'],
    #
    #                             'symbol_b': y['symbol_b'],
    #                             'baseAsset_b': y['baseAsset_b'],
    #                             'quoteAsset_b': y['quoteAsset_b'],
    #                             'stepSize_b': y['stepSize_b'],
    #                             'commission_b': y['commission_b'],
    #
    #
    #                             'symbol_c': symbol_c,
    #                             'baseAsset_c': main_currency,
    #                             'quoteAsset_c': y['quoteAsset_b'],
    #                             'stepSize_c': stepSize_c,
    #                             'commission_c': commission_c
    #                         }
    #                     )
    #
    #             count_pairs_cc += 1
    #
    #     for yyy in quoteAsset_b_main_currency:
    #         if y['quoteAsset_b'] == yyy:
    #             symbol_c = y['quoteAsset_b'] + main_currency
    #             for u in f_file_step_1_pairs_trade():
    #                 if u['symbol'] == symbol_c:
    #                     stepSize_c = u['filters'][1]['stepSize']
    #                     commission_c = main_commission
    #
    #                     for commission in zero_commission:
    #
    #                         if symbol_c == commission:
    #                             commission_c = float(0.0)
    #                             break
    #                         else:
    #                             commission_c = main_commission
    #
    #                     pairs_buy_para_c.append(
    #                         {
    #                             'symbol_a': y['symbol_a'],
    #                             'baseAsset_a': y['baseAsset_a'],
    #                             'quoteAsset_a': y['quoteAsset_a'],
    #                             'stepSize_a': y['stepSize_a'],
    #                             'commission_a': y['commission_a'],
    #
    #                             'symbol_b': y['symbol_b'],
    #                             'baseAsset_b': y['baseAsset_b'],
    #                             'quoteAsset_b': y['quoteAsset_b'],
    #                             'stepSize_b': y['stepSize_b'],
    #                             'commission_b': y['commission_b'],
    #
    #                             'symbol_c': symbol_c,
    #                             'baseAsset_c': y['quoteAsset_b'],
    #                             'quoteAsset_c': main_currency,
    #                             'stepSize_c': stepSize_c,
    #                             'commission_c': commission_c
    #                         }
    #                     )
    #
    #             count_pairs_cc += 1
    #
    print('Найдено и записано:', count_pairs_cc, 'пар для торговли по трем кругам')
    # for i in pairs_buy_para_c:
    #     print(i)
    #
    with open('1_pairs_buy_para_b_test.json', 'w') as file3:
        json.dump(pairs_buy_para_c, file3, indent=2)


else:
    print('Вы ввели не существующую валюту', "'", main_currency, "'", ', введите правильную валюту')
