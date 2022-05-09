# -*- coding: utf-8 -*-

from django.db import models


class IntegrationState(models.IntegerChoices):

    PENDING = 0
    RUNNING = 1
    DONE = 2
    ERROR = 3
    CANCELED = 4
