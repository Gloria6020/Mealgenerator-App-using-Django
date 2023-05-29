from django.shortcuts import render
import random

def index(request):
    return render(request, 'mealgenerator/index.html')


# Create your views here.
