"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...
"""

a = [None] * 20
a[0], a[1] = 1, 1

for i in range(2,20):
    a[i] = a[i-1] + a[i-2]

print(a)