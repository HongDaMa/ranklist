#!E:\py_virtual_env\saas_project\Scripts\python.exe
# -*- coding: utf-8 -*-
def judge_version(version1,version2):
    version1 = version1.split(".")
    version2 = version2.split(".")
    version1 = list(map(int,version1))
    version2 = list(map(int,version2))
    placeholder_len = len(version1) -len(version2)
    if placeholder_len > 0:
        for i in range(1,placeholder_len+1):
            version2.append(0)
    else:
        for i in range(1, placeholder_len + 1):
            version1.append(0)
    list_analyze(version1, version2)

def list_analyze(version1,version2):
    max_lenth = len(version1)
    for index in range(0,max_lenth):
        if version1[index] == version2[index]:
            continue
        elif version1[index] > version2[index]:
            return print(1)
        else:
            return print(-1)
    return print(0)

judge_version("0.1","1.1")
judge_version("1.0.1","1")
judge_version("7.5.2.4","7.5.3")
judge_version("1.01","1.001")
judge_version("1.0","1.0.0")