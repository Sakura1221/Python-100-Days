"""
继承的应用
- 抽象类
- 抽象方法
- 方法重写
- 多态
"""

# 要用到abc里的ABCMeta和abstractmethod
from abc import ABCMeta, abstractmethod
from math import pi

# 父类Shape
class Shape(object, metaclass=ABCMeta):

    # 继承了元类，可不初始化？

    # perimeter抽象方法
    @abstractmethod
    def perimeter(self):
        pass

    # area抽象方法
    @abstractmethod
    def area(self):
        pass

# 类Circle继承Shape
class Circle(Shape):

    # 初始化
    def __init__(self, radius):
        self._radius = radius

    # 重写perimeter
    def perimeter(self):
        return 2 * pi * self._radius

    # 重写area
    def area(self):
        return pi * self._radius ** 2

    # 重写__str__
    def __str__(self):
        return '我是一个半径为%.2f的圆' % self._radius

# 类Rect继承Shape
class Rect(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def perimeter(self):
        return (self._width + self._height) * 2

    def area(self):
        return self._width * self._height

    def __str__(self):
        return '我是一个长为%.2f，宽为%f的矩形' % (self._width, self._height)


if __name__ == '__main__':
    # 3个实例组成的列表shapes
    shapes = [Circle(2.5), Circle(3.7), Rect(3.4, 5.6)]

    # 遍历列表，输出类和周长面积
    for shape in shapes:
        print(shape)
        print('周长：%.2f' % shape.perimeter())
        print('面积： %.2f' % shape.area())