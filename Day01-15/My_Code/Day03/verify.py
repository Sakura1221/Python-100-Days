"""
用户身份验证
"""

database = {'张三':'123', '李四':'456'}

user = input('请输入用户名：')
if user in database:
    password = input('请输入密码：')
    if password == database[user]:
        print('登录成功')
    else:
        print('密码错误')
else:
    print('用户不存在')