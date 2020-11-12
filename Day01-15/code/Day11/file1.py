
# _*_ coding: utf8 _*_
"""
从文本文件中读取数据

Version: 0.1
Author: 骆昊
Date: 2018-03-13
"""

import time


def main():
    path = r'D:\WorkSpace\GitHub\Python-100-Days\Day01-15\code\Day11\致橡树.txt'

    # 一次性读取整个文件内容
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())

    # 通过for-in循环逐行读取
    with open(path, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.25)
    print()

    # 读取文件按行读取到列表中
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)
    

if __name__ == '__main__':
    main()
