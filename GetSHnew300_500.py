# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 00:06:19 2020

@author: yongh

Next Step :
    分析楼盘的详细信息
    https://sh.fang.lianjia.com/loupan/p_jfcafsam/xiangqing/
    获取开盘信息（首页） 规划信息 配套信息（详情）
    规划信息
    
"""

import bs4,requests
import re
import csv

import codecs
from bs4 import BeautifulSoup


#Test : Get all items from page 1  Total 300 - 500

page = "https://sh.fang.lianjia.com/loupan/"
Tpage = "https://sh.fang.lianjia.com/loupan/bp300ep500pg"
xq = "xiangqing"

LP_name = []
CSV_headers = ["Name","Distric","Addr","Area","UnitP","TotalP"]

def getLPinfo(LPlist,url):

    #DICTtmp = {"Name": "", "Distric":"" ,"Addr":"", "Area":"", "UnitP":"", "TotalP":""}

    ht = requests.get(url)

    print("Web Page Reponse Code:",ht.status_code)
    bs1 = BeautifulSoup(ht.content,"lxml")
    lps = bs1.find_all(attrs={"class":"resblock-list post_ulog_exposure_scroll has-results"})
    

    for lp in lps:
        # Start Test Process
        
        test = lp.findChild().get_attribute_list("href")
        print("Test is :",test)
        web=page + test[0] +xq
        print(web)
        print("status is :",(requests.get(web)).status_code)
        
        #End Test Process
        
        DICTtmp = {"Name": "", "Distric":"" ,"Addr":"", "Area":"", "UnitP":"", "TotalP":""}
        #print("Found a new loupan\n")
        tmp=lp.findChild().findNextSibling()
        infos=tmp.findChild()   
        DICTtmp["Name"] = infos.a.get_text()
        #DICTtmp["Name"]  = '\ufeff' +"实验"
        #print("loupan Name: ",infos.a.get_text())
        #print("loupan name is :",DICTtmp["Name"])
        
        infos=infos.findNextSibling()
        DICTtmp["Distric"] = infos.span.get_text()         
        #print("loupan Distric: ",infos.span.get_text())
        #print("loupan District",DICTtmp["Distric"])
        DICTtmp["Addr"] = infos.a.get_text()
        #print("loupan Addr: ",infos.a.get_text())
        #print("loupan Addr:",DICTtmp["Addr"])
        infos=infos.findNextSibling().findNextSibling()
        DICTtmp["Area"] = infos.span.get_text()
        #print("loupan Area: ",infos.span.get_text())
        #print("loupan Area: ",DICTtmp["Area"])
        infos=infos.findNextSibling().findNextSibling().findNextSibling()
        DICTtmp["UnitP"] = infos.div.span.get_text()
        #print("loupan Single Price/m2: ",infos.div.span.get_text())
        #print("loupan Single Price/m2: ",DICTtmp["UnitP"])
        for tp in infos.findNext().fetchNextSiblings():
            DICTtmp["TotalP"] = tp.get_text()
            #print("loupan total Price: ",tp.get_text())
            #print("loupan total Price: ",DICTtmp["TotalP"])
        #DICTnew = DICTtmp
        
        LPlist.append(DICTtmp)
        del DICTtmp
        #print(LPlist)
        #del DICTnew
    

    return LPlist
    

def write2csv(LP,csvfile):
    with codecs.open(csvfile,'wb','utf_8_sig')as f:
        
        if f.writable():
            
            f_csv = csv.DictWriter(f,CSV_headers)
            f_csv.writeheader()
            
            f_csv.writerows(LP)
        else:
            print("The file is not writable, please close the open files")
        
    
        
            
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
    csvfile = 'test.csv'
    """
    LP = getLPinfo(LP_name,Tpage+'1')
    #print(LP)
    write2csv(LP,csvfile)
    #print("LP is :\n",LP)
    """
    #把楼盘信息写入文件
    for i in range(1):
        newpage = Tpage+str(i+1)
        
        LP = getLPinfo(LP_name,newpage)
        #write2csv(LP,csvfile)
    
    #生成
    #print("Get Loupan info :\n",LP)
    
    