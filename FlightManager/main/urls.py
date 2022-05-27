from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Flight list
    path('flight/list/', views.flightList, name='flight_list'),
    path('flight/detail/<str:pk>/', views.flightDetail, name='flight_detail'),
    path('flight/update/<str:pk>', views.flightUpdate, name='flight_update'),
    path('flight/detailupdate/<str:pk>/', views.flightDetailUpdate, name='flight_detail_update'),   #update flight detail
    path('flight/create/', views.flightCreate, name='flight_create'),
    path('flight/detailcreate/', views.flightDetailCreate, name='flight_detail_create'),   #create detail
    path('flight/delete/<str:pk>', views.flightDelete, name='flight_delete'),

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

    # Booking
    path('booking/', views.booking, name='booking'),

    # Report
    path('report/', views.report, name='report'),

    #customer
    #path('customer_list/', views.customer, name="customer_list"),
    path('customer_per/',views.customerPer, name="customer_per"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/', views.updateCustomer, name="update_customer"),
    path('delete_customer/', views.deleteCustomer, name="delete_customer"),
]