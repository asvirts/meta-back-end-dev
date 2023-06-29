from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('/account', views.account),
    path('drinks/<str:drink_name>', views.drinks, name="drink_name"),
]
