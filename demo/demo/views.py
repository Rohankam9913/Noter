from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def landingPage(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if not user.exists():
            messages.error(request, "You dont have an account")
            return redirect('/')

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/notes")

        if user is None:
            messages.error(request, "Invalid credentials")
            return redirect("/")

    return render(request, 'landingPage.html')

def register(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Account already exists")
            return redirect("/register/")
        
        user = User.objects.create_user(
            username=username,
            password=password
        )
        
        user.save()

        return redirect("/")


    return render(request, 'register.html')

def logout_user(request):
    logout(request)
    return redirect('/')