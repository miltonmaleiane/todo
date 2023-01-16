from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def helloworld(request):
    return HttpResponse("HELLO WOORLD!")

def taskList(request):
    return render(request, "tasks/list.html")

def sobre(request):
    return render(request,"tasks/sobre.html")

def about(request):
    return render(request,"tasks/about.html")

def yourName(request, name):
    return render(request,"tasks/yourname.html",{'name':name})