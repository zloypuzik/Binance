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

main_commission = float(input('Укажите вашу коммисию в процентах (Например "0,075"):'))

if check_main_currency:  # если основная валюта (main_currency) ровна 'True'

    ########################################################################################################
    # Проверяем кем является 'main_currency' относительно других основных монет
    ########################################################################################################

    main_currency_quoteAsset_b = []
    quoteAsset_b_main_currency = []

    for test in f_file_step_1_pairs_trade():
        if test['baseAsset'] == main_currency:
            main_currency_quoteAsset_b.append(test['quoteAsset'])

    # Пример: ETH/UAH

    for test2 in f_file_step_1_pairs_trade():
        if test2['quoteAsset'] == main_currency:
            for test22 in all_pairs_c:
                if test2['baseAsset'] == test22:
                    quoteAsset_b_main_currency.append(test2['baseAsset'])

    # Пример: BNB/ETH

    ########################################################################################################
    # Если в общем словаре "file_step_1_pairs_trade" вторая валюта это 'main_currency', то добавляем пару 'A' в список 'all_pairs_a'
    ########################################################################################################

    count_pairs_a = 0
    all_pairs_a = []

    for i in f_file_step_1_pairs_trade():
        if (i['quoteAsset']) == main_currency:
            symbol_a = (i['symbol'])
            baseAsset_a = (i['baseAsset'])
            quoteAsset_a = (i['quoteAsset'])
            stepSize_a = (i['filters'][1]['stepSize'])
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
            count_pairs_a += 1

    print('Найдено:', count_pairs_a, 'валют,', 'торгуемые с', main_currency)

    ########################################################################################################
    # Ищем все пары которые торгуются с 'main_currency' (из первого круга) и добавляем пару 'B' в список 'all_pairs_b'
    ########################################################################################################

    count_pairs_b = 0
    all_pairs_b = []

    for ii in f_file_step_1_pairs_trade():
        for iii in all_pairs_a:
            if (iii['baseAsset_a']) == (ii['baseAsset']) and (ii['quoteAsset'] != main_currency):
                symbol_b = (ii['symbol'])
                baseAsset_b = (ii['baseAsset'])
                quoteAsset_b = (ii['quoteAsset'])
                stepSize_b = (ii['filters'][1]['stepSize'])
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

    print('Найдено:', count_pairs_b, 'возможных пар, для торговли второго круга')

    ########################################################################################################

    count_pairs_c = 0
    pairs_buy_para_b = []

    for t in all_pairs_a:
        for tt in all_pairs_b:
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
                        'commission_b': tt['commission_b']
                    }
                )
                count_pairs_c += 1

    ########################################################################################################

    count_pairs_cc = 0
    pairs_buy_para_c = []

    for y in pairs_buy_para_b:
        for yy in main_currency_quoteAsset_b:
            if y['quoteAsset_b'] == yy:
                symbol_c = main_currency + y['quoteAsset_b']
                for u in f_file_step_1_pairs_trade():
                    if u['symbol'] == symbol_c:
                        stepSize_c = u['filters'][1]['stepSize']
                        commission_c = main_commission

                        for commission in zero_commission:

                            if symbol_c == commission:
                                commission_c = float(0.0)
                                break
                            else:
                                commission_c = main_commission

                        pairs_buy_para_c.append(
                            {
                                'symbol_a': y['symbol_a'],
                                'baseAsset_a': y['baseAsset_a'],
                                'quoteAsset_a': y['quoteAsset_a'],
                                'stepSize_a': y['stepSize_a'],
                                'commission_a': y['commission_a'],

                                'symbol_b': y['symbol_b'],
                                'baseAsset_b': y['baseAsset_b'],
                                'quoteAsset_b': y['quoteAsset_b'],
                                'stepSize_b': y['stepSize_b'],
                                'commission_b': y['commission_b'],

                                'symbol_c': symbol_c,
                                'baseAsset_c': main_currency,
                                'quoteAsset_c': y['quoteAsset_b'],
                                'stepSize_c': stepSize_c,
                                'commission_c': commission_c
                            }
                        )

                count_pairs_cc += 1

        for yyy in quoteAsset_b_main_currency:
            if y['quoteAsset_b'] == yyy:
                symbol_c = y['quoteAsset_b'] + main_currency
                for u in f_file_step_1_pairs_trade():
                    if u['symbol'] == symbol_c:
                        stepSize_c = u['filters'][1]['stepSize']
                        commission_c = main_commission

                        for commission in zero_commission:

                            if symbol_c == commission:
                                commission_c = float(0.0)
                                break
                            else:
                                commission_c = main_commission

                        pairs_buy_para_c.append(
                            {
                                'symbol_a': y['symbol_a'],
                                'baseAsset_a': y['baseAsset_a'],
                                'quoteAsset_a': y['quoteAsset_a'],
                                'stepSize_a': y['stepSize_a'],
                                'commission_a': y['commission_a'],

                                'symbol_b': y['symbol_b'],
                                'baseAsset_b': y['baseAsset_b'],
                                'quoteAsset_b': y['quoteAsset_b'],
                                'stepSize_b': y['stepSize_b'],
                                'commission_b': y['commission_b'],

                                'symbol_c': symbol_c,
                                'baseAsset_c': y['quoteAsset_b'],
                                'quoteAsset_c': main_currency,
                                'stepSize_c': stepSize_c,
                                'commission_c': commission_c
                            }
                        )

                count_pairs_cc += 1

    print('Найдено и записанно:', count_pairs_cc, 'пар для торговли по трем кругам')

    with open('1_pairs_buy_para_b_test.json', 'w') as file3:
        json.dump(pairs_buy_para_c, file3, indent=2)


else:
    print('Вы ввели не существующую валюту', "'", main_currency, "'", ', введите правильную валюту')
