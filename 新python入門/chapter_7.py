# 関数を作る
def say_hello():
    print("hello world")

say_hello()

→
hello world

関数の名前は、次のルールに従って付ける
・1文字目：英語または、「_」(アンダーバー)
・2文字目以降：英語の大文字・小文字・数字「_」(アンダーバー)

例：
・ hello　 1文字目が、英小文字
・ _attack　 1文字目が、「_」(アンダーバー)
・ move01 2文字目以降に数字
・ move_left 2文字目以降「_」(アンダーバー)
・ moveLeft 2文字目以降に英大文字

慣習として、関数の先頭には大文字を使わない
また、動詞を表す単語を使うと、コードがわかりやすくなる


# 引数と戻り値を追加する
def sum(x):　　→ xが引数
    print(x + 20)
sum(30)
sum(3)
→
50
23

def sum(x, y):
    print(x + y)
sum(30, 20)
sum(3, 2)
→
50
5

# 引数と戻り値を追加する
def sum(x, y):
    return x + y
num1 = sum(3, 4)
print(num1)
num2 = sum(30, 40)
print(num2)

戻り値 = 関数が返す値 で、return 文で指定する
ここだと、戻り値は7と70


# 掛け算関数を呼び出してみよう
def multiply(x, y):
    return x * y
ans = multiply(3, 4)
print(ans)

def multiply(x, y):
    return x * y
print(multiply(3, 4))


# 九九の表を作成してみよう
def multiply(x, y):
    return x * y
for x in range(1, 10):　→ 1〜9の行（縦の数字）をループ
    for y in range(1, 10):　→ 1〜9の列（横の数字）をループ
        print(multiply(x, y), end="")　→ x*y を表示、改行はしない
        if y < 9:
            print(", ", end="")　→ 列の間にカンマとスペースを入れる（最後の列は不要）
    print("")　→ 1行分が終わったら改行
→
1, 2, 3, 4, 5, 6, 7, 8, 9
2, 4, 6, 8, 10, 12, 14, 16, 18
3, 6, 9, 12, 15, 18, 21, 24, 27
4, 8, 12, 16, 20, 24, 28, 32, 36
5, 10, 15, 20, 25, 30, 35, 40, 45
6, 12, 18, 24, 30, 36, 42, 48, 54
7, 14, 21, 28, 35, 42, 49, 56, 63
8, 16, 24, 32, 40, 48, 56, 64, 72
9, 18, 27, 36, 45, 54, 63, 72, 81


def multiply(x, y):
    return x * y
for x in range(1, 10):
    for y in range(1, 10):
        print(f"{multiply(x, y):2}", end="  ")  # 2桁で右寄せ
    print()  # 行ごとに改行
→
1  2  3  4  5  6  7  8  9  
2  4  6  8 10 12 14 16 18  
3  6  9 12 15 18 21 24 27  
4  8 12 16 20 24 28 32 36  
5 10 15 20 25 30 35 40 45  
6 12 18 24 30 36 42 48 54  
7 14 21 28 35 42 49 56 63  
8 16 24 32 40 48 56 64 72  
9 18 27 36 45 54 63 72 81  


# スコープ
変数の有効範囲が決まっていること
Pythonでは、関数定義の中と外ではローカル変数は分離している。
同じ名前の変数があっても、独立しているので、それぞれ違う変数として扱われる。

# グローバル変数
スコープがなく、関数定義を超えて利用できる。
ただし、どこで値が代入されたのか分かりにくくなるので、あまり奨励されない。



msg = "hello"

def say_hello(): 
    global msg →グローバル変数を変更したい場合はここにこれを入れる
    msg += " "
    msg += "paiza"
    print(msg)

say_hello()
→
hello paiza


# RPGの攻撃シーン
import random

def attack(enemy):
    print('勇者は' + enemy + 'を攻撃した。')
    hit = random.randint(1, 10)
    if hit < 6:
        print(f"{enemy}に{hit}のダメージを与えた！")
    else:
        print(f"クリティカルヒット！！！！{enemy}に100のダメージを与えた！")

enemies = ['スライム', 'モンスター', 'ドラゴン']
for enemy in enemies:
    attack(enemy)
→
勇者はスライムを攻撃した。
スライムに5のダメージを与えた！
勇者はモンスターを攻撃した。
モンスターに3のダメージを与えた！
勇者はドラゴンを攻撃した。
クリティカルヒット！！！！ドラゴンに100のダメージを与えた！


# RPGの攻撃シーン

def attack(person):
    print(person + "はスライムを攻撃した")

def output_enemy_hp(enemy_hp):
    print("敵のHPは残り" + str(enemy_hp) + "です")

enemy_hp = int(input())
team = {"勇者" : 200, "戦士" : 150, "魔法使い" : 100}

for person, power in team.items():
    attack(person)
    # 以下に、敵の体力を減少させるコードを書く
    enemy_hp -= power
    output_enemy_hp(enemy_hp)
(入力)
730
→
勇者はスライムを攻撃した
敵のHPは残り530です
戦士はスライムを攻撃した
敵のHPは残り380です
魔法使いはスライムを攻撃した
敵のHPは残り280です


# 引数のデフォルト値
def introduce(greeting, name = '村人'): → デフォルト値を設定するのは後ろの引数。しない引数は前に置く
    print(f'私は{name}です＾＾{greeting}!')

introduce('hello')
introduce("よろしくね", '勇者')
→
私は村人です＾＾hello!
私は勇者です＾＾よろしくね！


# 可変長引数
def introduce(greeting, *names):
    for name in names:
        print(f'私は{name}です＾＾{greeting}!')

introduce('hello', '勇者', '村人', '兵士')
→
私は勇者です＾＾hello!
私は村人です＾＾hello!
私は兵士です＾＾hello!


# 可変長引数　辞書ver
def introduce(**people):
    for name, greeting in people.items():
        print(f'私は{name}です。{greeting}!')

introduce(hero = "はじめまして", villager = "こんにちは", soldier = "よろしくお願いします")


# キーワード引数
関数の引数にラベルを付ける機能

# キーワード引数
def say_hello(greeting = "hello", target = "world"):
    print(f"{greeting} {target}")
    
say_hello()
say_hello('こんにちは', 'みなさん')
say_hello('hi!')
say_hello(target = 'ねこさん')

→
hello world
こんにちは みなさん
hi! world
hello ねこさん
