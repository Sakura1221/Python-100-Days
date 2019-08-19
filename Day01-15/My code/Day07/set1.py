"""
定义和使用集合
"""


def main():
    # 创建集合
    set1 = {1, 2, 3, 2, 3, 1}
    print(set1)
    # 获取集合长度
    print(len(set1))
    # 使用range创造集合
    set2 = set(range(1,5))
    print(set2)
    # 添加元素
    set1.add(4)
    print(set1)
    # 添加多个元素
    set2.update(range(5,11))
    print(set2)
    # 删除元素
    set2.pop() # 删除第一个元素
    print(set2)
    set2.discard(11) # 如果不存在不会报错
    print(set2)
    # remove的元素如果不存在会引发KeyError
    if 10 in set2:
        set2.remove(10)
    print(set2)
    # 遍历集合容器
    for member in set2:
        print(member, end=' ')
    print()
    # 将元组转换成集合
    tuple3 = (1, 2, 3, 2, 1)
    set3 = set(tuple3)
    print(set3)

if __name__ == '__main__':
    main()
