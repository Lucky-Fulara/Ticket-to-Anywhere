import json
import http.client
from .forms import InfoForm
from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from .forms import BookingForm
from django.http import JsonResponse
import requests

# Create your views here.
def start(request):
    return render(request, 'm.html')
def about_us(request):
    return render(request, 'about_us.html')
def help(request):
    return render(request, 'help.html')
def feedback(request):
    return render(request, 'feedback.html')
def offers(request):
    return render(request, 'offers.html')
def match(request):
    return render(request, 'match.html')
def crick(request):
    return render(request, 'cric.html')

#bus data
# views.py
from django.shortcuts import render, redirect
from .forms import BusBookingForm

from django.shortcuts import render
from .forms import BusBookingForm

def search_buses(request):
    if request.method == "POST":
        departure = request.POST['departure']
        arrival = request.POST['arrival']
        date = request.POST['date']
        buses = get_bus_data(departure, arrival, date)
        form = BusBookingForm()
        return render(request, 'book_bus.html', {'form': form, 'buses': buses})
    else:
        form = BusBookingForm()
    return render(request, 'bus.html', {'form': form})
from django.shortcuts import render
from .forms import BusBookingForm
def get_bus_data(departure, arrival, date):
    # Mock bus data with real cities of India and additional details
    all_buses = [
        {
            'BusNumber': 'ABC123',
            'Departure': 'Delhi',
            'Arrival': 'Mumbai',
            'Time': '9:00 AM',
            'Price': '100 INR',
            'SeatsAvailable': 30,
            'Duration': '10 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'ABC Travels',
            'Rating': 4.5,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'XYZ456',
            'Departure': 'Bangalore',
            'Arrival': 'Chennai',
            'Time': '11:00 AM',
            'Price': '120 INR',
            'SeatsAvailable': 25,
            'Duration': '6 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'XYZ Buses',
            'Rating': 4.0,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'PQR789',
            'Departure': 'Kolkata',
            'Arrival': 'Jaipur',
            'Time': '8:00 AM',
            'Price': '150 INR',
            'SeatsAvailable': 20,
            'Duration': '12 hours',
            'Amenities': ['AC', 'WiFi', 'Entertainment System'],
            'Operator': 'PQR Travels',
            'Rating': 4.2,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'LMN321',
            'Departure': 'Hyderabad',
            'Arrival': 'Pune',
            'Time': '10:30 AM',
            'Price': '110 INR',
            'SeatsAvailable': 28,
            'Duration': '8 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'LMN Buses',
            'Rating': 3.8,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'STU654',
            'Departure': 'Ahmedabad',
            'Arrival': 'Surat',
            'Time': '12:00 PM',
            'Price': '90 INR',
            'SeatsAvailable': 35,
            'Duration': '4 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'STU Travels',
            'Rating': 4.1,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'EFG987',
            'Departure': 'Lucknow',
            'Arrival': 'Bhopal',
            'Time': '2:00 PM',
            'Price': '130 INR',
            'SeatsAvailable': 22,
            'Duration': '14 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'EFG Buses',
            'Rating': 3.9,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'JKL654',
            'Departure': 'Chandigarh',
            'Arrival': 'Amritsar',
            'Time': '3:30 PM',
            'Price': '80 INR',
            'SeatsAvailable': 40,
            'Duration': '5 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'JKL Travels',
            'Rating': 4.3,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'NOP321',
            'Departure': 'Goa',
            'Arrival': 'Mangalore',
            'Time': '5:00 PM',
            'Price': '100 INR',
            'SeatsAvailable': 18,
            'Duration': '7 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'NOP Buses',
            'Rating': 4.0,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'QWE789',
            'Departure': 'Indore',
            'Arrival': 'Nagpur',
            'Time': '6:30 PM',
            'Price': '120 INR',
            'SeatsAvailable': 25,
            'Duration': '9 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'QWE Travels',
            'Rating': 4.4,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'RTY456',
            'Departure': 'Ranchi',
            'Arrival': 'Patna',
            'Time': '8:00 PM',
            'Price': '110 INR',
            'SeatsAvailable': 30,
            'Duration': '6 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'RTY Buses',
            'Rating': 4.1,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'UIO987',
            'Departure': 'Agra',
            'Arrival': 'Varanasi',
            'Time': '9:30 PM',
            'Price': '140 INR',
            'SeatsAvailable': 20,
            'Duration': '10 hours',
            'Amenities': ['AC', 'WiFi', 'Entertainment System'],
            'Operator': 'UIO Travels',
            'Rating': 4.3,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'ASD123',
            'Departure': 'Vadodara',
            'Arrival': 'Bhubaneswar',
            'Time': '11:00 PM',
            'Price': '160 INR',
            'SeatsAvailable': 28,
            'Duration': '12 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'ASD Buses',
            'Rating': 4.0,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'FGH456',
            'Departure': 'Thiruvananthapuram',
            'Arrival': 'Kochi',
            'Time': '1:00 AM',
            'Price': '130 INR',
            'SeatsAvailable': 22,
            'Duration': '5 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'FGH Travels',
            'Rating': 4.2,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'JKL789',
            'Departure': 'Raipur',
            'Arrival': 'Guwahati',
            'Time': '3:30 AM',
            'Price': '170 INR',
            'SeatsAvailable': 35,
            'Duration': '16 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'JKL Buses',
            'Rating': 4.5,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'QWE123',
            'Departure': 'Jodhpur',
            'Arrival': 'Udaipur',
            'Time': '5:00 AM',
            'Price': '90 INR',
            'SeatsAvailable': 18,
            'Duration': '4 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'QWE Travels',
            'Rating': 4.0,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'RTY456',
            'Departure': 'Shimla',
            'Arrival': 'Manali',
            'Time': '6:30 AM',
            'Price': '150 INR',
            'SeatsAvailable': 25,
            'Duration': '8 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'RTY Buses',
            'Rating': 4.3,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'UIO987',
            'Departure': 'Dehradun',
            'Arrival': 'Haridwar',
            'Time': '8:00 AM',
            'Price': '80 INR',
            'SeatsAvailable': 30,
            'Duration': '3 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'UIO Travels',
            'Rating': 4.1,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'ASD123',
            'Departure': 'Jaisalmer',
            'Arrival': 'Ajmer',
            'Time': '9:30 AM',
            'Price': '110 INR',
            'SeatsAvailable': 35,
            'Duration': '5 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'ASD Buses',
            'Rating': 4.4,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'FGH456',
            'Departure': 'Gangtok',
            'Arrival': 'Darjeeling',
            'Time': '11:00 AM',
            'Price': '120 INR',
            'SeatsAvailable': 22,
            'Duration': '6 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'FGH Travels',
            'Rating': 4.2,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'JKL789',
            'Departure': 'Leh',
            'Arrival': 'Srinagar',
            'Time': '1:00 PM',
            'Price': '140 INR',
            'SeatsAvailable': 20,
            'Duration': '10 hours',
            'Amenities': ['AC', 'WiFi', 'Entertainment System'],
            'Operator': 'JKL Buses',
            'Rating': 4.3,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'QWE123',
            'Departure': 'Shillong',
            'Arrival': 'Gangtok',
            'Time': '3:30 PM',
            'Price': '130 INR',
            'SeatsAvailable': 18,
            'Duration': '9 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'QWE Travels',
            'Rating': 4.1,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'RTY456',
            'Departure': 'Nainital',
            'Arrival': 'Mussoorie',
            'Time': '5:00 PM',
            'Price': '100 INR',
            'SeatsAvailable': 25,
            'Duration': '7 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'RTY Buses',
            'Rating': 4.0,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'UIO987',
            'Departure': 'Puri',
            'Arrival': 'Bhubaneswar',
            'Time': '6:30 PM',
            'Price': '110 INR',
            'SeatsAvailable': 30,
            'Duration': '2 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'UIO Travels',
            'Rating': 4.2,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'ASD123',
            'Departure': 'Kochi',
            'Arrival': 'Kozhikode',
            'Time': '8:00 PM',
            'Price': '120 INR',
            'SeatsAvailable': 35,
            'Duration': '5 hours',
            'Amenities': ['AC', 'WiFi', 'Charging Point'],
            'Operator': 'ASD Buses',
            'Rating': 4.4,
            'Date': '2024-05-28'
        },
        {
            'BusNumber': 'FGH456',
            'Departure': 'Visakhapatnam',
            'Arrival': 'Vijayawada',
            'Time': '9:30 PM',
            'Price': '130 INR',
            'SeatsAvailable': 22,
            'Duration': '6 hours',
            'Amenities': ['AC', 'Charging Point'],
            'Operator': 'FGH Travels',
            'Rating': 4.1,
            'Date': '2024-05-28'
        }
        # Add more buses here
    ]
    # Filter buses based on user input
    filtered_buses = [
        bus for bus in all_buses if bus['Departure'].lower() == departure.lower()
        and bus['Arrival'].lower() == arrival.lower()
        and bus['Date'] == date
    ]
    return filtered_buses

