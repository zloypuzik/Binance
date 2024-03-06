from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
# from test_site.arbitrazh.test_2 import a

# Create your views here.


def index(request):
    # testt = a
    return render(request, 'main/index.html', {'post': 'testt'})


def test(request):
    return render(request, 'main/test.html', {'post': 'sadas'})