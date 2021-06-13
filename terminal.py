
from cmd import Cmd
import os
import json

from templates.requester import requester
from templates.colors import *

url = ''


def json_dump(data):

    return json.dumps(data,indent=4)

    
class terminal(Cmd):
   
    
    prompt = f"\n{blue}[graphqlInjector] {reset}"
    intro = "\n[ SWITCHING TO INTERACTIVE INJECTOR SHELL ]\n\n"


    def do_save_url(self,args):

        global url
        url = args

    def do_run(self,query):

        global url
        payload = {'query':query}
        r = requester(url,payloads=payload,use_post=True)
        print(f"payload ---> {payload}")

        if r.status_code < 300:
            
            print(yellow,json_dump(r.json()),reset)

        else:
            print(red,"REQUEST FAILES ",r.status_code,reset)


    def default(self,line):
        os.system(line)



