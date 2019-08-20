"""
找出列表中最大或最小的元素
"""


def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
    # 直接使用内置的max和min函数找出列表中最大和最小元素
    # print(max(fruits))
    # print(min(fruits))
    max_value = min_value = fruits[0]
    for elem in fruits:
        if max_value < elem:
            max_value = elem
        if min_value > elem:
            min_value = elem
    print('Max:',max_value)
    print('Min:',min_value)


if __name__ == '__main__':
    main()
# 想一想如果最大的元素有两个要找出第二大的又该怎么做
# 在比较大小时保存上一个最大值即可