# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import render
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.translation import ugettext as _


class UsersList(ListView):
    """
    Display list of all users from database.
    """
    template_name = "blog/users_list.html"
    context_object_name = "users"
    model = User


class UserPosts(DetailView):
    """
    Display all records that the user has left.
    """
    template_name = "blog/post_list.html"
    context_object_name = "author"
    model = User


class DetailUserPost(DetailView):
    """
    Show full post.
    """
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    model = Post


class CreatePost(SuccessMessageMixin, CreateView):
    """
    Create new post.
    """
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_message = _("Post <%(title)s> successfully added!")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CreatePost, self).get_context_data(**kwargs)
        context["title"] = _("Create new post")
        return context


class EditPost(SuccessMessageMixin, UpdateView):
    """
    Update post.
    """
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    success_message = _("Post <%(title)s> successfully updated!")

    def dispatch(self, request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs["pk"])
        if post.author != self.request.user:
            raise Http404
        return super(EditPost, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EditPost, self).get_context_data(**kwargs)
        context["title"] = _("Editing post")
        return context


def custom_404(request):
    return render(request, 'errors/404.html', {}, status=404)
