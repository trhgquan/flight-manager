from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    # Flight list
    path('flights/', views.flights),

    
    path('customer/', views.customer),

    # Authentication
    path('signup/', views.signup, name='auth.signup'),
    path('login/', views.login, name='auth.login'),

    # Report
    path('report/', views.report, name='report'),
]