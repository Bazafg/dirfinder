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

urlsdbs = txt2list('lis.txt')
#urlsdbs = txt2list('fr.txt')  """
#urlsdbs = txt2list('list_urlls.txt')  
#keylst = txt2list('wtest.txt') #ALLLLLLLL 
checkeds = []

def get_sites(domain):
   

    #domain= 'wallet-validate.com'
    if domain not in site_list:
        print('Not in site list')
            
        print(f"Checking {domain}")
        if domain not in checkeds:
            try:  
                req = requests.get('http://'+domain, allow_redirects=True, timeout=3)
                print(req.status_code)
                if req.status_code:
                    checkeds.append(domain)
                    #urlsdbsm.append(url)
                    print(req.status_code, domain, 'Good..')
                    site_lnk=f"python.exe dirmap.py -i {domain} -lcf"
                    subprocess.Popen(site_lnk, shell=True)
                    #time.sleep(1)
                    site_scan=f"python SecretFinder.py -i http://{domain} -o cli -e -g default"
                    #site_scan=f"python SecretFinder.py -i http://{domain} -o cli"
                    subprocess.Popen(site_scan, shell=True)
                    time.sleep(20)
            
            except:
                print('fail')
    else:
        print('Повтор')
    return


for domain in tqdm(urlsdbs):
    get_sites(domain)


    
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