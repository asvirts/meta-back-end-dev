from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('/account', views.account),
    path('login/', views.login, name='login')
]
