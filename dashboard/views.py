from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import UserProfile

def landing_page(request):
    return render(request, 'dashboard/home.html')

@login_required
def role_redirect(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        return redirect('/admin/')

    if profile.role == 'ADMIN':
        return redirect('/admin/')
    elif profile.role == 'TESTER':
        return redirect('dashboard:tester_dashboard')
    elif profile.role == 'DEVELOPER':
        return redirect('dashboard:developer_dashboard')

    return redirect('/')
def tester_dashboard(request):
    return render(request, 'dashboard/tester_dashboard.html')
def developer_dashboard(request):
    return render(request, 'dashboard/developer_dashboard.html')