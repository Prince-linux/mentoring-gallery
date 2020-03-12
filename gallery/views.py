
from django.shortcuts import render, redirect

# from django.contrib import messages



def index(request):
    # return HttpResponse('Hello, World')
    return render(request, 'gallery/index.html', {'message': 'Hello World!'})


def signup(request):
    return render(request, 'gallery/signup.html', {})








