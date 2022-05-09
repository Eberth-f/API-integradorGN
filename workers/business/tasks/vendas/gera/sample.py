# -*- coding: utf-8 -*-

import time
import threading

from workers.tools.worker_task import WorkerTask


class SampleWorkerTask(WorkerTask):

    def __init__(self, logger):
        super(SampleWorkerTask, self).__init__(logger)

    def execute(self, body):
        self.logger.info("Task execute in T-{}: {}...".format(
            threading.current_thread().ident,
            body
        ))
        time.sleep(10)
        self.logger.info("Task executed in T-{} ended...".format(threading.current_thread().ident))
