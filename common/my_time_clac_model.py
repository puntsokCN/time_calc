#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author   : pingcuo
# Blog     : 
# Date     : 2019-08-21
# Name     : time_clac
# Software : vscode
# Note     : 
# 导入模块

import math
from .my_math_model import my_round

# 60进制转10进制
def to_dec(num) :
    minute = math.floor(num)
    second = (num - minute) * 100
    dec_time = minute + second / 60
    return dec_time


# 10进制转60进制
def to_sixty(num) : 
    minute = math.floor(num)
    second = ((num - minute) * 60) / 100
    sixty_time = minute + second
    return sixty_time

# 时间加减
def sum_sixty(num1, num2) :
    '''
    参数： 输入两个计算待计算的60进制的浮点数
    返回： 返回其其和值
    '''
    sum_sixty = float(my_round(to_sixty(to_dec(num1) + to_dec(num2))))
    return sum_sixty

# 时间减法
def subtract_sixty(num1, num2):
    '''
    参数： 输入两个计算待计算的60进制的浮点数
    返回： 差值
    '''
    subtract_sixty = float(my_round(to_sixty(to_dec(num1) - to_dec(num2))))
    return  subtract_sixty

# 入口函数
if __name__ == '__main__':
    pass