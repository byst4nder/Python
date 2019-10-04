#打印N以内的素数 pop 通过去除质数的倍数
import datetime
time1=datetime.datetime.now()
n=1000000
lst=list(range(3,n,2))
if n>=2:
    lst.append(2)
for y in range(0,int(len(lst)**0.5)+1):
    for i in range(y+1,len(lst)):
        if i <len(lst):
            if lst[i]%lst[y]==0:
                lst.pop(i)
#print(lst,'\n',len(lst))
time2=datetime.datetime.now()
print(time2-time1)
print(len(lst))

#打印N以内的素数 remove 通过去除质数的倍数
n=100
lst=list(range(3,n,2))
if n>=2:
    lst.append(2)
for y in range(0,int(len(lst)**0.5)+1):
    for i in lst[y+1:]:
        if i%lst[y]==0:
            lst.remove(i)
print(lst,len(lst))   

#求一定范围内的质数
intn=int(input("请输入一个整数："))
lst=list(range(3,intn,2))
if intn>=2:
    lst.append(2)
print(len(lst),lst)
for i in range(0,int(intn**0.5)+1):
    for y in range(i+1,len(lst)):
        if y<len(lst):
            if lst[y]%lst[i]==0:
                lst.pop(y)
#print(lst)
print(len(lst),lst)