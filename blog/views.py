from django.shortcuts import render
from blog.models import Configuracion, Post
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User

def index(request):
    posts = Post.objects.order_by('-date_published').all()
    return render(request, 'blog/index.html', {'posts': posts})

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

class ListPost(ListView):
    model = Post
    paginate_by = 2

class CreatePost(CreateView):
    model = Post
    fields = ['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")

class DetailPost(DetailView):
    model=Post

class UpdatePost(UpdateView):
    model=Post
    fields = ['title', 'short_content', 'content', 'image']
    success_url = reverse_lazy("list-post")

class DeletePost(DeleteView):
    model=Post
    success_url = reverse_lazy("list-post")


class SearchPostByName(ListView):
    def get_queryset(self):
        blog_title = self.request.GET.get('post-title')
        return Post.objects.filter(title__icontains=blog_title)

class BlogLogin(LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("list-post")

class BlogLogout(LogoutView):
    template_name = 'blog/blog_logout.html'

class BlogSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileUpdate(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("blog-login")