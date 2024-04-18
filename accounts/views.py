from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_view(request):
    return render(request, "accounts/login.html")

def signup_view(request):
    if request.method == "POST":
        return HttpResponseRedirect(reverse("courses:index"))
    return render(request, "accounts/register.html")

def logout(request):
    pass

def delete_account(request):
    pass