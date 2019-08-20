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

"""模块通用命令"""
# 导入模块
import csv
from xml import *

# dir()查看一个模块内定义的变量和函数
# __name__:模块名称，__file__文件路径，__doc__文档描述
print(dir(csv))



"""运行时服务模块"""

##########copy模块，深浅复制讲解##########
import copy
# python数据存储，只是将变量名贴在对应内存空间
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


##########pickle模块，数据保存与读取##########
import pickle, pprint
# python的pickle模块实现了基本的数据序列和反序列化。
# 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
data1 = {'a': [1, 2.0, 3, 4+6j],
        'b': 'string',
        'c': None}

ref_list = [1, 2, 3]

output = open('data.pkl', 'wb') # 以二进制文件存储
pickle.dump(data1, output)
pickle.dump(ref_list, output)
output.close()

pkl_file = open('data.pkl','rb')

# 一个load只加载一个dump数据，返回值与原始数据相同
data1 = pickle.load(pkl_file)
data2 = pickle.load(pkl_file)

# pprint可以保留数据结构
pprint.pprint(data1)
pprint.pprint(data2)


##########sys模块，系统特定的参数和功能##########
import sys
# 输出脚本的名称和参数，argv[0]为脚本名称，argv[1:]为脚本参数
print(sys.argv)




"""数学相关模块"""
##########decimal模块，准确十进制浮点运算##########
import decimal
print(decimal.Decimal('12.222')) # 输入整型或字符串，因为浮点数不准确（先转为str）
decimal.getcontext().prec = 6 # 设置统一的精度
print(decimal.Decimal(1) / decimal.Decimal(7))
# 四舍五入保留4位小数并转化成str类型
print(str(decimal.Decimal('3.14159').quantize(decimal.Decimal('0.0000'))))

##########math模块，浮点数数学运算##########
import math
print(math.e, math.pi, )
print(math.pow(2,3), math.log(4,2))
print(format(math.sin(math.radians(45)),'.3f')) # 默认以弧度制计算

##########random模块，浮点数数学运算##########
import random

print(random.random()) # 生成一个0到1之间的随机浮点数
print(random.uniform(1,3)) # 生成一个指定范围的随机浮点数
print(random.randint(1,3)) # 生成一个指定范围内的整数
print(random.randrange(0,100,2)) # 生成指定范围内的随机偶数

# random.choice用于从序列中随机获取一个元素
print(random.choice('改变世界'))
print(random.choice(['张三','李四','王五']))

# random.shuffle用于将列表元素打乱，无返回值，不可赋值和调用
list_shuffle = ['改','变','世','界']
random.shuffle(list_shuffle)
print(list_shuffle)

# random.sample用于从序列中获取指定长度的片段，返回list
print(random.sample(('张三', '李四', '王五', '赵六'), 2))




"""操作系统服务模块"""

##########os模块，系统相关操作##########
import os

#####目录相关#####
# 创建单级目录
if not os.path.exists('test'):
    os.mkdir('./test')
os.mkdir('./test1')
# 创建多级目录
os.makedirs('./test1/test2/test3')
# 删除单级目录，目录要为空
os.rmdir('./test1/test2/test3')
# 删除多级目录，必须把多级目录完全列出
os.removedirs('./test1/test2')

#####文件相关#####
# 创建文件（Windows不可用mknod）
# os.mknod('test_os.txt')
f1 = open('./test/test.txt','w')
f1.close()
# 重命名文件/目录
os.rename('./test/test.txt', './test/test_rename.txt')
# 删除文件
os.remove('./test/test_rename.txt')

#####路径相关#####
os.chdir('./test') # 改变当前工作目录
print(os.getcwd()) # 返回当前工作目录的绝对路径
print(os.listdir('./')) # 返回指定目录包含的文件/文件夹名字列表
os.chdir('..') # 返回上级目录
print(os.path.exists('./test')) # 判断目录/文件是否存在
print(os.path.abspath('./xxx.py')) # 返回绝对路径
print(os.path.dirname('test.txt')) # 返回文件的相对路径


##########datetime模块，日期相关##########
import datetime

# 格式化输出当前日期
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


##########time模块，计时相关##########
import time

start = time.perf_counter() # 开始计时
time.sleep(1) # 暂停1s
elapsed = time.perf_counter() - start # 计时结束

# 获取当前时间
tm = time.localtime(time.time())
hour = tm.tm_hour
minute = tm.tm_min
second = tm.tm_sec


##########logging模块，日志相关##########
import logging


##########io模块，计时相关##########



"""文件处理模块"""
##########shutil模块，文件相关操作##########

import shutil

# copy单个文件，使用copy方法可以跨目录复制，且直接覆盖同名文件
shutil.copy('test.txt', './test/test_copy.txt')

# copy一个目录(可以是多级)，第二目录必须是新建的，第一目录作为子目录
if not os.path.exists('./test/test'):
    shutil.copytree('./test', './test/test')

# 删除一个目录以及目录下的文件
shutil.rmtree('./test/test')

# 移动文件，目标路径要包含文件名
if not os.path.exists('./test_copy.txt'):
    shutil.move('./test/test_copy.txt', './test_copy.txt')
else:
    shutil.move('./test_copy.txt', './test/test_copy.txt')



"""进程和线程模块"""
