from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('greet/<str:name>/', views.greet_by_name),
]
