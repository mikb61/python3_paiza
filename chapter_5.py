# coding: utf-8
# リストのおさらい
enemyArray = ["スライム", "モンスター", "ドラゴン"]
print(enemyArray)
print(enemyArray[0])

# 辞書の具体例
enemyDictionary = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemyDictionary)
print(enemyDictionary["中ボス"])

level = "ラスボス"
print(enemyDictionary[level])
→
['スライム', 'モンスター', 'ドラゴン']
スライム
{'ザコ': 'スライム', '中ボス': 'ドラゴン', 'ラスボス': '魔王'}
ドラゴン
魔王

# 辞書の特定の値を出力してみよう
skills = {"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}
# この下で、辞書から出力してみよう
print(skills['職業'])
→
戦士


# coding: utf-8
# 辞書の基本操作
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["ザコ"])
print(len(enemies))

enemies['仲間'] = 'ねこ'
print(enemies)
print(len(enemies))

enemies['中ボス'] = 'レッドドラゴン'
print(enemies)
print(len(enemies))

del enemies["ザコ"]
print(enemies)
print(len(enemies))
→
{'ザコ': 'スライム', '中ボス': 'ドラゴン', 'ラスボス': '魔王'}
スライム
3
{'ザコ': 'スライム', '中ボス': 'ドラゴン', 'ラスボス': '魔王', '仲間': 'ねこ'}
4
{'ザコ': 'スライム', '中ボス': 'レッドドラゴン', 'ラスボス': '魔王', '仲間': 'ねこ'}
4
{'中ボス': 'レッドドラゴン', 'ラスボス': '魔王', '仲間': 'ねこ'}
3


# 辞書をループで処理する
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
for rank in enemies:
    print(enemies[rank] + 'が現れた！')
for (rank, enemy) in enemies.items():
    print(rank + 'の' + enemy + 'が現れた！')
→
{'ザコ': 'スライム', '中ボス': 'ドラゴン', 'ラスボス': '魔王'}
スライムが現れた！
ドラゴンが現れた！
魔王が現れた！
ザコのスライムが現れた！
中ボスのドラゴンが現れた！
ラスボスの魔王が現れた！


# ループで辞書の値を出力しよう
skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# この下で、辞書の値をループで出力してみよう
for item in skills:
    print(skills[item])
→
戦士
100
200
380


# ループで辞書のキーと値を出力しよう
skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# この下で、辞書の値をループで出力してみよう
for (key, item) in skills.items():
    print(key + "は" + str(item) + "です")
→
職業は戦士です
体力は100です
魔法力は200です
ゴールドは380です


# ループで合計を計算しよう
points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for key in points:
    sum += points[key]
print(sum)
→
157

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for (key, point) in points.items():
    sum += point
print(sum)
→
157


# リストの整列
weapons = ["イージスソード", "ウィンドスピア", "アースブレイカー", "イナズマハンマー"]
print(sorted(weapons))
print(sorted(weapons, reverse=True))
→
['アースブレイカー', 'イナズマハンマー', 'イージスソード', 'ウィンドスピア']
['ウィンドスピア', 'イージスソード', 'イナズマハンマー', 'アースブレイカー']


# 辞書の整列
weapons = {"イージスソード":40, "ウィンドスピア":12, "アースブレイカー":99}
print(weapons)
print(sorted(weapons))
print(sorted(weapons.items()))
→
{'イージスソード': 40, 'ウィンドスピア': 12, 'アースブレイカー': 99}
['アースブレイカー', 'イージスソード', 'ウィンドスピア']
[('アースブレイカー', 99), ('イージスソード', 40), ('ウィンドスピア', 12)]

# 辞書をソートして辞書で出力する
math = {"えんどう" : 99, "あだち" : 40, "いいだ" : 12}
print(sorted(math.items()))
→
[('あだち', 40), ('いいだ', 12), ('えんどう', 99)]


# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

num = int(input())
for i in range(num):
    print("<img src='" + items_imges[input().rstrip()] + "'>")
(入力)
6
回復薬
盾
クリスタル
クリスタル
剣
剣
→
アイコンが横に６個並ぶ
