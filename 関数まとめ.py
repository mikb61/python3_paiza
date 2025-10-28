# 🐍 Pythonの関数 完全まとめ
---

1. 基本構文（def）
def 関数名(引数1, 引数2, ...):
    処理
    return 戻り値  # 任意

def add(a, b):
    return a + b

print(add(3, 5))  # 8

2. 戻り値（return）
	•	return は関数の実行結果を返す
	•	複数値も返せる
	•	省略すると None が返る

def divide(a, b):
    return a // b, a % b

result = divide(10, 3)
print(result)  # (3, 1)


3. スコープ
| 種類           | 有効範囲       | 定義場所   |
|----------------|----------------|-----------|
| ローカル変数   | 関数内         | 関数内    |
| グローバル変数 | プログラム全体 | 関数外    |

x = 10  # グローバル変数
def func():
    x = 5  # ローカル変数
    print(x)  # 5
func()
print(x)  # 10

# グローバル変数を関数内で変更
x = 10
def change():
    global x
    x = 99
change()
print(x)  # 99


4. 可変長引数

def total(*args):
    return sum(args)
print(total(1, 2, 3))  # 6

def profile(**kwargs):
    print(kwargs)
profile(name="Marie", age=24)
# {'name': 'Marie', 'age': 24}


5. デフォルト引数
def greet(name="guest"):
    print("Hello,", name)

greet()        # Hello, guest
greet("Marie") # Hello, Marie


6. ラムダ式（無名関数）
add = lambda a, b: a + b
print(add(3, 5))  # 8

numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]


7. 再帰関数
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))  # 120


8. docstring（関数の説明文）
def greet(name):
    """名前を受け取り挨拶を表示する関数"""
    print(f"Hello, {name}!")

print(greet.__doc__)
→
名前を受け取り挨拶を表示する関数

9. 型ヒント
def add(a: int, b: int) -> int:
    return a + b


## 10. よく使う組み込み関数

| 関数        | 説明                     | 例                              |
|------------|------------------------|--------------------------------|
| len()      | 要素数を返す              | len([1,2,3]) → 3               |
| sum()      | 合計を返す                | sum([1,2,3]) → 6               |
| max()/min()| 最大/最小値を返す         | max([3,1,5]) → 5               |
| map()      | 関数を適用                | map(lambda x:x*2,[1,2])        |
| filter()   | 条件に合う要素を抽出       | filter(lambda x:x>2,[1,2,3])  |
| enumerate()| インデックス付きで取得     | for i,v in enumerate([10,20]): ... |

---

## 11. まとめ表

| 機能             | 記法               | 説明                     |
|-----------------|------------------|------------------------|
| 通常関数        | def f():          | 関数定義                |
| 戻り値           | return            | 実行結果を返す          |
| グローバル変数   | global            | 関数外変数を操作        |
| 可変長引数       | *args, **kwargs   | 引数不定                |
| デフォルト引数   | def f(x=10)       | 初期値を設定            |
| ラムダ式         | lambda x:x+1      | 無名関数                |
| 再帰             | 関数内で自分呼び出し | 自己呼び出し           |
| docstring        | """説明"""         | 関数の説明文            |
| 型ヒント         | a:int -> int       | 型を明示                |



⭐️おまけ
# map関数
リストなどの各要素に関数を適用して、新しいイテラブルを作る関数

map(関数, リスト)
結果は mapオブジェクト になるから、リストに変換して使うことが多い。


def square(x):
    return x**2
nums = [1, 2, 3, 4, 5]
squared = list(map(square, nums))
print(squared)  # [1, 4, 9, 16, 25]

①
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16, 25]

②
words = ["apple", "banana", "cherry"]
word_len = lambda x: len(x)
result = list(map(word_len, words))
print(result)  # [5, 6, 6]

③
nums = [1, -2, 3, -4, 5]
absolute = lambda x: x if x >= 0 else -x
result = list(map(absolute, nums))
print(result)  # [1, 2, 3, 4, 5]

⭐️三項演算子（条件式）
<値1> if <条件> else <値2>
	•	条件が True のとき → <値1> が返る
	•	条件が False のとき → <値2> が返る

x = 5
result = "正" if x > 0 else "負"
print(result)  # 正

x = -3
result = "正" if x > 0 else "負"
print(result)  # 負

x = -7
abs_val = x if x >= 0 else -x
print(abs_val)  # 7


⭐️リスト内包表記
[ 変換したい値  for 元の要素 in 元リスト  if 条件 ]
	•	変換したい値 → x をそのままにするか、x*2 とかで変換もできる
	•	元の要素 → ループで取り出す値
	•	条件 → 取り出すかどうかのフィルター

# 普通の書き方
result = []
for x in [1, 2, 3, 4, 5]:
    if x % 2 == 0:      # 偶数だけ取り出す
        result.append(x)
print(result)  # [2, 4]

これをリスト内包表記にすると：
result = [x for x in [1, 2, 3, 4, 5] if x % 2 == 0]
print(result)  # [2, 4]


nums = [3, -1, 4, -2, 5]
double_positive = lambda x: x*2 if x > 0 else 0
result = list(map(double_positive, nums))
result = [x for x in result if x != 0]
print(result)  # [6, 8, 10]

