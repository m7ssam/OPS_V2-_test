from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required()
def home(request):
  return render(request, 'home/home.html')

@login_required()
def Documentation(request):
  return render(request, 'home/Documentation.html')


@login_required()
def underconstruction(request):
  return render(request, 'underconstruction.html')

