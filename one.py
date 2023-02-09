import os
import subprocess
import time
import json
import requests
import asyncio
import threading
from subprocess import Popen, PIPE, STDOUT
import concurrent.futures
from tqdm import tqdm

def txt2list(fname): #функция чтения файла
    with open(fname, 'r', encoding="utf8") as f:
        return [line.strip() for line in f]

site_list = txt2list('list.txt')

#urlsdbs = txt2list('list.txt')
#urlsdbs = txt2list('fr.txt')  """
#urlsdbs = txt2list('list_urlls.txt')  
#keylst = txt2list('wtest.txt') #ALLLLLLLL 
#urlsdbsm = []

def get_sites():
   
    #https://raaribleh.com/connect/aWU/metamask/ph.js
    domain='assetsnetworkledger.net'


    if domain not in site_list:
        print('new site')
            
        print(f"Checking {domain}")
        try:  
            req = requests.get('http://'+domain,  allow_redirects=True)
            print(req.status_code)
            if req.status_code:
                print(req.status_code, domain, 'Good..')

                #site_scan=("python SecretFinder.py -i http://"+domain+" -o cli -e -g default")
                site_scan=f"python SecretFinder.py -i http://{domain} -o cli -e -g default"
                print(site_scan)
                subprocess.Popen(site_scan, shell=True)
                
                site_lnk=f"python.exe dirmap.py -i {domain} -lcf"
                print(site_lnk)
                subprocess.Popen(site_lnk, shell=True)
                


                #time.sleep(3)
        
        except:
            print('fail')
    else:
        print('Повтор')

get_sites()
    
"""

########################################################### 
get_sites()
#urlsdbs = txt2list('phish.txt')  
########################################################### 

print(urlsdbsm)


for i in tqdm(urlsdbsm):
    site_lnk = i
    site_lnk=f"python.exe dirmap.py -i {site_lnk} -lcf"
    print(site_lnk)
    #os.system("python i")
    #subprocess.Popen(site_lnk)
    subprocess.Popen(site_lnk, shell=True)
    time.sleep(5)
    #subprocess.Popen([i], creationflags=subprocess.CREATE_NEW_CONSOLE)
"""