from django.shortcuts import render
from django.http import HttpResponse

from .forms import TestForm, Sorted
from .models import Binance_all_pairs_trading_inf, Bybit_all_pairs_trading_inf, Binance_profit_tradeMaker_bss
from .Scripts import counting
from django.forms import formset_factory



def count_pairs(name_currency_exchange):

    if name_currency_exchange == 'binance':
        currency_pairs = Binance_all_pairs_trading_inf.objects.order_by('symbol')
    elif name_currency_exchange == 'bybit':
        currency_pairs = Bybit_all_pairs_trading_inf.objects.order_by('symbol')

    quantity_currency_pairs = 0
    for i in currency_pairs:
        quantity_currency_pairs += 1

    return quantity_currency_pairs


def get_bd_profitTrade_bss(selected_main_currencies):
    # print(selected_main_currencies)
    a = Binance_profit_tradeMaker_bss.objects.all()

    test_list = []

    for selectedMainCurrency in selected_main_currencies:
        for i in a:
            if selectedMainCurrency == i.id:
                test_list.append(i)



    # return a

    return test_list


def get_bd_profitTrade_bss_sec(a):

    bd = Binance_profit_tradeMaker_bss.objects.all()

    test_list = []
    for i_a in a:
        for i_bd in bd:
            # if i_a['i_selectedMainCurrency'] == i_bd.id:
            if i_a['i_selectedMainCurrency'] == i_bd.quoteAsset_a:
                print('dsfdsdsfsdfdsfsdfsdfdsf')
                profit_with_percents = str(i_a['profit_with_percents'])[0:8]
                profit_percent = str(i_a['profit_percent'])[0:6]

                test_listt = "ghfghfghfghfghfghfgh"
                print('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')

                test_list.append({
                    'symbol_a': i_bd.symbol_a,
                    'baseCurrency_a': i_bd.baseCurrency_a,
                    'quoteAsset_a': i_bd.quoteAsset_a,
                    'bidPrice_a': i_bd.bidPrice_a,

                    'symbol_b': i_bd.symbol_b,
                    'baseCurrency_b': i_bd.baseCurrency_b,
                    'quoteAsset_b': i_bd.quoteAsset_b,
                    'askPrice_b': i_bd.askPrice_b,

                    'symbol_c': i_bd.symbol_c,
                    'baseCurrency_c': i_bd.baseCurrency_c,
                    'quoteAsset_c': i_bd.quoteAsset_c,
                    'askPrice_c': i_bd.askPrice_c,

                    'time_create': counting.def_time_passed(i_bd.time_create),

                    'profit_percent': profit_percent,
                    'profit_with_percents': profit_with_percents,
                    'final_quantity_coins_circle_c_with_percent_makerStrategy': i_a['final_quantity_coins_circle_c_with_percent_makerStrategy'],
                    'costs_main_currency_makerStrategy': i_a['costs_main_currency_makerStrategy'],
                })

    print("sdfsfdds",test_list)

    return test_list

    #
    # a = Binance_profit_tradeMaker_bss.objects.all()
    #
    # test_list = []
    #
    # for selectedMainCurrency in selectedMainCurrency:
    #     for i in a:
    #         if selectedMainCurrency == i.id:
    #             test_list.append(i)


    # return a
    # return test_list

    #
    # a = Binance_profit_tradeMaker_bss.objects.all()
    #
    # test_list = []
    #
    # for selectedMainCurrency in selectedMainCurrency:
    #     for i in a:
    #         if selectedMainCurrency == i.id:
    #             test_list.append(i)


    # return a
    # return test_list

# kk = get_bd_profitTrade_bss()
# print('#############################', type(kk))

# for i in kk:
#     print(i['symbols'])
def testProfitView(mainCurrency):
    # Тестируем обработку фильтров внтуребиржевой торговли

    print(mainCurrency)

def arbitration_main(request):

    return render(request, 'arbitrazh/arbitration_main.html')

def create(request):
    if request.method == 'POST':
        print('####################################################')
