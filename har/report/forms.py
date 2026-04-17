from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'longitude', 'latitude', 'altitude', 'accuracy']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Report name', 'class': 'my-input-class'}),
            'longitude': forms.TextInput(attrs={'placeholder': 'Longitude', 'pattern': '(-|)\\d{1,3}.\\d+'}),
            'latitude': forms.NumberInput(attrs={'placeholder': 'Latitude', 'step': 'any'}),
            'altitude': forms.NumberInput(attrs={'placeholder': 'Altitude', 'step': 'any'}),
            'accuracy': forms.NumberInput(attrs={'placeholder': 'Accuracy', 'step': 'any', 'title': 'A decimal number'}),
        }

class ConnectionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email Address',
        'id': 'email' # Optional, but good for consistency
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'id': 'password', # CRITICAL: This allows document.getElementById("password") to work
        'class': 'password'
    }))
