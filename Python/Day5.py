#Opps concept

# class Emp:
#     def __init__(self,eid='10',ename='rahul',esal = 30000): 
#         self.eid = eid
#         self.ename = ename
#         self.esal = esal

#     def display(self):
#         print("Eid\tEname\tEsalary")
#         print(self.eid,"\t",self.ename,"\t",self.esal)
# if __name__=='__main__':
#     ob = Emp('E001','Rohan',20000)
#     ob.display()


# num = 20
# var = 10
# print(num.__add__(var))

#--------------------------------------------------------------------------------

# class Emp1:
#     def __init__(self,eid,ename,esal=50000):

#         self._eid =eid
#         self._ename =ename
#         self.__esal = esal
#     def disp(self):
#         print(self._eid,self._ename,self.__esal)

# ob = Emp1("10001",'Rohann',60000)
# ob.disp()
# print(ob._Emp1__esal)
# print(ob._eid)

#--------------------------------------------------------------------------------

# class Emp2(object):
#     org = "bajaj"   # class member
#     def __init__(self,eid,ename,esal):
#         self._eid =eid          # instance member
#         self._ename = ename
#         self.__esal = esal
#     def disp(self):
#         print("eid\tename\tesal")
#         print(self._eid,"\t",self._ename,"\t",self.__esal)

#     @classmethod
#     def modify(cls,n):
#         cls.org = n
#         print(cls.org)
#     @staticmethod
#     def static_demo(n):
#         Emp2.org = n
#         print(Emp2.org)

# if __name__=='__main__':
#     ob = Emp2('E001','Rohan',20000)
#     ob.disp()
#     print(ob.org)
#     ob.modify('Markets')
#     # Emp2.modify('Marketss')
#     # ob.static_demo('Bajaj Markets')
#     # Emp2.static_demo("finserv")
#     ob1 = Emp2('E002','Rohit',50000)
#     ob1.disp()
#     print(ob1.org)
#     print(Emp2.org)

#     # if we want to chang org value for one object we can use:
#     ob.org ="company"
#     print(ob.org)

#--------------------------------------------------------------------------------
#debuggin tool for ide - pdb
# import pdb
# pdb.set_trace()
# def my_fn(*args, **kwargs):  # kwargs is dict, args is tuple
#     print(type(args),type(kwargs))
#     print(args,kwargs)
#     for a in args:
#         print(a,end='')
#     for k,v in kwargs.items():
#         print(k,v)
    
# my_fn(1,2,3,4,5,6,7,z=1,x=2,a=44,b=11)
#--------------------------------------------------------------------------------
# class Person:
#     def __init__(self,name , job =None, pay = 0):
#         self.name = name
#         self.job= job
#         self.pay = pay
#     def lastName(self):
#         return self.name.split()[-1]

#     def give_raise(self,percent):
#         self.pay = int(self.pay + (self.pay * percent * 0.01))
#     def __repr__(self):
#         return "[Person:%s %s]"

#     def __str__(self):
#         return "[Person:%s %s]"        


# bob = Person("Bob Smith")
# sue = Person ("Sue Jones","dev",50000)
# bob.give_raise(40)
# sue.give_raise(20)
# print(bob.lastName(),"pay = ",bob.pay)
# print(sue.lastName(),"pay = ",sue.pay)


# import datetime
# now = datetime.datetime.now()
# print(now.__str__())
# print(now.__repr__())

#--------------------------------------------------------------------------------        

# operator overloading

# class Book1:
#     def __init__(self,pages):
#         self.pages = pages
#     def __add__(self,other_job):
#         return self.pages + other_job.pages
#     def __gt__(self,ob):
#         return self.pages > ob.pages
    
# class Book2:
#     def __init__(self,pages):
#         self.pages =pages
    
# b1 = Book1(100)
# b2 = Book2(500)
# print('Total pages = ',b1+b2)
# if b1>b2:
#     print("b1 has more pages")
# else:
#     print("b2 has more pages")
        
#--------------------------------------------------------------------------------
# regular expression methods-> match, search, findall, split
# \w -> any character in between A-Z or a-z or 0-9
# speacial char-> \A begining  \S \d \Z end \D \b  identify word 
import re
# p =re.compile(r'm\w\w')
# s = 'cat rat mat sat men '
# r = p.search(s)
# print(r.group())
# # method 2
# r = re.search(r'm\w\w',s)
# print(r.group())
# # delimeter
# ss = 'This; is the: "core" Python\'s'
# r = re.split('\W+',ss)
# print(r)
# # other examples
# s3 =" This is beautiful"
# r = re.sub(r'beautiful',r'ugly',s3)
# print(r)

# s4 = "an apple a day keeps the doctor away."
# r = re.findall(r'a[\w]*',s4)
# for w in r:
#     print(w)

# s = "one two three four five six sevennnnn 8 9 10"

# r = re.findall(r'\b\w{3,5}\b',s)
# print(r)

# r = re.findall(r'\b\d\b',s)
# print(r)

# s  ="one two three one two three"
# r = re.findall(r't[\w]$z',s)
# print(r)

# r= re.match(r'^o[\w]*',s)
# print(r.group())

# create one file with email ids and extract some email id
# s = 'helooworld sparsh.a@bajaj.finserv.in'
# with open("test.rtf","r") as f:
#      line = f.readline()
# r = re.findall(r'\S+@]\S+',line)
# print(r)

# problem "today is 19/01/2023. Next class will be from 6/10/2023 " print dates
#problem 
# s = "today is 19/01/2023. Next class will be from 6/10/2023 "
# r = re.findall(r'[0-9]{2}\S+[0-9]{2}\S+[0-9]{2}\S+',s)
# print(r)

#url =r"https://github.com/tokern/piicatcher/blob/master/tests/samples/sample-data.csv"
url = r"https://raw.githubusercontent.com/tokern/piicatcher/master/tests/samples/sample-data.csv"

from urllib.request import urlopen
def read_data(url):
    if url.startswith(('http:','https:','ftp.')):
        return urlopen(url).read()
    else:
        print(' not valid url')
s = read_data(url).decode('utf-8')
#print(s)
ss = "123-22-1222,123-22-2111"
r = re.findall(r'\d{3}[-]\d{2}[-]\d{4}',s)
print(r)

r = re.findall(r'\d[,]\w[,]',s)
print(r)

