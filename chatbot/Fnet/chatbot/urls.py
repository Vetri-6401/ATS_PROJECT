from django.urls import path
from . import views

urlpatterns = [
    path('',views.open_chat,name='Home'),
]