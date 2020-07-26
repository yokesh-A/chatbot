from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.GET.get("__a") == 'Home':
        return render(request, 'home.html', {})
    elif request.GET.get("__a") == 'Work':
        return render(request, 'work.html', {})
    elif request.GET.get("__a") == 'Portfolio':
        return render(request, 'portfolio.html', {})
    elif request.GET.get("__a") == 'About':
        return render(request, 'about.html', {})
    elif request.GET.get("__a") == 'Contact':
        return render(request, 'contact.html', {})

    return render(request, 'index.html', {})
