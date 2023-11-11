from django.shortcuts import redirect, render
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from .models import User_id

def home(request):
  return render(request, 'home/home.html')

def invalid_user(request):
  return render(request, 'registration/invalid.html')

def created(request):
  return render(request, 'registration/created.html')
# def created(request, id):
#   user = User_id.objects.get(pk = id)
#   context = {"user":user}
#   return render(request, 'registration/invalid.html',context)



def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_id_input = form.cleaned_data.get("id")
            # Check if the user ID exists in the User_id model
            if User_id.objects.filter(id=user_id_input).exists():
                user_record = User_id.objects.get(id=user_id_input)
                first_name = user_record.first_name
                last_name = user_record.last_name
                user.username = f"{first_name} {last_name}"
                user.is_active = False
                user.save()
                login(request, user)
                return redirect("/users/created")
            else:
                # Redirect the user to the login page
                return redirect("/users/invalid_user")  # Adjust the actual URL as needed
    else:
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"form": form})

"""
def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            login(request, user)
            return redirect('users/login/')
    else:
        form = RegisterForm()
    return render(request, "registration/sign_up.html", {"form": form})
"""
