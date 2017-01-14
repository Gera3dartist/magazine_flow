from blogpost.managers import BlogPostManager
from django.db import models

# Create your models here.


_app_label = 'blogpost'


class BlogPost(models.Model):
    title = models.CharField(max_length=128, default='some title')
    body = models.CharField(max_length=256, default='some body')
    is_confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to='reporter.Reporter', related_name='articles')
    objects = BlogPostManager()

    class Meta:
        db_table = 'blogpost_post'
        app_label = _app_label


