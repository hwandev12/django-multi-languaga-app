from django.shortcuts import render, get_object_or_404
from .models import Details

def home(request):
    return render(request, 'pages/home.html')

def details(request, slug):
    detail = get_object_or_404(Details, slug=slug)
    context = {
        'detail': detail
    }
    return render(request, 'pages/details.html', context)
