import argparse

from injector import Injector
from templates.banner import banner , print_line
from templates.colors import *
from terminal import terminal

if __name__ == '__main__':

    print_line(blue,reset)
    banner(yellow,reset)
    print_line(blue,reset)

    parser = argparse.ArgumentParser(description="graphql injector automation")
    parser.add_argument("-u","--url",dest="url",help="enter a valid url")
 
    parser.add_argument("-p","--proxy",dest="proxy",help="add a proxy interface [default : localhost:8080 ]",default="localhost:8080")
    parser.add_argument("-v","--verbose",action="store_true",default=False,dest="verbose",help="set for verbose output")

    parser = parser.parse_args()

    url = parser.url 
   
    verbose = parser.verbose
    proxy = parser.proxy

    
    if not url :
        print(f"{red}provide an url or try python3 start.py --help {reset}")
        quit()


    injector = Injector(url,verbose,proxy)
    injector.start()
    injector.enum_api()
    injector.dump_introspections()

    prompt = terminal()

    prompt.cmdloop()
    
