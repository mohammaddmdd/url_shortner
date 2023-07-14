from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
import uuid

from .forms import SignUpForm
from .models import Url
from django.http import HttpResponse



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('index')
            else:
                # Authentication failed, return an error message
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        # Render the login form page
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})

@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')


def generate(request):
    if request.method == 'POST':
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def follow(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
