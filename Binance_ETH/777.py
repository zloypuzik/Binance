#
#
# def f_minqty_size_up(kolichestvo, stepSize):
#
# 	def adjust_to_step(value, step, increase=True):
# 		return ((int(value * 100000000) - int(value * 100000000) % int(
# 			float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)
# 	sell_amount_a = adjust_to_step(kolichestvo, stepSize)
# 	return sell_amount_a
#
# # -*- coding: utf8 -*-
# def f_minqty_size_down(kolichestvo, stepSize):
#
# 	def adjust_to_step(value, step, increase=False):
# 		return ((int(value * 100000000) - int(value * 100000000) % int(
# 			float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)
#
# 	sell_amount_a = adjust_to_step(kolichestvo, stepSize)
#
# 	return sell_amount_a
#
#
# stepSize_WAVESETH_WAVESTRY = '0.01000000'
#
# price_a = float(6.323)
#
# price_asks_a_g_WAVESETH_WAVESTRY = float(0.00159200)
#
# # price_a = float(quantity_pair_b_raschet) * float(price_asks_a_g_WAVESETH_WAVESTRY)
# # price_a = round(price_a, 14)
# price_a = float(f_minqty_size_down(price_a, stepSize_WAVESETH_WAVESTRY))
# price_a = round(price_a, 14)
#
# print(price_a)

#(a / b - 1) * 100

# a = float(0.01)
# b = float(0.00999648)
#
# c = (a / b - 1) * 100
#
# print(c,'%')

import json

########################################################################################################

file_step_1_pairs_trade = '../Binance_ETH/1_25_step_1_pairs_trade.json'


def f_file_step_1_pairs_trade():
    with open(file_step_1_pairs_trade) as file_data:
        data_a = json.load(file_data)

    return data_a

for i in f_file_step_1_pairs_trade():
    symbol_a = (i['symbol'])
    baseAsset_a = (i['baseAsset'])
    for ch_stepsize in i['filters']:
        if ch_stepsize['filterType'] == 'LOT_SIZE':
            a = ch_stepsize['stepSize']
            print(a)
            break
    #print(i['filters'])
    # for ii in i['filters'][8]:
    #     if 'stepSize':
    #         print(i['filters'][1])
    #print(type(i['filters'][1]))

    # if i['filters'][1]['stepSize']:
    #     print('sd')
    # else:
    #     print('asd')
    #print(i['filters'][1]['stepSize'])
    #for ii in i['filters'][1]:
        #a = ii['stepSize']
        #if ii['stepSize'] == '1.00000000':

        #print(ii)
    # else:
    #     print('asd')
    # else:
    #     print('asd')
    # elif i['filters'][2]['stepSize'] == True:
    #     print("asda", i)
    #stepSize_a = (i['filters'][1]['stepSize'])
    #print(i['filters'][1])
    # print(i['filters'][2]['stepSize'])