from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def newpage(request):
    head=request.GET['s_head']
    menu=request.GET['s_menu']
    body=request.GET['s_body']
    menu=menu.split()
    return render(request,'newpg.html',{'head':head,'menu':menu,'body':body})
