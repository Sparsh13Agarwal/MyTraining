from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def index(request):
#     return HttpResponse("Hello from myapp views index")

def index(request):
    d = {
        'data':"Django is good"
    }
    list = [1,2,3,4,5,6,7,8,9]
    return render(request,"data.html",{'d':d,'list':list})