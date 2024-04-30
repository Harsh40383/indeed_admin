from django import forms
from .models import Job  # Import the Job model from your app

class JobRegister(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary']  # Removed extra space after 'title'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),  # Changed from EmailInput to TextInput
            'location': forms.TextInput(attrs={'class': 'form-control'}),  # Changed from PasswordInput to TextInput
            'salary': forms.NumberInput(attrs={'class': 'form-control'})  # Assuming salary is a number field
        }
