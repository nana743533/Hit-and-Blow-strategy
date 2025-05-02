from game_model import trial, init, confirm, get_remain
import random
import numpy as np

# 最小手数を目指す戦略でHit & Blowをプレイする関数
def choice_strategy():
    remain = init() # 正解候補のリスト（重複なし4桁数字）を初期化
    correct = random.choice(remain) # 出題者が選んだ正解の数字（ランダムに選ぶ）
    tesuu = 0 # 回数カウント

    while(True):
        if(len(remain)==1): # 正解が1つに絞れたら終了
            print(f"{tesuu}回でクリアしました。")
            return(tesuu)
        # remainで残っている正解の選択肢を管理する
        # 最初の一手は固定で '0123' を使用
        if(tesuu == 0):
            # 残っている選択肢の中から、「最も絞れる可能性の高い候補」を次の予想とする
            number = '0123'
        else:
            number = choice_number(remain)
        
        # 正解との照合（hitとblowを取得）
        hit,blow = confirm(correct,number)

        # 回答と結果に基づき、ありえる正解候補のみを残す
        remain = get_remain(remain,number,hit,blow)

        tesuu += 1 # 回数カウント


def choice_number(remain):
    vlist = []

    for i in remain:
        # 結果（hit, blow）の組み合わせごとの出現回数を記録する辞書
        dict = {(0,0):0, (0,1):0, (0,2):0, (0,3):0, (0,4):0, (1,0):0, (1,1):0, (1,2):0, (1,3):0, (2,0):0, (2,1):0, (2,2):0, (3,0):0, (3,1):0, (4,0):0}
        dict_key = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(3,1),(4,0)]

        # i（仮の予想）を基準に、全てのremain候補と照合して、(hit, blow) 結果の分布を集計
        for j in remain:
            x,y = confirm(i,j)
            dict[(x,y)] += 1

        # 結果の出現数リストを作り、分散を計算して記録
        ret = []
        for k in dict_key:
            ret.append(dict[k])
        vlist.append(np.var(ret)) 
    
    # 分散が小さいほど、結果がばらつかず、候補を絞りやすいと見なす
    return(remain[vlist.index(min(vlist))])


trial(100,choice_strategy)