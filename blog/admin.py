# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget
from blog.models import Post

from django.utils.translation import ugettext as _


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dt_create', 'dt_edit', 'is_publish',)
    list_filter = ('author', 'is_publish', )
    date_hierarchy = 'dt_create'
    search_fields = ['title', ]
    fieldsets = (
        (None, {'fields': ('author', 'title', 'text', 'is_publish', )}),
        (_("Important_dates"), {'fields': ('dt_create', 'dt_edit', )})
    )
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

admin.site.register(Post, PostAdmin)
