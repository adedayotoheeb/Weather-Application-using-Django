from django.urls import path
from .views import index
from . import views


app_name = 'hose'

urlpatterns = [
    path('', views.index, name='home')
]
