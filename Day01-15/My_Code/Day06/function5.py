"""
函数的参数
- 位置参数
- 可变参数
- 关键字参数
- 命名关键字参数
"""


# 参数默认值
def f1(a, b=2, c=3):
    return a + b + c

print(f1(1))
print(f1(3,4,5))
print(f1(a=5, b=6, c=7))

# 可变参数
def f2(*args):
    sum = 0
    for item in args:
        sum += item
    return sum

print(f2())
print(f2(1,2,3))

# 关键字参数
def f3(**kwargs):
    if 'name' in kwargs:
        print('你好，%s!' % kwargs['name'])
        if 'tel' in kwargs:
            print('电话是：%s' % kwargs['tel'])
        else:
            print('无号码')
    else:
        print('查无此人')

param = {'name':'李四', 'tel':'456'}
f3(name='张三', tel= '123')
f3(**param)

# 命名关键字参数，*后面的参数必须传入且要加参数名
def person(name, age, *, city, job):
    print(name, age, city, job)

person('Sakura', 23, job ='student', city= 'chongqing')







