from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('register/', views.Register, name='accounts.register'),
    path('login/', views.Login, name='login'),



]