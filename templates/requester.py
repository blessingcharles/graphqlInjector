from types import SimpleNamespace
import requests
from requests.api import post


headers = {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language' : 'en-US,en;q=0.5',
            'Accept-Encoding' : 'gzip, deflate',
            'Upgrade-Insecure-Requests' : '1',
             }

postHeaders =  {'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language' : 'en-US,en;q=0.5',
            'Accept-Encoding' : 'gzip, deflate',
            'Upgrade-Insecure-Requests' : '1',
             'Content-Type': 'application/json'}

def requester(url,payloads,proxy=None,use_post=False,use_get=False):
    
    try:
            if use_post :
           
                r = requests.post(url,data=payloads)
                return r

            if use_get :
                r = requests.get(url,headers=headers)
                
                return r
    except:
        pass