from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mp_list, Mp_history
from .forms import Mp_move
from .filters import Mp_list_Filter
from django.db import IntegrityError

@login_required()
def mp_list(request):
  mp_list = Mp_list.objects.select_related("code")
  mp_list_filter = Mp_list_Filter(request.GET, queryset= mp_list)
  mp_list = mp_list_filter.qs
  context = {
     "mp_list": mp_list,
     "mp_list_filter": mp_list_filter,
              }
  return render(request, 'manpower/mp_list.html',context )

@login_required()
def mp_move_list(request):
  list = Mp_history.objects.all()
  context = {"list": list}
  return render(request, 'manpower/mp_move_list.html',context)

@login_required()
def user_page(request,pk):
  target_user = Mp_list.objects.get(id = pk)
  context = {"target_user": target_user}
  return render(request, "manpower/user_page.html", context)


@login_required()
def mp_home(request):
  return render(request, 'manpower/mp_home.html')

@login_required()
def error(request):
  return render(request, 'manpower/error.html')

@login_required()
def something_went_wrong(request):
  return render(request, 'manpower/something_went_wrong.html')


@login_required()
def mp_move(request):
  if request.method == "POST":
      form = Mp_move(request.POST)
      if form.is_valid():
          change = form.save(commit=False)
          id_input = form.cleaned_data.get("id")
          # Check if the user ID exists in the Mp_list model
          if Mp_list.objects.filter(id=id_input).exists():
              try:
                change.save()
                return redirect("mp_home")
              except IntegrityError:
                return redirect("error")
          else:
              # Redirect the user to the login page
              return redirect("error")
  else:
    form = Mp_move()
  context = {"form": form}
  return render(request, 'manpower/mp_move.html',context)

