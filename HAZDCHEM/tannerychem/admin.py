from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Chemical

@admin.register(Chemical)
class ChemicalAdmin(admin.ModelAdmin):
    list_display = ['name', 'expiry_date', 'hazard_rating', 'banned_status']
    search_fields = ['name']
    list_filter = ['hazard_rating', 'banned_status']
