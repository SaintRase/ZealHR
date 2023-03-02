from django.urls import path
from . import views

urlpatterns = [
    path('app/', views.leave_request, name='leave_request'),
    path('success/', views.success, name='success'),
    path('leave-requests/', views.leave_requests_list, name='leave_requests_list')

]