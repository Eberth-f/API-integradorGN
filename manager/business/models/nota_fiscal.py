# -*- coding: utf-8 -*-

from django.db import models

from workers.business.models.integration_item import IntegrationItem

from manager.business.models.empresa import Empresa


class NotaFiscal(models.Model):

    nome = models.CharField(max_length=200)
    integracoes = models.ManyToManyField(IntegrationItem)
    ano = models.IntegerField()
    mes = models.IntegerField()
    dia = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=2)
    serie = models.CharField(max_length=3)
    numero = models.CharField(max_length=9)
    data_emissao = models.DateField()

    class Meta:

        constraints = [
            models.UniqueConstraint(name='UK_nota_fiscal_01', fields=['empresa', 'modelo', 'serie', 'numero'])
        ]

        indexes = [
            models.Index(name='IDX_nota_fiscal_01', fields=['ano']),
            models.Index(name='IDX_nota_fiscal_02', fields=['mes']),
            models.Index(name='IDX_nota_fiscal_03', fields=['dia']),
            models.Index(name='IDX_nota_fiscal_04', fields=['numero']),
            models.Index(name='IDX_nota_fiscal_05', fields=['modelo']),
            models.Index(name='IDX_nota_fiscal_06', fields=['data_emissao']),
            models.Index(name='IDX_nota_fiscal_07', fields=['ano', 'mes', 'dia']),
            models.Index(name='IDX_nota_fiscal_08', fields=['empresa', 'ano', 'mes', 'numero']),
        ]

    def __str__(self):
        return '{}/{}'.format(
            self.serie,
            self.numero
        )