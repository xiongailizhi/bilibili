import pymongo
import time
from __init__ import get

client = pymongo.MongoClient('localhost',27017)
bilibili = client['bilibili']
item_info = bilibili['item_info']

def get_Craw_num():
    print('--------菜 单--------')
    num = int(input('输入起始页码:'))
    print('--------------------')
    return num

'''
{"code":0,"data":{"aid":1008611,"view":24165,"danmaku":296,"reply":296,"favorite":273,"coin":25,
"share":31,"now_rank":0,"his_rank":319,"no_reprint":0,"copyright":2},"message":"0","ttl":1}
'''
def get_Item_info(url):
    r = get(url)
    time.sleep(0.5)
    if r.status_code == 200:
        try:
            j = r.json()['data']
            favorite = j['favorite']
            danmaku = j['danmaku']
            coin = j['coin']
            view = j['view']
            reply = j['reply']
            aid = j['aid']
            favorite = str(favorite)
            danmaku = str(danmaku) + " "
            coin = str(coin)
            view = str(view)
            reply = str(reply)
            av_num = "av" + str(aid)
            item_info.insert_one({'av_num':av_num,'favorite':favorite,'view':view,'danmaku':danmaku,'coin':coin,'reply':reply})
            print({'av_num':av_num,'favorite':favorite,'aid':aid,'view':view,'danmaku':danmaku,'coin':coin,'reply':reply})
        except Exception as e:
            pass