def intra_exch_arbitration_test(request, name_currency_exchange):

    listttt = []
    MainCurrency = counting.def_allMainCurrency('Binance')

    #
    # if request.method == 'POST':
    #
    #     print('324234234234234')
    #     selectedMainCurrency = request.POST['selectedMainCurrency'],
    #     print(selectedMainCurrency)
    #     # amount_main_currency = request.POST['amount_main_currency'],
    #     # commission = request.POST['commission'],
    #     # profit_procent = request.POST['profit_procent'],
    # else:
    #     print('huyyy')
    #     selectedMainCurrency = counting.f_get_bd_profitTrade_bss(['USDT'])
    #     amount_main_currency = 10
    #     commission = 0
    #     profit_procent = 0

    if request.method == 'POST':
        print(request.POST.getlist)
        # selected_main_currencies = 'BTC'
        selected_main_currencies = request.POST.getlist('selected_main_currencies[]')
        print('Пришел POST запрос', selected_main_currencies)
        amount_main_currency = 10.0
        commission = 0.0
        profit_procent = 0.0
    else:
        selected_main_currencies = ['BTC']
        amount_main_currency = 10.0
        commission = 0.0
        profit_procent = 0.0
        # amount_main_currency = request.POST['amount_main_currency']
        # print(amount_main_currency)

        # form = TestForm(request.POST)

        # id = request.POST.getlist('cheks[]')

        # print('iddddddddddddd', id)
        # if form.is_valid():
        #
        #     # request_form = request.POST
        #
            # selected_main_currencies = request.POST.getlist('selected_main_currencies[]')
        #     amount_main_currency = float(request.POST.getlist('amount_main_currency')[0])
        #     commission = float(request.POST.getlist('commission')[0])
        #     profit_procent = float(request.POST.getlist('profit_procent')[0])
            # print('########', type(profit_procent), type(amount_main_currency), type(commission))
            # print(profit_procent)
            # print(mainCurrency)
            #mainCurrency = request_form['mainCurrency']
            # amount_main_currency = request.POST['amount_main_currency']

            # print(amount_main_currency)
            #amount_main_currency = form.cleaned_data.get('amount_main_currency') # Извлечь можно так или как ниже
            # # amount_main_currency = float(request_form['amount_main_currency'])
            # commission = float(request_form['commission'])
            # profit_procent = float(request_form['profit_procent'])
            # selectedMainCurrency = counting.f_get_bd_profitTrade_bss(form.cleaned_data['allMainCurrency'])
        #
        #
    # else:
    #     # pass
    #     # form = TestForm({'amount_main_currency': 10, 'commission': 12, 'allMainCurrency': 'USDT', 'profit_procent': 0.001})
    #     # form = TestForm({'amount_main_currency': 10})
    #     selected_main_currencies = ['USDT']
    #     # selectedMainCurrency = counting.f_get_bd_profitTrade_bss('USDT')
    #     commission = float(0.0)
    #     profit_procent = float(0.0)
    #     amount_main_currency = float(10)
    # #     form = TestForm({'favorite_colors': 'BTC'})
    # #
    # #     allMainCurrency = 'USDT'
    # #     # favorite_colors =
    a = counting.testprocent(amount_main_currency, commission, selected_main_currencies, profit_procent)
    # print(amount_main_currency, commission, selected_main_currencies, profit_procent)


    if name_currency_exchange == 'binance':

        return render(request, 'arbitrazh/intra_exch_arbitration_main.html', {
            'count_pairs': count_pairs(name_currency_exchange),
            'name_currency_exchange': name_currency_exchange,
            # 'get_bd_profitTrade_bss': get_bd_profitTrade_bss(selected_main_currencies),
            # 'get_bd_profitTrade_bss': get_bd_profitTrade_bss(selectedMainCurrency),
            # 'form': form,
            'get_bd_profitTrade_bss_sec': get_bd_profitTrade_bss_sec(a),
            # 'form_sorted': form_sorted,
            # 'procentt': procentt,
            # 'test': test
            # 'test_formset': test_formset
            # 'testProfitView': testProfitView(selected_main_currencies),
            'MainCurrency': MainCurrency,

        })

    ###################################################################################################################

    elif name_currency_exchange == 'bybit':

        return render(request, 'arbitrazh/intra_exch_arbitration_main.html', {'count_pairs': count_pairs(name_currency_exchange), 'name_currency_exchange': name_currency_exchange})

    ###################################################################################################################

    else:
        return render(request, 'arbitrazh/arbitration_main.html')


def intra_exch_arbitration_main(request):

    return render(request, 'arbitrazh/intra_exch_arbitration_main.html', {'test': 'fsdfsdfs'})



# class ExchDetailView(DetailView):
#
#     model = Binance_all_pairs_trading_inf
#     template_name = 'arbitrazh/test.html'
#     context_object_name = 'exch'

