from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, 'home/home.html')

def Documentation(request):
  return render(request, 'home/Documentation.html')

def underconstruction(request):
  return render(request, 'underconstruction.html')

