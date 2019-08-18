"""
Python的内置函数
- 数学相关: abs / divmod / pow / round / min / max / sum
- 序列相关: len / range / next / filter / map / sorted / slice / reverse / all / any
- 类型转换: chr / ord / str / bool / int / float / complex / bin / oct / hex
- 数据结构: dict / list / set / tuple
- 其他函数: id / input / open / print / type
"""

### 数学相关
print(abs(-3)) # 绝对值

print(divmod(5, 2)) # 同时做除法和求余，(a // b, a % b)

print(pow(2, 3)) # 幂运算，a^b

print(round(3.1415926, 2)) # 指定位数四舍五入

print(min(2, 3, 4)) # 最小值，可用于序列对象和单独数字

print(max(2, 3, 4)) # 最大值，可用于序列对象和单独数字

print(sum((2, 3, 4))) # 求和，只能用于序列对象


### 序列相关
print(len('张治创'))

print((range(5,0,-1))) # 转换成tuple输出

print(next(iter([1, 2, 3]))) # 迭代序列

# filter(function, 序列) -> 迭代器对象 -> 数据类型转换
# 保留满足条件的元素
print(list(filter(lambda n: n % 2 == 1, [1, 2, 3, 4, 5])))

# map(function, 序列) -> 迭代器 -> 数据类型转换
# 对每一个元素做相同操作
print([map(int, '12345')])

# sorted(iterable, cmp = None, key = None, reverse = False)
# key排序值，序列元素为元组，列表，字典时,可以用lambda函数取值
print(sorted([('b',2),('a',1),('c',3)], key=lambda x:x[1]))

# slice(stop) slice(start, stop, [step])
# 切片，筛选指定下标的数据，相当于列表切片[start:stop:step]
print(['a','b','c','d','e'][slice(0,6,2)])

# list.reverse() 实现列表反转
print(['a','b','c','d','e'].reverse())

# all(iterable) 用来判断序列内所有元素是否都为True（非0、空、None、False）
print(all([0, None, 1]))

# any(iterable) 用来判断序列内所有元素是否都为False（0、空、None、False）
print(all([0, None, 1]))

### 类型转换，略


### 数据结构，略


### 其他函数
# input('input:') # 括号内为提示信息

print(1,'a',list((1,2))) # 括号内可以是不同数据类型组成的tuple

# id用来返回对象地址（数据/方法）,可用来检查是否为同一变量
a = b = 1
print(id(a) == id(b))

print(type(range(1,3))) # <class 'range‘>，因此需要数据类型转换


### python文件内容相关操作
# 写入内容
f1 = open('test.txt', 'w', encoding='utf-8')
f1.write('第1行\n')
f1.writelines(['第2行\n','第3行\n'])
f1.close()

# 删除内容
with open('test.txt', 'r', encoding='utf-8') as f2_r:
    lines2 = f2_r.readlines()
with open('test.txt', 'w', encoding='utf-8') as f2_w:
    f2_w.writelines(lines2[0:len(lines2)+1:2]) # 覆盖重写，保留奇数行，一行一个元素

# 修改内容
with open('test.txt', 'r', encoding='utf-8') as f3_r:
    lines3 = f3_r.readlines()
with open('test.txt', 'w', encoding='utf-8') as f3_w:
    for line in lines3:
        if '第3行' in line: # 同样是覆盖重写，遇到第3行就进行修改
            f3_w.write('第3行改\n')
            continue
        f3_w.write(line)

# 查找内容，输出行数
with open('test.txt', 'r', encoding='utf-8') as f4_r:
    lines4 = f4_r.readlines()
    idx = 0
    for line in lines4:
        idx += 1
        if '第3行' in line:
            print(idx)
