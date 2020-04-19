from django.urls import path

from . import views

app_name = 'dnswrl'
urlpatterns = [
    # path('', views.index, name='index'),
    path('choice/', views.choice, name='choice'),
    path('input/', views.inputText, name='inputText'),
    path('result/', views.result, name='result'),
]