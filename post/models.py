# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=30)
    def __str__(self):
        return u'%s' % self.name

class Post(models.Model):
    title = models.CharField(max_length=100,verbose_name='标题')
    content = models.TextField()
    created = models.DateField()
    category = models.ForeignKey(Category,verbose_name='类别')