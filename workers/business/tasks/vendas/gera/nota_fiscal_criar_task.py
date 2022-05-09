# -*- coding: utf-8 -*-

from workers.tools.worker_task import WorkerTask

from workers.business.models.integration_source import IntegrationSource
from workers.business.models.integration_item import IntegrationItem


class GeraNotaFiscalCriarWorkerTask(WorkerTask):

    def __init__(self, logger):
        super(GeraNotaFiscalCriarWorkerTask, self).__init__(logger)

    def _pre_execute(self, payload: str):
        object = super(GeraNotaFiscalCriarWorkerTask, self)._pre_execute(payload)

        data = object.get('command', {}).get('data', {})

        self._check_fields(
            data,
            ['modelo', 'serie', 'numero', 'codigo_gera', 'data_emissao']
        )

        return data

    def _execute(self, **kwargs: dict):
        
        modelo = kwargs.get('modelo')
        serie = kwargs.get('serie')
        numero = kwargs.get('numero')
        codigo_gera = kwargs.get('codigo_gera')
        data_emissao = kwargs.get('data_emissao')
        force = kwargs.get('force', False)

        key = 'GERA-' + '-'.join([
            codigo_gera,
            data_emissao,
            modelo,
            serie,
            numero
        ])

        # localiza o item de integração
        integration_item = IntegrationItem.objects.filter(key=key)

        # se deve forçar a criação ou se não existir cria a nota fiscal
        if force or not integration_item:

            source = IntegrationSource.objects.get(code='NotaFiscal')

            integration_item = IntegrationItem(
                # name = set name of integration item
                source=source,
                key = key
                # crate_date = set date now
                # init_date = 
                # end_date = 
                # state = set pending
            )
            integration_item.save()

        # localiza a empresa

        # localiza a nota fiscal

        pass
