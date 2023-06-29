from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    path = request.path
    user_agent = request.META['HTTP_USER_AGENT']
    return HttpResponse(path, context_type='text/html', charset='utf-8', ua=user_agent)


def account(request):
    path = request.path
    user_agent = request.META['HTTP_USER_AGENT']
    return HttpResponse(path, context_type='text/html', charset='utf-8', ua=user_agent)


def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name:{} UserID:{}".format(name, id))


def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)
