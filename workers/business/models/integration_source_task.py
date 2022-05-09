# -*- coding: utf-8 -*-

from django.db import models

from workers.business.models.integration_source import IntegrationSource
from workers.business.models.worker_task import WorkerTask


class IntegrationSourceTask(models.Model):

    sequence = models.IntegerField()
    source = models.ForeignKey(IntegrationSource, on_delete=models.CASCADE, related_name="tasks")
    task = models.ForeignKey(WorkerTask, on_delete=models.PROTECT)

    class Meta:

        constraints = [
            models.UniqueConstraint(name='UK_integration_source_task_01', fields=['sequence', 'source', 'task'])
        ]

    def __str__(self):
        return '{} - {}'.format(self.source.name, self.task.name)
