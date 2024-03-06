import json
import pymysql
import time
from datetime import datetime
################################################################################


try:
    connect_mysql = pymysql.connect(
        host='192.168.1.50',
        port=3306,
        user='test',
        password='Zz_479621212',
        database='arbitrazh_mezbirzh'
    )
    # print('Подключение к SQL: прошло успешно.')

except Exception as ex:
    print('Подключение к SQL: произошла ошибка !!!')
    print(ex)

################################################################################


symbol_kucoin = []
count_symbol_kucoin = 0
with connect_mysql.cursor() as cursor:
    test = "SELECT symbol FROM kucoin_get_orderbook_ticker"
    # select_symbol_query = F"SELECT symbol FROM kucoin_get_orderbook_ticker"
    cursor.execute(test)
    a = list(cursor.fetchall())
    for i in a:
        symbol_kucoin.append(i[0])
        count_symbol_kucoin += 1

################################################################################


symbol_binance = []
count_symbol_binance = 0
with connect_mysql.cursor() as cursor:
    test = "SELECT symbol FROM binance_get_orderbook_ticker"
    # select_symbol_query = F"SELECT symbol FROM kucoin_get_orderbook_ticker"
    cursor.execute(test)
    a = list(cursor.fetchall())
    for i in a:
        symbol_binance.append(i[0])
        count_symbol_binance += 1

################################################################################


test = []
all_symbol_coin = 0
for i in symbol_binance:
    for ii in symbol_kucoin:
        if i == ii:
            test.append(i)
            all_symbol_coin += 1
            break

################################################################################
# print(all_symbol_coin)

connect_mysql.close()

#######################################################################################


# binance_coin_info = '../Arbitrazj_mezh_birzh/Binance/Binance_coin_info_modifi.json'
binance_coin_info = '../Arbitrazj_mezh_birzh/Binance/Binance_coin_info_modifi.json'
kucoin_coin_info = '../Arbitrazj_mezh_birzh/Kucoin/Kucoim_coin_info_modifi.json'

def f_file_binance_coin_info():
    with open(binance_coin_info) as file_data:
        data_a = json.load(file_data)

    return data_a

def f_file_kucoin_coin_info():
    with open(kucoin_coin_info) as file_data:
        data_a = json.load(file_data)

    return data_a
#######################################################################################
test22 = []
for binance in f_file_binance_coin_info():
    symbol_coin_info = binance['symbol'] + 'USDT'
    for i in test:
        if symbol_coin_info == i:
            # print('######################')
            test22.append(binance)
            break
        # else:
        #     print(test)
sdfs = 0
for i in test22:
    sdfs += 1
# print(sdfs)

test33= []
for kucoin in f_file_kucoin_coin_info():
    symbol_coin_info = kucoin['symbol'] + 'USDT'
    for i in test:
        if symbol_coin_info == i:
            # print('######################')
            test33.append(kucoin)
            break
        # else:
        #     print(test)
sdfs2 = 0
for i in test33:
    sdfs2 += 1
# print(sdfs2)

