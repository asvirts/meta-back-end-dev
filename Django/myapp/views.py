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