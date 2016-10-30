import pymongo
import requests
import thre
import os


kech = {"video":"/video/8475"}

connection=pymongo.MongoClient("localhost",27017)

db = connection.mk

video = db.links

vide = video.find(kech)

for pos in vide:
    if pos['video'].split('/')[1] == 'code':
        continue
    vid = (pos['video'].split('/')[-1])
    mkdr = pos['types'] + '\\'+ pos['language'] + '\\'+ pos['subject'] + '\\'+ pos['course']
    name = mkdr + '\\'+ pos['summary'] + '.mp4'
    url = 'http://www.imooc.com/course/ajaxmediainfo/?mid=' + vid + '&mode=flash'
    r = requests.get(url)
    r = r.json()
    r = r['data']['result']['mpath']
    H = r[-1]#BD
    M = r[-2]#HD
    L = r[-3]#SD    
    if os.path.exists(mkdr)==False:            
        os.makedirs(mkdr)
    thre.download( H, name, blocks=3, proxies={} )
