"""
抽象类 / 方法重写 / 多态
实现一个工资结算系统 公司有三种类型的员工
- 部门经理固定月薪12000元/月
- 程序员按本月工作小时数每小时100元
- 销售员1500元/月的底薪加上本月销售额5%的提成
输入员工的信息 输出每位员工的月薪信息
"""

from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):

    # 初始化方法，传参name
    def __init__(self, name):
        self._name = name

    # name访问器
    @property
    def name(self):
        return self._name

    # 抽象方法get_salary
    @abstractmethod
    def get_salary(self):
        pass



class Manager(Employee):

    # 子类继承父类不做初始化，自动继承父类属性
    # 子类继承父类，不用super()调用父类构造器初始化，子类不会继承父类属性
    # 子类继承父类，用super()调用父类构造器初始化，子类会继承父类属性
    # 而且super()可以在父类基础上传入其他属性，子类同名属性会覆盖父类属性
    # 子类初始化参数至少要多于父类初始化参数

    # 子类调用super()初始化，同时额外传入other_name参数
    def __init__(self, name, other_name=None):
        super().__init__(name)
        if other_name is not None:
            self._name = other_name

    # get_salary方法
    def get_salary(self):
        return 12000



class Programmer(Employee):

    def __init__(self, name):
        super().__init__(name)

    # 子类可以额外增加一些方法
    def set_working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 100 * self._working_hour


class Salesman(Employee):

    def __init__(self, name):
        super().__init__(name)

    def set_sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1500 + self._sales * 0.05


if __name__ == '__main__':
    emps = [Manager('武则天', '武媚娘'), Programmer('狄仁杰'), Salesman('白元芳')]
    for emp in emps:
        # 如果是程序员，请输入xx本月工作时间
        if isinstance(emp, Programmer):
            working_hour = int(input('请输入%s本月工作时间：' % emp.name))
            emp.set_working_hour(working_hour)

        # 如果是销售员，请输入xx本月销售额
        if isinstance(emp, Salesman):
            sales = float(input('请输入%s本月销售额：' % emp.name))
            emp.set_sales(sales)

        print('%s本月月薪为: ￥%.2f元' % (emp.name, emp.get_salary()))
