# -*- coding: utf-8 -*-

import os

from pika.compat import url_unquote

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist

from workers.business.models.worker_pool import WorkerPool

from workers.tools.func import get_logger
from workers.tools.message_broker_consumer import MessageBrokerConsumer

from workers.business.tasks import FabricTask


class Command(BaseCommand):

    help = 'Run message broker worker'

    def add_arguments(self, parser):
        parser.add_argument('pool_code', nargs='+', type=str)

    def handle(self, *args, **options):

        try:

            consumer_threads = []
            pool_code = next(iter(options.get('pool_code')), None)

            try:
                pool = WorkerPool.objects.get(code=pool_code)
            except WorkerPool.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    'Pool não localizado para o código `{}`...'.format(pool_code or '<vazio>')
                ))
                return

            self.stdout.write(self.style.SUCCESS(
                'Iniciando processo para o poll `{}`...'.format(pool.name)
            ))

            for thread_number, pool_thread in enumerate(pool.pool_threads.all()):

                self.stdout.write(self.style.SUCCESS(
                    'Criando thread #{} para tarefa `{}` na fila `{}`...'.format(
                        thread_number + 1,
                        pool_thread.thread.name,
                        pool_thread.thread.queue.name
                    )
                ))

                logger = self._get_logger(pool_thread.thread.task.module_task, thread_number + 1)

                # create a task instance
                task = FabricTask.get_instance(
                    pool_thread.thread.task.module_task,
                    logger
                )
                
                # create consumer
                thread_consumer = MessageBrokerConsumer(
                    self._def_connection_url(pool_thread.thread.task.heartbeat or 60),
                    pool_thread.thread.queue.name,
                    task,
                    logger
                )
                consumer_threads.append(thread_consumer)

            self.stdout.write(self.style.SUCCESS('Aguardando por mensagens. Para sair pressione CTRL+C...'))

            # start consumer threads
            for thread in consumer_threads:
                thread.start()

            # await consumer threads done
            for thread in consumer_threads:
                thread.join()

            self.stdout.write(self.style.SUCCESS('CTRL+C pressionado. Fechando o programa...'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(
                'Erro ao inicializar o worker: {}'.format(e)
            ))

    def _def_connection_url(self, heartbeat):
        return 'amqp://{username}:{password}@{server}:{port}?heartbeat={heartbeat}'.format(
            username=url_unquote(settings.RABBITMQ_USERNAME),
            password=url_unquote(settings.RABBITMQ_PASSWORD),
            server=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            heartbeat=heartbeat
        )

    def _get_logger(self, logger_name: str, logger_number: int):

        log_path = settings.WORKERS_LOG_PATH
        if not os.path.isdir(log_path):
            os.makedirs(log_path)

        logger_name = logger_name.replace('.', '_')

        # create a logger
        return get_logger(
            os.path.join(
                log_path,
                'consumer_{}.log'.format('{}_{}'.format(logger_name, logger_number))
            ),
            rotate=True,
            logger_name='__consumer_{}_logger__'.format(
                '{}_{}'.format(logger_name, logger_number)
            )
        )
