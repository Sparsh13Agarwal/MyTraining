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

# class Test:
#     def func(self):
#         print("func() is called from Test")

#--------------------------------------------------------------------
#problem
# list method insert, extend, find
# test cases for these methods
# lst =["a",2,"xyz","2a"]
# lst1 =["apple","banana","cherry"]
# var = input("enter element to be inserted: ")
# pos = int(input("enter the index:"))

# item = input("enter the element")

# def insert_in_lst(lst,var,pos):
#     lst.insert(pos,var)
#     return lst

# def extend_in_list(lst,lst1):
#     lst.extend(lst1)
#     return lst

# def index_in_list(lst,item):
#     return lst.index(item)
    
# from Day9 import Emp

# class TestListMethods(unittest.TestCase):
#     def test_insert(self):
#         self.assertIn(lst[pos],insert_in_lst(lst,var,pos),"element not inserted")

#     def test_insert(self):
#         self.assertIn(lst1,extend_in_list(lst,lst1),"element not found")

#     def test_find(self):
#         self.assertIn(item,index_in_list(lst,item),"index not found")

#     def test_name(self):
#         e = Emp('101','Rahul', 30000)
#         self.assertEqual(e.disp_name,'Rahul',"Employee name doesn't exsist")
    
#     def test_sal(self):
#         e = Emp('101','Rahul', 30000)
#         self.assertEqual(e.disp_sal,30000,"wrong salary")

#     def test_id(self):
#         e = Emp('101','Rahul', 30000)
#         self.assertEqual(e.disp_id,'101',"Employee id doesn't exsist")
# if __name__=="__main__":
#     unittest.main()       
#--------------------------------------------------------------------
# from unittest import TestCase
# from mockito import when,verifyStubbedInvocationsAreUsed
# import Day9

# def two_plus_two():
#     return Day9.add(2,2)
# class SimpleMockitoTest(TestCase):
#     def test_two_plus_two(self):
#         when(Day9).add(2,2).thenReturn(4)
        
#         self.assertEqual(4,two_plus_two())
#         verifyStubbedInvocationsAreUsed()

# if __name__=="__main__":
#     unittest.main()
#--------------------------------------------------------------------
# from unittest import TestCase
# from mockito import when,mock,verifyStubbedInvocationsAreUsed

# from Day9 import *
# import requests
# def test_fetch():
#     url = "https://www.google.com"
#     response = mock({"text":"Ok"},spec=requests.Response)
#     session = mock(requests.Session)
#     when(session).get(url).thenReturn(response)
#     when(requests).Session().thenReturn(session)
#     r = fetch(url)
#     try:
#         assert r.text == 'Ok'
#         print('working fine')
#     except:
#         print("error")
#     verifyStubbedInvocationsAreUsed()

# test_fetch()
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------
#--------------------------------------------------------------------























