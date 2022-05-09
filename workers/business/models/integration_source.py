# -*- coding: utf-8 -*-

from django.db import models


class IntegrationSource(models.Model):

    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)

    def __str__(self):
        return self.name
