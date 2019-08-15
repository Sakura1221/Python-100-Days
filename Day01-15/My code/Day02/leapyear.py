"""
输入年份，如果是闰年输出True，否则输出False
闰年的条件有两条，被4整除且不被100整除，或者被400整除
"""
year = eval(input('请输入年份：'))
# 使用\或者()换行
is_leapyear = (year % 4 == 0 and year % 100 != 0 or
               year % 400 == 0)
print(is_leapyear)