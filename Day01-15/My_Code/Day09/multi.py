"""
多重继承
- 通过多重继承可以给一个类的对象具备多方面的能力
- 这样在设计类的时候可以避免设计太多层次的复杂的继承关系
"""

# Father类
class Father(object):

    # 初始化，传参name
    def __init__(self, name):
        self._name = name

    # gamble方法
    def gamble(self):
        print('%s正在打麻将' % self._name)

    # eat方法
    def eat(self):
        print('%s正在大吃大喝' % self._name)


# Monk类
class Monk(object):

    # 初始化方法，传参name
    def __init__(self, name):
        self._name = name

    # eat方法
    def eat(self):
        print('%s正在吃斋' % self._name)

    # chant方法
    def chant(self):
        print('%s正在念经' % self._name)



# Musician方法
class Musician(object):

    # 初始化方法，传参name
    def __init__(self, name):
        self._name = name

    # eat方法
    def eat(self):
        print('%s正在细嚼慢咽' % self._name)

    # play_piano方法
    def play_piano(self):
        print('%s正在弹钢琴' % self._name)



# 多继承的方法出现冲突，方法与继承顺序相关，选择最先继承的类的方法
# class Son(Monk, Father, Musician):
# class Son(Musician, Father, Monk):


class Son(Father, Monk, Musician):

    # 多继承初始化，同时初始化所有父类，随后即可调用
    def __init__(self, name):

        # 调用父类构造器初始化一定要加self参数，初始化顺序无影响
        Father.__init__(self, name)
        Monk.__init__(self, name)
        Musician.__init__(self, name)

son = Son('王大锤')
son.gamble()
# 调用继承自Father的eat方法
son.eat()
son.chant()
son.play_piano()
