# -*- coding: utf-8 -*-

import requests
import time
import json
import os

#website
raw_url='https://www.bilibili.com/index/recommend.json'

headers ={
        'Host':'www.bilibili.com',
        'X-Requested-With':'XMLHttpRequest',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'   
        }

def saveimage(url):
    dir = 'C:/Users/yuy15/Desktop/Training/Python/pic/'
#    print(url)
    filename=url.lstrip('http://').replace('.','').replace('/','').rstrip('jpg')+'.jpg'
#    print(filename)
    print(url)
    try:
        res=requests.get(url)
        print(res)
        if res.ok:
            print('hi Im here')
            img=res.content
            if not os.path.exists(filename):
                print('im here')
                with open(dir+filename,'wb') as f:
                    f.write(img)
    except Exception:
        print('fail to load picture')
        
        
def get_json():
    try:
        res=requests.get(raw_url,headers=headers)
        print(headers)
        if res.ok:
            return res.json()
        else:
            print('not ok')
            return False
    except Exception as e:
        print('Error here:\t',e)
        
        
def json_parser(json):
    if json is not None:
        new_list=json.get('list')
        if not new_list:
            return False
        for new_item in new_list:
            pic_url=new_item.get('pic')
#            print(pic_url)
            yield pic_url
            
def worker():
    raw_json=get_json()
#    print(raw_json)
    urls=json_parser(raw_json)
#    print(urls)
    for url in urls:
        saveimage(url)
        
if __name__=='__main__':
    worker()
        
        
        
        
        
        
        