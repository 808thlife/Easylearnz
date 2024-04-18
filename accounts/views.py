from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import User

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("courses:index"))
    if request.method == "POST":

        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("courses:index"))
        else:
            return render(request, "accounts/login.html", {
                "message": "Invalid username and/or password."
            })

    return render(request, "accounts/login.html")

def signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("courses:index"))
    else:
        if request.method == "POST":

            #getting information from request
            email = request.POST["email"]
            password = request.POST["password"]
            username = request.POST["username"]

            #user = authenticate(request, email = email, password = password)

            try:
                user = User.objects.create_user(email, password)
                user.username = username
                user.save()
            except IntegrityError:
                return render(request, "accounts/register.html", {
                    "message": "Username already taken."
                })

            return render(request, "accounts/login.html", {"messages":"You have successfully created an account! Now You have to Log in"})
        return render(request, "accounts/register.html")

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("accounts:signup"))

@login_required
def delete_account(request):
    user = request.user 
    user.delete()
    return HttpResponseRedirect(reverse("accounts:signup"))

def user_profile(request, ID):
    return render(request, "accounts/profile.html")