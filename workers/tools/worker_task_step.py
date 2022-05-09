# -*- coding: utf-8 -*-

class WorkTaskStep(object):

    def execute(self):
        self._pre_execute()
        result = self._execute()
        return self._post_execute() or result

    def _pre_execute(self):
        pass

    def _execute(self):
        return None

    def _post_execute(self):
        return None
