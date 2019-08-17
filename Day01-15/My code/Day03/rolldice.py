"""
掷骰子决定做什么事情
要生成1-6的随机数
"""

from random import randint

x = randint(1,6)
if x == 1:
    result = '学python'
elif x == 2:
    result = '学numpy'
elif x == 3:
    result = '学opencv'
elif x == 4:
    result = '学pytorch'
elif x == 5:
    result = '学yolo'
else:
    result = '学数据结构与算法'

print(result)