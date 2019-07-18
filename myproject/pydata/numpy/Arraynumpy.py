# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 10:15:03 2019

@author: yongh
"""

import numpy as np

"""
#1D
array1=np.array([3,5,7,9])
#2D
array2=np.array(((1,3,5),(2,4,6)))

print(array1)
print(array2)

"""
#testinfo = np.genfromtxt(fname=r'C:\Users\yongh\Desktop\py_data\test.txt',delimiter='\t',skip_header=1,dtype='str')

"""
print(type(testinfo))
print(testinfo.ndim)
print(testinfo.shape)
print(testinfo.size)
print(testinfo.dtype)
print(testinfo)

"""
arr3=np.array([[1,3,5],[2,4,6],[7,8,9],[1,2,3]])
arr4=np.array([1,2,3])
arr5=np.array([[5],[10],[15],[20]])

print(arr3.shape)
print('reshape\n',arr3.reshape(2,6))
print('resize\n',arr3.resize(2,6))
print('resize result\n',arr3)

#nD -> (n-1)D
array3=np.array([[1,3,5],[2,4,6],[7,8,9],[1,2,3]])
print(array3)
array31=array3.flatten()[0]=2000
print('flatten\n',array3)
print('arrayflatten\n',array31)
array3.ravel()[1]=1000
print('ravel:\n',array3)
array3.reshape(-1)[9]=3000
print('reshape\n',array3)

# Array1 & Array N
arr6=np.array([[1,3,5],[2,4,6],[7,8,9],[1,2,3]])
print('step1\n',arr6)
print('step2\n',np.vstack([arr6,arr4]))
print('step3\n',np.row_stack([arr6,arr4]))
print('step4\n',arr6)
print('step5\n',np.hstack([arr6,arr5]))















