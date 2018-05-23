from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from .models import Url


def index(request):
    all_urls = Url.objects.order_by('-pub_date')
    context = {
        'all_urls': all_urls,
    }
    return render(request, 'urls/index.html', context)

def short_url(request, short_url):
    response = "You would normally be redirected to the long url associated with %s"
    return HttpResponse(response % short_url)
