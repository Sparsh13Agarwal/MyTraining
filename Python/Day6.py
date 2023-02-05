# # OPPS Concept 
# # class Student:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age

# #     def get_stu_info(self):
# #         return self.name,self.age
    
# #     def set_stu_info(self,name,age):
# #         self.name = name
# #         self.age = age
    

# # class ScienceStudent(Student):
# #     def __init__(self, name, age):
# #         super().__init__(name, age) # super() is subscript for parent object
# #     def get_stud(self):
# #         return "Science"

# # s = ScienceStudent("Rohit",30)
# # print(s.get_stu_info())
# # s.set_stu_info("Rahul",29)
# # print(s.get_stu_info())
# # print(s.get_stud())
# #--------------------------------------------------------------------------------

# # class Animal:
# #     def __init__(self,animal):
# #         self.animal = animal
# #         print(self.animal,"is an animal.")
# #     def disp_info(self):
# #         return self.animal
    
# # class Mamaml(Animal):
# #     def __init__(self, mname):
# #         print(mname, "is a warm blooded.")
# #         super().__init__(mname)

# # class NonWingedMamal(Mamaml):
# #     def __init__(self, nwmamal):
# #         print(nwmamal,"can't swim")
# #         super().__init__(nwmamal)

# # class NonMarineMamal(Mamaml):
# #     def __init__(self, nmmamaml):
# #         print(nmmamaml,"can't swim too.")
# #         super().__init__(nmmamaml)
    
# # class Dog(NonMarineMamal,NonWingedMamal):
# #     def __init__(self):
# #         print('dog has four legs')
# #         super().__init__(self)


# # ob = NonWingedMamal("Dog")
# # obb = Mamaml('Cat')
# # print(ob.disp_info())
# # d=Dog()
# # print(Dog.mro())

# #--------------------------------------------------------------------------------
# # Polymorphism concept

# # class Cat:
# #     def __init__(self,name,age) -> None:
# #         self.name = name
# #         self.age = age
# #     def info(self):
# #         print(f'I am cat, my name is {self.name} and my age is {self.age}.')
    
# #     def speak(self):
# #         print('meowww')

# # class Dog:
# #     def __init__(self,name,age):
# #         self.name = name
# #         self.age = age
    
# #     def info(self):
# #         print(f'I am dog, my name is {self.name}, my age is {self.age}.')

# #     def speak(self):
# #         print('Bark')

# # cat1 = Cat('Kitty',2)
# # dog1 = Dog('Fluffy',3)
# # dog2 = Dog('simba',4)
# # for animal in (dog2,cat1,dog1):
# #     animal.info()
# #     animal.speak()
# #     print()
        
# #--------------------------------------------------------------------------------

# # from math import pi

# # class Shape:
# #     def __init__(self,name):
# #         self.name =name

# #     def area(self):
# #         pass

# #     def fact(self):
# #         return "2D Shape"
    
# #     def __str__(self):
# #         return self.name
    
# # class Square(Shape):
# #     def __init__(self, length):
# #         super().__init__("Square")
# #         self.length =length
    
# #     def area(self):
# #         return self.length **2
    
# #     def fact(self):
# #         return "Each angle is 90 degree"

# # class Circle(Shape):
# #     def __init__(self,r):
# #         self.r =r
# #         super().__init__("Circle")
        
# #     # fact is not defined in this class but it inherits from the parent classs
# #     def area(self):
# #         return pi*self.r**2

# # a = Square(4)
# # b = Circle(5.6)
# # print(b)
# # print()
# # print(b.fact())
# # print(a)
# # print(a.fact())
# # print(a.area())
# # print(b.area())

# #--------------------------------------------------------------------------------
# # # abstact class ex.
# # # to create abstract class we need abc
# # from abc import ABC, abstractmethod

# # class MyClass(ABC):
    
# #     @abstractmethod
# #     def Code(self,x):
# #         pass

# # class SubClass(MyClass):
# #     def Code(self, x):
# #         print("Square = ",x**2)
# # # if the class is abstract class we cannot have the obejct of the abstract class as its method can be access using inheritance

# # ob = SubClass()
# # ob.Code(15)
    
# # # pure abstract class example
# # class MyClass(ABC):
# #     # abstract method as the body of it is empty....
# #     def Connect(self):
# #         pass
# #     def disconnect(self):
# #         pass

# #--------------------------------------------------------------------------------
# # Error Handling

# # try:
# #     f = open("myfile.rtf","w")
# #     a,b = [int(x) for x in input("Enter two no:- ").split()]
# #     c = a/b
# #     f.write("Writing %d into file "%c)

# # except ZeroDivisionError as ze:
# #     print("Error occured:- \n",ze)


# # try:
# #     name = input("Enter please: ")
# #     f = open(name,"r")

# # except IOError as ie:
# #     print("file name is wrong.")
# # else:
# #     n = len(f.readlines())
# #     print("file has, ", n,"lines.")
# #     f.close()



# # def avg(L):
# #     t = 0
# #     for i in L:
# #         t+=i
# #     a = t/len(L)
# #     return t,a
# # try:
# #     t,a = avg([1,2,3,4],'p')
# #     print(f'Total = {t}, average = {a}')

# # except TypeError as te:
# #     print('Error:',te)

# # except ZeroDivisionError as ze:
# #     print('Error:- ',ze)
# #--------------------------------------------------------------------------------
# # import logging
# # logging.basicConfig(filename='/Users/sparshagarwal/Desktop/Sparsh/Training1/Python/mylogfile.log', filemode='w', level=logging.DEBUG)
# # logger = logging.getLogger()
# # logger.setLevel(logging.DEBUG)


# # class MyException(Exception):
# #     def __init__(self, arg):
# #         self.arg = arg
# #     def __str__(self) -> str:
# #         return 'Balance is zero'
# # def check(d):
# #     for k,v in d.items():
# #         print(k,v)
# #         if v<2000.0:
# #             raise MyException("Balance is 0")

# # b = {"raj":4000,"rahul":3000,"rohit":300,"ramu":1000}
# # for i in range(10):
# #     try:
# #         check(b)
# #     except MyException as me:
# #         logger.critical(me)
# #         print("Error:- ",me)

# # logging.debug('hiiiii')
# #--------------------------------------------------------------------------------

# # enerators
# # def Count(n):
# #     i=1
# #     while i<=n:
# #         yield i
# #         i+=1

# # g = Count(10000)
# # print(g)
# # for i in g:
# #     print(i)
# #     if i==10:
# #         break

# # Iterators
# class MyIterator:
#     def __init__(self,l,h):
#         self.l = l
#         self.h = h

#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.l <= self.h:
#             self.l += 1
#             return self.l -1
#         else:
#             raise StopIteration

# it = MyIterator(20,400)
# print(it)
# for i in it:
#     print(i)

#--------------------------------------------------------------------------------
# decorators

def my_decorator(func):
    def inner(n1,n2):           # this function is closure
        n = 10
        f = func(n1,n2)
        return 10+f      
    return inner

@my_decorator
def func(n1,n2):
    return n1 + n2

n1 = int(input("Enter no:- "))
n2 = int(input("Enter no:- "))
print(func(n1,n2))

# double decorator
def double_val(f):
    def inner(n1,n2):
        r =f(n1,n2)
        return r*2
    return inner


@double_val
@my_decorator
def my_func(a,b):
    return a**b
print(my_func(10,2))




