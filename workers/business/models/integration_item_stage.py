# -*- coding: utf-8 -*-

from django.db import models

from workers.business.enums.integration_state import IntegrationState

from workers.business.models.integration_item import IntegrationItem
from workers.business.models.worker_task import WorkerTask


class IntegrationItemStage(models.Model):

    item = models.ForeignKey(IntegrationItem, on_delete=models.CASCADE, related_name="stages")
    task = models.ForeignKey(WorkerTask, on_delete=models.PROTECT)
    sequence = models.IntegerField()
    state = models.IntegerField(choices=IntegrationState.choices, default=0)
    create_date = models.DateField()
    init_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    message = models.CharField(max_length=255, null=True)
    details = models.TextField(null=True)
    count = models.IntegerField(default=0)

    class Meta:

        constraints = [
            models.UniqueConstraint(name='UK_integration_stage_01', fields=['item', 'task', 'sequence'])
        ]

        indexes = [
            models.Index(name='IDX_integration_stage_01', fields=['state'])
        ]

    def __str__(self):
        return '{} - {}'.format(self.item.name, self.task.name)
