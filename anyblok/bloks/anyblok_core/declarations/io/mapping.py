# This file is a part of the AnyBlok project
#
#    Copyright (C) 2015 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok import Declarations
register = Declarations.register
Model = Declarations.Model
String = Declarations.Column.String
Json = Declarations.Column.Json
IOException = Declarations.Exception.IOException


@register(IOException)
class IOMappingCheckException(IOException):
    """ IO Exception for setter """


@register(IOException)
class IOMappingSetException(IOException):
    """ IO Exception for setter """


@register(Model.IO)
class Mapping:

    key = String(primary_key=True)
    model = String(primary_key=True,
                   foreign_key=(Model.System.Model, 'name'))
    primary_key = Json(nullable=False)

    @Declarations.hybrid_method
    def filter_by_model_and_key(self, model, key):
        return (self.model == model) & (self.key == key)

    @Declarations.hybrid_method
    def filter_by_model_and_keys(self, model, *keys):
        return (self.model == model) & self.key.in_(keys)

    @classmethod
    def multi_delete(cls, model, *keys):
        query = cls.query()
        query = query.filter(cls.filter_by_model_and_keys(model, *keys))
        if query.count():
            query.delete(synchronize_session='fetch')
            return True

        return False

    @classmethod
    def delete(cls, model, key):
        query = cls.query()
        query = query.filter(cls.filter_by_model_and_key(model, key))
        if query.count():
            query.delete()
            return True

        return False

    @classmethod
    def get_primary_keys(cls, model, key):
        query = cls.query()
        query = query.filter(cls.filter_by_model_and_key(model, key))
        if query.count():
            pks = query.first().primary_key
            cls.check_primary_keys(model, *pks.keys())
            return pks

        return None

    @classmethod
    def check_primary_keys(cls, model, *pks):
        M = cls.registry.loaded_namespaces[model]
        for pk in M.get_primary_keys():
            if pk not in pks:
                raise IOMappingCheckException(
                    "No primary key %r found in %r for model %r" % (
                        pk, pks, model))

    @classmethod
    def set_primary_keys(cls, model, key, pks):
        if cls.get_primary_keys(model, key):
            raise IOMappingSetException(
                "One value found for model %r and key %r" % (model, key))

        if not pks:
            raise IOMappingSetException(
                "No value to save %r for model %r and key %r" % (
                    pks, model, key))

        cls.check_primary_keys(model, *pks.keys())
        return cls.insert(model=model, key=key, primary_key=pks)

    @classmethod
    def set(cls, key, instance):
        pks = instance.to_primary_keys()
        return cls.set_primary_keys(instance.__registry_name__, key, pks)

    @classmethod
    def get(cls, model, key):
        pks = cls.get_primary_keys(model, key)
        if pks is None:
            return None

        M = cls.registry.loaded_namespaces[model]
        return M.from_primary_keys(**pks)
