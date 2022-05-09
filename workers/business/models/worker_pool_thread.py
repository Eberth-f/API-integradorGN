# -*- coding: utf-8 -*-

from django.db import models

from workers.business.models.worker_thread import WorkerThread
from workers.business.models.worker_pool import WorkerPool


class WorkerPoolThread(models.Model):

    def __str__(self):
        return '{} - {}'.format(self.pool.name, self.thread.name)

    pool = models.ForeignKey(WorkerPool, on_delete=models.CASCADE, related_name="pool_threads")
    thread = models.ForeignKey(WorkerThread, on_delete=models.PROTECT)
