"""
属性的使用
- 访问器/修改器/删除器
- 使用__slots__对属性加以限制
"""

# Car类
class Car(object):

    # slots魔法方法对属性加以限制，只对当前类有效，对子类没有作用
    __slots__ = ('_brand', '_max_speed')

    # 初始化参数_brand, _max_speed
    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed

    # _brand访问器
    @property
    def brand(self):
        return self._brand

    # _brand修改器
    @brand.setter
    def brand(self, brand):
        self._brand = brand

    # _brand删除器
    @brand.deleter
    def brand(self):
        del self._brand

    # _max_speed访问器
    @property
    def max_speed(self):
        return self._max_speed

    # _max_speed修改器
    @max_speed.setter
    def max_speed(self, max_speed):
        try: # 使用try和except可以捕捉错误，让程序继续进行
            if max_speed < 0:
                raise ValueError('Invalid max speed for car')
            self._max_speed = max_speed
        except ValueError:
            print('非法最高车速')

    # 字符串方法
    def __str__(self):
        return 'Car: [品牌=%s, 最高时速=%d]' % (self._brand, self._max_speed)

car = Car('QQ', 120)
print(car)
# ValueError
car.max_speed = -100 # 通过修改器可修改属性值
car.max_speed = 320
car.brand = 'Benz'
print(car)
# 使用__slots__属性限制后下面的代码将产生异常AttributeError
try:
    car.current_speed = 80 # 动态语言支持在运行时绑定新的属性
except AttributeError:
    print('属性限制，无法绑定新属性')
# 如果提供了删除器可以执行下面的代码
del car.brand
# 属性的实现
print(Car.brand) # 属性
print(Car.brand.fget) # 属性的访问器
print(Car.brand.fset) # 属性的修改器
print(Car.brand.fdel) # 属性的删除器
# 通过上面的代码帮助学生理解之前提到的包装器的概念
# Python中有很多类似的语法糖后面还会出现这样的东西
