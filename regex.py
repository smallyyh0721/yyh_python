# -*- coding: utf-8 -*-

"""
Created on Mon Feb 25 15:20:27 2019

@author: yuy15

Check RFD in readme

"""
import re
import requests

def retwostr(stra,strb):
    return re.match(stra,strb)
    
    
    
if __name__ == '__main__':
    stringa='.b'
    stringb='adbh7jh'
    result=retwostr(stringa,stringb)
    print(result)
    print(re.search('[a-z]\d','adb7h 85'))
    print(re.findall('\d','adb7h 85'))
    print(pic_url)