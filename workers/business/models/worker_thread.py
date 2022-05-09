# -*- coding: utf-8 -*-

from django.db import models

from workers.business.models.worker_queue import WorkerQueue
from workers.business.models.worker_task import WorkerTask
from workers.business.models.worker_pool import WorkerPool


class WorkerThread(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    queue = models.ForeignKey(WorkerQueue, on_delete=models.PROTECT)
    task = models.ForeignKey(WorkerTask, on_delete=models.PROTECT)
    # pool = models.ForeignKey(WorkerPool, on_delete=models.CASCADE, default=None, null=True)
