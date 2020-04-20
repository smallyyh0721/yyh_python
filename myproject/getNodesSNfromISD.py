# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import re
import time

html_addr="http://isd-logs.gemops.mfgops.com/logs/chassis_by_serial/"

url_chassis='http://isd-logs.gemops.mfgops.com/logs/chassis_by_serial/FNM00162300121/'
#url_chassis='http://isd-logs.gemops.mfgops.com/logs/chassis_by_serial/FNM00162400356/'
url_latest='http://isd-logs.gemops.mfgops.com/logs/chassis_by_serial/FNM00162300121/FNM00162300121_2020-01-30T09-00-15_cumulus/'
url_json='http://isd-logs.gemops.mfgops.com/logs/chassis_by_serial/FNM00162300121/FNM00162300121_2020-01-30T09-00-15_cumulus/TestContentFiles%5casbuilt_CHASSIS_FNM00162300121.json'


def getchassisNO(html_addr):
    
    html= requests.get(html_addr)
    print("I got reponse from html :",html)
#html='<tr><td valign="top"><img src="/icons/folder.gif" alt="[DIR]"></td><td><a href="FNM00162300121/">FNM00162300121/</a></td><td align="right">23-Mar-2020 23:07  </td><td align="right">  - </td><td>&nbsp;</td></tr>'
    soup = BeautifulSoup(html.text, 'html.parser')
    print("I have made soup")
    f=open('C:/Users/yuy15/Desktop/My Patch/chassisNO.txt','w') 
    f.truncate()
    print("I opened a file")
    for chassis in soup.find_all('a'):
#    print(chassis['href'])
        chassis_no=chassis['href']
        test_url='http://isd-logs.gemops.mfgops.com/logs/chassis_by_serial/'+chassis_no
        if requests.get(test_url):
            f.write(chassis_no+'\n')
        else:
            print("This is a invalid website")

    f.close()
    print("I have finished my job")
    

#get latest record of chassis
def getlatestrecord(url_chassis):
    record_count=0
    list_record=[""]
#    print(type(list_record))
#  Move to try/except
    try :
        html=requests.get(url_chassis)
        soup = BeautifulSoup(html.text, 'html.parser')
        for record in soup.find_all('a'):
            record_count=record_count+1
            list_record.append(record['href'])
#        print(record['href'])
#    print(list_record[record_count-1])
        latest_record=list_record[record_count-1]
        return latest_record
    except Exception:
        print("Something wrong with request:",url_chassis)
        return None
        
#get  chassis Json
def getchassisJson(url_latest,chassisNo):    
    try :
        html=requests.get(url_latest)
        rule='href=".*asbuilt_CHASSIS.*'+chassisNo+'.json"'         
        json_file=re.findall(rule,html.text)[0]
        json_name_temp=json_file[5:]
        json_name=json_name_temp.replace('\"','') 
        return json_name
    except Exception:
        print("Something wrong with json file:",chassisNo)
        return None
          
    

def getjson(url_json):
    try:
        res=requests.get(url_json)
        if res.ok:
#            print("get json ok")
            return res.json()
        else:
            print('not ok')
            return False
    except Exception as e:
        print('Error here:\t',e)
        
def parsejson(json_file,file):
#    print("Begin to parse Json file")
    if json_file is not None:
        new_list=json_file.get('ChassisTLA')
        if not new_list:
            return False
#        print(type(new_list['_NODE_01']))
#        print(new_list['_NODE_01']['NODE_INFO']['serial'])
        for items in new_list:
            if 'NODE_INFO' in new_list[items]:
#                print("Hi, I find node info: ")
                node_info= new_list[items]['NODE_INFO']
                print(node_info['serial'])
#                node_sn_list.append(node_info['serial'])
#                print("The process is running")
                file.write(node_info['serial'])
#                savefile.write('\n')
        return 'Success get Node sn'
    else:
        print("Something wrong with Json file")
        
if __name__ == '__main__':
    savefile=open('C:/Users/yuy15/Desktop/My Patch/nodeSN.txt','w')
    savefile.truncate()
    begin_str='Begin test on '+time.ctime()
    savefile.write(begin_str)
    savefile.write('\n')
    node_SN_list=[""]
    
    with open('C:/Users/yuy15/Desktop/My Patch/chassisNumber.txt','rb') as f:
        files = f.readlines()
        for i in files:
            new_i=(str(i,encoding = "utf-8")).replace('\r','')
            chassisNo=new_i.replace('\n','')
#            print ("Chassis No is : \n",chassisNo)
            #get url_chassis
            chassis_url=html_addr+chassisNo
#            print(requests.get(chassis_url))
            #Grep node SN
            #Latest record of this chassis
            latest_record=getlatestrecord(chassis_url)
            if latest_record is not None:
            #Generate new url :url_latest
                chassis_record_latest=chassis_url+latest_record
#            print(chassis_record_latest)
#            print("test connection: \n",requests.get(chassis_record_latest))
            #find Json file  !!!!!!!!!!
#            print("ChassisNo before:",chassisNo)
                chassisNoformat=chassisNo.replace('/','')
#            print("ChassisNo after:",chassisNoformat)
                json_name=getchassisJson(chassis_record_latest,chassisNoformat)
            else:
                json_name=None
                
            if json_name==None:
                print("Someting wrong with Json name")
            else:
            #parse Json
                json_url=chassis_record_latest+json_name
                json_file=getjson(json_url)
                node_SN_list=parsejson(json_file,savefile)
    #print(node_SN_list)            
    savefile.close()
    print("The process is finished")

            
        
#    getchassisNO(html_addr)  #get all chassis info
    #read chassis from files and search node sn one by one
    
    
    
"""
lastest_record=getlatestrecord(url_chassis)
    json_name=getchassisJson(url_latest)
#    print(url_chassis+lastest_record+json_name)
    json_url=url_chassis+lastest_record+json_name
    json_file=getjson(json_url)
    parsejson(json_file)
    
    
    
print(len(files))
        print(type(files))
        print(files[22])
        print(str(files[22],encoding = "utf-8"))
        url=html_addr+str(files[22],encoding = "utf-8")
        print(url)
        url1= 'http://isd-logs.gemops.mfgops.com/logs/chassis_by_serial/FNM00170206305/'
        print(url1)
        print(requests.get(url))
        print(requests.get(url1))
        if url==url1:
            print("They're the same")
        else:
            print("They're not the same")
        
        
        print(url.encode())
        print(url1.encode())
        
        new_url=url.replace('\r','')
        
        print(new_url.encode())
        
        final_url=new_url.replace('\n','')
        print(final_url.encode())
        print(requests.get(final_url))    
"""
    
    