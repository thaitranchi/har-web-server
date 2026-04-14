from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'longitude', 'latitude', 'altitude', 'accuracy']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Report name'}),
            'longitude': forms.NumberInput(attrs={'placeholder': 'Longitude', 'step': 'any'}),
            'latitude': forms.NumberInput(attrs={'placeholder': 'Latitude', 'step': 'any'}),
            'altitude': forms.NumberInput(attrs={'placeholder': 'Altitude', 'step': 'any'}),
            'accuracy': forms.NumberInput(attrs={'placeholder': 'Accuracy', 'step': 'any'}),
        }

class ConnectionForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
