# python 3
# 这是一个猜大小的游戏

from random import randint

#生成随机数
def randlist(n=3, start=1, end=6): return [
    randint(1, 6) for x in range(1, ｎ+1)]
#判断猜测结果 胜利 1，失败 0
def Guess(userguess,numlist):
    sumnum=sum(numlist)
    if numlist[0] == numlist[1] and numlist[1] == numlist[2] and userguess == '0':
        print('恭喜你！{}获得胜利，数字是{}-{}-{}。'.format(username,
                                               numlist[0], numlist[1], numlist[2]))
    elif sumnum < 10 and userguess == '-1':
        print('恭喜你！{}获得胜利，数字是{}-{}-{}。'.format(username,
                                               numlist[0], numlist[1], numlist[2]))
    elif sumnum >= 10 and userguess == '1':
        print('恭喜你！{}获得胜利，数字是{}-{}-{}。'.format(username,
                                               numlist[0], numlist[1], numlist[2]))
    else:
        print('你猜错了，数字是{}-{}-{}。'.format(numlist[0], numlist[1], numlist[2]))


        
print('游戏说明：这是一个猜大小的游戏，猜测”大“、”小“、”豹子“！！！')
username = ''
while username == '':
    username = input("请输入你的名字：")
print('你好{}，欢迎参加游戏，祝你玩得愉快！\n大输入1，小输入-1，豹子输入0。'.format(username))
userguess = ''
while userguess != 'exit':
    userguess = input('请输入你的猜想（1、0、-1）：')
    if userguess in ['exit',''] :
        continue
    numlist = randlist()
    sumnum = sum(numlist)
    if numlist[0] == numlist[1] and numlist[1] == numlist[2] and userguess == '0':
        print('恭喜你！{}获得胜利，数字是{}-{}-{}。'.format(username,
                                               numlist[0], numlist[1], numlist[2]))
    elif sumnum < 10 and userguess == '-1':
        print('恭喜你！{}获得胜利，数字是{}-{}-{}。'.format(username,
                                               numlist[0], numlist[1], numlist[2]))
    elif sumnum >= 10 and userguess == '1':
        print('恭喜你！{}获得胜利，数字是{}-{}-{}。'.format(username,
                                               numlist[0], numlist[1], numlist[2]))
    else:
        print('你猜错了，数字是{}-{}-{}。'.format(numlist[0], numlist[1], numlist[2]))