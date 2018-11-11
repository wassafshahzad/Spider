import os

def create_dir(direct):
        if not os.path.exists(direct):
            os.makedirs(direct)

def create_files(direct,url):
        que=direct+'/que.txt'
        cral=direct+'/crawl.txt'
        if not os.path.isfile(que):
                write_file(que,url)
        if not os.path.isfile(cral):
                write_file(cral,'')
                
                
def write_file(path,data):
        f=open(path,'w')
        f.write(data+'\n')
        f.close()

def append_file(path,data):
        try:
                f=open(path,'a')
                f.write(data+'\n')
                f.close()
        except Exception:
                print("file not appended")

def delete_file(path):
        try:
                f=open(path,'w')
                f.close()
        except Exception:
                print("file not appended")
def file_set(path):
        result=set()
        with open(path,'rt') as file:
                for line in file:
                        result.add(line.replace('\n',''))
        return

def set_file(link,file):
        delete_file(file)
        for l in sorted(link):
                append_file(file,link)
                
        
                        
