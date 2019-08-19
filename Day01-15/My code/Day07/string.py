def main():
    str1 = 'hello, world!'
    # 通过len函数计算字符串的长度
    print(len(str1))
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())
    # 获得字符串变大写后的拷贝
    print(str1.upper())
    # 从字符串中查找子串所在位置
    print(str1.find('llo'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('he'))
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('ld'))
    # 将字符串以指定的宽度居中并在两侧填充指定的字符
    print(str1.center(50,'*'))
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符
    print(str1.rjust(50,' '))
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[1])
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5]) # c12
    print(str2[2::2]) # c246
    print(str2[:7:2]) # ac24
    print(str2[::]) # abc123456
    print(str2[::2]) # ac246
    print(str2[::-1]) # 654321cba
    print(str2[-3:]) # 456
    # 检查字符串是否由数字构成
    print(str2.isdigit())
    # 检查字符串是否以字母构成
    print(str2.isalpha())
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())
    str3 = '  jackfrued@126.com '
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip()) # 默认为空格
    str4 = 'Hong Kong'
    # 以某些字符分割字符串，返回列表
    print(str4.split(' '))


if __name__ == '__main__':
    main()
