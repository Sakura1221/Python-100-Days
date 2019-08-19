"""
定义和使用字典
"""


def main():
    # 创建字典
    scores = {'张三': 60, '李四': 70, '王五': 80}
    print(scores['张三'])
    print(scores['李四'])
    # 遍历字典的键
    for elem in scores:
        print('%s\t-->\t%d' % (elem, scores[elem]))
    # 新增键值对
    scores['赵六'] = 90 # 元素存在则做修改，没有就添加
    scores.update(钱七=95, 孙八=100) # 添加多个值，key不需要加引号
    # 获取元素
    if '小猫' in scores:
        print(scores['小猫']) # 直接取值会报错
    print(scores.get('小猫')) # get方法不会报错，返回default=None
    print(scores.get('小猫', 50)) # get可以为不存在的值设置默认值，但不会改变字典
    print(scores)
    print(scores.popitem()) # 删除最后一个键值对并返回
    print(scores)
    print(scores.pop('张三', 100)) # 删除指定键值对，并返回对应的值，如果值不存在返回默认值
    print(scores.pop('小狗', 100)) # 不存在返回默认值
    print(scores)
    scores.clear() # 清空字典
    print(scores)
    # 删除元素



if __name__ == '__main__':
    main()
