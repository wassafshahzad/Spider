from bs4 import BeautifulSoup
from urllib import parse
from urllib.request import urlopen
from urllib.parse import urljoin
from parsing import *
class finder:

    def __init__(self,base_url,page_url,domain):
        self.base=base_url
        self.page=page_url
        self.domain=domain
        self.lnk=set()
        #self.lnk.add(page_url)
        
    def linker(self,doc):
        soup=BeautifulSoup(doc,'html.parser')
        for lnks in soup.find_all('a'):
           url =urljoin(self.base,lnks.get("href"))
           if (get_d(url)==self.domain):
               self.lnk.add(url)
               
        
    def getAll(self):
        return self.link
        
