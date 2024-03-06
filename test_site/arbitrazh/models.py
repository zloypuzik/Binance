from django.db import models


class Bybit_all_pairs_trading_inf(models.Model):
    symbol = models.CharField(blank=True, max_length=15)
    immutableNameBaseAsset = models.CharField(blank=True, max_length=15)
    immutableNameQuoteAsset = models.CharField(blank=True, max_length=15)
    baseAsset = models.CharField(blank=True, max_length=15)
    quoteAsset = models.CharField(blank=True, max_length=15)
    stepSize = models.FloatField(blank=True)

    #
    # class Meta:
    #     managed = False
    #
    # def __str__(self):
    #     return self.symbol


class Binance_pairs_strategy_b_s_s(models.Model):
    symbol_a = models.CharField(blank=True, max_length=15)
    baseCurrency_a = models.CharField(blank=True, max_length=15)
    quoteAsset_a = models.CharField(blank=True, max_length=15)
    stepSize_a = models.FloatField(blank=True, default=0)
    symbol_b = models.CharField(blank=True, max_length=15)
    baseCurrency_b = models.CharField(blank=True, max_length=15)
    quoteAsset_b = models.CharField(blank=True, max_length=15)
    stepSize_b = models.FloatField(blank=True, default=0)
    symbol_c = models.CharField(blank=True, max_length=15)
    baseCurrency_c = models.CharField(blank=True, max_length=15)
    quoteAsset_c = models.CharField(blank=True, max_length=15)
    stepSize_c = models.CharField(blank=True, max_length=25)


class Binance_BookTicker(models.Model):
    symbol = models.CharField(blank=True, max_length=15)
    bidPrice = models.CharField(blank=True, max_length=25)
    bidQty = models.CharField(blank=True, max_length=25)
    askPrice = models.CharField(blank=True, max_length=25)
    askQty = models.CharField(blank=True, max_length=25)


class TradedBundlesCurrency(models.Model):
    pairSymbols_A = models.CharField(blank=True, max_length=15)
    pairSymbols_B = models.CharField(blank=True, max_length=15)
    pairSymbols_C = models.CharField(blank=True, max_length=15)


class Binance_all_pairs_trading_inf(models.Model):
    symbol = models.CharField(blank=True, max_length=15)
    immutableNameBaseAsset = models.CharField(blank=True, max_length=15)
    immutableNameQuoteAsset = models.CharField(blank=True, max_length=15)
    baseAsset = models.CharField(blank=True, max_length=15)
    quoteAsset = models.CharField(blank=True, max_length=15)
    stepSize = models.CharField(blank=True, max_length=25)


class Binance_profit_tradeMaker_bss(models.Model):

    symbols = models.TextField(blank=True)
    symbol_a = models.CharField(blank=True, max_length=15)
    baseCurrency_a = models.CharField(blank=True, max_length=15)
    quoteAsset_a = models.CharField(blank=True, max_length=15)
    stepSize_a = models.CharField(blank=True, max_length=25)
    bidPrice_a = models.CharField(blank=True, max_length=25)
    bidQty_a = models.CharField(blank=True, max_length=25)
    askPrice_a = models.CharField(blank=True, max_length=25)
    askQty_a = models.CharField(blank=True, max_length=25)
    symbol_b = models.CharField(blank=True, max_length=15)
    baseCurrency_b = models.CharField(blank=True, max_length=15)
    quoteAsset_b = models.CharField(blank=True, max_length=15)
    stepSize_b = models.CharField(blank=True, max_length=25)
    bidPrice_b = models.CharField(blank=True, max_length=25)
    bidQty_b = models.CharField(blank=True, max_length=25)
    askPrice_b = models.CharField(blank=True, max_length=25)
    askQty_b = models.CharField(blank=True, max_length=25)
    symbol_c = models.CharField(blank=True, max_length=15)
    baseCurrency_c = models.CharField(blank=True, max_length=15)
    quoteAsset_c = models.CharField(blank=True, max_length=15)
    stepSize_c = models.CharField(blank=True, max_length=25)
    bidPrice_c = models.CharField(blank=True, max_length=25)
    bidQty_c = models.CharField(blank=True, max_length=25)
    askPrice_c = models.CharField(blank=True, max_length=25)
    askQty_c = models.CharField(blank=True, max_length=25)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)


    # class Meta:
    #     managed = False

    # def __str__(self):
    #     return self.quoteAsset
