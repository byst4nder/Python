# python3
# 这是一个打印表格格式测试程序
import string

def printTable(Table:list):
    #查找table中最长的字符

    lenlist=[]
    for x in Table:
        strlen=[]
        for y in x:
            strlen +=[len(y)]
        lenlist += [strlen]
    
    strlen=[0 for x in range(0,4)]

    for x in range(0,len(lenlist)):
        for y in range(0,len(lenlist[x])):
            if lenlist[x][y]>strlen[y]:
                strlen[y]=lenlist[x][y]
       

    print(lenlist,strlen)
    # 打印table
    for x in range(0,len(Table)):
        for y in range(0,len(Table[x])):
            if y == 0:
                print('{} '.format(Table[x][y]).rjust(strlen[y]+1),end='')
            else:
                print('{}'.format(Table[x][y]).ljust(strlen[y]+1),end='')
        print()

tableData = [['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
