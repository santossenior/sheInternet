from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
import pandas as pd
from django.http import HttpResponse
from django.contrib import admin
from .models import PartnerForm

@admin.action(description="Export selected partner form as Excel")
def export_selected_partnership_excel(modeladmin, request, queryset):
    # Convert the queryset to a list of dictionaries
    data = list(queryset.values('name', 'organization', 'email', 'message'))
    
    # Convert timezone-aware datetimes to timezone-naive
    
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Create the HTTP response
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="partnership.xlsx"'
    
    # Write the DataFrame to the response
    df.to_excel(response, index=False)
    
    return response

class PartnerFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization', 'email', 'message']
    list_filter = ['name', 'organization', 'email', 'message']
    actions = [export_selected_partnership_excel]

admin.site.register(PartnerForm, PartnerFormAdmin)