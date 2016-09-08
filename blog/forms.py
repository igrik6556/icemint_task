# -*- coding: utf-8 -*-
from django import forms
from blog.models import Post
from pagedown.widgets import PagedownWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "text", "is_publish")
        widgets = {"title": forms.TextInput(attrs={"class": "form-control"}),
                   "text": PagedownWidget(attrs={"rows": 15, "class": "form-control"})}
