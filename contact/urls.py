from django.urls import path
from contact import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]