from django.shortcuts import render
from project.models import Name
# Create your views here.
def home(request):
  name = Name.objects.all()
  context = {"name": name}
  return render(request, 'report/home.html',context )
def report(request):
  return render(request, 'report/project_report.html' )