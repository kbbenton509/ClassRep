import unittest
import Assignment1b.py
 
class CTest(unittest.TestCase):
	def test_f1(self):
		self.failUnless(c.csvRead())
	def test_f2(self):
		self.assertEqual(c.output(), 'The conversion worked')
 
if __name__ == '__main__':
	unittest.main()
