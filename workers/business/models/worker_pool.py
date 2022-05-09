# -*- coding: utf-8 -*-

from django.db import models


class WorkerPool(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)

