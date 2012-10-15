#! /usr/bin/env python

import os
import unittest
import tempfile
import subprocess


class TestLessCompiler(unittest.TestCase):

    def setUp(self):
        tmp_file = tempfile.gettempdir()
        self.less_file = os.path.join(tmp_file, 'test.less')
        self.css_file = os.path.join(tmp_file, 'test.css')

    def tearDown(self):
        os.remove(self.less_file)
        os.remove(self.css_file)

    def test_can_compile_sample_file(self):

        with open(self.less_file, 'w') as less_fh:
            less_fh.write("""@mycolor: #000;
body {
    background-color: @mycolor;
}""")

        subprocess.call(['lessc', self.less_file, self.css_file])

        with open(self.css_file) as css_fh:
            self.assertEquals(css_fh.read(), """body {
  background-color: #000000;
}
""")


if __name__ == "__main__":
    unittest.main()
