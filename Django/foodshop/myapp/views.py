from django.shortcuts import render
from .models import Item
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("helloo from my app")
    
def about(request):
    item_list = Item.objects.all()
    context = {'item_list':item_list}
    return render(request,'data.html',context)