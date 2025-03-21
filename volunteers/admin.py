from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
import pandas as pd
from django.http import HttpResponse
from django.contrib import admin
from .models import VolunteerForm

@admin.action(description="Export selected volunteer form as Excel")
def export_selected_volunteers_excel(modeladmin, request, queryset):
    # Convert the queryset to a list of dictionaries
    data = list(queryset.values('name', 'phone', 'email', 'contribution', 'time_commitment', 'message'))
    
    # Convert timezone-aware datetimes to timezone-naive
    
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Create the HTTP response
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="volunteers.xlsx"'
    
    # Write the DataFrame to the response
    df.to_excel(response, index=False)
    
    return response

class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'contribution',  'time_commitment', 'message']
    list_filter = ['name', 'phone', 'email', 'contribution', 'time_commitment', 'message']
    actions = [export_selected_volunteers_excel]

admin.site.register(VolunteerForm, VolunteerAdmin)