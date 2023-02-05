#Opps concept
from Day5 import Emp

class Student:
    def __init__(self,sid,sname,sfee = 200000): 
        self.sid = sid
        self.sname = sname
        self.sfee = sfee

    def display(self):
        print("sid\tsname\tsfee")
        print(self.sid,"\t",self.sname,"\t",self.sfee)
if __name__=='__main__':

    ob = Student('s001','Rohan',350000)
    ob.display()

    e = Emp('104','Ravi',50)
    e.display()

#--------------------------------------------------------------------------------












