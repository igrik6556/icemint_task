# -*- coding: utf-8 -*-
from django.conf.urls import url
from blog import views

from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^users/$', login_required(views.UsersList.as_view()), name='users'),
    url(r'^users/(?P<usr_pk>\d+)/$', login_required(views.UserPosts.as_view()), name='posts'),
    url(r'^(?P<post_pk>\d+)/$', login_required(views.DetailUserPost.as_view()), name='full_post'),
    url(r'^create/$', login_required(views.CreatePost.as_view()), name='create_post'),
    url(r'^(?P<post_pk>\d+)/update/$', login_required(views.EditPost.as_view()), name='edit_post'),
]
