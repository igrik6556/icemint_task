# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^$', auth_views.login,
        {
            'template_name': 'blog/login.html',
        },
        name='login'
        ),
    url(r'^logout/$', auth_views.logout,
        {
            'next_page': '/'
        },
        name='logout'
        ),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
]

handler404 = 'blog.views.custom_404'
