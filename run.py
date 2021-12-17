# -*- coding: utf-8 -*-
import unittest

if __name__ == '__main__':
    test_dir = "./unittcases"
    discover=unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
    unittest.TextTestRunner(verbosity=2).run(discover)

