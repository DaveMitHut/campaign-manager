from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse("Hello World! You are looking at the user management index.")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('index')

    else:
        form = UserCreationForm

    return render(request, 'usermanagement/index.html', {'form': form})
