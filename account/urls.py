from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('register/', views.Register, name='account.register'),
    path('login/', views.Login, name='account.login'),

    path('logout/', views.logout, name='account.logout'),



]