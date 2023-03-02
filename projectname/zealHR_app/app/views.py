from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LeaveRequestForm
from .models import LeaveRequest

from googles_calendar import create_calendar_event
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.oauth2 import service_account

def leave_request(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save()
            # Call create_calendar_event function with relevant details
            event_title = leave_request.reason
            start_time = leave_request.leave_start.isoformat()
            end_time = leave_request.leave_end.isoformat()
            create_calendar_event(event_title, start_time, end_time)
            return redirect('success')  # Redirect to a success page after submitting the form
    else:
        form = LeaveRequestForm()
    return render(request, 'myfirst.html', {'form': form})

def success(request):
    return render(request, 'success.html') 

def leave_requests_list(request):
    leave_requests = LeaveRequest.objects.all()
    return render(request, 'leave_requests_list.html', {'leave_requests': leave_requests})