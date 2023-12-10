from django.shortcuts import render
from project.models import Name
from django.contrib.auth.decorators import login_required

@login_required()
def home(request):
  return render(request, 'report/home.html' )

@login_required()
def Project_home(request):
  name = Name.objects.all()
  context = {"name": name}
  return render(request, 'report/Project_home.html',context )

@login_required()
def Revenue_home(request):
  context = None
  return render(request, 'report/Revenue_home.html',context )

@login_required()
def Eqp_home(request):
  context = None
  return render(request, 'report/Eqp_home.html',context )

@login_required()
def report(request):
  return render(request, 'report/project_report.html' )

@login_required()
def project_contract(request):
  return render(request, 'report/project_contract.html' )