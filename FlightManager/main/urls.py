from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),

    # Authentication
    path('register/', views.RegisterView.as_view(), name = 'auth.signup'),
    path('login/', views.LoginView.as_view(), name = 'auth.signin'),
    path('logout/', views.auth_logout, name = 'auth.signout'),

    # Profile
    path('profile/', views.profile_view, name = 'profile.view'),
    path('profile/update', views.UpdateProfileView.as_view(), name = 'profile.update_information'),
    path('profile/update/password', views.UpdatePasswordView.as_view(), name= 'profile.update_password'),

    # Airport
    path('airport/', views.ListAirportView.as_view(), name = 'airport.list'),
    path('airport/create/', views.CreateAirportView.as_view(), name = 'airport.create'),
    path('airport/update/<str:pk>/', views.UpdateAirportView.as_view(), name = 'airport.update'),
    path('airport/delete/<str:pk>/', views.DeleteAirportView.as_view(), name = 'airport.delete'),

    # Flight
    path('flight/', views.ListFlightView.as_view(), name = 'flight.list'),
    path('flight/create/', views.CreateFlightView.as_view(), name = 'flight.create'),
    path('flight/detail/<str:pk>/', views.DetailFlightView.as_view(), name = 'flight.detail'),
    path('flight/update/<str:pk>/', views.UpdateFlightView.as_view(), name = 'flight.update'),
    path('flight/delete/<str:pk>/', views.DeleteFlightView.as_view(), name = 'flight.delete'),

    # Flight Detail
    path('flight/detail/<str:pk>/update', views.UpdateFlightDetailView.as_view(), name = 'flight.detail.update'),   #update flight detail

    # Transition Airport

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