old_stack = [{'symbol': '0', 'network': '0', 'comission': '0', 'itog': '0', 'start_rime_chain': '0'}]
def run_sql():
    new_stack = []
    # old_stack = []
    for binance in test22:
        #######################################################################################
        try:
            connect_mysql = pymysql.connect(
                host='192.168.1.50',
                port=3306,
                user='test',
                password='Zz_479621212',
                database='arbitrazh_mezbirzh'
            )
            # print('Подключение к SQL: прошло успешно.')

        except Exception as ex:
            print('Подключение к SQL: произошла ошибка !!!')
            print(ex)
        #######################################################################################
        for kucoin in test33:
            if binance['symbol'] == kucoin['symbol']:
                #print(binance)
                index_network_binance = len(binance['networkList'])
                list_network_binance = []
                network_count_binance = 0

                while network_count_binance < index_network_binance:
                    # print(binance['networkList'][network_count_binance])
                    # print(binance['networkList'][network_count_binance]['network'])
                    binance_network = binance['networkList'][network_count_binance]['network']
                    binance_withdrawEnable = binance['networkList'][network_count_binance]['withdrawEnable']
                    binance_depositEnable = binance['networkList'][network_count_binance]['depositEnable']
                    binance_withdrawFee = binance['networkList'][network_count_binance]['withdrawFee']

                    index_network_kucoin = len(kucoin['networkList'])
                    list_network_kucoin = []
                    network_count_kucoin = 0

                    while network_count_kucoin < index_network_kucoin:
                        # print(kucoin['networkList'][network_count_kucoin]['network'])
                        kucoin_network = kucoin['networkList'][network_count_kucoin]['network']
                        kucoin_withdrawEnable = kucoin['networkList'][network_count_kucoin]['withdrawEnable']
                        kucoin_depositEnable = kucoin['networkList'][network_count_kucoin]['depositEnable']
                        kucoin_withdrawFee = kucoin['networkList'][network_count_kucoin]['withdrawFee']
                        network_count_kucoin += 1

                        if kucoin_network == binance_network:

                            if binance_withdrawEnable and kucoin_depositEnable:
                                with connect_mysql.cursor() as cursor:
                                    select_price_binance = F"SELECT askPrice FROM Binance_get_orderbook_ticker WHERE symbol = '{binance['symbol'] + 'USDT'}'"
                                    cursor.execute(select_price_binance)
                                    a = cursor.fetchone()
                                    binance_price_ask = a[0]

                                    select_price_kucoin = F"SELECT bidPrice FROM Kucoin_get_orderbook_ticker WHERE symbol = '{binance['symbol'] + 'USDT'}'"
                                    cursor.execute(select_price_kucoin)
                                    a = cursor.fetchone()
                                    kucoin_price_bid = a[0]


                                # binance_price_ask = float(f_get_orderbook_binance(binance['symbol'] + 'USDT', 'ask'))
                                # kucoin_price_bid = float(f_get_orderbook_kucoin(kucoin['symbol'] + '-USDT', 'bid'))
                                # # price_binance = a['askPrice']
                                # # print(binance)
                                # # print(kucoin)
                                # # print('########################################################')

                                    usdtCount = int(500)

                                    binance_kolichestvo_coin = usdtCount / float(binance_price_ask)

                                    binance_kolichestcvo_coin_posle_vivoda = binance_kolichestvo_coin - float(binance_withdrawFee)

                                    kucoin_usdt_posle_prodazhi = binance_kolichestcvo_coin_posle_vivoda * float(kucoin_price_bid)

                                    itog = kucoin_usdt_posle_prodazhi - usdtCount

                                    if itog > 1:
                                        # lll.append({binance['symbol'], binance_network, binance_withdrawFee, itog})
                                        print('##############################################################')
                                        print('binance')
                                        print('##############################################################')
                                        print(binance['symbol'], binance_network, '|', 'Комиссия:', binance_withdrawFee, '||', itog)
                                        # start_time = time.time()
                                        # # for i in old_stack:
                                        # #     if i['symbol'] == binance['symbol']:
                                        # #         pass
                                        # #     else:
                                        # new_stack.append({'symbol': binance['symbol'], 'network': binance_network, 'comission': binance_withdrawFee, 'itog': itog, 'start_rime_chain': start_time})
                                        # pass
                                    else:
                                        print('##############################################################')

                            # if kucoin_withdrawEnable == True and binance_depositEnable == True:
                            #     kucoin_price_ask = float(
                            #         f_get_orderbook_kucoin(kucoin['symbol'] + '-USDT', 'ask'))  # Узнаем цену продажи
                            #     binance_price_bid = float(f_get_orderbook_binance(binance['symbol'] + 'USDT', 'bid'))
                            #
                            #     kucoin_kolichestvo_coin = 1000 / kucoin_price_ask
                            #
                            #     kucoin_kolichestcvo_coin_posle_vivoda = kucoin_kolichestvo_coin - float(kucoin_withdrawFee)
                            #
                            #     binance_usdt_posle_prodazhi = kucoin_kolichestcvo_coin_posle_vivoda * binance_price_bid
                            #
                            #     itog = binance_usdt_posle_prodazhi - 1000
                            #     if itog > 2:
                            #         print('##############################################################')
                            #         print('kucoin')
                            #         print('##############################################################')
                            #         print(kucoin['symbol'], kucoin_network, '|', 'Komissiya:', kucoin_withdrawFee, itog)
                            #     # pass

                    network_count_binance += 1
        connect_mysql.close()
    # end_time = (time.time() - start_time)
    global old_stack
    #copy_old_stack = []
    # copy_old_stack = old_stack.copy()
    # old_stack = []
    # print('########################################')
    # print(copy_old_stack)
    # print('########################################')
    # for i in range(len(copy_old_stack)):
    #     a =False
    #     for t in new_stack:
    #         if copy_old_stack[i]['symbol'] == t['symbol'] and copy_old_stack[i]['network'] == t['network']:
    #             # print('1')
    #             # pass
    #             old_stack.append({'symbol': t['symbol'], 'network': t['network'], 'comission': t['comission'], 'itog': t['itog'],'start_rime_chain': copy_old_stack[i]['start_rime_chain']})
    #             # copy_old_stack[i]['comission'] = ii['comission']
    #             # copy_old_stack[i]['itog'] = ii['itog']
    #             a = True
    #             # break
    #         else :
    #             pass
    #     if a == False:
    #         old_stack.append({'symbol': t['symbol'], 'network': t['network'], 'comission': t['comission'], 'itog': t['itog'],'start_rime_chain': copy_old_stack[i]['start_rime_chain']})
                # break
    # for index, value in enumerate(new_stack):
    #     print(list((index, value)))
    #     print(list((value['symbol'])))
        # a = new_stack.index('symbol')

    # print ("\n" * 30)
    # print('/////////////////////////////////////////////////////////////')
    # for i in old_stack:
    #     print(i)
    # print(new_stack)
    #     print('Монета:', i['symbol'], 'сеть:', i['network'], 'комиссия:', i['comission'], 'прибыль:', i['itog'], 'время работы цепочки:', (time.time() - i['start_rime_chain']))
    # print(type(new_stack))
    # print(stack)
    # if binance['withdrawEnable'] and kucoin['depositEnable']:
                #     count_2 += 1
            # count += 1

while True:
    run_sql()