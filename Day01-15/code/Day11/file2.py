"""
读取圆周率文件判断其中是否包含自己的生日

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

birth = input('请输入你的生日: ')
path = r'D:\WorkSpace\GitHub\Python-100-Days\Day01-15\code\Day11\pi_million_digits.txt'
with open(path) as f:
    lines = f.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()
    if birth in pi_string:
        print('Bingo!!!')
