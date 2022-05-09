# -*- coding: utf-8 -*-

from django.db import models


class WorkerTask(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    module_task = models.CharField(max_length=255)

    heartbeat = models.IntegerField(
        default=60,
        help_text='''
            Indica o tempo de processamento máximo desta tarefa.
            Esse é o tempo que o message broker irá aguardar até que tarefa seja concluída.
            Caso a tarefa não seja concluída nesse internvalo o message broker irá fechar a conexão com o consumidor
            e mensagem será marcada para re-envio e processamento.
            É necessário monitorar o tempo máximo de processamento das tarefas para ajustar 
            adequadamente este intervalo.
        '''
    )
