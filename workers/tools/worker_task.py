# -*- coding: utf-8 -*-

import json
import threading
import traceback


class WorkerTask(object):

    logger = None

    def __init__(self, logger: object):
        self._logger = logger
        if not self._logger:
            raise Exception('Invalid logger!')

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def name(self):
        return self.__class__.__name__

    def execute(self, payload: str) -> bool:

        self._logger.info("Tarefa {} iniciado na Thread-{}...".format(
            self.name,
            threading.current_thread().ident
        ))

        try:
            data = self._pre_execute(payload)
            self._execute(**data)
        except Exception as e:
            self._logger.error('Erro ao processo tarefa {} na Thread-{}: {}\nDetalhes:\n{}'.format(
                self.name,
                threading.current_thread().ident,
                str(e),
                traceback.format_exc()
            ))
            return False

        self._logger.info("Tarefa {} concluída com sucesso na Thread-{}...".format(
            self.name,
            threading.current_thread().ident
        ))

        return True

    def _pre_execute(self, payload: str) -> dict:
        """Validate the JSON payload"""

        # check if JSON payload is alid
        try:
            object = json.loads(payload)
        except:
            raise Exception('Invalid JSON in payload!')
        
        # check if task name is informed
        task = object.get('command', {}).get('task_name')
        if not task:
            raise Exception('Invalid `task` property in JSON payload!')

        # check if task name is equal a task class name
        if task not in self.name:
            raise Exception('Invalid type `{}` for task `{}`'.format(task, self.name))

        # check if at least one parameter is passed
        if not any((
            value for key, value in object.get('command', {}).items() 
            if key in ['params', 'data']
        )):
            raise Exception('Invalid `{}` property in JSON!'.format(key))
                
        return object

    def _execute(self, data: dict):
        pass

    def _check_fields(self, data: dict, expected_fields: list):
        invalid_fields = [key for key in expected_fields if not data.get(key)]
        if invalid_fields:    
            raise Exception('Invalid {} field value!'.format(
                ','.join(['`{}`'.format(key) for key in invalid_fields])
            ))
