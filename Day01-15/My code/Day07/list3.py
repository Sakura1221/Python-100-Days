"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器
"""


# 生成Fibonacci序列的生成器
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        # yield相当于return，生成器函数调用一次，执行一次，是函数中断和开始的地方
        # 不会写生成器函数，可以先写循环输出函数，将print替换成yield即可
        yield a


def main():
    # 用range创建数值列表
    list1 = list(range(1, 11)) # range需要类型转换
    print(list1)

    # 生成表达式
    list2 = [x * x for x in range(1, 11)]
    print(list2)
    list3 = [m + n for m in 'ABCDEFG' for n in '12345'] # 两个for循环是嵌套关系
    print(list3)
    print(len(list3))

    # 生成器(节省空间但生成下一个元素时需要花费时间)
    # ()表达式创建生成器对象
    gen1 = (m + n for m in 'ABCDEFG' for n in '12345')
    # 直接print不返回值，只能通过遍历或者迭代
    print(gen1)
    # 遍历生成器
    for elem in gen1:
        print(elem, end=' ')
    print()
    # 调用生成器函数创建生成器对象
    gen2 = fib(20)
    print(gen2)
    # 迭代生成器
    try:
        while True:
            val = next(gen2) # 调用内置的next方法对生成器进行迭代
            print(val,end=' ') # 在这里可以对生成器内的每个值进行操作
    except StopIteration: # 当迭代器迭代结束时会报错，忽略即可
        pass
    print()




if __name__ == '__main__':
    main()