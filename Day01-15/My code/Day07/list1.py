"""
定义和使用列表
- 用下标访问元素
- 添加元素
- 删除元素
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    print(fruits)
    # 通过下标访问元素
    print(fruits[0])
    # 添加元素
    fruits.append('peach') # 添加一个元素
    print(fruits)
    fruits.extend(['pear', 'watermelon']) # 添加多个元素
    print(fruits)
    fruits.insert(2, 'pineapple') # 在指定位置添加元素
    print(fruits)
    # 删除元素
    print(fruits.pop()) # 删除最后一个元素并返回
    print(fruits)
    print(fruits.pop(0)) # 删除指定下标元素并返回
    print(fruits)
    del fruits[2] # 删除指定下标元素
    print(fruits)
    fruits.remove('apple') # 删除指定元素
    print(fruits)


if __name__ == '__main__':
    main()
