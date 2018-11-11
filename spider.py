#import general
from link import finder
from urllib.request import urlopen,Request
from parsing import *
import requests

class Spider:
    que=set()
    craw=set()
    base_url=''
    domain_name=''
   
   


    def __init__(self,base_url,page_url,d):
        Spider.base_url=base_url
        Spider.domain_name=d
        self.crawl(page_url)
        

    def crawl(self,page_url):
            
            if page_url not in Spider.craw:
                try:
                    #response=urlopen(page_url)
                    r = requests.get(page_url,timeout=None)
                    html=r.text
                    #html=response.read()
                    f=finder(Spider.base_url,page_url,Spider.domain_name)
                    f.linker((html))
                    for lnks in f.lnk:
                        if lnks not in Spider.craw and lnks not in Spider.que:
                            Spider.que.add(lnks)
                    Spider.craw.add(page_url)
                    if page_url in Spider.que:
                        #print('remove')
                        Spider.que.remove(page_url)
                except requests.exceptions.ConnectionError:
                    print("Url cannot be reached")
                except requests.exceptions.TooManyRedirects:
                    print("To many redirects")
                except requests.exceptions.MissingSchema:
                    print("Missing https or Http header please enter a valid url ")
            
                    
#Home ='http://animeheaven.eu/i.php?a=Boruto - Naruto Next Generations'
#Domain=get_d(Home)
#N=5
#queue = Queue()


#s=Spider(Home,Home,Domain)
#print(s.que)
#url = 'animeheaven.eu/i.php?a=Boruto - Naruto Next Generations'
#r = requests.get(url)
#print(r.text)
