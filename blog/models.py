# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.translation import ugettext as _


class PostManager(models.Manager):
    def published(self):
        return super().get_queryset().filter(is_publish=True)


class Post(models.Model):
    class Meta:
        db_table = "Post"
        ordering = ["-dt_create"]
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    title = models.CharField(
        _("Entry title"),
        max_length=100
    )
    text = models.TextField(_("Entry text"))
    dt_create = models.DateTimeField(
        _("Creation time"),
        auto_now_add=True
    )
    dt_edit = models.DateTimeField(
        _("Last edit"),
        null=True,
        blank=True
    )
    is_publish = models.BooleanField(_("Publish?"))
    author = models.ForeignKey(
        User,
        verbose_name=_("Entry author"),
        related_name="posts"
    )

    objects = PostManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            self.dt_edit = timezone.now()
        super(Post, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return "blog:post_detail", [self.pk]
