"""
函数的定义和使用 - 求最大公约数和最小公倍数
"""

# 从小往大数效率低，应该从大往小数
# def gcd(x, y):
#     factor = 1
#     for i in range(1,min(x, y) + 1):
#         if (x % i == 0) and (y % i == 0):
#             factor = i
#     return factor

def gcd(x,y):
    for factor in range(min(x,y), 0, -1): # start stop(不包括) step
        if (x % factor) == 0 and (y % factor) == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)

if __name__ == '__main__':
    print(gcd(21, 36), lcm(21, 36))
