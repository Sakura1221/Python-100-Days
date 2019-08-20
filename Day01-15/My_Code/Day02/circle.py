"""
输入半径计算圆的周长和面积
圆周率要用到math库
"""

import math

r = eval(input('请输入圆的半径：'))
c = 2 * math.pi * r
s = math.pi * (r ** 2)
print('圆的面积是{1:.2f},周长是{0:.2f}'.format(c,s))

