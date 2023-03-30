# temperament_app1/urls.py
from django.urls import path

from temperament_app1.views import index, home, input_from, quest_input


urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('input', input_from, name='input'),
    path('calculate', quest_input)
]