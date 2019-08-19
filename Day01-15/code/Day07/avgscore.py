"""
输入学生考试成绩计算平均分
用列表保存名字和分数
"""


def main():
    number = int(input('请输入学生人数：'))
    name = [None] * number # 用空list储存数据
    score = [None] * number
    for index in range(number):
        name[index] = input('请输入第%d个学生的名字：' % (index+1))
        score[index] = int(input('请输入第%d个学生的成绩：' % (index+1)))
    avgscore = sum(score) / number
    print('平均分为：%.2f' % avgscore)

if __name__ == '__main__':
    main()
