# mockito
#import unittest
# unit testing in python

# n =0
# assert n>1,'the condition is wrong'

# x = int(input("enter a no greater than zero:"))
# try:
#     assert x>0,'wrong input for x' + 'wrong input for x'
#     print('You have entered the correct value for variable x=',x)
# except AssertionError as ae:
#     print(ae)


#assertEqual(a,b)  assertNotEqual(a,b)  assertTrue(x) assertFalse(x) assertIn(x,y) x in y
# 

import unittest


# class Calculator:
#     def __init__(self,a,b) -> None:
#         self.a =a
#         self.b =b


#     def get_addition(self):
#         return self.a + self.b
#     def get_subtraction(self):
#         return self.a - self.b
#     def get_product(self):
#         return self.a * self.b
#     def get_division(self):
#         return self.a / self.b
#--------------------------------------------------------------------

#problem
# list method insert, extend, find
# test cases for these methods

#problem
# create a class emp - eid,ename,esal 
# bouns - raise salary fn.
# gross - bonus + sal.



    

class Emp:
    def __init__(self,eid='10',ename='rahul',esal = 30000): 
        self.eid = eid
        self.ename = ename
        self.esal = esal

    # def display(self):
    #     print("Eid\tEname\tEsalary")
    #     print(self.eid,"\t",self.ename,"\t",self.esal)

    def bounus(self):
        return self.esal + 0.2*self.esal

    def grossSal(self):
        hr = self.esal* 0.15 
        da = self.esal* 0.25
        return self.esal + hr + da
        
    def disp_name(self):
        return self.ename

    def disp_id(self):
        return self.eid

    def disp_sal(self):
        return self.esal
        
# if __name__=='__main__':
#     ob = Emp('E001','Rohan',20000)
#     ob.display()
#--------------------------------------------------------------------


# unit test with mockito

# def add(a,b):
#     return (10*(a+b))

#--------------------------------------------------------------------
# import requests

# def fetch(url):
#     session = requests.Session()
#     return session.get(url)