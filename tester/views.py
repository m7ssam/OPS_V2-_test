from django.shortcuts import redirect, render
from .forms import T1Form
from django.contrib.auth import login, logout, authenticate
from .models import T1, T2
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required

@login_required()
def test_home(request):
  return render(request, 'test/home.html')

@login_required()
def t1(request):
  t1 = T1.objects.all()
  if request.method == 'POST':
    if "save" in request.POST:
      form = T1Form(request.POST)
      if form.is_valid():
        form.save()
    elif "delete" in request.POST:
      pk = request.POST.get("delete")
      td = T1.objects.get(id = pk)
      td.delete()
    elif "edit" in request.POST:
      pass
      pk = request.POST.get("edit")
      td = T1.objects.get(id = pk)
      form = T1Form(instance=td)
  form = T1Form()
  context = {"t1":t1 , "form": form, "count": t1.count()}
  return render(request, 'test/t1.html', context)



@login_required()
def t2(request):
  return render(request, 'test/t2.html')
