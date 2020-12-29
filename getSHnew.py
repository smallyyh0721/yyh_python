# -*- coding: utf-8 -*-

#获取安居客上海市全部新盘信息

#https://sh.fang.anjuke.com/loupan/all/
#https://sh.fang.anjuke.com/loupan/all/p2/
#https://sh.fang.lianjia.com/loupan/pg2/
#https://shanghai.anjuke.com/sale/p2/

"""
Next Step :
    分析楼盘的详细信息
    https://sh.fang.lianjia.com/loupan/p_jfcafsam/xiangqing/
    获取开盘信息（首页） 规划信息 配套信息（详情）
    规划信息
"""
import bs4,requests
import re
from bs4 import BeautifulSoup

#Test : Get all items from page 1  Total 300 - 500

Tpage = "https://sh.fang.lianjia.com/loupan/bp300ep500pg1"
Kaipan = "https://sh.fang.lianjia.com/loupan/p_gmssysblcwa/"
LP_name = []

#def getLPinfo()  Return a list of LP and Input a web
def getLPinfo(LPlist,url):
    LPlist = []
    LPtmp = []
    LPinfo = []
    index = 0
    ht = requests.get(url)

    print("Web Page Reponse Code:",ht.status_code)
    bs1 = BeautifulSoup(ht.content,"lxml")
    lp = bs1.find(attrs={"class":"resblock-list post_ulog_exposure_scroll has-results"})
    test = lp.a['href']
    #print(test)
        #print(LPinfo)

    #print("The new LPinfo is :",LPinfo)
        #print("LP info is :",LPtmp)
        
    return test
      
# Get latest kaipan date
def getkaipan(url):
    ht = requests.get(url)
    bs1 = BeautifulSoup(ht.content,"lxml")
    OpenDate = (bs1.find(attrs={"class":"open-date"})).findChild().findNextSibling() 
    return OpenDate.get_text()

# Get Configuration data
def getconf(url):
    ht = requests.get(url)
    bs1 = BeautifulSoup(ht.content,"lxml")
    
    
      
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
    #LP = getLPinfo(LP_name,Tpage)
    #print("Get Loupan info :\n",LP)
    LP_kP = getkaipan(Kaipan)
    print(LP_kP)

    
    
    





