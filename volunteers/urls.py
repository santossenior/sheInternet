from django.urls import path
from . import views

urlpatterns = [
    path('submit-volunteer-form/', views.submit_volunteer_form, name='volunteer'),
]
