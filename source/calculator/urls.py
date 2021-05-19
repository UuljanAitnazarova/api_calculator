from django.contrib import admin
from django.urls import path

from calculator.views import add_view, get_token_view, subtract_view, multiply_view, divide_view

urlpatterns = [
    path('get_token/', get_token_view, name='token'),
    path('add/', add_view, name='add'),
    path('subtract/', subtract_view, name='subtract'),
    path('multiply/', multiply_view, name='multiply'),
    path('divide/', divide_view, name='divide'),

]