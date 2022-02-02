from django.shortcuts import render
from .models import HomePageSlider, HomePageBody



def homedisplay(request):
    return render(request, 'donor_home.html')


