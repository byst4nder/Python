#打印质数   去除质数倍数法

#n=int(input("Please input a number:"))
n=1000
lst=list(range(3,n,2))
if n>=2:
    lst.append(2)
for i in range(0,int(len(lst)**0.5)+1):
    for y in range(i+1,len(lst)):
        if y<len(lst):
            if lst[y]%lst[i]==0:
                lst.pop(y)
lst.sort()
print(len(lst),lst)

#打印质数   保留质数法
#n=int(input("Please input a number:"))
lst=list()
if n>=2:
    lst.append(2)
for inti in range(3,n,2):
#    print(list(range(3,int(inti**0.5)+1)))
    for inty in range(3,int(inti**0.5)+1):
        if inti%inty==0:
            break
    else:
        lst.append(inti)
print(len(lst),lst)





