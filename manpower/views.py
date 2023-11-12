from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required()
def mp_list(request):
  return render(request, 'manpower\mp_list.html')

@login_required()
def mp_meta(request):
  return render(request, 'manpower\mp_meta')


@login_required()
def mp_home(request):
  return render(request, 'manpower\mp_home.html')