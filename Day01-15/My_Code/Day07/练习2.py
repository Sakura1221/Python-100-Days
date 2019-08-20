"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
"""
import random

def generate_code(code_len):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(code_len):
        index = random.randint(0, len(all_chars) - 1)
        code += all_chars[index]
    return code

