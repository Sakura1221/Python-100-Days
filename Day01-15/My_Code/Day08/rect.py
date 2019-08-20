"""
定义和使用矩形类
"""

class Rect(object):
    """矩形类"""

    def __init__(self, width=0, height=0):
        """初始化方法"""
        self.__width = width # 私有属性，只有类自己能访问
        self.__height = height

    def perimeter(self):
        """计算周长"""
        return (self.__width + self.__height) * 2

    def area(self):
        """计算面积"""
        return self.__width * self.__height

    def __str__(self):
        """
        系统定义特殊方法
        输出字符串
        print(类的实例可调用输出)
        """
        return '矩形[%f,%f]' % (self.__width, self.__height)

    def __del__(self):
        """
        析构器
        类实例引用计数为0时自动销毁
        """
        print('销毁矩形对象')


if __name__ == '__main__':

    rect1 = Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())

    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())