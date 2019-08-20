class Test:

    def __init__(self, foo1, foo2):
        self.__foo1 = foo1 # 私有变量，只有类内部可调用
        self._foo2 = foo2 # 保护变量

    def __bar1(self): # 私有方法
        print(self.__foo1)
        print('__bar1')

    def _bar2(self): # 保护方法
        print(self._foo2)
        print('_bar2')


def main():
    test = Test('hello1', 'hello2')
    test._Test__bar1() # 强制调用__bar1
    test._bar2() # 强制调用bar2
    print(test._Test__foo1) # 强制访问__foo1
    print(test._foo2) # 强制访问_foo2


if __name__ == "__main__":
    main()
