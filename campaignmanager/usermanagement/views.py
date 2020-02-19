from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import authenticate, login

# Create your views here.
def index_view(request):
    return HttpResponse("Hello World! You are looking at the user management index.")

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("Successfully logged in.")
    
    else:
        return HttpResponse("Something went wrong.")


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('index')

    else:
        form = UserCreationForm

    return render(request, 'usermanagement/index.html', {'form': form})
