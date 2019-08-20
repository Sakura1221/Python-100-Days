"""
输出10行的杨辉三角 - 二项式的n次方展开系数
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
... ... ...
"""


def main():
    row_num = int(input('请输入行数：'))
    yh = [[]] * row_num # 每行长度不同，不统一赋值
    for row in range(row_num):
        yh[row] = [None] * (row + 1)
        for col in range(row + 1):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col - 1] + yh[row - 1][col]
    print(yh)


if __name__ == '__main__':
    main()
