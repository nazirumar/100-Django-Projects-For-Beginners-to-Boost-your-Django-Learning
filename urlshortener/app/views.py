from django.shortcuts import render, redirect

# Create your views here.

import pyshorteners

def shorturl(original_url):
   shorturl_url=pyshorteners.Shortener().tinyurl.short(original_url)
   return shorturl_url



def index(request):
    original_url = request.POST.get('original_url')
    shorturls = ''
    if request.method == 'POST':
        if original_url:
            shorturls = shorturl(original_url)
        shorturls = shorturl('https//')
    context = {
        'shorturls':shorturls
    }
    return render(request, 'index.html', context)