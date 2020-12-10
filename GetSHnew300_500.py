# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:06:19 2020

@author: yongh
"""

import bs4,requests
import re
from bs4 import BeautifulSoup

#Test : Get all items from page 1  Total 300 - 500

Tpage = "https://sh.fang.lianjia.com/loupan/bp300ep500pg"
LP_name = []

def getLPinfo(LPlist,url):
    #LPlist = []
    LPtmp = []
    LPinfo = []
    index = 0
    ht = requests.get(url)

    print("Web Page Reponse Code:",ht.status_code)
    bs1 = BeautifulSoup(ht.content,"lxml")
    lps = bs1.find_all(attrs={"class":"resblock-list post_ulog_exposure_scroll has-results"})
    

    for lp in lps:
        print("Found a new loupan\n")
        tmp=lp.findChild().findNextSibling()
        infos=tmp.findChild()
        print("loupan Name: ",infos.a.get_text())
        infos=infos.findNextSibling()        
        print("loupan Distric: ",infos.span.get_text())
        print("loupan Addr: ",infos.a.get_text())
        infos=infos.findNextSibling().findNextSibling()
        print("loupan Area: ",infos.span.get_text())
        infos=infos.findNextSibling().findNextSibling().findNextSibling()
        print("loupan Single Price/m2: ",infos.div.span.get_text())
        for tp in infos.findNext().fetchNextSiblings():
            print("loupan total Price: ",tp.get_text())

    return LPlist
    

    
        #print(LPinfo)

    #print("The new LPinfo is :",LPinfo)
        #print("LP info is :",LPtmp)
        
    return LPtmp
            
class loupan:
    name=""
    price=""
    total=""
    def __init__(self,n,p,t):
        self.name = n
        self.price = p
        self.total = t
    def getinfo(self):
        print("The info of loupan is :",self.name,self.price)
        

if __name__=="__main__":
    #LP = getLPinfo(LP_name,Tpage+'1')
    
    for i in range(30):
        newpage = Tpage+str(i+1)
        print(newpage)
        LP = getLPinfo(LP_name,newpage)
    #print("Get Loupan info :\n",LP)
    
