from django.http import HttpResponse

def index(request):
    return HttpResponse("hello from  myproject views index inside myproject")