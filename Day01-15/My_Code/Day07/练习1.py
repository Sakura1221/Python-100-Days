"""
在屏幕上显示跑马灯文字
"""

import os
import time

def main():
    str = "我爱你中国，亲爱的母亲！"
    while True:
        os.system('cls')
        time.sleep(0.2)
        print(str)
        str = str[1:] + str[0]

if __name__ == '__main__':
    main()