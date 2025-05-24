from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('contact/', views.ContactFormView.as_view(), name='contact_form'),
    path('contact/success/', views.ContactSuccessView.as_view(), name='contact_success'),
    path('contact/submit/', views.contact_submit_ajax, name='contact_submit'),
]