"""
流水灯程序

"""

import os
import time


def main():
    str = 'Welcome to 1000 Phone Chengdu Campus      '
    while True:
        print(str)
        time.sleep(0.2) # 暂停0.2s
        str = str[1:] + str[0:1] # 实现字符串循环
        # for Windows use os.system('cls') instead
        os.system('cls') # 必须在终端运行才有清屏效果


if __name__ == '__main__':
    main()
