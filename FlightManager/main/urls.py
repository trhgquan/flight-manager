from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),

    # Flight list
    path('flight/list/', views.flightList, name = 'flight_list'),
    path('flight/detail/<str:pk>/', views.flightDetail, name = 'flight_detail'),
    path('flight/update/<str:pk>', views.flightUpdate, name = 'flight_update'),
    path('flight/detailupdate/<str:pk>/', views.flightDetailUpdate, name = 'flight_detail_update'),   #update flight detail
    path('flight/create/', views.flightCreate, name = 'flight_create'),
    path('flight/detailcreate/', views.flightDetailCreate, name = 'flight_detail_create'),   #create detail
    path('flight/delete/<str:pk>', views.flightDelete, name = 'flight_delete'),

    # Airport
    path('airport/', views.ListAirportView.as_view(), name = 'airport.list'),
    path('airport/create/', views.CreateAirportView.as_view(), name = 'airport.create'),
    path('airport/update/<str:id>/', views.UpdateAirportView.as_view(), name = 'airport.update'),
    path('airport/delete/<str:id>/', views.deleteAirport, name = 'airport.delete'),

    # Authentication
    path('register/', views.RegisterView.as_view(), name = 'auth.signup'),
    path('login/', views.LoginView.as_view(), name = 'auth.signin'),
    path('logout/', views.auth_logout, name = 'auth.signout'),

    # Profile
    path('profile/', views.profile_view, name = 'profile.view'),
    path('profile/update', views.UpdateProfileView.as_view(), name = 'profile.update_information'),
    path('profile/update/password', views.UpdatePasswordView.as_view(), name= 'profile.update_password'),

    # Booking
    path('booking/', views.booking, name = 'booking'),

    # Report
    path('report/', views.report, name = 'report'),

    #customer
    #path('customer_list/', views.customer, name = "customer_list"),
    path('customer_per/',views.customerPer, name = "customer_per"),
    path('create_customer/', views.createCustomer, name = "create_customer"),
    path('update_customer/', views.updateCustomer, name = "update_customer"),
    path('delete_customer/', views.deleteCustomer, name = "delete_customer"),
]