"""
英寸和厘米转换
"""

value = float(input('请输入数值:'))
unit = input('请输入单位:')

if unit == '英寸' or unit == 'in':
    print('%.2fin = %.2fcm' % (value, 2.54 * value))
elif unit == '厘米' or unit == 'cm':
    print('%.2fcm = %.2fin' % (value, value / 2.54))
else:
    print('单位输入错误')