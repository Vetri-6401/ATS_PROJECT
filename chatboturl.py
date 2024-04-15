from django.urls import path
from . import views

urlpatterns = [
    path('',views.open_chat,name='Home'),
    path('get_user_input', views.get_user_input_view, name='get_user_input'),
]
