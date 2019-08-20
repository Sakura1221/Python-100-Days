"""
面向对象版本的猜数字游戏
增加答案，次数，提醒属性
增加重置方法
"""

from random import randint

class GuessMachine(object):

    def __init__(self, times):
        self._answer = None
        self._counter = None
        self._hint = None
        self._times = times

    def reset(self):
        self._answer = randint(1, 100)
        self._counter = 0
        self._hint = None

    def guess(self, your_answer):
        print('你还有%d次机会' % (self._times - self._counter))
        self._counter += 1
        if your_answer > self._answer:
            self._hint = '猜大了'
        elif your_answer < self._answer:
            self._hint = '猜小了'
        else:
            self._hint = '猜对了'
            return True # 返回值用来提供程序运行标志
        return False

    @property
    def counter(self):
        return self._counter  # 装饰器配合保护变量使用

    @property
    def hint(self):
        return self._hint

    @property
    def times(self):
        return self._times

    @property
    def answer(self):
        return self._answer

if __name__ == '__main__':
    gm = GuessMachine(7)
    play_again = True
    while play_again:
        you_win = False
        gm.reset()
        while not you_win:
            your_answer = int(input('请猜一个1到100的整数：'))
            you_win = gm.guess(your_answer)
            print(gm.hint)
            if gm.counter > gm.times:
                print('机会用尽, 答案是 %d' % gm.answer)
                break
        play_again = input('要再玩一局吗？ yes or no \n') == 'yes'
