from django import forms

class InfoForm(forms.Form):
    from_station = forms.CharField(label='From', max_length=100)
    to_station = forms.CharField(label='To', max_length=100)
    date = forms.DateField(label='Date', widget=forms.SelectDateWidget)
    travel_class = forms.ChoiceField(label='Class', choices=[
        ('general', 'General'),
        ('sleeper', 'Sleeper'),
        ('ac1', 'AC 1'),
        ('ac2', 'AC 2'),
        ('ac3', 'AC 3'),
    ])
    disability = forms.BooleanField(label='Person With Disability Concession', required=False)
    flexible = forms.BooleanField(label='Flexible With Date', required=False)
    available_berth = forms.BooleanField(label='Train with Available Berth', required=False)
    railway_pass = forms.BooleanField(label='Railway Pass Concession', required=False)
# forms.py
class BookingForm(forms.Form):
    train_number = forms.CharField(label='Train Number', max_length=100)
    class_type = forms.CharField(label='Class Type', max_length=100)
    passenger_name = forms.CharField(label='Passenger Name', max_length=100)
    # Add more fields as needed

class FlightSearchForm(forms.Form):
    departure_airport = forms.CharField(label='From', max_length=100)
    arrival_airport = forms.CharField(label='To', max_length=100)
    date = forms.DateField(label='Date', widget=forms.DateInput(attrs={'type': 'date'}))
    from django import forms

from django import forms
from .models import BusBooking

# forms.py
from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100, label='Name')
    email = forms.EmailField(label='Email')
    seat_quantity = forms.IntegerField(min_value=1, label='Seat Quantity')


class BusBookingForm(forms.ModelForm):
    class Meta:
        model = BusBooking
        fields = ['name', 'age', 'bus_number', 'seat_number']
from django import forms

class BusBookingForm(forms.Form):
    # You can add fields here if needed for booking
    pass