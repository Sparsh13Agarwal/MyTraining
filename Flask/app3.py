import psycopg2
import os
from psycopg2 import Error
from pet_shop.db import *

class Student:
    def __init__(self,sid,sname,sadd) -> None:
        self.sid = sid
        self.sname = sname
        self.sadd = sadd
   
# if __name__=='__main__':
 