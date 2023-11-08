from django.shortcuts import render
from .models import Name
# Create your views here.
def home(request):
  name = Name.objects.all()
  context = {"name": name}
  return render(request, 'project/home.html',context )

