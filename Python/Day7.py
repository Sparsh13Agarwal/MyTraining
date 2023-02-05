# # lst =[]
# # for i in range(1,51):
# #     lst.append(i)

# # for i in lst:
# #     if i%3==0:
# #         print(i,end=" ")

# ######3
# # f=open("test.rtf","r")
# # st=f.read()
# # st=st.lower()
# # st=st.split(" ")
 
# # v=set(st)
# # d=dict()
 
# # for i in v:
# #  val=st.count(i)
# #  if val in d:
# #     d[val].append(i)
# #  else:
# #     d[val]=[i]
 
# # print(d)



# # ######3
# # f=open("test.rtf","r")
# # data = f.read().lower()
# # data = data.split(" ")
 
# # word=set(data)
# # d=dict()
 
# # for w in word:
# #     temp = data.count(w)
# #     if temp in d:
# #         d[temp].append(w)
# #     else:
# #         d[temp] =[w]
# # print(d)


# #--------------------------------------------------------------------------------
# # Read the file
# # Create a dictionary keys should be counts and value is a list of works having the same occurrence as key in the given file


# # f = open("test.rtf","r")
# # wd = f.read()
# # wd = wd.split(" ")


# # mydic = dict()
# # for w in wd:
# #     w = w.lower()
# #     if w in mydic:
# #         mydic[w] +=1
# #     else:
# #         mydic[w] =1
    
# # print(mydic)


# # li1 = [1,2,3,]
# # li2 = [1,2,3,10000]
# # li3 = [1,2,3,10000]
# # def func(li):
# #     li2 = li1
# #     li2.append(10000)
# #     print(li2)
# #     return li2

# # li1 = [1,2,3]
# # li3 = func(li1)
# # print(li1,li3)

# # def func(l1):
# #     l2 = l1.copy()

# #     l2.append(10000)

# #     return l2
# # l1 = [1,2,3]
# # l3 = func(l1)
# # print(l1,l3)


# # shallow copy n deep copy

# # import copy
# # def func(li1):
# #     li2 = copy.deepcopy(li1)
# #     li2[-1].append('D')
# #     print(li2)
# #     return li2

# # li1 = [1,2,3,['A','B']]
# # li3 = func(li1)
# # print(li1,li3)
# # li1 = [1,2,3,4]
# # li2 = li1
# # li3 = li2[:]

# # print(li1 is li2)


# ##########

# # pro_lan = ['Python','C','Java','VC++']
# # temp = sorted(pro_lan,key=len)
# # print(temp)

# # for w in pro_lan:
# #     l = len(w)

# #--------------------------------------------------------------------------------
# # sort the list based on first element
# # li = [(1,2,3),(4,3,6),(2,5,7),(1,0,9)]
# # var = sorted(li,key= lambda x:x[1])
# # print(var)
# #--------------------------------------------------------------------------------
# # # sol 
# # path = "/content/files"
# # import os
# # ls = os.listdir(path)
# # # ls = ['index.html', 'py.txt']
# # res= sorted(ls, reverse=True, key= lambda x : os.path.getsize(path+"/"+x))
# # # res= ['py.txt', 'index.html']

# # path = os.getcwd()
# # filenames = os.listdir(path)
# # filenames.sort(key=lambda x:os.path.getsize(path + '/' + x))
# # print('\n'.join(filenames))

# # import os

# # path = "/Users/sparshagarwal/Desktop/Sparsh/Training1"

# # file_list = os.listdir(path)
# # print(file_list)
# # size = os.path.getsize(path)
# # var = file_list.sort(key= lambda x: size + x)
# # print(var)

# # probl combine negh. wordss on the basis of input no. if no is 2 so output is python is,  easy to , learn
# # textList = text.split()
# # n = int(input())
# # ans = [textList[i:i+n] for i in range(len(textList) - n + 1)]
# # print(ans)
# # text = 'Python is easy to learn. it reduces devlopment time'
# # lst = text.split()
# # n = int(input("enter:- "))
# # c =0
# # temp = list()
# # last = lst
# # for i in lst:
# #     temp.append(lst[c:n])
# #     c=n
# #     n +=2
# # print(temp)


# # text = 'Python is easy to learn. it reduces devlopment time'
# # text = text.split()
# # from itertools import combinations
# # n = int(input("enter no:- "))
# # var = list(combinations(text,n))
# # print(var)

# # text = 'Python is easy to learn. It reduce development time'
# # text = text.split()
# # n = int(input("enter no:"))
# # var = [text[x:x+n] for x in range(len(text) - n + 1)]
# # print(var)
# #--------------------------------------------------------------------------------

# #print(*'Python') # unpack all the elemetns
# #print(*'Python')
# import copy
# i = 2
# j =2
# l1 = [1,2,3,4]
# l2 = l1
# l3 = l1.copy()
# #print(l3[1] is j)
# l4 = [1,2,3,4,5,[2,3],(1,2,3)]
# l5 = l4.copy()
# print(l5[-1] is l4[-1])
# print(l5[-2] is l4[-2])
# print(l5[-3] is l4[-3])


# l6 = copy.deepcopy(l4)
# print(l6[-1] is l4[-1])
# print(l6[-2] is l4[-2])
# print(l6[-3] is l4[-3])
#--------------------------------------------------------------------------------

# str = 'Pyth0n29#8496'
# sum =0
# count = 0
# for i in str:
    
#     if i.isdigit():
#         sum +=int(i)
#         count+=1
# print("sum",sum)
# print("avg: ", sum/count)


sampleDict ={
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":90,
                "history":88
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])





