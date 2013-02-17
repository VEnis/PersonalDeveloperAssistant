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
        self.config["myparam"] = "myvalue"
        self.assertEquals(self.config["myparam"], "myvalue")

    def test_different_value_types_support(self):
        for i, val in enumerate(self.values):
            param_name = "param_{0}".format(i)
            self.config[param_name] = val
            self.assertEquals(self.config[param_name], val)

    def test_possibility_to_delete(self):
        self.config["myparam"] = "myvalue"
        self.assertEquals(self.config["myparam"], "myvalue")

        del self.config["myparam"]

        with self.assertRaises(KeyError) as context:
            self.config["myparam"]

    def test_key_availability_checking(self):
        self.assertFalse("myparam" in self.config)
        self.config["myparam"] = "myvalue"
        self.assertTrue("myparam" in self.config)

if __name__ == '__main__':
    unittest.main()
