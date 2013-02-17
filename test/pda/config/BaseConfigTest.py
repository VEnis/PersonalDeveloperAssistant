# -*- encoding: utf-8 -*-
from types import IntType

import unittest
from pda.config.BaseConfig import BaseConfig


class BaseConfigTest(unittest.TestCase):
    def setUp(self):
        self.config = BaseConfig()

        def tmp_fun(param):
            pass

        self.values = [
            5,
            True,
            int(10),
            long(123123),
            float(10.57),
            complex(1, 2),
            "MyString",
            u"Привет, мир",
            [1, 2, "Test"],
            tuple('abc'),
            bytearray(5),
            {'orange', 'pear', 'apple', 'banana'},
            {'jack': 4098, 'sjoerd': 4127},
            tmp_fun,
            IntType,
            None
        ]

    def test_simple_get_set(self):
        self.config.set("myparam", "myvalue")
        self.assertEquals(self.config.get("myparam"), "myvalue")

    def test_different_value_types(self):
        for i, val in enumerate(self.values):
            param_name = "param_{0}".format(i)
            self.config.set(param_name, val)
            self.assertEquals(self.config.get(param_name), val)

    def test_different_value_types_with_dict_interface(self):
        for i, val in enumerate(self.values):
            param_name = "param_{0}".format(i)
            self.config[param_name] = val
            self.assertEquals(self.config[param_name], val)

    def test_delete_possibility(self):
        self.config["myparam"] = "myvalue"
        self.assertEquals(self.config["myparam"], "myvalue")

        del self.config["myparam"]

        self.assertIsNone(self.config.get("myparam"))

    def test_delete_possibility_with_dict_interface(self):
        self.config["myparam"] = "myvalue"
        self.assertEquals(self.config["myparam"], "myvalue")

        self.config.delete("myparam")

        self.assertIsNone(self.config.get("myparam"))

    def test_key_availability(self):
        self.assertFalse("myparam" in self.config)
        self.config["myparam"] = "myvalue"
        self.assertTrue("myparam" in self.config)

if __name__ == '__main__':
    unittest.main()
