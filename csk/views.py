from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def msd(request):
    return render(request,'msd.html')
def bumrah(request):
    return HttpResponse('Boom Boom BUmrah')
