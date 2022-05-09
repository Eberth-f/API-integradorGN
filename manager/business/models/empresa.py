# -*- coding: utf-8 -*-

from django.db import models


class Empresa(models.Model):

    nome = models.CharField(max_length=200)
    codigo_sap = models.CharField(max_length=4)
    codigo_gera = models.CharField(max_length=4, null=True)

    class Meta:

        constraints = [
            models.UniqueConstraint(name='UK_empresa_01', fields=['codigo_sap'])
        ]

        indexes = [
            models.Index(name='IDX_empresa_01', fields=['nome'])
        ]

    def __str__(self):
        return '{} - {}'.format(
            self.nome,
            self.codigo_sap
        )