def book_bus(request, bus_number):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            # Handle booking logic here, e.g., save booking to the database
            return render(request, 'booking_confirmation.html', {'form': form, 'bus_number': bus_number})
    else:
        form = BookingForm()
    return render(request, 'book_bus.html', {'form': form, 'bus_number': bus_number})
# views.py
from django.shortcuts import render

# views.py
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import BookingForm

def confirm_bus_booking(request, bus_number):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Collect the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            seat_quantity = form.cleaned_data['seat_quantity']

            # Redirect to the success page with the booking details
            return redirect(reverse('home:booking_confirmation_success') + f"?bus_number={bus_number}&name={name}&email={email}&seat_quantity={seat_quantity}")
    else:
        form = BookingForm()

    context = {
        'bus_number': bus_number,
        'form': form,
    }
    return render(request, 'confirm_booking.html', context)

import random
from django.shortcuts import render

def booking_confirmation_success(request):
    bus_number = request.GET.get('bus_number')
    name = request.GET.get('name')
    email = request.GET.get('email')
    seat_quantity = int(request.GET.get('seat_quantity', 1))  # Default to 1 seat if not provided

    # Generate random price per seat between $20 and $50
    price_per_seat = random.randint(100, 600)
    total_price = seat_quantity * price_per_seat

    # Generate random ticket number and seat number
    ticket_number = random.randint(100000, 999999)
    seat_number = random.randint(1, 50)

    context = {
        'bus_number': bus_number,
        'name': name,
        'email': email,
        'seat_quantity': seat_quantity,
        'price_per_seat': price_per_seat,
        'total_price': total_price,
        'ticket_number': ticket_number,
        'seat_number': seat_number,
    }
    return render(request, 'booking_confirmation_success.html', context)

