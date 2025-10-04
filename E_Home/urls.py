
from django.urls import path ,include
from .import views

urlpatterns = [
    path('',views.home, name='home' ),
    path('cart/',views.cart, name='cart'),
    path('login/',views.login, name='login'),
    path('register/',views.register ,name='register')
]
