# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 14:03:05 2019

@author: yongh
"""

import numpy as np


def arrayop(arr1,arr2,ops):
    if ops=='+':
        result=np.add(arr1,arr2)
    elif ops=='-':
        result=arr1-arr2
    elif ops=='>':
        result=np.maximum(arr1,arr2)
    elif ops=='<':
        result=np.minimum(arr1,arr2)
    else:
        try:
            print('Warn!')
        except ValueError:
            print('error!!!input wrong parameter')
            
    return result

if __name__ == '__main__':
    arr3=np.array([4,5,6])
    arr4=np.array([1,2,3])
    arr5=arrayop(arr3,arr4,'<')
    print(arr5)
            
    