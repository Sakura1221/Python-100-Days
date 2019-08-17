"""
输入非负整数n计算n!
"""

n = int(input("请输入一个非负整数:"))
result = 1
if n == 0:
    result = 1
else:
    for i in range(1,n+1):
        result *= i
print(result)