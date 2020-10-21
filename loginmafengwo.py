# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import requests
import http.cookiejar as cookielib
websession=requests.session()
websession.cookies=cookielib.LWPCookieJar(filename="session.txt")

#useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
header = {
        #"Origin":"https://passport.mafengwo.cn",
        "Referer":"https://passport.mafengwo.cn/",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"       
        }
posturl="https://passport.mafengwo.cn/login/"
#posturl="http://www.mafengwo.cn/msg/entry/friends?msgtype=0&offset=0"
postdata={
            "passport": "13006179753",
            "password": "yuyonghao123"           
            }

def loginweb(posturl,postdata):
    print("Start login web")
    responseRes = requests.post(posturl, data = postdata, headers = header,verify=False)
    print(f"statusCode = {responseRes.status_code}")
#    print(f"text = {responseRes.text}")
    websession.cookies.save()
    return responseRes

if __name__ == '__main__':

    websession.cookies.load()
    myres=loginweb(posturl,postdata)    
    resp=websession.get("http://www.mafengwo.cn/plan/fav_type.php",headers = header, allow_redirects = True,verify=False)
    content=myres.text
    print("resp status")
    print(resp.status_code)
    with open('C:/Users/yuy15/Desktop/My Patch/PSP464/cookiemfw.txt','w',encoding='UTF-8') as s:
        s.truncate()
        s.writelines(content)    
        
        