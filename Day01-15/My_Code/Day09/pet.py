"""
抽象方法：表示父类存在这个方法，但是没有实现（pass），不能实例化
子类必须重写才能实例化，不然就会报错
抽象方法要将元类设置为ABCMeta

不使用抽象方法也可以重写，就没有强制性了
"""

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass=ABCMeta):

    def __init__(self, nick_name):
        self._nickname = nick_name

    @abstractmethod
    def make_voice(self):
        pass

class Dog(Pet):

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)

class Cat(Pet):

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)

def main():
    pets = [Dog('旺财'), Cat('泡芙'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()

if __name__ == '__main__':
    main()
