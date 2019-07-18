# -*- coding: utf-8 -*-
"""
Created on Wed May  8 20:53:39 2019

@author: yongh
"""

import re
import requests


def dowmloadPic(html, keyword,count):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
#    count=12
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    
    for each in pic_url:
#        print(each)
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        dir = 'D:/python/picture_of_beauty/' + keyword + '_' + str(i) + '.jpg'
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1
        count=count-1
        if(count==0):
            fp.close()
            break
            
            #exit(1)


if __name__ == '__main__':
    word = input("Input key word: ")
    countpic = int(input("Input picture amount: "))
 #   url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word='+word
    print(url)
    result = requests.get(url,timeout=10)
    print(result)
    dowmloadPic(result.text, word,countpic)