#cricket data

def cricket_booking_confirmation(request):
    if request.method == 'POST':
        # Retrieve booking details from POST data
        name = request.POST.get('name')
        email = request.POST.get('email')
        match_date = request.POST.get('match_date')
        ticket_type = request.POST.get('ticket_type')
        quantity = request.POST.get('quantity')
        
        # Render the confirmation HTML file with booking details
        return render(request, 'cric_conf.html', {
            'name': name,
            'email': email,
            'ticket_type': ticket_type,
            'quantity': quantity
        })
    else:
        # Render the booking form template for GET requests
        return render(request, 'cric_conf.html')
#upload

import http.client
import json
from django.shortcuts import render
from django.http import HttpResponse

def upload_info(request):
    if request.method == 'POST':
        from_station_code = request.POST.get('from_station_code')
        to_station_code = request.POST.get('to_station_code')
        date_of_journey = request.POST.get('date_of_journey')

        conn = http.client.HTTPSConnection("irctc1.p.rapidapi.com")

        headers = {
            
            'X-RapidAPI-Key': "f1678ef839mshfb4e8c348c2a764p1c1c77jsn1af780cc608d",
            'X-RapidAPI-Host': "irctc1.p.rapidapi.com"
        }

        endpoint = f"/api/v3/trainBetweenStations?fromStationCode={from_station_code}&toStationCode={to_station_code}&dateOfJourney={date_of_journey}"
        conn.request("GET", endpoint, headers=headers)

        res = conn.getresponse()
        data = res.read()
        
        try:
            train_data = json.loads(data)
        except json.JSONDecodeError:
            return render(request, 'upload_info.html', {'error_message': 'Error decoding the train data response.'})

        if 'data' in train_data:
            trains = train_data['data']
            
            for train in trains:
                availability_endpoint = f"/api/v1/checkSeatAvailability?classType=2A&fromStationCode={from_station_code}&quota=GN&toStationCode={to_station_code}&trainNo={train['train_number']}&date={date_of_journey}"
                conn.request("GET", availability_endpoint, headers=headers)
                availability_res = conn.getresponse()
                availability_data = availability_res.read()
                
                try:
                    availability_json = json.loads(availability_data)
                except json.JSONDecodeError:
                    train['availability'] = []
                    continue
                
                train['availability'] = availability_json.get('data', [])

            return render(request, 'display_info.html', {'trains': trains})
        else:
            error_message = train_data.get('message', 'No train data available.')
            return render(request, 'upload_info.html', {'error_message': error_message})
    else:
        return render(request, 'upload_info.html')

