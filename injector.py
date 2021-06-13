import json
import re

import templates.HandleSignals
from templates.banner import banner , print_line
from templates.colors import *
from templates.requester import requester
from templates.dir_create import dir_create

class Injector:

    def __init__(self,url,verbose,proxy):
        self.url = url
        self.verbose = verbose

        self.proxy = {
            'http':f'http://{proxy}',
            'https':f'https://{proxy}',
        }

        self.list = []

    def start(self):

        ## finding various endpoints for running our queries
        with open('payloads/endpoints.txt','r') as r:
            r = r.readlines()
            print(f"{green}\t AVAILABLE ENDPOINTS {reset}")

            for endpoints in r:
                r = requester(f"{self.url}/{endpoints.strip()}",payloads=None,use_get=True,proxy=self.proxy)
                if(r.status_code < 401):
                    print(f"{self.url}/{endpoints}")
                    self.list.append(f"{self.url}/{endpoints.strip()}")


    def enum_api(self):
     
            #basic enumeration of the api
            query = {'query': '{__schema { types { name,kind ,fields{ name } }} }' }

            for urls in self.list:  
                print_line(green,reset)
                print(f"URL : {red}    {urls}     {reset}  " )
                
                if self.verbose : print(f"query  ----> {query}" )

                r = requester(urls,use_post=True,payloads=query,proxy=self.proxy)
                print(yellow)
                if r.status_code < 400:
                    jsondata = r.json()
                    for types in jsondata['data']['__schema']['types']:
                        if types['kind'] == "OBJECT":
                            print(types['name'])
                            if "__" not in types['name']:
                                for fields in types['fields']:

                                    print(fields)

            print(reset)

    def dump_introspections(self):

        INJECTOR_DIR_NAME = "graphql_dumps"
        dir_create(INJECTOR_DIR_NAME)
        
        print(f"{red} DUMPING  INTROSPECTIONS{reset}")
        with open('payloads/introspections.txt') as f:
            f = f.readlines()
            for q in f:
                query = {"query":q}
                for urls in self.list:
                    r = requester(urls,use_post=True,payloads=query,proxy=self.proxy)
                    if r.status_code < 400 :

                        file_name = re.findall("//.*$",urls)[0]
                        file_name = file_name.replace('/','_')
                        print(f"{blue} SAVING INTROSPECTIONS OF {urls} IN ----> {file_name}{reset}")

                        with open(f"{INJECTOR_DIR_NAME}/{file_name}",'w') as f:
                            data = self.json_dump(r.json())
                           
                            f.write(data)
                           


    def json_dump(self,data):

        return json.dumps(data,indent=4)








