from django.shortcuts import render
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

def login(request):
  return render(request, 'users\login.html')


def sign_up(request):
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect ('')
  else:
    form = RegisterForm()
  return render(request, "registration/sign_up.html", {"form": form})
