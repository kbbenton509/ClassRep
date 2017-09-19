import unittest
import Assignment1b.py #imports the Assignment file to use for the unittest
 
class CTest(unittest.TestCase): #class used to test the functions
	def test_f1(self):
		self.failUnless(c.csvRead()) #the test fails unless the function works properly
	def test_f2(self):
		self.assertEqual(c.output(), 'The conversion worked') #tests to see if the function propely prints out the right statement
 
if __name__ == '__main__':
	unittest.main()
