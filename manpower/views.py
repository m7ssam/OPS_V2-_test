from django.shortcuts import render

# Create your views here.
def mp_list(request):
  return render(request, 'manpower\mp_list.html')

def mp_meta(request):
  return render(request, 'manpower\mp_meta')


def mp_home(request):
  return render(request, 'manpower\mp_home.html')