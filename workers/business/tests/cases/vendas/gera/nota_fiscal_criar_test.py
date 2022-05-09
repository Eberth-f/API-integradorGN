# -*- coding: utf-8 -*-

import json
import logging

from django.test import TestCase

from manager.business.models.nota_fiscal import NotaFiscal
from manager.business.models.empresa import Empresa
from workers.business.models.integration_item import IntegrationItem

from workers.business.tasks.vendas.gera.nota_fiscal_criar_task import GeraNotaFiscalCriarWorkerTask

from workers.business.tests.stubs.vendas.nota_fiscal_stub import NotaFiscalStub

class GeraNotaFiscalCriarWorkerTaskTestCase(TestCase):

    fixtures = ["manager_dev_fixture.yaml"]

    logger = None

    def setUp(self):
        self.logger = logging.Logger(__name__)

    def test_nota_fiscal_criar_task(self):
        """Test GeraNotaFiscalCriarWorkerTask class"""

        task_name = 'GeraNotaFiscalCriarWorkerTask'

        empresa = Empresa.objects.first()
        nota_fiscal = NotaFiscalStub.get_nota_fiscal_model(empresa)

        payload = NotaFiscalStub.get_gera_nota_fiscal_criar_task_contract(nota_fiscal)

        key = self._get_nota_fiscal_key(nota_fiscal)

        task = GeraNotaFiscalCriarWorkerTask(self.logger)
        result = task.execute(json.dumps(payload))

        self.assertTrue(
            result,
            'Tarefa {} não executou corretamente!'.format(task_name)
        )

        integration_item = IntegrationItem.objects.filter(key=key)

        self.assertTrue(
            len(integration_item) > 0,
            'Tarefa {} não criou a nota fiscal!'.format(task_name)
        )

    def _get_nota_fiscal_key(self, nota_fiscal: NotaFiscal) -> str:
        """Retorna a chave única da nota fiscal na integração
           Eg.: Origem Integracao + Loja + Data Emissao + Modelo + Serie/PDV + Numero NF"""

        return 'GERA-' + '-'.join([
            nota_fiscal.empresa.codigo_gera,
            nota_fiscal.data_emissao,
            str(nota_fiscal.modelo),
            str(nota_fiscal.serie),
            str(nota_fiscal.numero)
        ])
