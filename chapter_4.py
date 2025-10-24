# リスト
まとまったデータを便利に扱うことができるデータ構造。
インデックスと呼ばれる番号で、それぞれのデータを区別する。
他のプログラミング言語では「配列」と呼ばれる機能が、Pythonでは「リスト」という名前で提供されている。

# 変数で、リストに代入する
player_1 = "勇者"
player_2 = "魔法使い"
player_3 = "戦士"

# player_1 ~ 3を、リストに記述して、print関数で出力してください。
team = [player_1, player_2, player_3]
print(team)
→
['勇者', '魔法使い', '戦士']

# リストの参照
print(team[0]) 直接数値で指定する
print(team[num]) 変数で指定する
print(team[num + 1]) 計算式で指定する

# len関数　要素の数
print(len(team))

# coding: utf-8
# リストの要素の個数を出力する
weapon = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣", "石斧", "エクスカリバー"]
# ここに、要素数を出力するコードを記述する
print(len(weapon))

# append関数  リストの末尾に要素を追加
team.append("戦士")

# coding: utf-8
# リストに要素を追加する
weapon = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
# ここに、要素を追加するコードを記述する
weapon.append("石斧")
print(weapon)
→
['木の棒', '鉄の棒', '鉄の剣', '銅の剣', '石斧']


# リストの要素を上書き
team[0] = "ドラゴン"

# リストの要素を上書きする
weapon = ["木の棒", "鉄の棒", "鉄の剣", "サビた剣"]
# ここに、要素を上書きするコードを記述する
weapon[3] = "石斧"
print(weapon)
→
['木の棒', '鉄の棒', '鉄の剣', '石斧']


# リストの要素を削除
team.pop(0)

# coding: utf-8
# リストの要素を削除する
weapon = ["木の棒", "鉄の棒", "鉄の剣", "銅の剣"]
# ここに、要素を削除するコードを記述する
weapon.pop(2)
print(weapon)
→
['木の棒', '鉄の棒', '銅の剣']

# coding: utf-8
#リストの中身をループで表示する
enemy = ["スライム", "モンスター", "ゾンビ", "ドラゴン", "魔王"]
# ここに、要素をループで表示するコードを記述する
for i in enemy:
    print(i + "が現れた")
→
スライムが現れた
モンスターが現れた
ゾンビが現れた
ドラゴンが現れた
魔王が現れた


# coding: utf-8
# 要素の合計を計算する
numbers = [12, 34, 56, 78, 90]
total = 0
for num in numbers:
	# ここに、合計を計算するコードを記述する
	total += num
print(total)
→
270


# split関数
与えられたデータを指定の記号で分割し、リストとして戻す

line = "勇者,戦士,魔法使い"
print(line.split(","))
→
['勇者', '戦士', '魔法使い']


# coding: utf-8
#英文の単語数を数える
str = "One cold rainy day when my father was a little boy he met an old alley cat on his street"
print(len(str.split(" ")))
→
20


# sys.stdin.readlines関数
ファイルを全て読み込み、1行毎に処理
stdin は英語で 「standard input（スタンダード・インプット）」 の略

import sys
line = sys.stdin.readlines()


# 💡 よく一緒に使われる sys モジュールの機能一覧
| コード例 | 読み方 | 説明 |
|-----------|---------|------|
| `sys.stdin` | シス・スタディン | 標準入力（キーボードやファイルなどから読み取る） |
| `sys.stdout` | シス・スタドアウト | 標準出力（printと同じ） |
| `sys.stderr` | シス・スタドエラー | エラー出力を扱う |
| `sys.argv` | シス・アーグブ | コマンドライン引数（プログラム実行時に渡す値） |
| `sys.exit()` | シス・エグジット | プログラムを途中で終了する |
| `sys.version` | シス・バージョン | Pythonのバージョン情報を取得する |

---

## 🧠 使用例
```python
import sys

# Pythonのバージョンを表示
print("Python version:", sys.version)

# コマンドライン引数を表示
print("Arguments:", sys.argv)

# 標準入力から複数行を読み取る
lines = sys.stdin.readlines()
print("入力された内容：", lines)

# プログラムを終了する
# sys.exit()


# coding: utf-8
# 複数行のカンマ区切りデータを出力する
import sys
for line in sys.stdin.readlines():
	# ここに、文字列を分割して、出力するコードを書く
	enemy = line.rstrip().split(",")
	print(enemy[0] + "が" + enemy[1] +"匹現れた")
(入力）
スライム,30
モンスター,23
ゾンビ,15
ドラゴン,3
魔王,1
→
スライムが30匹現れた
モンスターが23匹現れた
ゾンビが15匹現れた
ドラゴンが3匹現れた
魔王が1匹現れた


# randrange関数
ランダムな値を生成する
引数を1つ指定した場合は、ゼロから引数未満の値をランダムに生成する

# coding: utf-8
# リストを使ったランダムくじ
# スライム,モンスター,ドラゴン,魔王
import random
line = input().rstrip().split(",")
for enemy in line:
	print(enemy + "が現れた！")
#ランダムな数を作る範囲を調べる
num = len(line)
print("敵は" + str(num) + "匹")
#ランダムな数を生成
attack = random.randrange(num)
#選んだ後に、「会心の一撃！」と表示
print(line[attack] + 'に会心の一撃!' + line[attack] + "を倒した！")
(入力)
スライム,モンスター,ドラゴン,魔王
→
スライムが現れた！
モンスターが現れた！
ドラゴンが現れた！
魔王が現れた！
敵は4匹
モンスターに会心の一撃!モンスターを倒した！
