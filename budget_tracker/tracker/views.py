from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# view function for the dashboard
@login_required
def dashboard(request):
    return render(request,'tracker/dashboard.html')

