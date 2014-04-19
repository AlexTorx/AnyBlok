from anyblok.tests.testcase import DBTestCase
from anyblok import Declarations
target_registry = Declarations.target_registry
Model = Declarations.Model
Mixin = Declarations.Mixin
Core = Declarations.Core


def simple_subclass_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Model)
    class Test:
        id = Integer(label="id", primary_key=True)
        name = String(label="Name")

    @target_registry(Model)  # noqa
    class Test:
        other = String(label="Other")


def simple_subclass_model_change_type():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Model)
    class Test:
        id = Integer(label="id", primary_key=True)
        name = String(label="Name")

    @target_registry(Model)  # noqa
    class Test:
        name = Integer(label="Name")


def simple_subclass_model_change_type_and_subclass_add_field():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Model)
    class Test:
        id = Integer(label="id", primary_key=True)
        name = String(label="Name")

    @target_registry(Model)  # noqa
    class Test:
        name = Integer(label="Name")

    @target_registry(Model)  # noqa
    class Test:
        other = String(label="Other")


def mixin_one_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Mixin)
    class MixinName:

        name = String(label="Name")

    @target_registry(Model)
    class Test(Mixin.MixinName):

        id = Integer(label="id", primary_key=True)
        other = String(label='Other')


def mixin_two_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Mixin)
    class MixinName:

        name = String(label="Name")

    @target_registry(Model)
    class Test(Mixin.MixinName):

        id = Integer(label="id", primary_key=True)
        other = String(label='Other')

    @target_registry(Model)
    class Test2(Mixin.MixinName):

        id = Integer(label="id", primary_key=True)
        other = String(label='Other')


def mixin_one_model_with_subclass():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Mixin)
    class MixinName:

        name = String(label="Name")

    @target_registry(Model)
    class Test(Mixin.MixinName):

        id = Integer(label="id", primary_key=True)

    @target_registry(Model)  # noqa
    class Test:

        other = String(label="Other")


def mixin_one_model_by_subclass():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Mixin)
    class MixinName:

        name = String(label="Name")

    @target_registry(Model)
    class Test:

        id = Integer(label="id", primary_key=True)

    @target_registry(Model)  # noqa
    class Test(Mixin.MixinName):

        other = String(label='Other')


def mixin_with_foreign_key_one_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Model)
    class TestFk:

        name = String(label="Name", primary_key=True)

    @target_registry(Mixin)
    class MixinName:

        name = String(label="Name", foreign_key=(Model.TestFk, 'name'))

    @target_registry(Model)
    class Test(Mixin.MixinName):

        id = Integer(label="id", primary_key=True)


def mixin_with_foreign_key_two_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Model)
    class TestFk:

        name = String(label="Name", primary_key=True)

    @target_registry(Mixin)
    class MixinName:

        name = String(label="Name", foreign_key=(Model.TestFk, 'name'))

    @target_registry(Model)
    class Test(Mixin.MixinName):

        id = Integer(label="id", primary_key=True)

    @target_registry(Model)
    class Test2(Mixin.MixinName):

        id = Integer(label="id", primary_key=True)


def mixin_one_model_by_subclass_and_with():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Mixin)
    class MixinName:

        name = String(label="Name")

    @target_registry(Model)
    class Test:

        id = Integer(label="id", primary_key=True)

    @target_registry(Model)  # noqa
    class Test(Mixin.MixinName):
        pass

    @target_registry(Model)  # noqa
    class Test:

        other = String(label="Other")


def mixin_one_model_with_subclass_and_subclass_mixin():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Mixin)
    class MixinName:

        name = String(label="Name")

    @target_registry(Model)
    class Test:

        id = Integer(label="id", primary_key=True)

    @target_registry(Model)  # noqa
    class Test(Mixin.MixinName):
        pass

    @target_registry(Mixin)  # noqa
    class MixinName:

        other = String(label="Other")


def inherit_by_another_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Model)
    class MainModel:

        id = Integer(label="Id", primary_key=True)
        name = String(label="Name")

    @target_registry(Model)
    class Test(Model.MainModel):

        id = Integer(label="id", primary_key=True)
        mainmodel = Integer(label="Main model", foreign_key=(Model.MainModel,
                                                             'id'))
        other = String(label="Other")


def inherit_by_two_another_model():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Model)
    class MainModel:

        id = Integer(label="Id", primary_key=True)
        name = String(label="Name")

    @target_registry(Model)
    class Test(Model.MainModel):

        id = Integer(label="id", primary_key=True)
        mainmodel = Integer(label="Main model", foreign_key=(Model.MainModel,
                                                             'id'))
        other = String(label="Other")

    @target_registry(Model)
    class Test2(Model.MainModel):

        id = Integer(label="id", primary_key=True)
        mainmodel = Integer(label="Main model", foreign_key=(Model.MainModel,
                                                             'id'))
        other = String(label="Other")


def inherit_by_another_model_and_subclass_mainmodel():
    Integer = Declarations.Column.Integer
    String = Declarations.Column.String

    @target_registry(Model)
    class MainModel:

        id = Integer(label="Id", primary_key=True)
        name = String(label="Name")

    @target_registry(Model)
    class Test(Model.MainModel):

        id = Integer(label="id", primary_key=True)
        mainmodel = Integer(label="Main model", foreign_key=(Model.MainModel,
                                                             'id'))

    @target_registry(Model)  # noqa
    class MainModel:

        other = String(label="Other")


def inherit_base_and_add_method():

    @target_registry(Core)
    class Base:

        def method_from_base(self, x):
            return x * 2

    @target_registry(Model)
    class Test:
        pass


def inherit_base_and_add_method_after_create_model():

    @target_registry(Model)
    class Test:
        pass

    @target_registry(Core)
    class Base:

        def method_from_base(self, x):
            return x * 2


