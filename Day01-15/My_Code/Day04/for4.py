"""
输入一个正整数判断它是不是素数
"""
from math import sqrt

num = int(input("请输入一个正整数："))

is_prime = True
if num == 1:
    is_prime = False
else:
    for i in range(2, int(sqrt(num)+1)):
            if num % i == 0:
                is_prime = False
                break
print(is_prime)