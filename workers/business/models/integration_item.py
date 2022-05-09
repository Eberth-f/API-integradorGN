# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.core.exceptions import ValidationError

from workers.business.enums.integration_state import IntegrationState

from workers.business.models.integration_source import IntegrationSource


class IntegrationItem(models.Model):

    name = models.CharField(max_length=200, blank=False)
    source = models.ForeignKey(IntegrationSource, on_delete=models.PROTECT, blank=False)
    key = models.CharField(
        max_length=255,
        blank=False,
        help_text='''
            Chave única que identifica o item na base de integração. 
            Exemplo: Origem Integracao + Loja + Data Emissao + Modelo + Serie/PDV + Numero NF
        '''
    )
    crate_date = models.DateField()
    init_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    state = models.IntegerField(choices=IntegrationState.choices, default=0)

    def __str__(self):
        return self.name

    def clean(self):
        self._validate_fields()
        self._set_fields()

    def _validate_fields(self):
        if not self.name:
            raise ValidationError('Invalid integration `name` field!')

    def _set_fields(self):
        self.create_date = datetime.date.today()
        self.state = IntegrationState.PENDING
        self.name = self.source.name + ' - '  + self.name