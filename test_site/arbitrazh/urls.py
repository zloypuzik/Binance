from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', arbitration_main, name='arbitration_main'),

    path('intra_exch_arbitration_main/', intra_exch_arbitration_main, name='intra_exch_arbitration_main'),
    path('intra_exch_arbitration_main/<str:name_currency_exchange>/', intra_exch_arbitration_test, name='intra_exch_arbitration_test'),
    # path('intra_exch_arbitration/', intra_exch_arbitration, name='intra_exch_arbitration')
    # path('intra_exch_arbitration/<int:test_id>', intra_exch_arbitration, name='intra_exch_arbitration'),
    #path('<int:pk>', views.ExchDetailView.as_view(), name='exchange-detail')

]

