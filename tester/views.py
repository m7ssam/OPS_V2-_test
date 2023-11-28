from django.shortcuts import redirect, render
from .forms import T1Form
from django.contrib.auth import login, logout, authenticate
from .models import T1, T2
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


@login_required()
def test_page(request):
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
  form = T1Form()
  context = {"t1":t1 , "form": form, "count": t1.count()}
  return render(request, 'test/test.html', context)
