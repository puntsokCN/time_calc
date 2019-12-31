#! /usr/bin/env python3
# -*- coding:utf-8 -*-


def my_round(value, decDigits=2):
    '''
    由于内置round精确度问题，自建四舍五入函数
    value： 传入的待处理数字
    decDigits： 精确到小数点的位数，默认为2位
    返回： 四舍五入后的数字
    '''
    result = str(value).strip()
    if result != '':
        zeroCount = decDigits
        indexDec = result.find('.')
        if indexDec > 0:
            zeroCount = len(result[indexDec + 1:])
            if zeroCount > decDigits:
                if int(result[indexDec + decDigits + 1]) > 4:

                    result = str(value + pow(10,decDigits * -1))

                #存在进位的可能，小数点会移位
                indexDec = result.find('.')
                result = result[:indexDec + decDigits + 1]
                zeroCount = 0
            else:
                zeroCount = decDigits - zeroCount
        else:
            result += '.'
        for i in range(zeroCount):
            result += '0'
    return result

# 入口函数
if __name__ == '__main__':
    pass