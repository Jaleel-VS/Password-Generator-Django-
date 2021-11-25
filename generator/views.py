from random import choice

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # names = ('Joseph', 'Mary', 'Steve', 'Peter')
    # return HttpResponse(f'Hello, there {choice(names)} ')
    return render(request, 'generator/home.html', {'password': '11rqfadqi'})


def eggs(request):
    return HttpResponse('I like eggs')
