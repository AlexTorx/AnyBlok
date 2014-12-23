# This file is a part of the AnyBlok project
#
#    Copyright (C) 2014 Jean-Sebastien SUZANNE <jssuzanne@anybox.fr>
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file,You can
# obtain one at http://mozilla.org/MPL/2.0/.
from anyblok.tests.testcase import DBTestCase


class TestInstrumentedList(DBTestCase):

    def test_all_method_on_query_return_InstrumentedList(self):

        def dummy():
            pass

        registry = self.init_registry(dummy)
        check = isinstance(registry.System.Blok.query().all(),
                           registry.InstrumentedList)
        self.assertEqual(check, True)

    def test_M2M_with_InstrumentedList(self):

        def m2m_with_instrumentedlist():

            from anyblok import Declarations
            Integer = Declarations.Column.Integer
            Many2Many = Declarations.RelationShip.Many2Many
            Model = Declarations.Model

            @Declarations.target_registry(Model)
            class Test:
                id = Integer(primary_key=True)

            @Declarations.target_registry(Model)
            class Test2:
                id = Integer(primary_key=True)
                tests = Many2Many(model=Model.Test, many2many="tests2")

        registry = self.init_registry(m2m_with_instrumentedlist)

        t = registry.Test.insert()
        t2 = registry.Test2.insert()
        t.tests2.append(t2)
        self.assertEqual(t2.tests, [t])
        check = isinstance(t.tests2, registry.InstrumentedList)
        self.assertEqual(check, True)
        check = isinstance(t2.tests, registry.InstrumentedList)
        self.assertEqual(check, True)

    def test_O2M_is_InstrumentedList(self):

        def o2m_with_instrumentedlist():

            from anyblok import Declarations
            Integer = Declarations.Column.Integer
            One2Many = Declarations.RelationShip.One2Many
            Model = Declarations.Model

            @Declarations.target_registry(Model)
            class Test2:
                id = Integer(primary_key=True)

            @Declarations.target_registry(Model)
            class Test:
                id = Integer(primary_key=True)
                test2 = Integer(foreign_key=(Model.Test2, 'id'))

            @Declarations.target_registry(Model)  # noqa
            class Test2:
                tests = One2Many(model=Model.Test)

        registry = self.init_registry(o2m_with_instrumentedlist)

        t = registry.Test.insert()
        t2 = registry.Test2.insert()
        t2.tests.append(t)
        check = isinstance(t2.tests, registry.InstrumentedList)
        self.assertEqual(check, True)

    def test_O2M_linked_is_InstrumentedList(self):

        def o2m_with_instrumentedlist():

            from anyblok import Declarations
            Integer = Declarations.Column.Integer
            Many2One = Declarations.RelationShip.Many2One
            Model = Declarations.Model

            @Declarations.target_registry(Model)
            class Test:
                id = Integer(primary_key=True)

            @Declarations.target_registry(Model)
            class Test2:
                id = Integer(primary_key=True)
                test = Many2One(model=Model.Test, one2many="tests2")

        registry = self.init_registry(o2m_with_instrumentedlist)

        t = registry.Test.insert()
        t2 = registry.Test2.insert()
        t.tests2.append(t2)
        check = isinstance(t.tests2, registry.InstrumentedList)
        self.assertEqual(check, True)

    def test_call_column(self):

        def call_column():

            from anyblok import Declarations
            Integer = Declarations.Column.Integer
            Model = Declarations.Model

            @Declarations.target_registry(Model)
            class Test:
                id = Integer(primary_key=True)

        registry = self.init_registry(call_column)

        t = registry.Test.insert()
        self.assertEqual(registry.Test.query().all().id, [t.id])

    def test_call_method(self):

        def call_method():

            from anyblok import Declarations
            Integer = Declarations.Column.Integer
            Model = Declarations.Model

            @Declarations.target_registry(Model)
            class Test:
                id = Integer(primary_key=True)

                def foo(self):
                    return self.id

        registry = self.init_registry(call_method)

        t = registry.Test.insert()
        self.assertEqual(registry.Test.query().all().foo(), [t.id])

    def test_inherit(self):

        def inherit():

            from anyblok import Declarations
            Core = Declarations.Core

            @Declarations.target_registry(Core)
            class InstrumentedList:

                def foo(self):
                    return True

        registry = self.init_registry(inherit)
        self.assertEqual(registry.System.Blok.query().all().foo(), True)
