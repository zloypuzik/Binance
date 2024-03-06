# -*- coding: utf8 -*-
import json
import time
import comm

import requests

########################################################################################################

file_step_1_pairs_trade = '../kucoin/1_25_step_1_pairs_trade.json'


def f_file_step_1_pairs_trade():
    with open(file_step_1_pairs_trade) as file_data:
        data_a = json.load(file_data)

    return data_a


########################################################################################################
# Пары с нулевой комисcией (Binance)
#######################################################################################################

zero_commission = []

########################################################################################################
# Валюта, за которую можно купить или продать другие валюты.
########################################################################################################

all_pairs_c = ['BTC', 'KCS', 'ETH', 'TRX', 'DOGE', 'USDT', 'TUSD', 'DAI', 'USDC']

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

# main_commission = float(input('Укажите вашу комиссию в процентах (Например "0,075"):'))

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

    quoteCurrency_main_currency = False
    baseCurrency_main_currency = False

    count_pairs_a_quoteCurrency_mc = 0
    count_pairs_a_baseCurrency_mc = 0
    all_pairs_a = []

    for i in f_file_step_1_pairs_trade():
        if i['quoteCurrency'] == main_currency and i['baseCurrency'] != not_pair_a:
            symbol_a = i['baseCurrency'] + i['quoteCurrency']
            baseCurrency_a = i['baseCurrency']
            quoteCurrency_a = i['quoteCurrency']
            stepSize_base_a = i['baseIncrement']
            stepSize_quote_a = i['quoteIncrement']
            # for ch_stepsize in i['filters']:
            #     if ch_stepsize['filterType'] == 'LOT_SIZE':
            #         stepSize_a = ch_stepsize['stepSize']
            #         break

            commission_a = comm.check_commissions(baseCurrency_a, quoteCurrency_a)

            all_pairs_a.append(
                {
                    'symbol_a_original': i['symbol'],
                    'symbol_a': symbol_a,
                    'baseCurrency_a': baseCurrency_a,
                    'quoteCurrency_a': quoteCurrency_a,
                    'stepSize_base_a': stepSize_base_a,
                    'stepSize_quote_a': stepSize_quote_a,
                    'commission_a': commission_a
                }
            )
            count_pairs_a_quoteCurrency_mc += 1


    all_count_pairs_a = count_pairs_a_quoteCurrency_mc + count_pairs_a_baseCurrency_mc

    print('Найдено:', count_pairs_a_quoteCurrency_mc, 'валют,', 'торгуемые с', main_currency,
          ', где основная валюта "quoteCurrency"')
    print('Найдено:', count_pairs_a_baseCurrency_mc, 'валют,', 'торгуемые с', main_currency,
          ', где основная валюта "baseCurrency"')
    print('Найдено всего:', all_count_pairs_a, 'валют,', 'торгуемые с', main_currency,
          ', (и "baseCurrency", и "quoteCurrency")')
    #
    #     ########################################################################################################
    #     # Ищем все пары которые торгуются с 'main_currency' (из первого круга) и добавляем пару 'B' в список 'all_pairs_b'
    #     ########################################################################################################
    #
    count_pairs_b = 0
    all_pairs_b = []

    for ii in f_file_step_1_pairs_trade():
        for iii in all_pairs_a:
            if ii['quoteCurrency'] != main_currency and ii['baseCurrency'] != main_currency:

                if iii['baseCurrency_a'] == ii['baseCurrency'] or iii['baseCurrency_a'] == ii['quoteCurrency']:
                    symbol_b = ii['baseCurrency'] + ii['quoteCurrency']
                    baseCurrency_b = (ii['baseCurrency'])
                    quoteCurrency_b = (ii['quoteCurrency'])
                    stepSize_base_b = ii['baseIncrement']
                    stepSize_quote_b = ii['quoteIncrement']

                    commission_b = comm.check_commissions(baseCurrency_b, quoteCurrency_b)

                    all_pairs_b.append(
                        {
                            'symbol_b_original': ii['symbol'],
                            'symbol_b': symbol_b,
                            'baseCurrency_b': baseCurrency_b,
                            'quoteCurrency_b': quoteCurrency_b,
                            'stepSize_base_b': stepSize_base_b,
                            'stepSize_quote_b': stepSize_quote_b,
                            'commission_b': commission_b
                        }
                    )
                    count_pairs_b += 1
                    break
                elif iii['quoteCurrency_a'] == ii['baseCurrency'] or iii['quoteCurrency_a'] == ii['quoteCurrency']:
                    symbol_b = ii['baseCurrency'] + ii['quoteCurrency']
                    baseCurrency_b = (ii['baseCurrency'])
                    quoteCurrency_b = (ii['quoteCurrency'])
                    stepSize_base_b = ii['baseIncrement']
                    stepSize_quote_b = ii['quoteIncrement']

                    commission_b = comm.check_commissions(baseCurrency_b, quoteCurrency_b)

                    all_pairs_b.append(
                        {
                            'symbol_b_original': ii['symbol'],
                            'symbol_b': symbol_b,
                            'baseCurrency_b': baseCurrency_b,
                            'quoteCurrency_b': quoteCurrency_b,
                            'stepSize_base_b': stepSize_base_b,
                            'stepSize_quote_b': stepSize_quote_b,
                            'commission_b': commission_b
                        }
                    )
                    count_pairs_b += 1
                    break
    print('Найдено:', count_pairs_b, 'возможных пар, для торговли второго круга')

    ########################################################################################################

    count_pairs_c = 0
    pairs_buy_para_b = []

    for t in all_pairs_a:
        for tt in all_pairs_b:
            if t['quoteCurrency_a'] == main_currency:
                if t['baseCurrency_a'] == tt['baseCurrency_b']:
                    pairs_buy_para_b.append(
                        {
                            'symbol_a_original': t['symbol_a_original'],
                            'symbol_a': t['symbol_a'],
                            'baseCurrency_a': t['baseCurrency_a'],
                            'quoteCurrency_a': t['quoteCurrency_a'],
                            'stepSize_base_a': t['stepSize_base_a'],
                            'stepSize_quote_a': t['stepSize_quote_a'],
                            'commission_a': t['commission_a'],

                            'symbol_b_original': tt['symbol_b_original'],
                            'symbol_b': tt['symbol_b'],
                            'baseCurrency_b': tt['baseCurrency_b'],
                            'quoteCurrency_b': tt['quoteCurrency_b'],
                            'stepSize_base_b': tt['stepSize_base_b'],
                            'stepSize_quote_b': tt['stepSize_quote_b'],
                            'commission_b': tt['commission_b'],
                            'trade_pair_c': tt['quoteCurrency_b']
                        }
                    )
                    count_pairs_c += 1

                elif t['baseCurrency_a'] == tt['quoteCurrency_b']:
                    pairs_buy_para_b.append(
                        {
                            'symbol_a_original': t['symbol_a_original'],
                            'symbol_a': t['symbol_a'],
                            'baseCurrency_a': t['baseCurrency_a'],
                            'quoteCurrency_a': t['quoteCurrency_a'],
                            'stepSize_base_a': t['stepSize_base_a'],
                            'stepSize_quote_a': t['stepSize_quote_a'],
                            'commission_a': t['commission_a'],

                            'symbol_b_original': tt['symbol_b_original'],
                            'symbol_b': tt['symbol_b'],
                            'baseCurrency_b': tt['baseCurrency_b'],
                            'quoteCurrency_b': tt['quoteCurrency_b'],
                            'stepSize_base_b': tt['stepSize_base_b'],
                            'stepSize_quote_b': tt['stepSize_quote_b'],
                            'commission_b': tt['commission_b'],
                            'trade_pair_c': tt['baseCurrency_b']
                        }
                    )
                    count_pairs_c += 1

            if t['baseCurrency_a'] == main_currency:
                if t['quoteCurrency_a'] == tt['quoteCurrency_b']:
                    pairs_buy_para_b.append(
                        {
                            'symbol_a_original': t['symbol_a_original'],
                            'symbol_a': t['symbol_a'],
                            'baseCurrency_a': t['baseCurrency_a'],
                            'quoteCurrency_a': t['quoteCurrency_a'],
                            'stepSize_base_a': t['stepSize_base_a'],
                            'stepSize_quote_a': t['stepSize_quote_a'],
                            'commission_a': t['commission_a'],

                            'symbol_b_original': tt['symbol_b_original'],
                            'symbol_b': tt['symbol_b'],
                            'baseCurrency_b': tt['baseCurrency_b'],
                            'quoteCurrency_b': tt['quoteCurrency_b'],
                            'stepSize_base_b': tt['stepSize_base_b'],
                            'stepSize_quote_b': tt['stepSize_quote_b'],
                            'commission_b': tt['commission_b'],
                            'trade_pair_c': tt['baseCurrency_b']
                        }
                    )
                    count_pairs_c += 1

                elif t['quoteCurrency_a'] == tt['baseCurrency_b']:
                    pairs_buy_para_b.append(
                        {
                            'symbol_a_original': t['symbol_a_original'],
                            'symbol_a': t['symbol_a'],
                            'baseCurrency_a': t['baseCurrency_a'],
                            'quoteCurrency_a': t['quoteCurrency_a'],
                            'stepSize_base_a': t['stepSize_base_a'],
                            'stepSize_quote_a': t['stepSize_quote_a'],
                            'commission_a': t['commission_a'],

                            'symbol_b_original': tt['symbol_b_original'],
                            'symbol_b': tt['symbol_b'],
                            'baseCurrency_b': tt['baseCurrency_b'],
                            'quoteCurrency_b': tt['quoteCurrency_b'],
                            'stepSize_base_b': tt['stepSize_base_b'],
                            'stepSize_quote_b': tt['stepSize_quote_b'],
                            'commission_b': tt['commission_b'],
                            'trade_pair_c': tt['quoteCurrency_b']
                        }
                    )
                    count_pairs_c += 1

    test = 0

    count_pairs_cc = 0
    pairs_buy_para_c = []

    for y in pairs_buy_para_b:
        for u in f_file_step_1_pairs_trade():
            if u['baseCurrency'] == main_currency and u['quoteCurrency'] == y['trade_pair_c']:
                stepSize_base_c = u['baseIncrement']
                stepSize_quote_c = u['quoteIncrement']
                symbol_c = u['baseCurrency'] + u['quoteCurrency']
                commission_c = comm.check_commissions(u['baseCurrency'], u['quoteCurrency'])

                pairs_buy_para_c.append(
                    {
                        'main_currency': main_currency,
                        'symbol_a_original': y['symbol_a_original'],
                        'symbol_a': y['symbol_a'],
                        'baseCurrency_a': y['baseCurrency_a'],
                        'quoteCurrency_a': y['quoteCurrency_a'],
                        'stepSize_base_a': f_step_size(y['stepSize_base_a']),
                        'stepSize_quote_a': f_step_size(y['stepSize_quote_a']),
                        'commission_a': y['commission_a'],

                        'symbol_b_original': y['symbol_b_original'],
                        'symbol_b': y['symbol_b'],
                        'baseCurrency_b': y['baseCurrency_b'],
                        'quoteCurrency_b': y['quoteCurrency_b'],
                        'stepSize_base_b': f_step_size(y['stepSize_base_b']),
                        'stepSize_quote_b': f_step_size(y['stepSize_quote_b']),
                        'commission_b': y['commission_b'],

                        'symbol_c_original': u['symbol'],
                        'symbol_c': symbol_c,
                        'baseCurrency_c': u['baseCurrency'],
                        'quoteCurrency_c': u['quoteCurrency'],
                        'stepSize_base_c': f_step_size(stepSize_base_c),
                        'stepSize_quote_c': f_step_size(stepSize_quote_c),
                        'commission_c': commission_c
                    }
                )

                count_pairs_cc += 1

    for y in pairs_buy_para_b:
        for u in f_file_step_1_pairs_trade():
            if u['quoteCurrency'] == main_currency and u['baseCurrency'] == y['trade_pair_c']:
                stepSize_base_c = u['baseIncrement']
                stepSize_quote_c = u['quoteIncrement']
                symbol_c = u['baseCurrency'] + u['quoteCurrency']
                commission_c = comm.check_commissions(u['baseCurrency'], u['quoteCurrency'])


                pairs_buy_para_c.append(
                    {
                        'main_currency': main_currency,
                        'symbol_a_original': y['symbol_a_original'],
                        'symbol_a': y['symbol_a'],
                        'baseCurrency_a': y['baseCurrency_a'],
                        'quoteCurrency_a': y['quoteCurrency_a'],
                        'stepSize_base_a': f_step_size(y['stepSize_base_a']),
                        'stepSize_quote_a': f_step_size(y['stepSize_quote_a']),
                        'commission_a': y['commission_a'],

                        'symbol_b_original': y['symbol_b_original'],
                        'symbol_b': y['symbol_b'],
                        'baseCurrency_b': y['baseCurrency_b'],
                        'quoteCurrency_b': y['quoteCurrency_b'],
                        'stepSize_base_b': f_step_size(y['stepSize_base_b']),
                        'stepSize_quote_b': f_step_size(y['stepSize_quote_b']),
                        'commission_b': y['commission_b'],

                        'symbol_c_original': u['symbol'],
                        'symbol_c': symbol_c,
                        'baseCurrency_c': u['baseCurrency'],
                        'quoteCurrency_c': u['quoteCurrency'],
                        'stepSize_base_c': f_step_size(stepSize_base_c),
                        'stepSize_quote_c': f_step_size(stepSize_quote_c),
                        'commission_c': commission_c
                    }
                )
            count_pairs_cc += 1

    print('Найдено и записано:', count_pairs_cc, 'пар для торговли по трем кругам')

    # print(pairs_buy_para_c[0])
    # print(pairs_buy_para_c[1])
    # x = 0
    # y = 0
    # z = 0
    # d = 0
    # dd = 0
    # ddd = 0
    # pairs_buy_para_cc = []
    # for ll in pairs_buy_para_c:
    #     x += 1
    #
    #     for pp in commission_class_a:
    #         mm1 = False
    #         mmm1 = False
    #         if ll['baseCurrency_a'] == pp:
    #             mm1 = True
    #             break
    #     for ppp in commission_class_a:
    #         if ll['quoteCurrency_a'] == ppp:
    #             mmm1 = True
    #             break
    #     if mm1 and mmm1:
    #         #print(ll['baseCurrency_a'], ll['quoteCurrency_a'])
    #         y += 1
    #     # else:
    #     #     print(ll['baseCurrency_a'], ll['quoteCurrency_a'])
    #     ##################################################
    #     for pp in commission_class_a:
    #         mm2 = False
    #         mmm2 = False
    #         if ll['baseCurrency_b'] == pp:
    #             mm2 = True
    #             break
    #     for ppp in commission_class_a:
    #         if ll['quoteCurrency_b'] == ppp:
    #             mmm2 = True
    #             break
    #     if mm2 and mmm2:
    #         z += 1
    #     # else:
    #     #     print(ll['baseCurrency_b'], ll['quoteCurrency_b'])
    #     ##################################################
    #     for pp in commission_class_a:
    #         mm3 = False
    #         mmm3 = False
    #         if ll['baseCurrency_c'] == pp:
    #             mm3 = True
    #             break
    #     for ppp in commission_class_a:
    #         if ll['quoteCurrency_c'] == ppp:
    #             mmm3 = True
    #             break
    #     if mm3 and mmm3:
    #         d += 1
    #     if mm1 and mmm1 and mm2 and mmm2 and mm3 and mmm3:
    #         pairs_buy_para_cc.append(ll)
    #         # time.sleep(1)
    #     else:
    #
    #         dd += 1
    # print(dd)
            # print(ll['baseCurrency_c'], ll['quoteCurrency_c'])
        # else:
        #     print(ll['baseCurrency_b'], ll['quoteCurrency_b'])
        # break

        #for pp in commission_class_a:
                # for xxx in commission_class_a:
                #     if ll['quoteCurrency_a'] != xxx:
                #         print(pp)
                #         print(ll['baseCurrency_a'], ll['quoteCurrency_a'])
                #         z += 1
                #         break
                #break
        # for ppp in commission_class_a:
        #     if ll['baseCurrency_b'] or ll['quoteCurrency_b'] == ppp:
        #
        #                 for pppp in commission_class_a:
        #                     if ll['baseCurrency_c'] or ll['quoteCurrency_c'] == pppp:
        #                         y += 1
        #                         print(y)
        #                         with open('1_pairs_buy_para_b_test.json', 'w') as file3:
        #                             json.dump(pairs_buy_para_c, file3, indent=2)
        # continue

    # print(x)
    # print(y)
    # print(z)
    # print(d)
    # print(ddd)
        # #                 print()
        #
        # print(ll['symbol_b_original'])
    # for uuu in pairs_buy_para_cc:
    #     print(uuu)
    with open('1_pairs_buy_para_b_test.json', 'w') as file3:
        json.dump(pairs_buy_para_c, file3, indent=2)


else:
    print('Вы ввели не существующую валюту', "'", main_currency, "'", ', введите правильную валюту')
