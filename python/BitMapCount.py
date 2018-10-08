#!/usr/bin/env python
#coding:utf-8
"""
  Author:   chenzejiang--<>
  Purpose: 
  Created: 2017/9/28
"""

import unittest


import os, sys, array

CWD = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(CWD, '../..'))


def power2n(x):
    '''
    求比x大且是2的n次方的数
    '''
    for i in (1, 2, 4, 8, 16, 32):  # 支持到64位int型，加上64则可以支持到128等等
        x |= x >> i
    # print(x + 1)
    return x + 1


class BitMap():
    def __init__(self):
        self.K = 5
        self.BIT_NUM = 1 << self.K
        self.BIT_TYPE = 'I'  # 32位unsighed int存储位。note:可能8位char存储对小数据更好一丢丢
        self.shift = 0  # 如果数组中有<0的数，则所有数都要减去最小的那个负数

    def fit(self, x):
        '''
        将数据读入bitmap中存储
        '''
        MIN_NUM = min(x)
        if MIN_NUM < 0:
            self.shift = -MIN_NUM  # 如果数组中有<0的数，则所有数都要减去最小的那个负数
            x = [i + self.shift for i in x]
        else:
            self.shift = 0
        MAX_NUM = max(x)

        num_int = power2n(MAX_NUM) >> self.K
        num_int = num_int if num_int > 0 else 1  # 至少应该有一个数组
        # print(num_int)
        self.a = array.array(self.BIT_TYPE, [0] * num_int)
        for xi in x:
            self.set(xi)

    def set(self, xi, value=1):
        '''
        设置数xi在数组a中对应元素对应的位为1
        '''
        array_ix = xi >> self.K  # 数组的元素位置(从0开始)
        bit_ix = xi & ((1 << self.K) - 1)  # 数组元素中的bit位置(从0开始)，取模
        if value == 1:
            self.a[array_ix] |= 1 << bit_ix  # 对应的第bit_ix位置的2**bit_ix置1
        else:
            self.a[array_ix] &= ~((1 << bit_ix))  # 对应的第bit_ix位置的2**bit_ix置0

    def show_array(self):
        for ai in self.a:
            print('{:032b}'.format(ai))  # bin(ai)

    def search(self, xi):
        '''
        bitmap查找
        '''
        if self.shift != 0:
            xi += self.shift

        array_ix = xi >> self.K
        bit_ix = xi & ((1 << self.K) - 1)
        if (self.a[array_ix] & (1 << bit_ix)):
            flag = True
        else:
            flag = False
        return flag

    def sort(self):
        '''
        bitmap排序
        '''
        sorted_x = []
        for array_ix, ai in enumerate(self.a):
            for bit_ix in range(self.BIT_NUM):
                # 首先得到该第j位的掩码（0x01＜＜j），将内存区中的,位和此掩码作与操作。最后判断掩码是否和处理后的结果相同
                if (ai & (1 << bit_ix)) == (1 << bit_ix):
                    sorted_x.append(self.BIT_NUM * array_ix + bit_ix)
        # print(sorted_x)
        if self.shift != 0:
            sorted_x = [i - self.shift for i in sorted_x]
        return sorted_x


def test():
    bm = BitMap()
    #bm.fit([-3, -44, 7, 2, 5, 3, 32])
    bm.fit([33, 44, 7, 2, 5, 3, 32])
    bm.show_array()
    print(bm.search(7))
    print(bm.search(6))
    print(bm.sort())


test()





if __name__ == '__main__':
    unittest.main()
