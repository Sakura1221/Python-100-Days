"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

from random import randint

num = randint(1,100)
times = 7

while times > 0:
    guess = int(input('猜一个1到100的整数:'))
    if guess == num:
        print('猜对了')
        break
    else:
        times -= 1
        print('你还有%d次机会' % times)
        if guess > num:
            print('猜大了')
        else:
            print('猜小了')
if times == 0:
    print('这都猜不到，数字是%d' % num)
