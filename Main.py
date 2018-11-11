from general import *
from queue import Queue
import threading
from spider import Spider
from parsing import *

#Project_name='Anime'
 


def create_w():
    for i in range(0,N):
        t= threading.Thread(target=work)
        t.daemon=True
        t.start()
        
def work():
    while True:
        url=queue.get()
        print("currently on page\n")
        print(url)
        print(len(s.craw))
        s.crawl(url)
        queue.task_done()


def crawl_t():
    if (len(Spider.que)>0 and len(s.craw)<100):
        #print(len(Spider.que))
        for lnks in Spider.que:
            queue.put(lnks)
        queue.join()
        crawl_t()


Home =input("Enter a valid URL:\n")
Domain=get_d(Home)
N=5 ## number of threads
queue = Queue()
s=Spider(Home,Home,Domain)           

create_w()
crawl_t()



