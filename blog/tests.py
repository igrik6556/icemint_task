# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from blog.models import Post
from django.contrib.auth.models import User


class Test(TestCase):

    def test_post(self):
        """
        This test create user and login.
        Then add and edit post.
        """
        c = Client()
        User.objects.create_user(username='Ihor', password='123')
        c.login(username="Ihor", password='123')

        response = c.get(reverse('blog:users'))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('blog:posts', kwargs={'usr_pk': 1}))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('blog:create_post'))
        self.assertEqual(response.status_code, 200)

        response = c.post(reverse('blog:create_post'), data={
            'title': 'Test post',
            'text': 'Some text',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='Test post').exists())

        response = c.get(reverse('blog:full_post', kwargs={'post_pk': 1}))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('blog:edit_post', kwargs={'post_pk': 1}))
        self.assertEqual(response.status_code, 200)

        response = c.post(reverse('blog:edit_post', kwargs={'post_pk': 1}), data={
            'title': 'Test post',
            'text': 'Some edited text',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(text='Some edited text').exists())

