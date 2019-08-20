"""
计算指定的年月日是这一年的第几天
"""

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 \
            and year % 400 == 0:
        return True
    else:
        return False

def which_day(year, month, day):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]
    total = 0
    for index in range(month - 1):
        if is_leap_year(year):
            total += days_of_month[1][index]
        else:
            total += days_of_month[0][index]
    print(total + day)

which_day(2019,8,20)