# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.utils.translation import ugettext as _


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
        default=timezone.now
    )
    dt_edit = models.DateTimeField(
        _("Last edit"),
        null=True,
        blank=True
    )
    is_publish = models.BooleanField(_("Publish?"))
    author = models.ForeignKey(
        User,
        verbose_name=_("Entry author")
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if Post.objects.filter(id=self.id).exists():
            self.dt_edit = timezone.now()
        super(Post, self).save(*args, **kwargs)

    def get_user_post(self):
        return Post.objects.filter(author=self).filter(is_publish=True)

    def get_my_post(self):
        return Post.objects.filter(author=self)

    @models.permalink
    def get_absolute_url(self):
        return "blog:full_post", [self.pk]
