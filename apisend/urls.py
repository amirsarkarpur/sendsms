from django.urls import path
from .views import send,SmsList


urlpatterns = [
    path('send/', send.as_view(), name='send'),
    path('list/', SmsList.as_view(), name='List'),

] 
