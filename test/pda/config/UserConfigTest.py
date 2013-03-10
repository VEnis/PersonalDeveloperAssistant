# -*- encoding: utf-8 -*-
import os

import unittest
from pda.config.UserConfig import UserConfig


class UserConfigTest(unittest.TestCase):
    def setUp(self):
        self._delete_persistent_data()

        self.values = [
            5,
            True,
            int(10),
            float(10.57),
            #complex(1, 2),
            "MyString",
            #u"Привет, мир",
            [1, 2, "Test"],
            tuple('abc'),
            bytearray(5),
            {'orange', 'pear', 'apple', 'banana'},
            {'jack': 4098, 'sjoerd': 4127},
            None
        ]

    def tearDown(self):
        self._delete_persistent_data()

    def test_data_is_shared_between_instances(self):
        config1 = UserConfig()
        config1["param1"] = "value1"
        config1.save()

        config2 = UserConfig()
        self.assertEquals(config2["param1"], "value1")

    def test_data_can_be_reloaded_from_file(self):
        config1 = UserConfig()
        config1["param1"] = "value1"
        config1.save()

        config1["param1"] = "value2"
        config1.load()

        self.assertEquals(config1["param1"], "value1")

    def test_data_is_automatically_saved(self):
        config1 = UserConfig()
        config1["param1"] = "value1"

        del config1

        config2 = UserConfig()
        self.assertEquals(config2["param1"], "value1")

    def test_complex_data_can_be_saved(self):
        config1 = UserConfig()

        for i, val in enumerate(self.values):
            param_name = "param_{0}".format(i)
            config1[param_name] = val

        config1.save()

        config2 = UserConfig()

        for i, val in enumerate(self.values):
            param_name = "param_{0}".format(i)
            self.assertEqual(config2[param_name], val)

    def _delete_persistent_data(self):
        if os.path.exists(UserConfig.getPersistentPath()):
            os.remove(UserConfig.getPersistentPath())


if __name__ == '__main__':
    unittest.main()
