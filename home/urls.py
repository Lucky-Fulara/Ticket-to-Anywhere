from django.contrib import admin
from django.urls import path
from . import views
app_name = 'home'  # Set the namespace here
urlpatterns = [ 
    path('wwe/', views.start, name='wwe'), 
    path('help/', views.help, name='help'),
    path('feedback/', views.feedback, name='feedback'), 
    path('offers/', views.offers, name='offers'), 
    path('about-us/', views.about_us, name='about_us'), 
    
    path('search/', views.search_flights, name='search_flights'),
    path('book/', views.book_flight, name='book_flight'),
    path('confirm/', views.confirm_booking, name='confirm_booking'),
    
    path('mat/', views.match, name='match'),
    path('cric/', views.crick, name='cric'),
    path('cricket_booking_confirmation/', views.cricket_booking_confirmation, name='cricket_booking_confirmation'),

    path('search_buses', views.search_buses, name='search_buses'),
    path('home/book_bus/<str:bus_number>/', views.book_bus, name='book_bus'),
    path('confirm_bus_booking/<str:bus_number>/', views.confirm_bus_booking, name='confirm_bus_booking'),
    path('booking_confirmation_success/', views.booking_confirmation_success, name='booking_confirmation_success'),



    path('upload_info/', views.upload_info, name='upload_info'),
    path('display-info/', views.display_info, name='display_info'),   
    path('book-tickets/', views.book_tickets, name='book_tickets'),
    path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
