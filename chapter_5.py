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
