from typing import Any
from django.db.models.query import QuerySet
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import T1Form
from django.contrib.auth import login, logout, authenticate
from .models import T1, Post,  ExampleModel
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


@login_required()
def test_home(request):
  return render(request, 'tester/home.html')

# T1 -----------------------------------------------------------------------------------
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
  return render(request, 'tester/t1.html', context)

# T2 -----------------------------------------------------------------------------------
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

class PostList(ListView):
  model = Post ## using defult post_list

  # # ------------------------------------------------
  # context_object_name = all_posts                 #|
  # # ------------------------------------------------
  # queryset = Post.objects.filter(title = "java")  #|
  # # ------------------------------------------------
  # def get_queryset(self) -> QuerySet[Any]:        #|
  #   return Post.objects.filter(title = "java")    #|
  # # ------------------------------------------------
  # template_name = "templates/test"                #|
  # # ------------------------------------------------

  def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    context = super().get_context_data(**kwargs)
    counter = Post.objects.count()
    context['passed_data'] = "this is a data passed from get_context_data "
    context['counter'] = counter
    return context
  
  ordering = ["-id"]
  paginate_by = None

class PostDetail(DetailView):
  model = Post
  

class PostCreate(CreateView):
  fields = ("title" , "content")
  model =Post

class PostUpdate(UpdateView):
  fields = ("title" , "content")
  model =Post
  def get_object(self, queryset=None):
    try:
        # Try to get the object based on the pk
        return super().get_object(queryset=queryset)
    except Http404:
        # If the object is not found, raise Http404 exception
        raise Http404("Post does not exist")

  def get(self, request, *args, **kwargs):
      try:
          # Try to get the object based on the pk
          return super().get(request, *args, **kwargs)
      except Http404:
          # If the object is not found, redirect to a custom 404 page
          return render(request, '404.html', status=404)

  def post(self, request, *args, **kwargs):
      try:
          # Try to get the object based on the pk
          return super().post(request, *args, **kwargs)
      except Http404:
          # If the object is not found, redirect to a custom 404 page
          return render(request, '404.html', status=404)


class PostDelete(DeleteView):
  model =Post
  success_url = reverse_lazy("post_list")



"""
@login_required()
def t2(request):
  post = Post.objects.all()
  context = {"post" : post}
  return render(request, 'test/t2.html', context)
@login_required()
def t2_1(request, pk):
  post = None
  context = {"post" : post}
  return render(request, 'test/t2.1.html', context)
"""


# T3 -----------------------------------------------------------------------------------
# views.py
def t3(request):
    # Retrieve all blog posts from the database
    blog_posts = ExampleModel.objects.all()

    # Pass the blog posts to the template
    return render(request, 'tester/t3.html', {'blog_posts': blog_posts})

