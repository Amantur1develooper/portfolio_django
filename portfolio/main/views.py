from django.http.response import HttpResponseRedirect

from django.shortcuts import render
from .models import SendMessage

# Create your views here.
def index(request):
    return render(request,"index.html")
    
def formMessage(request):
    if request.method=='POST':
        sendmessege=SendMessage()
        sendmessege.email=request.POST.get('email')
        sendmessege.phone_number=request.POST.get('phone_number')
        sendmessege.message=request.POST.get("message")
        sendmessege.sent_at=request.POST.get('sent_at')
        sendmessege.save()

        return HttpResponseRedirect('/')