from random import choice
from string import (ascii_lowercase as lower,
                    ascii_uppercase as upper,
                    punctuation as special,
                    digits as numbers)

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    # names = ('Joseph', 'Mary', 'Steve', 'Peter')
    # return HttpResponse(f'Hello, there {choice(names)} ')
    return render(request, 'generator/home.html')


def password(request):
    all_characters = lower

    password_options = {
        'uppercase': upper,
        'special': special,
        'numbers': numbers,
    }  # 2

    for k, v in password_options.items():
        if request.GET.get(k):
            all_characters += v

    length = int(request.GET.get('length', 12))

    generated_password = ''

    for x in range(length):
        generated_password += choice(all_characters)

    return render(request, 'generator/password.html', {'password': generated_password})


def about(request):
    return render(request, 'generator/about.html')
