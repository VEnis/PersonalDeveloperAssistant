# -*- encoding: utf-8 -*-

import unittest
from pda.config.PersistentConfig import PersistentConfig


class PersistentConfigTest(unittest.TestCase):

    def test_persistent_path_retrieving_not_implemented(self):
        with self.assertRaises(NotImplementedError):
            path = PersistentConfig.getPersistentPath()

if __name__ == '__main__':
    unittest.main()
