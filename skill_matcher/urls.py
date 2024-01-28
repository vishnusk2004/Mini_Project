from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('try',views.mainpage,name='mainpage'),
    path('input',views.input,name='input'),
    path('output',views.output,name='output'),
    path('documentation',views.documentation,name='documentation'),
]