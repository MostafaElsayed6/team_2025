from django import forms
from .models import Trip #userInput
# from .models import Booking

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['title', 'description', 'image', 'capacity']


# class UserInputForm(forms.ModelForm):
#     class Meta:
#         model = userInput
#         fields = ['name', 'email', 'phone', 'address', 'trip_dateTime']


# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['user_name', 'email', 'phone', 'address', 'booking_date']
#         widgets = {
#             'booking_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
#         }