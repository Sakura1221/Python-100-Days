"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14
"""

import math

for num in range(1, 10000):
    end = int(math.sqrt(num))
    sum = 0
    for factor in range(1, end+1): # 根号只能求得较小的那个因数
        if num % factor == 0:
            sum += factor
            if factor != 1 and num // factor != factor:
                sum += num // factor # 加上较大且不重复（非本身）的因数
    if num == sum:
        print(num)