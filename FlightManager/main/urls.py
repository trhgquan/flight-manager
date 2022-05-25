from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('flights/', views.flights),
    path('customer/', views.customer),

    # Authentication
    path('signup/', views.signup, name='auth.signup'),
    path('login/', views.login, name='auth.login'),
]