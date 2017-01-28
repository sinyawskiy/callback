# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Callback(models.Model):
    name = models.CharField(u'имя', max_length=255, blank=True, null=True)
    email = models.EmailField(u'e-mail', blank=True, null=True)
    phone = models.CharField(u'телефонный номер', max_length=255)
    created_at = models.DateTimeField(u'создано', default=timezone.now)

    class Meta:
        verbose_name = u'запрос'
        verbose_name_plural = u'запросы'