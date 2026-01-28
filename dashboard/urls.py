from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.landing_page, name='home'),
    path('redirect/', views.role_redirect, name='role_redirect'),
    path('tester/', views.tester_dashboard, name='tester_dashboard'),
    path('developer/', views.developer_dashboard, name='developer_dashboard'),
]
