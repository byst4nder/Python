#打印字符网络图
grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.']]


for i in range(len(grid[0])):
    for y in range(len(grid)):
        print(' {0} '.format(grid[y][i]),end='')
    print()



#好玩游戏的物品清单
#你在创建一个好玩的视频游戏。用于对玩家物品清单建模的数据结构是一个字
#典。其中键是字符串，描述清单中的物品，值是一个整型值，说明玩家有多少该物
#品。例如，字典值{'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}意味着玩
#家有 1 条绳索、 6 个火把、 42 枚金币等。写一个名为 displayInventory()的函数，它接受任何可能的物品清单


def displayInventory(lst):
    count = 0
    print('displayInventory:')
    for i in lst.keys():
        count += lst.get(i)
        print('\t{1:<3} {0}'.format(i,lst.get(i)))
    print('Total number of items:{}'.format(count))

print('------------------------{}---------------------'.format('分隔符'))
lsta={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(lsta)




#写一个名为 addToInventory(inventory, addedItems)的函数， 其中 inventory 参数
#是一个字典， 表示玩家的物品清单（像前面项目一样）， addedItems 参数是一个列表，
#就像 dragonLoot。
print('------------------------{}---------------------'.format('分隔符'))

def addToInventory(inventory,addedItems):
    
    for i in addedItems:
        inventory.setdefault(i,0)
        inventory[i] += 1


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}
addToInventory(inv,dragonLoot)
displayInventory(inv)





