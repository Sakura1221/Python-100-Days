"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
"""

import math

# 数据的读入用到了字符串的分割方法，序列的映射方法
a, b, c = map(float, input('请输入三角形边长，以空格隔开：').split())

if a + b > c and a + c > b and b + c >a:
    print('周长 = %f' % (a + b + c))
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('面积 = %f' % area)
else:
    print('不能构成三角形')