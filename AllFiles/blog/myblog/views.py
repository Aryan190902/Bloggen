from tkinter.tix import Tree
from urllib import request
from xml.etree.ElementTree import Comment
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categories, Post, Comment
from .forms import PostForm, EditForm, choiceLst, CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    #ordering = ['-post_date']
    ordering = ['-id']

class Article(DetailView):
    model = Post
    template_name = 'articleDetail.html'
    def get_context_data(self, **kwargs):
        context = super(Article, self).get_context_data(**kwargs)
        like = get_object_or_404(Post, id= self.kwargs['pk'])
        total_likes = like.total_likes()

        liked = False
        if like.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class About(ListView):
    model = Post
    template_name = 'about.html' 

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # for providing author username
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

    #fields = '__all__'

class AddCategory(CreateView):
    model = Categories
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'

def Category(request):
    category_lst = choiceLst
    #form_class = PostForm
    return render(request, 'categories.html', {'categoryLst':category_lst})

def Cat(request, cats):
    category_post = Post.objects.filter(category=cats)
    return render(request, 'categoryPost.html', {'cats':cats, 'category_post':category_post})

def LikePost(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('likeButton'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('articleDetail', args=[str(pk)]))

class EditPost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')

class AddComment(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('home')
    # for providing author username
    def form_valid(self, form):
        form.instance.author= self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)