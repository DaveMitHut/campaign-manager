from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello World! You are looking at the user management index.")