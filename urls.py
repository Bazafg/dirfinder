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

urlsdbsm = []
urlsdbs = txt2list('urls.txt')
#urlsdbs = txt2list('fr.txt')  """
#urlsdbs = txt2list('list_urlls.txt')  
#keylst = txt2list('wtest.txt') #ALLLLLLLL 
checkeds = []
def get_sites():
    
    for urrl in urlsdbs:
        response = requests.request("GET", urrl) #, headers=headers
        data=json.loads(response.text)
        for x in range(500):
            try:
                url= data["results"][x]["task"]["domain"]
                print(f"Checking {url}")
                if url not in site_list:
                    print('Not in site list')
                    if url not in checkeds:
                            
                        x = requests.get('http://'+url,  allow_redirects=True)
                        if x.status_code:
                            checkeds.append(url)
                            print(url, x.status_code)
                            site_lnk=f"python.exe dirmap.py -i {url} -lcf"
                            subprocess.Popen(site_lnk, shell=True)
                            #time.sleep(10)

                            site_scan=f"python SecretFinder.py -i http://{url} -o cli -e -g default"
                            subprocess.Popen(site_scan, shell=True)
                            time.sleep(20)
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