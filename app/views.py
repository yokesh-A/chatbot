from django.shortcuts import render
from django.http import HttpResponse
from .models import dictionary
import json

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
    elif request.GET.get("__a") == 'Chatbot':
        data = request.GET.get("msg")
        replies = getreply(data)
        return HttpResponse(replies)
    elif request.GET.get("__a") == 'Suggest':
        ai = dictionary.objects.all().order_by('-usage')
        suggest = []
        for row in ai:
            if row.keys.strip():
                suggest.append(row.question)
        return HttpResponse(json.dumps(suggest))

    return render(request, 'index.html', {})

def getreply(data):
    message = data.lower()
    reply = []

    ai = dictionary.objects.all()
    for row in ai:
        if row.keys.strip():
            keys = row.keys.split()
            chk = 1
            for k in keys:
                if k in message:
                    chk = chk*1
                else:
                    chk = chk*0
            if chk > 0:
                reply.append(row.answer)
                row.usage = row.usage+1
                row.save()


    if reply == []:
        reply.append("sorry Unable to understand")
        msg = dictionary(question=message)
        msg.save()
    return " ".join(reply)