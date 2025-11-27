from django.contrib import admin
from .models import Donation  # Import the Donation model

# Register the model with Django's admin site
@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'timestamp')  # Fields to show in list view
    search_fields = ('name',)  # Add search box
    list_filter = ('timestamp',)  # Add filter sidebar
