"""
字典的常用操作

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():
    stu = {'name':'张三', 'age': '23', 'gender': True}
    # 取键
    print(stu.keys())
    # 取值
    print(stu.values())
    # 取键值对
    print(stu.items())
    # 遍历字典的键值对
    for item in stu.items():
        print(item) # 输出键值对tuple
        print(item[0], item[1]) # 分开输出键值对的键和值
    # 元素赋值
    if 'score' in stu:
        stu['score'] = 90 # 直接对不存在的键赋值会报错
    print(stu)
    print(stu.setdefault('score', 90)) # 与get读取对应，有key获取value，无key设置value为default并返回
    print(stu)
    print(stu.setdefault('score', 100)) # 有key获取value返回
    print(stu)



if __name__ == '__main__':
    main()
