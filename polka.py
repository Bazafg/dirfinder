import requests
import json
import time
from tqdm import tqdm
import subprocess
from subprocess import Popen, PIPE, STDOUT

def txt2list(fname): #функция чтения файла
    with open(fname, 'r', encoding="utf8") as f:
        return [line.strip() for line in f]
site_list = txt2list('list.txt')


def get_sites():
    
    phfrom = 'https://raw.githubusercontent.com/polkadot-js/phishing/master/meta/2023-02.json'

    response = requests.request("GET", phfrom) #, headers=headers
    data=json.loads(response.text)

    for x in data:# range(100):
        url= x['url']

        if url not in site_list:
                
            print(f"New site.. Checking.. {url}")



            try:
                
                x = requests.get('http://'+url,  allow_redirects=True)
                print(f"Checking {url}")
                if x.status_code:
                    print(url, x.status_code, 'Good..')
                    site_lnk=f"python.exe dirmap.py -i {url} -lcf"
                    subprocess.Popen(site_lnk, shell=True)
                    #time.sleep(1)
                    #python SecretFinder.py -i http://web3rpc.net -o cli -e -g default
                    site_scan=f"python SecretFinder.py -i http://{url} -o cli -e -g default"
                    subprocess.Popen(site_scan, shell=True)
                    #time.sleep(5)

            except:
                print('Fail', url)
        else:
            print('Повтор ', url)

    #print(data)

########################################################### 
get_sites()
