from django.urls import path
from . import views

urlpatterns = [
    path('register-user/', views.registerUser, name='register_user'),
    path('register-vendor/', views.registerVendor, name='register_vendor'),
]
