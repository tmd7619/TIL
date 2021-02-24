
from django.contrib import admin
from django.urls import path, include
from frontApp    import views
urlpatterns = [
    path('main/', views.index),
    path('nonParamAjax/', views.nonAjax,    name='nonParamAjax'),
    path('ParamAjax/',    views.paramAjax,  name='paramAjax'),
    path('chart/',    views.chart,  name='chart'),
]
