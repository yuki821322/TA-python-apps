# Create your views here.
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def index(request):
    return HttpResponse("たけのこ")