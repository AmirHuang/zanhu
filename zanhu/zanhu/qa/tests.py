from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)

    content_type = models.ForeignKey(ContentType, verbose_name='关联的表的名称')
    object_id = models.CharField(verbose_name='关联的表的某一条数据的id')

    content_object = GenericForeignKey('content_type', 'object_id')


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    comment = GenericRelation(Comment)


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    comment = GenericRelation(Comment)


class Picture(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    comment = GenericRelation(Comment)
