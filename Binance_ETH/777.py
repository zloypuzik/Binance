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

a = float(0.01)
b = float(0.00999648)

c = (a / b - 1) * 100

print(c,'%')