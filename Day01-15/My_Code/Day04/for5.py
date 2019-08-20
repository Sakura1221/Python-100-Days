"""
输入两个正整数计算最大公约数和最小公倍数
"""

a, b = map(int,input("请输入两个正整数，空格隔开:").split())
factor = 1
for i in range(1,min(a,b)+1):
    if a % i == 0 and b % i == 0:
        factor = i
print('最大公因数为%d，最小公倍数为%d' % (factor, a * b / factor))