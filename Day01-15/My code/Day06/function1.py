"""
函数的定义和使用 - 计算组合数C(7,3)
将求阶乘的功能以及求组合数的功能封装成函数
"""

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def combination(m, n):
    result = factorial(m) // factorial(n) //factorial(m - n) # 这里要用整除，保持int类型
    return result

if __name__ == '__main__':
    print(combination(7,3))