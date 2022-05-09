# -*- coding: utf-8 -*-

import importlib


BASE_MODULE_TASK = 'workers.business.tasks'


class FabricTask:

    @classmethod
    def get_instance(cls, module_task: str, logger: object):
        
        path_list = (BASE_MODULE_TASK + '.' + module_task).split('.')
        module_name = '.'.join(path_list[0:len(path_list) - 1])
        class_name = path_list[len(path_list) - 1]

        try:
            module = importlib.import_module(module_name)
        except:
            raise Exception('Module not found: {}...'.format(module_name))

        cls = getattr(module, class_name)
        if not cls:
            raise Exception('Class not found: {}...'.format(class_name))

        return cls(logger)
