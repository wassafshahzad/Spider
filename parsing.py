from urllib.parse import urlparse


def get_d(url):
    try:
        result=urlparse(url).netloc.split('.')
        result=result[-2]+"."+result[-1]
        return result
    except:
        return '404'
