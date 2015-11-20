# -*- coding: utf-8 -*-

import sys
import unittest
from tests.write_letter import WriteLetterTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(WriteLetterTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
