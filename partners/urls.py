from django.urls import path
from .views import submit_partner_form

urlpatterns = [
    path('submit-partner-form/', submit_partner_form, name='submit_partner_form'),
]