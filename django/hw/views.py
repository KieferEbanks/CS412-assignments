# file: django/hw/views.py
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def home(request: HttpRequest) -> HttpResponse:
    '''A function that responds to the home request'''

    response_text = '''
    <html>
        <h1>Hello, World!</h1>
    </html>
    '''

    return HttpResponse(response_text)
