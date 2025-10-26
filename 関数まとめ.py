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
