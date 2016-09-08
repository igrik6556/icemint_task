# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from blog.models import Post
from blog.forms import PostForm
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from django.utils.translation import ugettext as _


class UsersList(ListView):
    """
    Display list of all users from database.
    """
    template_name = "blog/all_users.html"
    context_object_name = "users"
    model = User


class UserPosts(ListView):
    """
    Display all records that the user has left.
    """
    template_name = "blog/posts_list.html"
    model = Post
    page_kwarg = "usr_pk"

    def get_context_data(self, **kwargs):
        context = super(UserPosts, self).get_context_data(**kwargs)
        if int(self.request.user.id) == int(self.kwargs["usr_pk"]):
            context["posts"] = Post.get_my_post(self.request.user.id)
        else:
            context["posts"] = Post.get_user_post(self.kwargs["usr_pk"])
        context["auth"] = User.objects.get(pk=self.kwargs["usr_pk"])
        return context


class DetailUserPost(DetailView):
    """
    Show full post.
    """
    template_name = "blog/full_post.html"
    context_object_name = "post"
    model = Post
    pk_url_kwarg = "post_pk"


class CreatePost(SuccessMessageMixin, CreateView):
    """
    Create new post.
    """
    form_class = PostForm
    template_name = "blog/create_post.html"
    success_message = _("Post <%(title)s> successfully added!")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreatePost, self).form_valid(form)


class EditPost(SuccessMessageMixin, UpdateView):
    """
    Update post.
    """
    model = Post
    form_class = PostForm
    template_name = "blog/edit_post.html"
    success_message = _("Post <%(title)s> successfully updated!")
    pk_url_kwarg = "post_pk"

    def form_valid(self, form):
        if form.instance.author != self.request.user:
            return HttpResponseForbidden()
        return super(EditPost, self).form_valid(form)


def custom_404(request):
    return render(request, 'errors/404.html', {}, status=404)
