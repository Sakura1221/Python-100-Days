"""
Python常用模块
- 模块通用命令: import / dir
- 运行时服务相关模块: copy / pickle / sys / ...
- 数学相关模块: decimal / math / random / ...
- 字符串处理模块: codecs / re / ...
- 文件处理相关模块: shutil / gzip / ...
- 操作系统服务相关模块: datetime / os / time / logging / io / ...
- 进程和线程相关模块: multiprocessing / threading / queue
- 网络应用相关模块: ftplib / http / smtplib / urllib / ...
- Web编程相关模块: cgi / webbrowser
- 数据处理和编码模块: base64 / csv / html.parser / json / xml / ...
"""

########## 模块通用命令 ##########
# 导入模块
import copy, os, pickle, sys
from math import *

# dir()查看一个模块内定义的变量和函数
# __name__:模块名称，__file__文件路径，__doc__文档描述
print(dir(os))

########## 运行时服务模块 ##########

### python数据存储，只是将变量名贴在对应内存空间
# 为变量开辟新的内存空间赋新值
a = [1, 2, 3] # 内存中开辟空间存储这个list，并命名为a
b = a # 相同的空间，两个命名id(a)==id(b)或者a is b
a = [4, 5, 6] # 此时a的名称被贴在另一个list
print(b) # b还被贴在第一个list上，因此值不变

# 在相同的内存空间为变量赋新值
c = [1, 2, 3]
d = c
c[0],c[1],c[2] = 4,5,6 # 这次改变的是list内的值，c对应的地址不变
print(c, d, sep='\n') # d也指向相同的list，因此值会被修改

### copy模块，深浅复制
# 浅复制不会为复杂对象（序列里嵌套序列）的子对象开辟新的内存地址
# 浅复制的copy变量会随origin的值改变
# 深复制会为复杂对象（序列里嵌套序列）的子对象开辟新的内存地址
# 深复制的copy变量不会随origin的值改变
# 对于没有嵌套的序列，两者相同，都会开辟新的内存地址，变量不会随origin改变
origin = [1, 2, [3, 4]]
cop1 = copy.copy(origin)
cop2 = copy.deepcopy(origin)
print(cop1 == cop2, cop1 is cop2) # copy与deepcopy值相同但是不是同一对象
origin[2][0] = 'hey'
print(origin, cop1, cop2, sep='\n') # copy对象会随origin改变，deepcopy不会


### 数学相关模块

### 文件处理模块

### 操作系统服务模块

### 进程和线程模块
