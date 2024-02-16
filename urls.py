from django.urls import path
from . import views
# 
urlpatterns = [
    path('dashboard/',views.board,name='home'),

    path('',views.loginpage,name='loginpage'),

    path('loginuser/',views.loginuser,name='loginuser'),

    path('logout/',views.logout,name='logout'),

    path('registerhere/',views.registerhere,name='registerhere'),

    path('register/',views.register,name='register'),

    path('opening/',views.Job_openings,name='opening'),

    path('Total_applicants',views.Total_applicants,name='Total_applicants'),

    path('schedule/', views.schedule_interviews, name='schedule'),

    path('schedule/<int:pk>/', views.schedule_interviews, name='updateinterviews'),

    path('deleteinteview/<str:pk>/',views.delete_interview,name='deleteinterview'),

    path('addcandidate', views.addcandidate, name='addcandidate'),

    path('addcandidate/<str:pk>', views.addcandidate, name='updatecandidate'),

    path('delete_candidate/<str:pk>', views.deletecandidate, name='delete_candidate'),

    path('hire/', views.Hire, name='hire'),

    path('hire/<int:pk>/', views.Hire, name='update_hire'),

    path('delete_hire/<str:pk>/',views.delete_hire,name='delete_hire'),

    path('add_vacant/',views.vacant,name='add_vacant'),

    path('update_vacant/<str:pk>/',views.vacant,name='update_vacant'),

]
