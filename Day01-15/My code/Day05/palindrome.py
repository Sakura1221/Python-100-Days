"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数
"""

# num = input('请输入一个正整数：')
# a = [map(int,num)] # 生成列表
# if a == a[::-1]: # 列表反转
#     print(True)
# else:
#     print(False)

num = int(input('请输入一个正整数：'))
temp = num # num后续有用，不可直接操作，复制一份
num2 = 0
while temp:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print(True)
else:
    print(False)

### 取数字通用算法
# list = []
# while(num):
#     list.append(num % 10)
#     num // 10

### 数字组成数通用算法
# list = [1,2,3]
# num = 0
# for i in range(len(list)):
#     num *= 10
#     num += list[i]
