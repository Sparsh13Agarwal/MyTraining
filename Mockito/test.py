#from Day9 import Calculator
import unittest

# class TestCode(unittest.TestCase):
#     def test_sum(self):
#         c = Calculator(10,1)
#         self.assertEqual(c.get_addition(),11,'The sum is wrong')
        
# using setup n terdown

# class TestCode(unittest.TestCase):
#     def setUp(self) -> None:
#         self.c = Calculator(9,6)
#         self.f = open("hello.txt",r)
#     def tearDown(self) -> None:
#         self.f.close()
        
# if __name__=='__main__':
#     unittest.main()

# --------------------------------------------------------------------

# class TestStrMethods(unittest.TestCase):
#     def test_Upper(self):
#         self.assertEqual("foo".upper(),"FOO")
    
#     def test_isUpper(self):
#         self.assertTrue("FOO".isupper())
#         self.assertFalse("foo".isupper())

#     def test_Split(self):
#         s = "hello world"
#         self.assertEqual(s.split(),["hello","world"])

# if __name__=="__main__":
#     unittest.main()

# commands for running test file in different ways 
# python -m unittest filename  - whole file
#python -m unittest -v filename - more details
# python -m unittest -v filename.classname.functionname   

#--------------------------------------------------------------------
# monkey patching - changin the behaviour of the class members n fucntions at runtime

class Test:
    def func(self):
        print("func() is called from Test")























