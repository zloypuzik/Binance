from django import forms
from .Scripts import counting


class TestForm(forms.Form):
    # BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    FAVORITE_COLORS_CHOICES = [
        ('BTC', 'BTC'),
        ('USDT', 'USDT'),
    ]
    #
    Test = counting.def_allMainCurrency('Binance')
    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    allMainCurrency = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Test,
    )

    # USDT = forms.BooleanField(required=False, initial=True, label='USDT')
    # BTC = forms.SelectMultiple
    #
    # # all_main_curency = counting.def_allMainCurrency('Binance')
    # # print(all_main_curency)
    # # required - может быть пустым или нет
    # # initial - ставить галку или нет
    # # a = test()
    amount_main_currency = forms.FloatField(label='Количество валюты', required=False)
    commission = forms.FloatField(label='Комиссия', required=False)
    # profit_procent = forms.FloatField(label='Прибыль в %', required=False)
    profit_procent = forms.FloatField(label='Прибыль в %', required=False)
    profit_procent_t = forms.FloatField(step_size=0.1, label='Прибыль в %_t', required=False)

    # for i in a:
    #     prosdasdcent = forms.IntegerField(label='Комиsdссия', required=False)

    # b = test()
    # procdent = forms.IntegerField(label='Комиссия', required=False)
    # transaction_volume = forms.FloatField()
    # print('sssssssssssssssssssssss', all_main_curency)
    # for i in all_main_curency:
    # #     print(i)
    #     # p = forms.IntegerField(label='Комиссия', required=False)
    #     t = forms.BooleanField(required=False, initial=True, label=i)
    #     procent = forms.IntegerField(label='Комиссия', required=False)

class Sorted(forms.Form):
    profit_procent = forms.ChoiceField(label='Прибыль', required=False, choices=[
        ['up', 'По возростанию'],
        ['down', 'По убыванию']
    ])