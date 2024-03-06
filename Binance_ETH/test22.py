# -*- coding: utf8 -*-
# trade_pair_c_sell = [
#     f"\t\t\tprice_b_size = float(f_minqty_size_down(price_b, stepSize_g_)) \n"
#     f"\t\t\tprice_c = float(price_b_size) / float(price_bids_g_) \n"
#     # f"\t\t\tprice_cc = float(f_minqty_size_down(price_c, stepSize_g_{symbol_c})) \n"
#     f"\t\t\t# price_c = jklj'' \n"
# ]
# for i in trade_pair_c_sell:
# 	print(i)
# from decimal import *
# #
# # test2 = Decimal('22')
# # test3 = Decimal('30')
# # # a = test3 + test2
# # # print(a)
# # while test3 != test2:
# #     test2 += Decimal('0.01')
# #     #test2 = test2.quantize(Decimal('0.01'), rounding=ROUND_UP)
# #     print(test2)
# stepSize = Decimal('0.01')
# kolichestvo = Decimal('0.07')
#
# sell_amount_a = kolichestvo.quantize(Decimal(stepSize), ROUND_DOWN)
#
# print(sell_amount_a)
import decimal
from decimal import Decimal


# commission_a = Decimal('0.075')
# commission_b = Decimal('0.075')
# commission_c = Decimal('0.075')
# commission_all = Decimal(commission_a) + Decimal(commission_b) + Decimal(commission_c)
# #commission_all = commission_all.quantize(Decimal('0.00010'))
# print(commission_all)

# def f_minqty_size_up(kolichestvo, stepSize):
#     def adjust_to_step(value, step, increase=True):
#         return ((int(value * 100000000) - int(value * 100000000) % int(
#             float(step) * 100000000)) / 100000000) + (float(step) if increase else 0)
#
#     sell_amount_a = adjust_to_step(kolichestvo, stepSize)
#
#     return sell_amount_a
#
# def f_minqty_size_down(kolichestvo, stepSize):
#     def adjust_to_step(value, step, increase=False):
#         return ((int(value * 100000000) - int(value * 100000000) % int(
#             Decimal(step) * 100000000)) / 100000000) + (Decimal(step) if increase else 0)
#
#     sell_amount_a = adjust_to_step(kolichestvo, stepSize)
#
#     return sell_amount_a


# №	Операция	Результат	Замечание
# 1	x < y	True если x меньше y, иначе False
# 2	x <= y	True если x меньше или равно y, иначе False
# 3	x > n	True если x больше y, иначе False
# 4	x >= n	True если x больше или равно y, иначе False
# 5	x == y	True если x равно y, иначе False
# 6	x != y	True если x не равно y, иначе False
# 7	x is y	True если x и y это один и тот же объект, иначе False
# 8	x is not y	True если x и y это не один и тот же объект, иначе False

# def f_minqty_size_up(kolichestvo, stepSize):
#
#     sell_amount_a = ((int(kolichestvo * 100000000) - int(kolichestvo * 100000000) % (stepSize * 100000000)) / 100000000) + stepSize
#     return sell_amount_a
#
#
# def f_minqty_size_down(kolichestvo, stepSize):
#
#     sell_amount_a = ((int(kolichestvo * 100000000) - int(kolichestvo * 100000000) % (stepSize * 100000000)) / 100000000)
#     return sell_amount_a
#
# # quantity_pair_c_raschet = 0.23
# # stepSize_g = 0.01
# #test = decimal.Decimal()
# quantity_pair_c_raschet = Decimal('3.232342')
# stepSize_g = Decimal('1.0')
#
# quantity_pair_c_raschet = f_minqty_size_down(quantity_pair_c_raschet, stepSize_g)
# print(quantity_pair_c_raschet)

#inn = ['1.000', '0.10000']
# list = []
# for p in inn:
#     for i in range(len(p)-1, 0, -1):
#         if p[i] != str(0):
#             list.append(p[0:i+1])
#             break
#         if
# for pp in list:
#     print(pp)
# p = '1.0000'
# for i in range(len(p) - 1, 0, -1):
#     if p[i] != str(0):
#         p = (p[0:i + 1])
#         # list.append(p[0:i + 1])
#         break
# x = ''
# if p == '1.':
#     p = '1.0'
#
# print(p)
# print(x) 219.0433616450603486812695574
# a = Decimal('0.0098')
# b = Decimal('0.00004474')
# c = a / b
# print(c)
# test3 = Decimal('33.9')
# test2 = Decimal('30.0')
# while test3 <= test2:
#     test2 += Decimal('0.01')
#     #test2 = test2.quantize(Decimal('0.01'), rounding=ROUND_UP)
# print(test2)
#Пара_B: TRXXRP # Продаем 34.0 TRX за 217.9906392254920818106046034 XRP по цене 0.15579000
a = 34.0
b = 0.15579000
c = a / b
print(c)