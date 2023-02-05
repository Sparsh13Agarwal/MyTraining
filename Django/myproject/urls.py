from django.urls import path,include
from .myproject import views

path('myapp/',include('myapp.urls'))
path('',views.index, name = 'index')




