from django.urls import path
from .views import ContactMessageCreateView

app_name = 'contact_api'

urlpatterns = [
    # Create new contact message
    path('contact', ContactMessageCreateView.as_view(), name='contact-create'),
]
