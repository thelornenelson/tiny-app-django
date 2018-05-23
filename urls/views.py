from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .models import Url


def index(request):
    all_urls = Url.objects.order_by('-pub_date')
    context = {
        'all_urls': all_urls,
    }
    return render(request, 'urls/index.html', context)

def short_url(request, short_url):
    url = get_object_or_404(Url, short_url=short_url)
    return redirect(url.long_url)
