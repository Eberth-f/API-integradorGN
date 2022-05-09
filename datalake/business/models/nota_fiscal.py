# -*- coding: utf-8 -*-

from django.db import models


class NotaFiscal(models.Model):

    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = 'vendas\".\"nota_fiscal'