def inherit_base_and_add_method_sub_classes():

    @target_registry(Core)
    class Base:

        def method_from_base(self, x):
            return x * 2

    @target_registry(Model)
    class Test:

        def method_from_base(self, x):
            return super(Test, self).method_from_base(x) + 3


def inherit_base_and_add_method_sub_classes_by_mixin():

    @target_registry(Core)
    class Base:

        def method_from_base(self, x):
            return x * 2

    @target_registry(Mixin)
    class TestMixin:

        def method_from_base(self, x):
            return super(TestMixin, self).method_from_base(x) + 3

    @target_registry(Model)
    class Test(Mixin.TestMixin):
        pass


def inherit_sql_base_on_simple_model():

    @target_registry(Core)
    class Base:

        def is_sql_base(self):
            return False

    @target_registry(Core)
    class SqlBase:

        def is_sql_base(self):
            return True

    @target_registry(Model)
    class Test:
        pass


def inherit_sql_base_on_sql_model():
    Integer = Declarations.Column.Integer

    @target_registry(Core)
    class Base:

        def is_sql_base(self):
            return False

    @target_registry(Core)
    class SqlBase:

        def is_sql_base(self):
            return True

    @target_registry(Model)
    class Test:

        id = Integer(label='ID', primary_key=True)


class TestInherit(DBTestCase):

    def check_registry(self, Model):
        t = Model.insert(name="test", other="other")
        t2 = Model.query().first()
        self.assertEqual(t2, t)

    def test_simple_subclass_model(self):
        registry = self.init_registry(simple_subclass_model)
        self.check_registry(registry.Test)

    def test_simple_subclass_model_change_type(self):
        registry = self.init_registry(simple_subclass_model_change_type)

        t = registry.Test.insert(name=1)
        t2 = registry.Test.query().first()
        self.assertEqual(t2, t)
        self.assertEqual(t.name, 1)

    def test_simple_subclass_model_change_type_and_subclass_add_field(self):
        registry = self.init_registry(
            simple_subclass_model_change_type_and_subclass_add_field)

        t = registry.Test.insert(name=1, other='other')
        t2 = registry.Test.query().first()
        self.assertEqual(t2, t)
        self.assertEqual(t.name, 1)

    def test_mixin_one_model(self):
        registry = self.init_registry(mixin_one_model)
        self.check_registry(registry.Test)

    def test_mixin_two_model(self):
        registry = self.init_registry(mixin_two_model)
        self.check_registry(registry.Test)
        self.check_registry(registry.Test2)

    def test_mixin_one_model_with_subclass(self):
        registry = self.init_registry(mixin_one_model_with_subclass)
        self.check_registry(registry.Test)

    def test_mixin_one_model_by_subclass(self):
        registry = self.init_registry(mixin_one_model_by_subclass)
        self.check_registry(registry.Test)

    def test_mixin_with_foreign_key_one_model(self):
        registry = self.init_registry(mixin_with_foreign_key_one_model)

        val = 'test'
        registry.TestFk.insert(name=val)
        t = registry.Test.insert(name=val)
        t2 = registry.Test.query().first()
        self.assertEqual(t2, t)

    def test_mixin_with_foreign_key_two_model(self):
        registry = self.init_registry(mixin_with_foreign_key_two_model)

        for val in ('test', 'test2'):
            registry.TestFk.insert(name=val)

        t = registry.Test.insert(name='test')
        t2 = registry.Test.query().first()
        self.assertEqual(t2, t)

        t3 = registry.Test2.insert(name='test2')
        t4 = registry.Test2.query().first()
        self.assertEqual(t3, t4)

    def test_mixin_one_model_by_subclass_and_with(self):
        registry = self.init_registry(mixin_one_model_by_subclass_and_with)
        self.check_registry(registry.Test)

    def test_mixin_one_model_with_subclass_and_subclass_mixin(self):
        registry = self.init_registry(
            mixin_one_model_with_subclass_and_subclass_mixin)
        self.check_registry(registry.Test)

    def test_inherit_by_another_model(self):
        registry = self.init_registry(inherit_by_another_model)
        self.check_registry(registry.Test)

    def test_inherit_by_two_another_model(self):
        registry = self.init_registry(inherit_by_two_another_model)
        self.check_registry(registry.Test)
        self.check_registry(registry.Test2)

    def test_inherit_by_another_model_and_subclass_mainmodel(self):
        registry = self.init_registry(
            inherit_by_another_model_and_subclass_mainmodel)
        self.check_registry(registry.Test)

    def check_inherit_base(self, function, value):
        registry = self.init_registry(function)
        test = registry.Test()
        self.assertEqual(test.method_from_base(2), value)

    def test_inherit_base_and_add_method(self):
        self.check_inherit_base(inherit_base_and_add_method, 4)

    def test_inherit_base_and_add_method_after_create_model(self):
        self.check_inherit_base(inherit_base_and_add_method_after_create_model,
                                4)

    def test_inherit_base_and_add_method_sub_classes(self):
        self.check_inherit_base(inherit_base_and_add_method_sub_classes, 7)

    def test_inherit_base_and_add_method_sub_classes_by_mixin(self):
        self.check_inherit_base(
            inherit_base_and_add_method_sub_classes_by_mixin, 7)

    def check_inherit_sql_base(self, function, value):
        registry = self.init_registry(function)
        test = registry.Test()
        self.assertEqual(test.is_sql_base(), value)

    def test_inherit_sql_base_on_simple_model(self):
        self.check_inherit_sql_base(inherit_sql_base_on_simple_model, False)

    def test_inherit_sql_base_on_sql_model(self):
        self.check_inherit_sql_base(inherit_sql_base_on_sql_model, True)
