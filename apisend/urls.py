from django.urls import path
from .views import send


urlpatterns = [
    path('send/', send.as_view(), name='send'),
] 
