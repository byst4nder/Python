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