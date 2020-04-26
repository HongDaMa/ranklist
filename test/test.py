#!E:\py_virtual_env\saas_project\Scripts\python.exe
# -*- coding: utf-8 -*-
import requests
import json
import random

def client_send_text():
    """客户端发送数据测试"""
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    for client_id in range(1,11):
        score = random.randrange(1,10000000)
        r = requests.post('http://127.0.0.1:8000/uploading_score/', data=json.dumps({'port':client_id,'score':score}),headers=headers)
        print(r.json())
    for client_id in range(1,6):
            url = "http://127.0.0.1:8000/select_ranking/" +str(client_id)+"/"
            r = requests.get(url)
            print(r.json())
            print('-------------------------')

if __name__ == '__main__':
    client_send_text()
