from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flights/', views.flights, name='flights'),
    path('customer/', views.customer, name='customer'),

    # Airport
    path('airport/list/', views.airport_list, name='airport_list'), 
    path('airport/create/', views.createAirport, name='create_airport'),
    path('airport/update/<str:pk>/', views.updateAirport, name='update_airport'),
    path('airport/delete/<str:pk>/', views.deleteAirport, name='delete_airport'),

    # Authentication
    path('signup/', views.signup, name='auth.signup'),
    path('login/', views.login, name='auth.login'),

    # Report
    path('report/', views.report, name='report'),
]