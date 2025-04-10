import pandas as pd
from django.http import HttpResponse
from django.contrib import admin
from .models import Subscriber

@admin.action(description="Export selected newsletter as Excel")
def export_selected_newsletter_excel(modeladmin, request, queryset):
    # Convert the queryset to a list of dictionaries
    data = list(queryset.values('name', 'email'))
    
    # Convert timezone-aware datetimes to timezone-naive
    
    
    # Create a DataFrame
    df = pd.DataFrame(data)
    
    # Create the HTTP response
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="newsletter.xlsx"'
    
    # Write the DataFrame to the response
    df.to_excel(response, index=False)
    
    return response

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', ]
    
    actions = [export_selected_newsletter_excel]

admin.site.register(Subscriber, SubscriberAdmin)