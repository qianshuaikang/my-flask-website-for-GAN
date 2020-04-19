# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:15:05 2020

@author: win7
"""
'''
import os
import time
import json
import requests
 
def getManyPages(pages):
    params=[]
    for i in range(0, 12*pages+12, 12):
        params.append({
            'resource_id': 28266,
            'from_mid': 1,
            'format': 'json',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'query': '印度明星',
            'sort_key': '',
            'sort_type': 1,
            'stat0': '',
            'stat1': '印度',
            'stat2': '',
            'stat3': '',
            'pn': i,
            'rn': 12
                  })
    url = 'https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php'
#    names = []
#    img_results = []
    x = 0
    f = open('indianstarName.txt', 'w')
    for param in params:
        try:
            res = requests.get(url, params=param)
            js = json.loads(res.text)
            results = js.get('data')[0].get('result')
        except AttributeError as e:
            print(e)
            continue
        for result in results:
            img_name = result['ename']
#            img_url = result['pic_4n_78']
#            img_result =  [img_name,img_url]
#            img_results.append(img_result)
            f.write(img_name+'\n')
    #        names.append(img_name)
 
        if x % 10 == 0:
            print('第%d页......'%x)
        x += 1
    f.close()
 
if __name__ == '__main__':
    getManyPages(10)'''
'''import os
from icrawler.builtin import BingImageCrawler
path = r'E:\Python深度学习\Dataset'
f = open('japanstarName.txt', 'r')
lines = f.readlines()
for i, line in enumerate(lines):
    name = line.strip('\n')
    file_path = os.path.join(path, name)
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    bing_storage = {'root_dir': file_path}
    bing_crawler = BingImageCrawler(parser_threads=2, downloader_threads=4, storage=bing_storage)
    bing_crawler.crawl(keyword=name, max_num=10)
    print('第{}位明星：{}'.format(i, name))
'''
import os
import glob  #用来glob包用来返回特定路径下的所有文件
import numpy as np
path='E:\\Python深度学习\\Dataset'
files=glob.glob(os.path.join(path,'*\\*.jpg'))
number=len(files)
shuffle=np.random.permutation(number)
for i in shuffle:
    image=files[i].split('\\')[-1].split('.')[-1]
    os.rename(files[i],os.path.join(path,str(i)+'.'+image))
    