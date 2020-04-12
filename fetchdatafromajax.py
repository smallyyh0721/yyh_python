# -*- coding: utf-8 -*-

# Fetch data via ajax
#target site :
#https://hotels.ctrip.com/Domestic/tool/AjaxHotelFaqLoad.aspx?hotelid=346412&currentPage=2
import requests
import json
page_id=1
#from pprint import pprint
url ="https://hotels.ctrip.com/Domestic/tool/AjaxHotelFaqLoad.aspx?hotelid=346412&currentPage="
page_id=input("please input a page ID: ")
target_ur=url+page_id
print(target_ur)

res=requests.get(target_ur)
js1=json.loads(res.text)
asklist =dict(js1).get('AskList')
print(len(asklist))
for one in asklist:
#    print(one)
    print("Asking : ",one['AskContentTitle'])
    print("Answer : ",one['ReplyList'][0]['ReplyContentTitle'])
    
#print(asklist[0])