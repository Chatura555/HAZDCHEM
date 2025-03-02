from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Home page
    path('chemicals/', views.chemical_list, name='chemical_list'),  # Chemical list page
    path('compatibility-checker/', views.compatibility_checker, name='compatibility_checker'),  # Compatibility checker page
]