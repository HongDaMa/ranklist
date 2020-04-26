#!E:\py_virtual_env\saas_project\Scripts\python.exe
# -*- coding: utf-8 -*-
import sys
import requests

def client_test(port_id,begin,end):
    print('------------**** 范围测试 ****-------------')
    url = "http://127.0.0.1:8000/select_ranking/" + str(port_id) + "/" + begin +'-'+ end +"/"
    print(url)
    r = requests.get(url)
    print(r.json())

if __name__ == '__main__':
    port_id = sys.argv[1]
    begin = sys.argv[2]
    end = sys.argv[3]
    client_test(port_id,begin,end)