from django import forms
from .models import LeaveRequest
from django.forms.widgets import DateInput

# from django.forms import ModelForm

class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['first_name', 'last_name', 'leave_start', 'leave_end', 'leave_type', 'reason', 'total_days', 'total_left']
        widgets = {
            'leave_start': DateInput(attrs={'type': 'date'}),
            'leave_end': DateInput(attrs={'type': 'date'})
        } 