# book

from django.shortcuts import render, redirect

def book_tickets(request):
    if request.method == 'POST':
        train_number = request.POST.get('train_number')
        class_type = request.POST.get('class_type')
        return render(request, 'book_tickets.html', {
            'train_number': train_number,
            'class_type': class_type
        })
    else:
        # Pass default values for train_number and class_type
        return redirect('home:train_tickets', train_number='', class_type='')

# book confirm
from django.shortcuts import render, redirect
import random

def booking_confirmation(request):
    if request.method == 'POST':
        passenger_name = request.POST.get('passenger_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        train_number = request.POST.get('train_number')
        seat_type = request.POST.get('seat_type')

         # Generate random ticket number and seat number
        ticket_number = random.randint(100000, 999999)
        seat_number = random.randint(1, 100)
        
        confirmation_message = f"Booking confirmed for {passenger_name} on train {train_number}"

        return render(request, 'booking_confirmation.html', {
            'confirmation_message': confirmation_message,
            'passenger_name': passenger_name,
            'age': age,
            'gender': gender,
            'train_number': train_number,
            'seat_type': seat_type,
            'ticket_number': ticket_number,
            'seat_number': seat_number
        })
    else:
        return redirect('home:train_tickets')

#display
def display_info(request):
    data = request.session.get('api_data')
    if data:
        return render(request, 'home:display_info.html', {'data': data})
    else:
        return redirect('train_tickets') 

# home/views.py

from django.shortcuts import render, redirect
from django.http import HttpResponse

# Placeholder function to fetch flight data
def get_flight_data(departure, arrival, date):
    # Replace this with actual data fetching logic (e.g., API call or scraping)
    all_flights = [
        {
            'FlightNumber': 'AI202',
            'Departure': 'BLR',
            'Arrival': 'DEL',
            'Time': '10:00 AM',
            'Price': '5000 INR'
        },
        {
            'FlightNumber': '6E505',
            'Departure': 'BLR',
            'Arrival': 'DEL',
            'Time': '02:00 PM',
            'Price': '4500 INR'
        },
        {
            'FlightNumber': 'AI203',
            'Departure': 'DEL',
            'Arrival': 'BLR',
            'Time': '04:00 PM',
            'Price': '5500 INR'
        },
        {
            'FlightNumber': 'AI204',
            'Departure': 'BOM',
            'Arrival': 'DEL',
            'Time': '09:00 AM',
            'Price': '6000 INR'
        },
        # Additional mock flights
        {
            'FlightNumber': 'AI205',
            'Departure': 'BLR',
            'Arrival': 'BOM',
            'Time': '08:00 AM',
            'Price': '5500 INR'
        },
        {
            'FlightNumber': '6E506',
            'Departure': 'BLR',
            'Arrival': 'BOM',
            'Time': '12:00 PM',
            'Price': '4800 INR'
        },
        {
            'FlightNumber': 'AI206',
            'Departure': 'BLR',
            'Arrival': 'MAA',
            'Time': '03:00 PM',
            'Price': '4000 INR'
        },
        {
            'FlightNumber': '6E507',
            'Departure': 'BLR',
            'Arrival': 'MAA',
            'Time': '06:00 PM',
            'Price': '4200 INR'
        },
        {
            'FlightNumber': 'AI207',
            'Departure': 'BLR',
            'Arrival': 'HYD',
            'Time': '11:00 AM',
            'Price': '3500 INR'
        },
        {
            'FlightNumber': '6E508',
            'Departure': 'BLR',
            'Arrival': 'HYD',
            'Time': '04:00 PM',
            'Price': '3800 INR'
        },
        {
            'FlightNumber': 'AI208',
            'Departure': 'BLR',
            'Arrival': 'CCU',
            'Time': '09:00 AM',
            'Price': '4500 INR'
        },
        {
            'FlightNumber': '6E509',
            'Departure': 'BLR',
            'Arrival': 'CCU',
            'Time': '01:00 PM',
            'Price': '4700 INR'
        },
        {
            'FlightNumber': 'AI209',
            'Departure': 'BLR',
            'Arrival': 'GOI',
            'Time': '10:00 AM',
            'Price': '5500 INR'
        },
        {
            'FlightNumber': '6E510',
            'Departure': 'BLR',
            'Arrival': 'GOI',
            'Time': '03:00 PM',
            'Price': '5300 INR'
        },
        {
            'FlightNumber': 'AI210',
            'Departure': 'BLR',
            'Arrival': 'AMD',
            'Time': '02:00 PM',
            'Price': '4800 INR'
        },
        {
            'FlightNumber': '6E511',
            'Departure': 'BLR',
            'Arrival': 'AMD',
            'Time': '07:00 PM',
            'Price': '5100 INR'
        },
        {
            'FlightNumber': 'AI211',
            'Departure': 'BLR',
            'Arrival': 'COK',
            'Time': '01:00 PM',
            'Price': '4900 INR'
        },
        {
            'FlightNumber': '6E512',
            'Departure': 'BLR',
            'Arrival': 'COK',
            'Time': '05:00 PM',
            'Price': '5200 INR'
        },
        {
            'FlightNumber': 'AI212',
            'Departure': 'BLR',
            'Arrival': 'PNQ',
            'Time': '03:00 PM',
            'Price': '4700 INR'
        },
        {
            'FlightNumber': '6E513',
            'Departure': 'BLR',
            'Arrival': 'PNQ',
            'Time': '07:00 PM',
            'Price': '4900 INR'
        },
        # Add more mock flights as needed
    ]

    # Debug: Print the received departure, arrival, and date
    print(f"Departure: {departure}, Arrival: {arrival}, Date: {date}")

    # Filter flights based on departure and arrival
    filtered_flights = [flight for flight in all_flights if flight['Departure'] == departure and flight['Arrival'] == arrival]

    # Debug: Print the filtered flights
    print(f"Filtered Flights: {filtered_flights}")

    return filtered_flights


def search_flights(request):
    if request.method == 'POST':
        departure = request.POST.get('departure')
        arrival = request.POST.get('arrival')
        date = request.POST.get('date')
        
        flight_data = get_flight_data(departure, arrival, date)
        
        return render(request, 'search_results.html', {'flights': flight_data})
    
    return render(request, 'search_flights.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse

def book_flight(request):
    if request.method == 'GET':
        flight_number = request.GET.get('flight_number')
        return render(request, 'book_flight.html', {'flight_number': flight_number})
    elif request.method == 'POST':
        # Process the booking confirmation here (e.g., save to database)
        # Then redirect to the confirmation page
        return redirect('home:confirm_booking')

def confirm_booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        flight_number = request.POST['flight_number']
        selected_class = request.POST['class']
        selected_seat = request.POST['seat']
        
        context = {
            'name': name,
            'age': age,
            'flight_number': flight_number,
            'selected_class': selected_class,
            'selected_seat': selected_seat
        }
        
        return render(request, 'book_confirmation.html', context)
    else:
        return HttpResponse("Invalid request method.", status=405)