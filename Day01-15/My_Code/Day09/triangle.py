"""
实例方法和静态方法的应用
静态方法不调用类的属性和方法，不需要实例化就可以调用
静态方法只是借用了类的命名空间
"""

from math import sqrt

# Triangle类
class Triangle(object):

    # 初始化_a, _b, _c
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 静态方法is_valid判断三条边能否组成三角形
    @staticmethod
    def is_valid(a, b, c):
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False

    # 实例方法perimeter求周长
    def perimeter(self):
        return self._a + self._b + self._c

    # 实例方法area求面积
    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


if __name__ == '__main__':
    # 用字符串的split方法将字符串拆分成一个列表
    # 再通过map函数对列表中的每个字符串进行映射处理成小数
    a, b, c = map(float, input('请输入三角形的三条边，空格隔开').split())
    # 先判断给定长度的三条边能否构成三角形
    # 如果能才创建三角形对象
    if Triangle.is_valid(a, b, c):
        tri = Triangle(a, b, c)
        print(type(tri))
        print('周长：', tri.perimeter())
        print('面积：', tri.area())

