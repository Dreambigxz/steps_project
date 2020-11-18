from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .form import PostForm, CommentForm
from django.views.generic import (TemplateView,
                                  ListView,DetailView,
                                  DeleteView, CreateView,
                                  UpdateView)

from .models import Post, Comment
from  django.utils import  timezone
from django.urls import  reverse_lazy
from django.contrib.auth.decorators import login_required  ######fuction base view
from django.contrib.auth.mixins import  LoginRequiredMixin  ####class base view

from datetime import datetime
from datetime import timedelta

# Create your views here.

class BaseView(TemplateView):

    template_name = 'blog/base.html'


class AboutView(TemplateView):

    template_name = 'blog/about.html'


class PostListView(ListView):
    login_url = 'about'
    #redirect_field_name = 'about'

    model = Post

    def get_queryset(self):

        obj= Post.objects.filter().order_by('-created_date')
        return obj


class PostDetailView(DetailView):
    login_url = 'about'
    redirect_field_name = 'about'

    model = Post

    ###########CRUD REQUIRE LOGIN ###########



class CreatePost(LoginRequiredMixin,CreateView ):

    login_url = 'about'
    redirect_field_name = 'about'

    #form_class = PostForm
    model = Post
    success_url = 'post_list'
    fields = ['author', 'tittle', 'text']



class EditPost(LoginRequiredMixin, UpdateView):


    login_url = ''
    redirect_field_name = ''

    fields = ('tittle', 'text')
    model = Post

class DeletePost(LoginRequiredMixin, DeleteView):


    login_url = 'about'
    redirect_field_name = 'about'

    model = Post
    success_url = reverse_lazy('post_list')


    ###########DRAFT LIST VIEW

class DraftListView(LoginRequiredMixin, ListView):

    login_url = 'about'
    redirect_field_name = 'about'


    model = Post


    def get_queryset(self):

        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')

##################function base view handling comment ##########




@login_required()
def post_publish(request, pk):


    post= get_object_or_404(Post, pk=pk)

    post.publish()


    return redirect('')


#@login_required(login_url='about')
def create_comment(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method=='POST':

        form= CommentForm(request.POST)

        if form.is_valid():
            comment= form.save(commit=False)
            comment.post=post

            comment.save()

            return redirect('detail', post.pk)


    else:

        form=CommentForm()

    return render(request, 'blog/comment.html', {'form':form })



@login_required()
def comment_approve(request, pk):

    comment= get_object_or_404(Comment, pk=pk)

    comment.approve()

    return redirect('detail', comment.post.pk)


@login_required()
def delete_comment(request, pk):

    comment= get_object_or_404(Comment, pk=pk)

    # x=print('Are you sure you want to delete this comment ?', 'yes', 'no')
    #
    # if x== 'yes':

    comment.delete()

    return redirect('detail', comment.post.pk)


###################TRYING OUT SOMETHING ###############

# def dashbord(request, pk):









