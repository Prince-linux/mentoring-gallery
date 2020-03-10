from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse('Hello, World')
    return render(request, 'gallery/index.html', {'message': 'Hello World!'})

