import random
import numpy as np

# 重複のない4桁の数字（0000〜9999のうち有効なもの）をリストで返す
def init():
    numbers = []
    ret=[]
    for i in range(10000):
        numbers.append(str(i).zfill(4))
    for i in numbers:
        if((i[0]!=i[1]) and (i[0]!=i[2]) and (i[0]!=i[3]) and (i[1]!=i[2]) and (i[1]!=i[3]) and (i[2]!=i[3])):
            ret.append(i)
    return(ret) # 例: ["0123", "0132", ...]

# 2つの数字文字列（x:正解, y:回答）を比較して、HitとBlowの数を返す
def confirm(x,y):
    hit,blow = 0,0
    for i in range(4):
        if(x[i]==y[i]):
            hit += 1
    for i in y:
        if(i in x):
            blow += 1
    blow -= hit
    return(hit,blow)

# ある回答とその結果に一致する候補だけを残す
def get_remain(remain,number,hit,blow):
    list = []
    for i in remain:
        h,b = confirm(i,number)
        if(hit==h and blow==b):
            list.append(i)
    return(list)

# 試行回数c回、指定された戦略モデルで実行し、平均と分散を表示
def trial(c, model):
    tl = []
    for i in range(c):
        t = model()
        tl.append(t)
    mean = np.mean(tl)
    variance = np.var(tl)
    print("平均:", mean, "分散:", variance)