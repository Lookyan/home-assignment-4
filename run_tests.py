# -*- coding: utf-8 -*-

import sys
import unittest
from tests.write_letter_test import WriteLetterTest
from tests.write_letter_test2 import WriteLetterTest2

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(WriteLetterTest),
        # unittest.makeSuite(WriteLetterTest2)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
