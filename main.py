from multiprocess import Pool
from bilibili import get_Craw_num
from bilibili import get_Item_info

def get_Url_lists():
    num = get_Craw_num()
    urls = []
    for i in range(num,num+10001):
        url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(i)
        urls.append(url)
    #print(urls)
    return urls

if __name__=='__main__':
    urls = get_Url_lists()
    pool = Pool(processes = 4)
    pool.map(get_Item_info,urls)
