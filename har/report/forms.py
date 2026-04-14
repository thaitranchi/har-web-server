from django import models
from django import forms
from .models import Report
from django.contrib.auth.models import User

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'latitude', 'longitude', 'altitude', 'accuracy']

class ConnectionForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    password = forms.CharField(widget=forms.PasswordInput)
