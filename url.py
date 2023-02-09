import os
import subprocess
import time
import json
import requests
import random
import asyncio
import threading
from subprocess import Popen, PIPE, STDOUT
import concurrent.futures
from tqdm import tqdm

proxies=['http://jtsbbs:9N5cinQezk@185.191.144.94:50100','http://jtsbbs:9N5cinQezk@185.191.144.146:50100','http://jtsbbs:9N5cinQezk@185.191.144.146:50101','http://jtsbbs:9N5cinQezk@185.191.144.253:50100','http://jtsbbs:9N5cinQezk@185.191.144.253:50101','http://jtsbbs:9N5cinQezk@185.191.144.251:50100','http://jtsbbs:9N5cinQezk@185.191.144.251:50101','http://jtsbbs:9N5cinQezk@185.191.144.250:50100','http://jtsbbs:9N5cinQezk@185.191.144.250:50101','http://jtsbbs:9N5cinQezk@185.191.144.129:50100','http://jtsbbs:9N5cinQezk@185.191.144.129:50101','http://jtsbbs:9N5cinQezk@185.191.144.249:50100','http://jtsbbs:9N5cinQezk@185.191.144.249:50101','http://jtsbbs:9N5cinQezk@185.191.144.125:50100','http://jtsbbs:9N5cinQezk@185.191.144.125:50101','http://jtsbbs:9N5cinQezk@185.191.144.242:50100','http://jtsbbs:9N5cinQezk@185.191.144.242:50101','http://jtsbbs:9N5cinQezk@185.191.144.241:50100','http://jtsbbs:9N5cinQezk@185.191.144.241:50101','http://jtsbbs:9N5cinQezk@185.191.144.120:50100','http://jtsbbs:9N5cinQezk@185.191.144.120:50101','http://jtsbbs:9N5cinQezk@185.191.144.80:50100','http://jtsbbs:9N5cinQezk@185.191.144.80:50101','http://jtsbbs:9N5cinQezk@185.191.144.243:50100','http://jtsbbs:9N5cinQezk@185.191.144.243:50101','http://jtsbbs:9N5cinQezk@185.191.144.140:50100','http://jtsbbs:9N5cinQezk@185.191.144.140:50101','http://jtsbbs:9N5cinQezk@185.191.144.144:50100','http://jtsbbs:9N5cinQezk@185.191.144.144:50101','http://jtsbbs:9N5cinQezk@185.191.144.152:50100','http://jtsbbs:9N5cinQezk@185.191.144.152:50101','http://jtsbbs:9N5cinQezk@185.191.144.142:50100','http://jtsbbs:9N5cinQezk@185.191.144.142:50101','http://jtsbbs:9N5cinQezk@89.46.99.0:50100','http://jtsbbs:9N5cinQezk@89.46.99.0:50101','http://jtsbbs:9N5cinQezk@89.46.99.1:50100','http://jtsbbs:9N5cinQezk@89.46.99.1:50101','http://jtsbbs:9N5cinQezk@89.46.99.4:50100','http://jtsbbs:9N5cinQezk@89.46.99.4:50101','http://jtsbbs:9N5cinQezk@89.46.99.9:50100','http://jtsbbs:9N5cinQezk@89.46.99.9:50101','http://jtsbbs:9N5cinQezk@89.46.99.197:50100','http://jtsbbs:9N5cinQezk@89.46.99.197:50101','http://jtsbbs:9N5cinQezk@185.191.144.219:50100','http://jtsbbs:9N5cinQezk@185.191.144.219:50101','http://jtsbbs:9N5cinQezk@185.191.144.217:50100','http://jtsbbs:9N5cinQezk@185.191.144.217:50101','http://jtsbbs:9N5cinQezk@185.191.144.215:50100','http://jtsbbs:9N5cinQezk@185.191.144.215:50101','http://jtsbbs:9N5cinQezk@185.191.144.98:50100','http://jtsbbs:9N5cinQezk@185.191.144.98:50101','http://jtsbbs:9N5cinQezk@185.191.144.175:50100','http://jtsbbs:9N5cinQezk@185.191.144.175:50101','http://jtsbbs:9N5cinQezk@185.191.144.180:50100','http://jtsbbs:9N5cinQezk@185.191.144.180:50101','http://jtsbbs:9N5cinQezk@185.191.144.79:50100','http://jtsbbs:9N5cinQezk@185.191.144.79:50101','http://jtsbbs:9N5cinQezk@185.191.144.252:50100','http://jtsbbs:9N5cinQezk@185.191.144.252:50101','http://jtsbbs:9N5cinQezk@185.191.144.248:50100','http://jtsbbs:9N5cinQezk@185.191.144.248:50101','http://jtsbbs:9N5cinQezk@89.46.99.199:50100','http://jtsbbs:9N5cinQezk@89.46.99.199:50101','http://jtsbbs:9N5cinQezk@185.191.144.255:50100','http://jtsbbs:9N5cinQezk@185.191.144.255:50101','http://jtsbbs:9N5cinQezk@185.191.144.177:50100','http://jtsbbs:9N5cinQezk@185.191.144.177:50101','http://jtsbbs:9N5cinQezk@185.191.144.173:50100','http://jtsbbs:9N5cinQezk@185.191.144.173:50101','http://jtsbbs:9N5cinQezk@185.191.144.170:50100','http://jtsbbs:9N5cinQezk@185.191.144.170:50101','http://jtsbbs:9N5cinQezk@185.191.144.161:50100','http://jtsbbs:9N5cinQezk@185.191.144.161:50101','http://jtsbbs:9N5cinQezk@185.191.144.159:50100','http://jtsbbs:9N5cinQezk@185.191.144.159:50101','http://jtsbbs:9N5cinQezk@185.191.144.143:50100','http://jtsbbs:9N5cinQezk@185.191.144.143:50101','http://jtsbbs:9N5cinQezk@185.191.144.134:50100','http://jtsbbs:9N5cinQezk@185.191.144.134:50101','http://jtsbbs:9N5cinQezk@185.191.144.135:50100','http://jtsbbs:9N5cinQezk@185.191.144.135:50101','http://jtsbbs:9N5cinQezk@185.191.144.254:50100','http://jtsbbs:9N5cinQezk@185.191.144.254:50101','http://jtsbbs:9N5cinQezk@185.191.144.71:50100','http://jtsbbs:9N5cinQezk@185.191.144.71:50101','http://jtsbbs:9N5cinQezk@185.191.144.124:50100','http://jtsbbs:9N5cinQezk@185.191.144.124:50101','http://jtsbbs:9N5cinQezk@185.191.144.127:50100','http://jtsbbs:9N5cinQezk@185.191.144.127:50101','http://jtsbbs:9N5cinQezk@185.191.144.138:50100','http://jtsbbs:9N5cinQezk@185.191.144.138:50101','http://jtsbbs:9N5cinQezk@185.191.144.174:50100','http://jtsbbs:9N5cinQezk@185.191.144.174:50101','http://jtsbbs:9N5cinQezk@185.191.144.82:50100','http://jtsbbs:9N5cinQezk@185.191.144.82:50101','http://jtsbbs:9N5cinQezk@185.191.144.148:50100','http://jtsbbs:9N5cinQezk@185.191.144.148:50101','http://jtsbbs:9N5cinQezk@185.191.144.97:50100','http://jtsbbs:9N5cinQezk@185.191.144.97:50101']


