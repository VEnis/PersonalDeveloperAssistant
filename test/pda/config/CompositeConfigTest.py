# -*- encoding: utf-8 -*-
import unittest
from pda.config.CompositeConfig import CompositeConfig
from pda.config.Config import Config


class CompositeConfigTest(unittest.TestCase):
    def setUp(self):
        self.config = CompositeConfig(dict={
            'own_param1': 'own_value1',
            'own_param2': 'own_value2'
        }, configs=[
            Config(dict={'top_param1': 'top_value1', 'top_param2': 'top_value2', 'common_param': 'top_value'}),
            Config(dict={'middle_param1': 'middle_value1', 'middle_param2': 'middle_value2', 'common_param': 'middle_value'}),
            Config(dict={'bottom_param1': 'bottom_value1', 'bottom_param2': 'bottom_value2', 'common_param': 'bottom_value'})
        ])

    def test_length_is_correct(self):
        self.assertEquals(len(self.config), 9)

    def test_it_is_possible_to_get_all_values_from_all_configs(self):
        self.assertEquals(self.config["own_param1"], "own_value1")
        self.assertEquals(self.config["own_param2"], "own_value2")
        self.assertEquals(self.config["top_param1"], "top_value1")
        self.assertEquals(self.config["top_param2"], "top_value2")
        self.assertEquals(self.config["middle_param1"], "middle_value1")
        self.assertEquals(self.config["middle_param2"], "middle_value2")
        self.assertEquals(self.config["bottom_param1"], "bottom_value1")
        self.assertEquals(self.config["bottom_param2"], "bottom_value2")
        self.assertEquals(self.config["common_param"], "top_value")

    def test_get_with_fail_object_works(self):
        self.assertEquals(self.config.get("common_param"), "top_value")
        self.assertEquals(self.config.get("invalid_key", 5), 5)

    def test_keys_are_correct(self):
        config_keys = self.config.keys()
        etalon_keys = [
            'own_param1',
            'own_param2',
            'top_param1',
            'top_param2',
            'middle_param1',
            'middle_param2',
            'bottom_param1',
            'bottom_param2',
            'common_param'
        ]

        config_keys.sort()
        etalon_keys.sort()
        self.assertListEqual(config_keys, etalon_keys)

    def test_values_are_correct(self):
        config_values = self.config.values()
        etalon_values = [
            'own_value1',
            'own_value2',
            'top_value1',
            'top_value2',
            'middle_value1',
            'middle_value2',
            'bottom_value1',
            'bottom_value2',
            'top_value'
        ]

        config_values.sort()
        etalon_values.sort()
        self.assertListEqual(config_values, etalon_values)

    def test_items_are_correct(self):
        config_items = self.config.items()
        etalon_items = [('middle_param2', 'middle_value2'),
                        ('own_param1', 'own_value1'),
                        ('own_param2', 'own_value2'),
                        ('middle_param1', 'middle_value1'),
                        ('top_param2', 'top_value2'),
                        ('top_param1', 'top_value1'),
                        ('bottom_param1', 'bottom_value1'),
                        ('bottom_param2', 'bottom_value2'),
                        ('common_param', 'top_value')]

        self.assertItemsEqual(config_items, etalon_items)

    def test_keys_are_iterable(self):
        config_keys = self.config.iterkeys()
        etalon_keys = [
            'own_param1',
            'own_param2',
            'top_param1',
            'top_param2',
            'middle_param1',
            'middle_param2',
            'bottom_param1',
            'bottom_param2',
            'common_param'
        ]

        self.assertItemsEqual(config_keys, etalon_keys)

    def test_values_are_iterable(self):
        config_values = self.config.itervalues()
        etalon_values = [
            'own_value1',
            'own_value2',
            'top_value1',
            'top_value2',
            'middle_value1',
            'middle_value2',
            'bottom_value1',
            'bottom_value2',
            'top_value'
        ]

        self.assertItemsEqual(config_values, etalon_values)

    def test_items_are_iterable(self):
        config_items = self.config.iteritems()
        etalon_items = [('middle_param2', 'middle_value2'),
                        ('own_param1', 'own_value1'),
                        ('own_param2', 'own_value2'),
                        ('middle_param1', 'middle_value1'),
                        ('top_param2', 'top_value2'),
                        ('top_param1', 'top_value1'),
                        ('bottom_param1', 'bottom_value1'),
                        ('bottom_param2', 'bottom_value2'),
                        ('common_param', 'top_value')]

        self.assertItemsEqual(config_items, etalon_items)

    def test_key_availability_can_be_checked(self):
        self.assertTrue(self.config.has_key("middle_param1"))
        self.assertFalse(self.config.has_key("invalid key"))

        self.assertTrue("middle_param2" in self.config)
        self.assertFalse("invalid key2" in self.config)

    def test_missing_keys_can_be_handled(self):
        def missing_handler(self, key):
            return "missing: {0}".format(key)

        self.config.__class__.__missing__ = missing_handler

        self.assertEqual("missing: abc", self.config["abc"])

        del self.config.__class__.__missing__

    def test_unhandled_missing_keys_raises_exception(self):
        with self.assertRaises(KeyError):
            value = self.config["invalid key"]
            print value

    def test_representation_is_correct(self):
        config_repr = repr(self.config)
        required_repr = "{'middle_param2': 'middle_value2', 'own_param1': 'own_value1', 'own_param2': 'own_value2', 'middle_param1': 'middle_value1', 'top_param2': 'top_value2', 'top_param1': 'top_value1', 'bottom_param1': 'bottom_value1', 'bottom_param2': 'bottom_value2', 'common_param': 'top_value'}"

        self.assertEqual(config_repr, required_repr)

    def test_configs_must_be_a_list(self):
        with self.assertRaises(ValueError) as context:
            config = CompositeConfig(dict={
                'own_param1': 'own_value1',
                'own_param2': 'own_value2'
            }, configs=5)

        self.assertEqual(context.exception.message, 'Passed configs value is not List')

    def test_configs_list_must_contain_only_config_class_childrens(self):
        with self.assertRaises(ValueError) as context:
            config = CompositeConfig(dict={
                'own_param1': 'own_value1',
                'own_param2': 'own_value2'
            }, configs=[
                Config(dict={'top_param1': 'top_value1', 'top_param2': 'top_value2', 'common_param': 'top_value'}),
                5,
                Config(dict={'middle_param1': 'middle_value1', 'middle_param2': 'middle_value2', 'common_param': 'middle_value'}),
                Config(dict={'bottom_param1': 'bottom_value1', 'bottom_param2': 'bottom_value2', 'common_param': 'bottom_value'})
            ])

        self.assertEqual(context.exception.message, 'Some items in the configs list does not inherited from pda.config.Config')

    def test_changing_internal_configs_correctly_handled(self):
        self.assertEqual(self.config["middle_param1"], "middle_value1")

        self.config.configs[1]["middle_param1"] = "updated_middle_value"
        self.assertEqual(self.config["middle_param1"], "updated_middle_value")

        print self.config.configs[2]
        self.config.configs[2]["common_param"] = "updated_common_value"
        self.assertEqual(self.config["common_param"], "top_value")

if __name__ == '__main__':
    unittest.main()
