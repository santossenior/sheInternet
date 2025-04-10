import pandas as pd
from django.http import HttpResponse
from django.contrib import admin
from .models import SheInternetForm

@admin.action(description="Export selected community as Excel")
def export_selected_community_excel(modeladmin, request, queryset):
    # Convert the queryset to a list of dictionaries
    data = list(queryset.values('name', 'email', 'country', 'description', 'interested', 'about'))
    
    # Convert timezone-aware datetimes to timezone-naive
    for item in data:
        if item['subscribed_at']:
            item['subscribed_at'] = item['subscribed_at'].replace(tzinfo=None)
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Create the HTTP response
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="community.xlsx"'
    
    # Write the DataFrame to the response
    df.to_excel(response, index=False)
    
    return response

class SheInternetFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'description', 'interested', 'about']
    actions = [export_selected_community_excel]

admin.site.register(SheInternetForm, SheInternetFormAdmin)