from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

from .models import Profile
from .forms import ProfileForm

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"])
            form = ProfileForm(request.POST)
            if form.is_valid():
                profile = Profile()
                profile.user = user
                profile.college = form.cleaned_data['college']
                profile.department = form.cleaned_data['department']
                profile.save()
                auth.login(request, user)
                return redirect('lecture:list')
            else:
                user.delete()
        
        form = ProfileForm()
        return render(request, 'accounts/signup.html', {
            'form' : form,
        })
    form = ProfileForm()
    return render(request, 'accounts/signup.html',  {
            'form' : form,
        })

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('lecture:list')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('lecture:list')