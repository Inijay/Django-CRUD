from django.shortcuts import render
from django.views import Post

from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    fields='_all_'
    success_url  = reverse_lazy('blog:all')

class PostCreateView(CreateView):
    model = Post
    fields = '_all_'
    template_name=["base.html","post_confirm_detele.html","post_details.html","post_forms.html","post_list.html"]
    
class PostDetailView(DetailView):
    model = Post
    fields='_all_'
    success_url  = reverse_lazy('blog:all')

class PostUpdateView(UpdateView):
    model = Post
    fields='_all_'
    success_url  = reverse_lazy('blog:all')

class PostDeleteView(DeleteView):
    model = Post
    fields='_all_'
    success_url  = reverse_lazy('blog:all')
