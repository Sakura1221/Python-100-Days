"""
学生考试成绩表
"""


def main():
    students = ['张三', '李四', '王五', '赵六']
    subjects = ['语文', '数学', '英语']
    scores = [[None] * len(subjects)] * len(students)
    for row, student in enumerate(students): # 可以通过枚举方法同时获得索引
        for col, subject in enumerate(subjects):
            score = input('请输入%s的%s成绩：' % (student, subject))
            scores[row][col] = score
    print((scores))

if __name__ == "__main__":
    main()