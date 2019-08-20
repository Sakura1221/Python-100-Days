"""
定义和使用学生类
"""



class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s正在学习%s" % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是很多程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_av(self):
        if self.age < 18:
            print('%s还不能看' % self.name)
        else:
            print('%s可以看' % self.name)

def main():
    stu1 = Student('张三', 17)
    stu2 = Student('李四', 18)
    print(stu1.name, stu1.age)
    stu1.study('Python')
    stu1.watch_av()
    stu2.study('Cpp')
    stu2.watch_av()



if __name__ == '__main__':
    main()
