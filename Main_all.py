#from general import *
from queue import Queue
import threading
from spider import Spider
from parsing import *
#Project_name='Anime'
 

def append_file(data,name):
        try:
                f=open(name+'.txt','a')
                for l in data:
                    f.write(l+'\n\n')
                f.close()
        except Exception:

                print("file not appended")
def create_w():
    for i in range(0,N):
        t= threading.Thread(target=work)
        t.daemon=True
        t.start()
        
def work():
    while True:
        url=queue.get()
        print("current Page")
        print(url)
        s.crawl(url)
        queue.task_done()


def crawl_t():
    if (len(Spider.que)>0):
        #print(len(Spider.que))
        for lnks in Spider.que:
            queue.put(lnks)
        queue.join()
        crawl_t()


Home =input("Enter a valid URL:\n")
name =input("Enter a Name of file :\n")
Domain=get_d(Home)
N=5 ## number of threads
queue = Queue()
s=Spider(Home,Home,Domain)           

create_w()
crawl_t()

append_file(Spider.craw,name)
print("File Saved")

