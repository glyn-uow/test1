# SPDX-License-Identifier: MIT

import sys
import unittest


class TestPythonVersion(unittest.TestCase):

    def test_python_version(self):
        self.assertTrue(sys.version.startswith("3."), "Python version = %s" % sys.version)


if __name__ == '__main__':
    unittest.main()
