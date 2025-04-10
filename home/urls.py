from django.urls import path
from . import views



urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.aboutpage, name='about'),
    path('involved/', views.getinvolvedpage, name='involved'),
    path('program/', views.programpage, name='program'),
]
