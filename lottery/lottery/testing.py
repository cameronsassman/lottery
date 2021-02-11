import unittest

class agetest(unittest.TestCase):
    def testentry(self):

        x =34
        message="false"
        self.assertIn(x, range(1, 110), message)
