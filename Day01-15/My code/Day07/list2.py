"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    # 列表连接
    fruits += ['peach', 'watermelon']
    print(fruits)
    # 获取长度
    print(len(fruits))
    # 遍历列表
    for item in fruits:
        print(item, end=' ')
    print()
    # 列表切片
    print(fruits[::2])
    # 复制列表
    # fruits2 = fruits # 没有复制列表，只是创建了新的引用
    fruits2 = fruits[:]
    print(fruits2)
    # 列表排序
    fruits.sort(key=len) # list专门的排序方法，会修改原list，选择排序方法为长度
    print(fruits)
    print(sorted(fruits,reverse=True)) # python内置针对序列的排序方法，不改变原list
    print(fruits)
    # 列表反转
    fruits.reverse() # 会改变原list
    print(fruits)
    print(fruits[::-1]) # 不改变原list
    # 查找元素
    print(fruits.index('grape')) # 元素只有一个可用
    fruits.append('apple')
    print(fruits)
    for idx, key in enumerate(fruits): # 当元素不止一个时使用
        if key == 'apple':
            print(idx,end=' ')

if __name__ == '__main__':
    main()
