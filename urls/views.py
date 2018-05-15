from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the urls index.")

def short_url(request, short_url):
    response = "You would normally be redirected to the long url associated with %s"
    return HttpResponse(response % short_url)
