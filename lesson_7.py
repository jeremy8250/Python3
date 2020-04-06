# 练习1：在屏幕上显示跑马灯文字。
import os
from time import sleep


def light():
    content = "上海欢迎您......"
    while True:
        os.system('cls')
        print(content)
        sleep(0.1)
        content = content[1:] + content[0]


# 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random


def captcha(code_length=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    all_chars_len = len(all_chars) - 1
    code = ''
    for i in range(code_length):
        index = random.randint(0, all_chars_len)
        code = code + all_chars[index]
    return code


# 练习3：设计一个函数返回给定文件名的后缀名。
def get_ext():
    while True:
        filename = input("请输入文件名:")
        if '.' in filename:
            ext = filename.split('.')[-1]
            print("文件后缀为:%s" % ext)
        else:
            print("文件没有后缀名")

# 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值。



# 计算指定的年月日是这一年的第几天。