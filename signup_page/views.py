# views.py
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from .models import Signup

def index(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process form data and redirect
            return redirect('success_url')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def homepage(request):
    return render(request, 'homepage.html')



# Create your views here.
