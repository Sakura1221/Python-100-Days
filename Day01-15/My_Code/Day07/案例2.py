"""
《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，
他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。
由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
"""

def main():
    persons = [True] * 30 # 因为模拟的过程是在剔除，故初始化均为True
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]: # 被剔除不加1
            number += 1
            if number == 9:
                persons[index] =False # 被剔除了
                counter += 1 # 剔除人数加1
                number = 0 # 重新开始计数
        index += 1 # 轮到下一个人
        index %= 30 # 一个循环30人
    for person in persons:
        print('基' if person else '非', end=' ')

if __name__ == '__main__':
    main()