def txt2list(fname): #функция чтения файла
    with open(fname, 'r', encoding="utf8") as f:
        return [line.strip() for line in f]
site_list = txt2list('list.txt')

urlsdbsm = []
urlsdbs = txt2list('url.txt')
#urlsdbs = txt2list('fr.txt')  """
#urlsdbs = txt2list('list_urlls.txt')  
#keylst = txt2list('wtest.txt') #ALLLLLLLL 

def get_sites():
    
    for urrl in urlsdbs:

        proxy_index = random.randint(0, len(proxies) - 1)
        #print(proxy_index)
        proxy = {"http": proxies[proxy_index]}
                
        response = requests.request("GET", urrl, proxies=proxy) #, headers=headers
        data=json.loads(response.text)
        for x in range(10000):
            try:
                url= data["results"][x]["task"]["domain"]
                print(f"Checking {url}")
                if url not in site_list:
                        
                    x = requests.get('http://'+url,  allow_redirects=True)
                    if x.status_code:
                        print(url, x.status_code)
                        site_lnk=f"python.exe dirmap.py -i {url} -lcf"
                        subprocess.Popen(site_lnk, shell=True)
                        #time.sleep(10)

                        site_scan=f"python SecretFinder.py -i http://{url} -o cli -e -g default"
                        subprocess.Popen(site_scan, shell=True)
                        time.sleep(25)
                #if x.status_code == 200:
                #    urlsdbsm.append(url)
                #    print(x.status_code, url, 'Good..')
                #else:
                #    urlsdbsm.append(url)
                #    if x.status_code == 400:
                #        print(x.text, url, 'Site down..')
                #        continue
            except:
                print('Fail', url)
        #return urlsdbsm

########################################################### 
get_sites()
#urlsdbs = txt2list('phish.txt')  
########################################################### 

#print(urlsdbsm)

"""
for i in tqdm(urlsdbsm):
    site_lnk = i
    site_lnk=f"python.exe dirmap.py -i {site_lnk} -lcf"
    print(site_lnk)
    #os.system("python i")
    #subprocess.Popen(site_lnk)
    subprocess.Popen(site_lnk, shell=True)
    time.sleep(30)
    #subprocess.Popen([i], creationflags=subprocess.CREATE_NEW_CONSOLE)
"""