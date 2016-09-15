# -*- coding: utf-8 -*-
from django.conf.urls import url
from blog import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^users/$', login_required(views.UsersList.as_view()), name='users_list'),
    url(r'^users/(?P<pk>\d+)/$', login_required(views.UserPosts.as_view()), name='post_list'),
    url(r'^(?P<pk>\d+)/$', login_required(views.DetailUserPost.as_view()), name='post_detail'),
    url(r'^create/$', login_required(views.CreatePost.as_view()), name='post_create'),
    url(r'^(?P<pk>\d+)/update/$', login_required(views.EditPost.as_view()), name='post_edit'),
]