①　 nums = [1, 2, 3, 4, 5] の 各要素を3倍したリスト
nums = [1, 2, 3, 4, 5]
result = [num*3 for num in nums]
print(result)  # [3, 6, 9, 12, 15]

nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x*3, nums))
print(result)  # [3, 6, 9, 12, 15]

②　 nums = [1, 2, 3, 4, 5] から 偶数だけを取り出したリスト
nums = [1, 2, 3, 4, 5]
result = [num for num in nums if num % 2 == 0]
print(result)  # [2, 4]

nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)  # [2, 4]

③ リスト words = ["cat", "dog", "apple", "hi", "banana"] から 文字列の長さを2倍したリスト 
words = ["cat", "dog", "apple", "hi", "banana"]
result = [len(word)*2 for word in words]
print(result)  # [6, 6, 10, 4, 12]

words = ["cat", "dog", "apple", "hi", "banana"]
result = list(map(lambda w: len(w)*2, words))
print(result)  # [6, 6, 10, 4, 12]


💡 内包表記と map/filter の関係：
	•	[処理 for x in リスト] → map(lambda x: 処理, リスト)
	•	[x for x in リスト if 条件] → filter(lambda x: 条件, リスト)


🔹 filter関数
条件を満たす要素だけ取り出す関数
filter(関数, イテラブル)
	•	関数は True/False を返す必要がある
	•	イテラブルはリストやタプルなど
　
①　偶数だけ 
nums = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, nums)
print(list(result))  # [2, 4]

② 長さ >= 4 の単語だけ取り出す
words = ["cat", "dog", "apple", "hi", "banana"]
result = list(filter(lambda word : len(word) >= 4 , words))
print(result)  # 期待される出力: ["apple", "banana"]

③　20以上の数だけ
nums = [5, 12, 17, 20, 25, 30]
result = list(filter(lambda x: x >= 20, nums))
print(result)  # [20, 25, 30]


⭐️アンパック
リストやタプル、辞書の中身をバラバラにして関数に渡す

① * は「リストやタプルの中身をバラす」
words = ["spam", "ham", "eggs"]
print(*words)
= print("spam", "ham", "eggs")
→
spam ham eggs

②　** は「辞書の中身をキーワード引数にして渡す」
options = {"sep": "&", "end": "!"}
print("spam", "ham", "eggs", **options)
= print("spam", "ham", "eggs", sep="&", end="!")
→
spam&ham&eggs!


words = ["spam", "ham", "eggs"]
options = {"sep": "&"}
print(*words, **options)
= print("spam", "ham", "eggs", sep="&")
→
spam&ham&eggs


⭐️リストとタプルの違い
# 🐍 タプルとリストの違いまとめ
| 特徴 　　　| リスト（list） 　　| タプル（tuple） |
|------　　　|----------------|----------------|
| 定義の仕方 | `[]`（角かっこ） | `()`（丸かっこ） |
| 変更　　　 | ✅ できる（追加・削除・変更OK） | ❌ できない（不変） |
| 速度 　　　| 少し遅い | 少し速い（固定長のため） |
| 使う場面 　| データを更新する場合 | データを固定して扱う場合 |
| 例　　　　 | `[1, 2, 3]` | `(1, 2, 3)` |

	
📚 タプルの特徴（immutable：変更不可）
	•	作ったあとで「要素の追加・削除・変更」ができません。
	•	そのため、安全に固定データを扱いたいとき に使います。
	•	例：座標、RGB値、設定情報など。
	•	要素が1つだけのタプルは、カンマが必要！
point = (10, 20)
print(point[0])  # 10
x = (5)     # これはただの数値
y = (5,)    # これはタプル！
print(type(x))  # <class 'int'>
print(type(y))  # <class 'tuple'>


🛠 リストの特徴（mutable：変更可能）
	•	要素を 追加・削除・並べ替え できます。
	•	よく使うメソッド：
nums = [1, 2, 3]
nums.append(4)    # [1, 2, 3, 4]
nums.remove(2)    # [1, 3, 4]
nums.sort()       # [1, 3, 4]


⭐️while 文と for 文の比較
while 文と for 文は以下のように使い分けると良い
    while 文: 繰り返す回数を柔軟に決めたいとき
		ループの冒頭に条件式によって「繰り返し処理を続けるかどうか」判定をおこなうため、
       「繰り返す回数はわからないが、繰り返し処理を終了する条件はわかっている」ときに有用
        たとえば、1 + 2 + 3 + ... と順に整数を足していったとき、何回目ではじめて 10000 を超えるか、を調べたいときなど
sum = 0
i = 0
while sum < 10000:
    sum += i
    i += 1
    if sum >= 10000:
        print(i,sum)
		
    for 文: 繰り返す回数が明確に決まっているとき
        break 文などの例外もあるが、for 文は in (イン) のうしろに書かれる値によってあらかじめ繰り返す回数が決められる
        また、リストなどの要素を先頭から順に取得することが簡単にできる
        たとえば、リストのすべての要素を出力したり、range 関数を使って 100 回同じことをしたいときなど
