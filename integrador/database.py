# -*- coding: utf-8 -*-

from datalake.business.models.nota_fiscal import NotaFiscal

DJANGO_APPS = ['auth','admin','sessions','contenttypes']
PROJECT_APPS = ['workers', 'manager']
ALL_APPS = DJANGO_APPS + PROJECT_APPS

ROUTES = {
    'vendas': [
        NotaFiscal._meta.model_name
    ]
}


class DatabaseRouter(object):

    def db_for_read(self, model, **hints):
        """Returns the database schema for specify table."""
        return self._get_model_database(model)

    def db_for_write(self, model, **hints):
        """Returns the database schema for specify table."""
        return self._get_model_database(model)

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Return if model can by migration in atual database."""

        model = hints.get('model')
        if not model:
            return None

        database = self._get_model_database(model)
        return database == db

    def allow_relation(self, model1, model2, **hints):
        # Allow relations between two models that are both Django core app models
        if model1._meta.app_label in ALL_APPS and model2._meta.app_label in ALL_APPS:
            return True
        # If neither object is in a Django core app model (defer to other routers or default database)
        elif model1._meta.app_label not in ALL_APPS or model2._meta.app_label not in ALL_APPS:
            return None
        return None

    def _get_model_database(self, model):
        """Return the correct db connection."""
        for database, models in ROUTES.items():
            if model._meta.model_name in models:
                return database
        return 'default'
