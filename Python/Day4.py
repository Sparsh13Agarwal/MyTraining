
# problem 1
# rows = int(input("enter rows:- "))
# temp = rows - 1
# for i in range(rows+1):
#     print(" "*(temp),"* "*i)
#     temp-=1

#--------------------------------------------------------------------------------
# problem 2
# var = int(input("enter rwos:- "))
# count = 65
# temp = var -1
# for i in range(1,var+1):
#     print(" "*(temp),end="")
#     for j in range(0,i):
#         print(chr(count),end=" ")
#         count+=1
#     print()
#     temp -=1

# def my_function():
#     '''Demonstrates triple double quotes
#     docstrings and does nothing really.'''
   
#     return None
  

#print(my_function.__doc__)
  
# x=100
# print(id(x))

# a = 10
# b =10
# c=11
# print(id(a),id(b),id(c))

# s = 'I am learning python'
# print(s[5:10])

# print(s[10:5:-1])
# print(s[:2:-1])

# s ="hi:hello:hey"
# print(s.split(':'))

# print(s.find('a',3,14)) # return -1 if not found
# print(s.index('s')) # shows error if not found


# print("{:5d}".format(12))
# print("{:2d}".format(1234))
# print("{:8.3f}".format(12.2346))
# print("{:05d}".format(12))
# print("{:08.3f}".format(12.2346))
# print("{:^10.3f}".format(12.2346))
# print("{:<05d}".format(12))
# print("{:>08.3f}".format(12.2346))
# print("{:=8.3f}".format(-12.2346))
#--------------------------------------------------------------------------------
# Problemm
#s = "I am learning python"
# coun no of occurence of char in the string

# lst =[]
# for i in s:
#     if i not in lst:
#         lst.append(i)

# print(lst)
# count=0
# for x in lst:
#     for y in s:
#         if x == y:
#             count+=1
#     print(x,"->",count)
#     count=0
#--------------------------------------------------------------------------------

# lst = [0,1,2,3,(1,2,3),5,6]

# print('before: ',lst)

# temp =list(lst[4])
# #print(temp)
# temp[1]=7
# lst[4] = tuple(temp)
# print('after:  ',lst)
#--------------------------------------------------------------------------------

# l = [1,2,3,4,5]
# d1 = dict.fromkeys(l,0)
# print(d1)

#--------------------------------------------------------------------------------
# l1 =['india','china','srilanka','xyz']
# l2 = ['pune','bejing','kolambo']

# d = dict(list(zip(l1,l2)))
# print(d)

#--------------------------------------------------------------------------------
# s1 ={1,2,3,4,5,6,7,8,9}
# s2 = {1,2,3,4,5,6,11}

# print(s1.union(s2))
# print(s1|s2)

# print(s1-s2)
# print(s1.difference(s2))

# print(s1.symmetric_difference(s2))
# print(s1^s2)

# print(s1.intersection(s2))
# print(s1&s2)
#--------------------------------------------------------------------------------
# d = {
#     "year": 1964,
#   "brand": "Ford",
#   "model": "Mustang"
  
# }
# print(sorted(d))
#--------------------------------------------------------------------------------
# def fn():
#     return 2,4,6

# print(type(fn()))


# l =[1,2,3,4,5]
# def func(mylist):
#     mylist.append(100)

# print(l)
# func(l)
# print(l)
#--------------------------------------------------------------------------------
# problemm
# x  = int(input("enter: "))
# def myfn(x):
#     if x==0:
#         return 1
#     return x*myfn(x-1)
# print(myfn(x))
# temp = str(myfn(x))

# print(temp[::-1])

#--------------------------------------------------------------------------------
# lammbda 
# x = lambda x,y:x+y
# print(x(10,20))

# l = [1,2,3,4,5,6,7]
# l = list(map(lambda x: x**2,l))
# print(l)

# l = list(filter( lambda x:x%2==0 ,l))
# print(l)

# l = reduce((lambda x,y:x+y),l)
# print(l)
#--------------------------------------------------------------------------------

#import os

# f =open("/Users/sparshagarwal/Desktop/Training/test.rtf","w")
# f.write("this is file demo\n")
# f.write("Second line\n")
# f.write("Third line")
# f.close()

# with open("test.rtf","r") as f:
#     #line = f.readline()
#     for line in f:
#         print(line)


# f = open("testfile.rtf","w")
# for i in range(1,11):
#     s = "This is line "+str(i)+".\n"
#     f.write(s)
# f.close

# with open("testfile.rtf","r")as f:
#     # f.seek(0,0)
#     line = f.readlines()
#     # print(line)
#     line[3] = "This is updated line 4.\n"
#     with open("testfile.rtf","w") as fr:
#         fr.writelines(line)
#         fr.close
#     f.close

