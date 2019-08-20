"""
生成斐波拉切数列
用列表保存数据
数列均可使用append方法
"""


def main():
    f = [1, 1]
    for i in range(2, 20):
        f.append(f[i-1] + f[i-2])
    print(f)


if __name__ == '__main__':
    main()