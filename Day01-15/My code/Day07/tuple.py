"""
元组的定义和使用

"""


def main():
    # 定义元组
    t = ('张治创', 23, True, '重庆')
    print(t)
    # 获取元组中的元素
    print(t[0])
    # 遍历元组中的值
    for member in t:
        print(member)
    # 重新给元组赋值
    # t[0] = '王大锤'      # TypeError 元组内的元素只读不可写
    # 变量t重新引用了新的元组 原来的元组被垃圾回收
    t = ('王大锤', 20, True, '昆明')
    # 元组和列表的转换
    person = list(t)
    print(person)
    person[0] = '李小龙'
    person[1] = 25
    print(person)

    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_tuple)
    print(fruits_tuple[1])


if __name__ == '__main__':
    main()