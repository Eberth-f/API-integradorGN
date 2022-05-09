# -*- coding: utf-8 -*-

from django.contrib import admin

from workers.business.models.worker_queue import WorkerQueue
from workers.business.models.worker_task import WorkerTask
from workers.business.models.worker_thread import WorkerThread
from workers.business.models.worker_pool import WorkerPool
from workers.business.models.worker_pool_thread import WorkerPoolThread


# register models in admin management interface
# TODO : This can be replaced by API views in the future
admin.site.register(WorkerQueue)
admin.site.register(WorkerTask)


class WorkerThreadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WorkerThread._meta.concrete_fields]


admin.site.register(WorkerThread, WorkerThreadAdmin)

admin.site.register(WorkerPool)
admin.site.register(WorkerPoolThread)