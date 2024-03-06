import time
import sqlite3
import datetime

from Scripts_arbitrzh_Django import API


def f_strategy (strategyName, strategyData):

    with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:

        cursor = connect_db.cursor()
        cursor.execute(F"SELECT * FROM arbitrazh_binance_pairs_{strategyName}")
        bd_binance_all_pairs_trading_inf = cursor.fetchall()

        #  Удаляем запись из БЛ, если ее нет в 'strategyData'

        for i_bd_binance_all_pairs_trading_inf in bd_binance_all_pairs_trading_inf:

            exists_in_the_table_bd = None
            bd_id = i_bd_binance_all_pairs_trading_inf[0]
            bd_symbol_a = i_bd_binance_all_pairs_trading_inf[1]
            bd_symbol_b = i_bd_binance_all_pairs_trading_inf[5]
            bd_symbol_c = i_bd_binance_all_pairs_trading_inf[9]

            for i_strategy in strategyData:

                if i_strategy['symbol_A'] == bd_symbol_a and i_strategy['symbol_B'] == bd_symbol_b and i_strategy['symbol_C'] == bd_symbol_c:

                    exists_in_the_table_bd = 'is not None'
                    break

                else:

                    exists_in_the_table_bd = None

            if exists_in_the_table_bd is None:
                cursor.execute(F"DELETE from arbitrazh_binance_pairs_{strategyName} where id = {bd_id}")

    for i_strategyData in strategyData:

        with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:

            cursor = connect_db.cursor()
            cursor.execute(F"SELECT symbol_a, symbol_b, symbol_c FROM arbitrazh_binance_pairs_{strategyName} WHERE symbol_a = '{i_strategyData['symbol_A']}' and symbol_b = '{i_strategyData['symbol_B']}' and symbol_c = '{i_strategyData['symbol_C']}'")

            if cursor.fetchone() is None:

                # symbol_A = i_strategyData['symbol_A'][0],
                # baseCurrency_A = i_strategyData['baseCurrency_A'],
                # quoteAsset_A = i_strategyData['quoteAsset_A'],
                # symbol_B = i_strategyData['symbol_B'],
                # baseCurrency_B = i_strategyData['baseCurrency_B'],
                # quoteAsset_B = i_strategyData['quoteAsset_B'],
                # symbol_C = i_strategyData['symbol_C'],
                # baseCurrency_C = i_strategyData['baseCurrency_C'],
                # quoteAsset_C = i_strategyData['quoteAsset_C']
                #
                # print(i_strategyData['symbol_A'], symbol_A, type(baseCurrency_A))

                cursor.execute(F"INSERT INTO  arbitrazh_binance_pairs_{strategyName} VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (i_strategyData['symbol_A'], i_strategyData['baseCurrency_A'], i_strategyData['quoteAsset_A'], i_strategyData['stepSize_A'], i_strategyData['symbol_B'], i_strategyData['baseCurrency_B'], i_strategyData['quoteAsset_B'], i_strategyData['stepSize_B'], i_strategyData['symbol_C'], i_strategyData['baseCurrency_C'], i_strategyData['quoteAsset_C'], i_strategyData['stepSize_C']))


                # a = i_strategy['symbol_A']
                # print(a)

            cursor.close()

with sqlite3.connect('../../test_site/arbitrazh.db') as connect_db:

    cursor = connect_db.cursor()
    cursor.execute(F"SELECT * FROM arbitrazh_binance_all_pairs_trading_inf")
    bd_binance_all_pairs_trading_inf = cursor.fetchall()

    baseCurrency = API.def_allMainCurrency('Binance')

    dict_strategy_b_s_s = []

    for i_pair_a in bd_binance_all_pairs_trading_inf:

        # print(i[2])
        # baseCurrency - это что продаем или покупаем
        # quoteAsset - это за что покупаем или что получим при продаже

        symbol_A = i_pair_a[1]
        baseCurrency_A = i_pair_a[2]
        quoteAsset_A = i_pair_a[3]
        stepSize_A = i_pair_a[6]

        for i_pair_b in bd_binance_all_pairs_trading_inf:

            symbol_B = i_pair_b[1]
            baseCurrency_B = i_pair_b[2]
            quoteAsset_B = i_pair_b[3]
            stepSize_B = i_pair_b[6]

            ##########################################################
            #
            ##########################################################

            # BUY   baseCurrency_A
            # SELL  baseCurrency_B
            # SELL  baseCurrency_C или BUY  baseCurrency_C

            if symbol_A != symbol_B and baseCurrency_A == baseCurrency_B:



                for i_pair_c in bd_binance_all_pairs_trading_inf:

                    symbol_C = i_pair_c[1]
                    baseCurrency_C = i_pair_c[2]
                    quoteAsset_C = i_pair_c[3]
                    stepSize_C = i_pair_c[6]

                    # SELL  baseCurrency_C
                    if symbol_B != symbol_C and quoteAsset_B == baseCurrency_C:

                        if quoteAsset_C == quoteAsset_A:

                            list_strategy_b_s_s ={
                                'symbol_A': symbol_A,
                                'baseCurrency_A': baseCurrency_A,
                                'quoteAsset_A': quoteAsset_A,
                                'stepSize_A': stepSize_A,
                                'symbol_B': symbol_B,
                                'baseCurrency_B': baseCurrency_B,
                                'quoteAsset_B': quoteAsset_B,
                                'stepSize_B': stepSize_B,
                                'symbol_C': symbol_C,
                                'baseCurrency_C': baseCurrency_C,
                                'quoteAsset_C': quoteAsset_C,
                                'stepSize_C': stepSize_C,
                            }

                            dict_strategy_b_s_s.append(list_strategy_b_s_s)

                            #pass
                            # print("#" * 79)
                            # print(symbol_A, '|', symbol_B, '|', symbol_C)
                            # break

                    #  BUY baseCurrency_C
                    elif symbol_B != symbol_C and quoteAsset_B == quoteAsset_C:

                        if baseCurrency_C == quoteAsset_A:

                            pass
                            # print("#" * 79)
                            # print(symbol_A, '|', symbol_B, '|', symbol_C)

            ##########################################################
            # END
            ##########################################################

            # BUY   baseCurrency_A
            # BUY   baseCurrency_B
            # SELL  baseCurrency_C или BUY  baseCurrency_C

            if symbol_A != symbol_B and baseCurrency_A == quoteAsset_B :

                for i_pair_c in bd_binance_all_pairs_trading_inf:

                    symbol_C = i_pair_c[1]
                    baseCurrency_C = i_pair_c[2]
                    quoteAsset_C = i_pair_c[3]
                    stepSize_C = i_pair_c[6]

                    # SELL  baseCurrency_C
                    if symbol_B != symbol_C and baseCurrency_B == baseCurrency_C:

                        if quoteAsset_C == quoteAsset_A:

                            pass
                            # print("#" * 79)
                            # print(symbol_A, '|', symbol_B, '|', symbol_C)

                    # BUY  baseCurrency_C
                    if symbol_B != symbol_C and baseCurrency_B == quoteAsset_C:

                        if baseCurrency_C == quoteAsset_A:

                            pass
                            # print("#" * 79)
                            # print(symbol_A, '|', symbol_B, '|', symbol_C)

            ##########################################################
            # END
            ##########################################################


            ##################################################################################################################

            # SELL  baseCurrency_A
            # SELL  baseCurrency_B
            # BUY   baseCurrency_C

            if symbol_A != symbol_B and quoteAsset_A == baseCurrency_B:

                for i_pair_c in bd_binance_all_pairs_trading_inf:

                    symbol_C = i_pair_c[1]
                    baseCurrency_C = i_pair_c[2]
                    quoteAsset_C = i_pair_c[3]
                    stepSize_C = i_pair_c[6]

                    # SELL  baseCurrency_C
                    if symbol_B != symbol_C and quoteAsset_B == baseCurrency_C:

                        if quoteAsset_C == baseCurrency_A:

                            pass
                            # print("#" * 79)
                            # print(symbol_A, '|', symbol_B, '|', symbol_C)

                    #  BUY baseCurrency_C
                    elif symbol_B != symbol_C and quoteAsset_B == quoteAsset_C:

                        if baseCurrency_C == baseCurrency_A:

                            pass
                            # print("#" * 79)
                            # print(symbol_A, '|', symbol_B, '|', symbol_C)

            ##########################################################
            # END
            ##########################################################

            # SELL  baseCurrency_A
            # BUY   baseCurrency_B
            # BUY   baseCurrency_C или SELL  baseCurrency_C

            if symbol_A != symbol_B and quoteAsset_A == quoteAsset_B :

                for i_pair_c in bd_binance_all_pairs_trading_inf:

                    symbol_C = i_pair_c[1]
                    baseCurrency_C = i_pair_c[2]
                    quoteAsset_C = i_pair_c[3]
                    stepSize_C = i_pair_c[6]

                    # SELL  baseCurrency_C
                    if symbol_B != symbol_C and baseCurrency_B == baseCurrency_C:

                        if quoteAsset_C == baseCurrency_A:

                            pass
                            # print("#" * 79)
                            # print(symbol_A, '|', symbol_B, '|', symbol_C)

                    # BUY  baseCurrency_C
                    if symbol_B != symbol_C and baseCurrency_B == quoteAsset_C:

                        if baseCurrency_C == baseCurrency_A:

                            pass
                            # print("#" * 79)
                            # print(symbol_A, '|', symbol_B, '|', symbol_C)
    # {'strategyName': 'strategy_b_s_s'}
    strategy_b_s_s = [{'strategyName': 'strategy_b_s_s', 'strategyData': dict_strategy_b_s_s}]
    list_strategy = [strategy_b_s_s]

    # print(strategy_b_s_s)

    for i in list_strategy:

        f_strategy(i[0]['strategyName'], i[0]['strategyData'])


####################################################################################################################
# BUY   baseCurrency_A
####################################################################################################################
#						# SELL  baseCurrency_B
####################################################################################################################
#												# SELL  baseCurrency_C
####################################################################################################################
#																		LINKBTC | LINKETH | ETHBTC
#																		ETHUSDT | ETHAEUR | AEURUSDT
####################################################################################################################
#												# BUY  	baseCurrency_C
####################################################################################################################
#																		BNBETH | BNBBRL | ETHBRL
#																		EOSBTC | EOSUSDT | BTCUSDT
####################################################################################################################
#						# BUY   baseCurrency_B
####################################################################################################################
#												# SELL  baseCurrency_C
####################################################################################################################
#																		BTCUSDT | JOEBTC | JOEUSDT
#																		BNBETH | SOLBNB | SOLETH
####################################################################################################################
#												# BUY  	baseCurrency_C
####################################################################################################################
#																		NULL
####################################################################################################################


####################################################################################################################
# SELL  baseCurrency_A
####################################################################################################################
#						# SELL  baseCurrency_B
####################################################################################################################
#												# SELL  baseCurrency_C
####################################################################################################################
#																		NULL
####################################################################################################################
#												#  BUY baseCurrency_C
####################################################################################################################
#																		XVGETH | ETHTRY | XVGTRY
#																		ETHBTC | BTCUSDT | ETHUSDT
####################################################################################################################
#						# BUY   baseCurrency_B
####################################################################################################################
#												# SELL  baseCurrency_C
####################################################################################################################
#																		BTCUSDT | QKCUSDT | QKCBTC
#																		FDUSDTRY | USTCTRY | USTCFDUSD
####################################################################################################################
#												# BUY  baseCurrency_C
####################################################################################################################
#																		LUNCTRY | USDTTRY | LUNCUSDT
#																		BTCUSDT | AEURUSDT | BTCAEUR
####################################################################################################################
