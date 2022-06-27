import random

import const as con

#待抓麻将池
mahjong_pool = []
#垃圾池
rubbish_pool=[]
# 麻将数据结构的定义
class Mahjong:
    def __init__(self):
        # 花色
        self.kind = None
        # 牌值
        self.point = None

# 定义打麻将的结构
class
# 定义打牌人的数据结构
class Player:
    def __int__(self):
        # 打牌人的姓名
        self.name = ''
        # 打牌人的上家
        self.pre_player = None
        # 打牌人的下家
        self.next_player = None
        # 打牌人的手牌
        self.cards = []
        # 打牌人的明牌（杠、碰……）
        self.public_cards = []
        # 打牌人的暗牌
        self.private_cards = []


# 麻将池初始化
def init_mahjong():
    # 初始麻将池
    # 先把花牌入池,默认先不要花牌
    # for m in con.Flowers:
    #     mj = mahjong()
    #     mj.kind = con.Flower
    #     mj.point = m
    #     mahjong_pool.append(mj)
    # 再把风、箭牌入池
    i = 0
    while i < con.Amount:
        for m in con.Winds:
            mj = Mahjong()
            mj.kind = con.Wind
            mj.point = m
            mahjong_pool.append(mj)
        for m in con.Dragons:
            mj = Mahjong()
            mj.kind = con.Dragon
            mj.point = m
            mahjong_pool.append(mj)
        # 万、筒、条牌入池
        for n in [con.Character, con.Dot, con.Bamboo]:
            for m in con.Ranks:
                mj = Mahjong()
                mj.kind = n
                mj.point = m
                mahjong_pool.append(mj)
        i += 1
    print("麻将池初始化完成，总张数=", len(mahjong_pool))
    random.shuffle(mahjong_pool)
    for m in mahjong_pool:
        print(m.point + m.kind)
    return mahjong_pool

#初始阶段，每人发13张牌
def init_player():
    player=Player()
    cards=[]
    # 发牌
    i = 0
    while i < 13:
        cards.append(mahjong_pool.pop())
    player.cards=cards
    #初始13张牌全部为暗牌
    player.private_cards=cards
    return player

# 抓牌打牌，一共144张牌，打完为止
# 打牌
def play_mahjong():
    # step1:先掷骰子，决定谁坐庄,默认甲坐庄
    # step2：每人发13张牌
    mahjong_pool = init_mahjong()
    # 每个人的手牌
    jia_player=init_player()
    jia_player.name="甲"
    yi_player=init_player()
    yi_player.name="乙"
    bing_player=init_player()
    bing_player.name="丙"

    print("甲的牌张数为：", len(jia_cards))
    for mj in jia_cards:
        print(mj.point + mj.kind)
    print("麻将池还剩牌的张数为：", len(mahjong_pool))
    # step3：开始从甲开始，抓牌打牌
    while len(mahjong_pool) > 0:
        jia_cards.append(mahjong_pool.pop())
