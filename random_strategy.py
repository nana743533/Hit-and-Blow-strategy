from game_model import trial, init, confirm, get_remain
import random

# ランダム戦略でHit & Blowをプレイする関数
def random_strategy():
    remain = init() # 正解候補のリスト（重複なし4桁数字）を初期化
    correct = random.choice(remain) # 出題者が選んだ正解の数字（ランダムに選ぶ）
    tesuu = 0 # 回数カウント

    while(True):
        if(len(remain)==1): # 正解が1つに絞れたら終了
            print(f"{tesuu}回でクリアしました。")
            return(tesuu)
            break

        # 残っている正解の選択肢を管理する
        # 残っている選択肢の中からランダムに選択し、次の予想とする
        number = random.choice(remain)

        # 正解との照合（hitとblowを取得）
        hit,blow = confirm(correct,number)

        # 回答と結果に基づき、ありえる正解候補のみを残す
        remain = get_remain(remain,number,hit,blow)

        #回数をカウント
        tesuu += 1

# ランダム戦略で1000回試行して平均回数・分散を出す
trial(1000,random_strategy)