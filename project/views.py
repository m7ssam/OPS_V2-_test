from django.shortcuts import render
from .models import Name
from django.contrib.auth.decorators import login_required
@login_required()
def home(request):  
  name = Name.objects.all()
  context = {"name": name}
  return render(request, 'project/home.html',context )

