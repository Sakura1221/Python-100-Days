"""
格式化输出
"""

a = eval(input('请输入一个整数：'))
b = eval(input('请输入另一个整数：'))

print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %.5f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b)) # 需要输入两个%
print('%d ** %d = %.5e' % (a, b, a ** b))
print('a除以b的商和余数为: {2} 和 {3}'.format(a, b, a // b, a % b))