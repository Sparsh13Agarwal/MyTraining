import random
st = 'goggle'
map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
surl =str()
temp = random.randint(97,121)
id =12345


while(id>0):
    surl += map[id%temp]
    #print(surl)
    id //=temp
print(surl)




