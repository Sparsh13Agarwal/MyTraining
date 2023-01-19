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

class Emp2(object):
    org = "bajaj"   # class member
    def __init__(self,eid,ename,esal):
        self._eid =eid          # instance member
        self._ename = ename
        self.__esal = esal
    def disp(self):
        print("eid\tename\tesal")
        print(self._eid,"\t",self._ename,"\t",self.__esal)

    @classmethod
    def modify(cls,n):
        cls.org = n
        print(cls.org)
    @staticmethod
    def static_demo(n):
        Emp2.org = n
        print(Emp2.org)

if __name__=='__main__':
    ob = Emp2('E001','Rohan',20000)
    ob.disp()
    print(ob.org)
    ob.modify('Markets')
    # Emp2.modify('Marketss')
    # ob.static_demo('Bajaj Markets')
    # Emp2.static_demo("finserv")
    ob1 = Emp2('E002','Rohit',50000)
    ob1.disp()
    print(ob1.org)
    print(Emp2.org)

    # if we want to chang org value for one object we can use:
    ob.org ="company"
    print(ob.org)





        




