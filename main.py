#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author   : pingcuo
# Blog     : 
# Date     : 2019-08-21
# Name     : time_clac
# Software : vscode
# Note     : 
# 导入模块

from common import my_time_clac_model
import sys, os

# #重启程序
# def restart_program():
#   python = sys.executable
#   os.execl(python, python, * sys.argv)

# 输入第一个数据
def input_num1() :
    while True:
        try:
            num1 = input('请输入第一个数据：>>>')
            if num1 == 'restart' :
                os.system('cls')        # 执行cls命令清空Python控制台
                main(-1)
            else:
                num1 = float(num1)
            break
        except ValueError:
            print('***抱歉只能输入数字!!! 请重新输入!***')
        else :
            input_num1()
            
    return num1

# # 输入第二个数据
def input_num2() :
    while True:
        try:
            num2 = input('请输入下一个数据：>>>')
            if num2 == 'restart' :
                os.system('cls')        # 执行cls命令清空Python控制台
                main(-1)
            else:
                 num2 = float(num2)
            break
        except ValueError:
            print('***抱歉只能输入数字!!! 请重新输入!***')
        else :
            input_num2()
    return num2

#  输入数学符号
def clac_symbol():
    while True:
        try:
            clac = input("请按需输入  '+'  或  '-'：>>> ")
            if clac  == 'restart' :
                os.system('cls')        # 执行cls命令清空Python控制台
                main(-1)
            else:
                 clac = clac
            break
        except ValueError:
            print("*** 抱歉只接受‘+’或‘-’作为运算符！*** ")
        else:
            clac_symbol()
    return  clac

# 主函数
def main(lastsum) :   # 参数用于判断是否第一次输入
    # 输入处理
    if lastsum < 0 :
        num1 = input_num1()
    else :
        num1 = lastsum
    num2 = input_num2()
    clac = clac_symbol()
    # 计算
    if clac == '+' :
        sum = my_time_clac_model.sum_sixty(num1, num2)
    elif clac == '-' :
        sum = my_time_clac_model.subtract_sixty(num1, num2)

    print('#总共时长： ', sum, '\n')
    main(sum)  # 迭代主函数，以继续计算

# 入口函数
if __name__ == '__main__':
    print(' '*34 + '欢迎使用时长计算器' + ' '*34 + '\n')
    print(' '*32 + '1.请以 分钟.秒 的形式输入' + ' '*33)
    print(' '*32 + '2.输入 restart 可实现程序重启' + ' '*31 + '\n')
    print('-'*80)
    # 执行主函数
    main(-1)  # 传小于零的参数，以通知首次计算 