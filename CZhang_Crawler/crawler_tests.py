import unittest
import pytest
import sys
import io
from crawler2 import get_urls


class Test_Crawler(unittest.TestCase):

    def setUp(self):
        self.a = sys.argv[1]

    def runTest(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        # test on a website with no children URLs
        get_urls(self.a)
        self.assertEqual(capturedOutput.getvalue(), 'https://crouton.net/\n')
        sys.stdout = sys.__stdout__

unittest.TextTestRunner().run(Test_Crawler())
