
import time

new_stack = [{'symbol': 'GNS', 'network': 'MATIC', 'comission': '11', 'itog': 3, 'start_rime_chain': 32}, {'symbol': 'WRX', 'network': 'BNB', 'comission': '0.94', 'itog': 1.4311001289506748, 'start_rime_chain': 3335}]

# old_stack = [{'symbol': 'GNS', 'network': 'MATIC', 'comission': '444', 'itog': 2.222198732394361, 'start_rime_chain': 1680023057.6786323},
#              {'symbol': 'WRX', 'network': 'BNB', 'comission': '0.94', 'itog': 1.4311001289506748, 'start_rime_chain': 1680023058.1561325},
#              {'symbol': 'sss', 'network': 'MATIC', 'comission': '444', 'itog': 2.222198732394361, 'start_rime_chain': 1680023057.6786323}]
# old_stack = [{'symbol': '0', 'network': '0', 'comission': '0', 'itog': '0', 'start_rime_chain': '0'}]
old_stack = [{'symbol': 'GNS', 'network': 'MATIC', 'comission': '11', 'itog': 3, 'start_rime_chain': 32}, {'symbol': 'WRX', 'network': 'BNB', 'comission': '0.94', 'itog': 1.4311001289506748, 'start_rime_chain': 3335}]
# for i in new_stack:
#     # print(i['symbol'])
#     a = False
#     for ii in range(len(old_stack)):
#
#         if i['symbol'] != old_stack[ii]['symbol'] and i['network'] != old_stack[ii]['network']:
#             a = False
#         elif i['symbol'] == old_stack[ii]['symbol'] and i['network'] == old_stack[ii]['network']:
#             old_stack[ii]['comission'] = i['comission']
#             old_stack[ii]['itog'] = i['itog']
#             a = True
#             break

# def test():
# time.sleep(2)
# for i in range(len(copy_old_stack)):
#     for ii in new_stack:
#         if copy_old_stack[i]['symbol'] == ii['symbol'] and copy_old_stack[i]['network'] == ii['network']:
#             old_stack.append({'symbol': ii['symbol'], 'network': ii['network'], 'comission': ii['comission'], 'itog': ii['itog'], 'start_rime_chain': copy_old_stack[i]['start_rime_chain']})
#             # copy_old_stack[i]['comission'] = ii['comission']
#             # copy_old_stack[i]['itog'] = ii['itog']
#             break
#         else:
#             old_stack.append(
#                 {'symbol': ii['symbol'], 'network': ii['network'], 'comission': ii['comission'], 'itog': ii['itog'],
#                  'start_rime_chain': copy_old_stack[i]['start_rime_chain']})
# global old_stack
x = old_stack
copy_old_stack = x.copy()
old_stack = []

# for i in range(len(copy_old_stack)):
#     a = False
#     for t in new_stack:
#         if copy_old_stack[i]['symbol'] == t['symbol'] and copy_old_stack[i]['network'] == t['network']:
#
#             a= True
#
#             # copy_old_stack[i]['comission'] = ii['comission']
#             # copy_old_stack[i]['itog'] = ii['itog']
#
#         else:
#             pass
#             # old_stack.append({'symbol': t['symbol'], 'network': t['network'], 'comission': t['comission'], 'itog': t['itog'],'start_rime_chain': copy_old_stack[i]['start_rime_chain']})
#     if a ==True:
#         print('True')
# print('#' * 20)
# print(new_stack)
# print(copy_old_stack)
# print(old_stack)

for i, ii in range(len(copy_old_stack)), new_stack :
    print(i, ii)

#     test()



    # if a == False:
    #     print('@@@')
        # old_stack.remove(old_stack[ii])
            # old_stack.remove(old_stack[ii])


            # a[ii]['symbol'] = 'Shardul'
# print(a)
# for index, value in enumerate(new_stack):
#     print(list((index, value)))
#     if
#     print(list((value['symbol'])))

# prices = [29.30, 10.20, 44.00, 5.99, 81.90]
#
# for index, item in enumerate(prices):
#     #if item > 40:
#     # prices[index] = round(prices[index] - (prices[index] * 30 / 100))
#
# print(prices)