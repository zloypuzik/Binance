# # -*- coding: utf8 -*-
#
# raschet_pair_c_buy = [
#                 f"\t\t\tquantity_pair_c_raschet = usdt_count * float(price_asks_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
#                 f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
#                 f"\t\t\tquantity_pair_c_raschet = float(f_minqty_size_down(quantity_pair_c_raschet, stepSize_g_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
#                 f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
#                 f"\t\t\t# quantity_pair_c_raschet = количество '{i['quoteAsset_c']}' \n"
# ]
#
# raschet_pair_c_sell = [
#                 f"\t\t\tquantity_pair_c_raschet = usdt_count / float(price_bids_g_{symbol_c})  # Определяем, сколько нужно валюты 'c', для торговли в паре 'b' \n"
#                 f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
#                 f"\t\t\tquantity_pair_c_raschet = float(f_minqty_size_down(quantity_pair_c_raschet, stepSize_g_{symbol_c}))  # Округляем согласно шагу Binance 'stepSize' \n"
#                 f"\t\t\tquantity_pair_c_raschet = round(quantity_pair_c_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
#                 f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_c']}' \n"
# ]
#
# ######################################
#
# raschet_pair_b_buy = [
#                 f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) * float(price_bids_g_{symbol_b})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
#                 f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
#                 f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
#                 f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
#                 f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
#                 "\n"
#     ]
#
raschet_pair_b_sell = [
                f"\t\t\tquantity_pair_b_raschet = float(quantity_pair_c_raschet) / float(price_bids_g_{symbol_b})  # Определяем, сколько нужно валюты 'b', для торговли в паре 'a' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\tquantity_pair_b_raschet = float(f_minqty_size_up(quantity_pair_b_raschet, stepSize_g_{symbol_b}))  # Округляем согласно шагу Binance 'stepSize' \n"
                f"\t\t\tquantity_pair_b_raschet = round(quantity_pair_b_raschet, 14)  # Округляем (обрезаем кучу 0, если таковые есть) \n"
                f"\t\t\t# quantity_pair_c_raschet = количество '{i['baseAsset_b']}' \n"
                "\n"
    ]
import json

# check_quote_pairs = '../Binance_ETH/1_pairs_buy_para_b_test.json'
#
#
# def f_file_step_1_pairs_trade():
#     with open(check_quote_pairs) as file_data:
#         data_a = json.load(file_data)
#
#     return data_a
#
# for i in f_file_step_1_pairs_trade():
#     if i['baseAsset_a'] == i['baseAsset_b']:
#         print(i)

# a = float(1138038)
# b = float(1000)
#
# c = b / a
# print(c)











#
# test2 = "test22" + ".py"
#
# for i in test:
#     aaa = i
#
# with open(test2, 'w') as file3:
#     file3.write(
#            aaa
#     )