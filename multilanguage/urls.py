from django.urls import path
from .views import details, home

app_name = 'lanapp'

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>/', details, name='details'),
]