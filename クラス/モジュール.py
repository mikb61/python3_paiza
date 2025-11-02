# モジュール（module）
Pythonのコードをまとめたファイルのこと。
他のファイルから読み込んで再利用することで、コードを整理・分割できる。

📄 モジュール = .py ファイル
例）mymodule.py というファイルを作ると、それが1つのモジュールになる。

# モジュールの利点
異なるモジュールどうしで同じ変数名を使える
コードの再利用ができる

# mymodule.py
def greet(name):
    print(f"Hello, {name}!")

# main.py
import mymodule

mymodule.greet("Marie")  # Hello, Marie!


🐍 Pythonの import の使い方まとめ
✅ 1. モジュール全体をインポート
import math

# mathモジュールの関数を使うときは、math. をつける
print(math.sqrt(9))  # 3.0
print(math.pi)       # 3.141592653589793

✅ 2. モジュールに別名をつけてインポート
import numpy as np

# np という短い名前でアクセスできる
arr = np.array([1, 2, 3])
print(arr)

✅ 3. モジュールの中の特定の関数だけをインポート
from math import sqrt

# sqrt() を直接使える
print(sqrt(16))  # 4.0

✅ 4. 特定の関数に別名をつけてインポート
from math import sqrt as s

print(s(25))  # 5.0

⚠️ 5. モジュールのすべてをインポート（非推奨）
from math import *

# すべての関数を使えるが、名前の衝突リスクが高い
print(sin(0))  # 0.0

💡 補足：複数モジュールを同時にインポート
import os, sys

print(os.name)
print(sys.version)

💬 ポイントまとめ
	•	import は 外部モジュール（標準 / 自作 / 外部ライブラリ）を読み込むための構文
	•	as を使うと短く呼び出せて便利
	•	from ... import ... で必要な関数だけを取り込める
	•	from ... import * は便利だが、名前が衝突するリスクがあるため非推奨


🐍 __name__ とは？

Pythonの特別な変数で、
**「このファイルが直接実行されたのか」「他のファイルからインポートされたのか」**を区別するために使う。

✅ 1. 基本の仕組み
# sample.py
print(__name__)

▶ 実行結果
python sample.py
# 出力: __main__

✅ 2. インポートされたときの挙動
# main.py
import sample

▶ 実行結果
python main.py
# 出力: sample

✅ 3. よく使われる定型パターン
テストコードやデモ実行部分を if __name__ == "__main__": に入れておくと、
import 時に実行されないようにできる

# sample.py
def greet():
    print("Hello from sample!")

# この下のブロックは、「直接実行されたときだけ」動く
if __name__ == "__main__":
    greet()
    print("sample.py was run directly!")


# main.py
import sample  # greet() は実行されない！
print("main.py is running!")

▶ 実行結果
python sample.py　→　Hello from sample!sample.py was run directly!
python main.py　→ main.py is running!



# 標準ライブラリ
あらかじめ用意されているモジュール群
どこに配置されたモジュールからでもインポートすることができる
標準ライブラリには、
 random モジュール
 math モジュール
 sys モジュール
などがある

# random モジュール
疑似乱数に関するモジュール
たとえば、次のコードで指定した範囲からランダムで整数を得ることができる

import random
n = random.randint(1, 5)
print(n)
→ 1~5のうちランダムで数字が出力される

## 🎲 randomモジュール（乱数関連）

| 関数 | 説明 | 使用例 |
|------|------|--------|
| `random()` | 0.0以上1.0未満の乱数を返す | `random.random()` |
| `randint(a, b)` | a以上b以下の整数をランダムに返す | `random.randint(1, 6)` |
| `uniform(a, b)` | a以上b以下の実数をランダムに返す | `random.uniform(0, 1)` |
| `choice(seq)` | シーケンスから1つランダムに選ぶ | `random.choice(['a', 'b', 'c'])` |
| `shuffle(seq)` | シーケンスの要素をシャッフルする（リストを直接変更） | `random.shuffle(cards)` |
| `sample(seq, k)` | シーケンスから重複なしでk個ランダムに選ぶ | `random.sample(range(10), 3)` |


# math モジュール
数学におけるさまざまな演算に関するモジュール
たとえば、次のコードで指定した数値の平方根を得ることができる

import math
x = math.sqrt(2)
print(x)
→ 1.14142135623730951

🧮 mathモジュール（数学関数）まとめ
✅ 基本的な数値計算
関数	説明	使用例
math.sqrt(x)	xの平方根（√x）を返す	math.sqrt(16) → 4.0
math.pow(x, y)	xのy乗を返す（x ** y と同等）	math.pow(2, 3) → 8.0
math.fabs(x)	絶対値をfloatで返す	math.fabs(-5) → 5.0
math.factorial(x)	xの階乗を計算（整数のみ）	math.factorial(5) → 120
⸻
🧭 切り上げ・切り捨て・丸め
関数	説明	使用例
math.ceil(x)	x以上の最小の整数（切り上げ）	math.ceil(3.2) → 4
math.floor(x)	x以下の最大の整数（切り捨て）	math.floor(3.7) → 3
math.trunc(x)	小数点以下を切り捨てて整数にする	math.trunc(3.9) → 3
math.modf(x)	小数部分と整数部分をタプルで返す	math.modf(3.14) → (0.14, 3.0)

⸻
📐 三角関数（ラジアン指定）
関数	説明	使用例
math.sin(x)	sin関数	math.sin(math.pi / 2) → 1.0
math.cos(x)	cos関数	math.cos(0) → 1.0
math.tan(x)	tan関数	math.tan(math.pi / 4) → 1.0
math.degrees(x)	ラジアン → 度 に変換	math.degrees(math.pi) → 180.0
math.radians(x)	度 → ラジアン に変換	math.radians(180) → 3.1415...

⸻
🧠 対数・指数関数
関数	説明	使用例
math.log(x)	自然対数（底e）	math.log(math.e) → 1.0
math.log10(x)	常用対数（底10）	math.log10(100) → 2.0
math.exp(x)	eのx乗	math.exp(1) → 2.718...

⸻
📏 定数
定数	説明	値の例
math.pi	円周率	3.141592653589793
math.e	ネイピア数（自然対数の底）	2.718281828459045
math.inf	無限大（infinity）	math.inf
math.nan	非数（Not a Number）	math.nan

⸻
💡 使用例まとめ

import math

print(math.sqrt(25))      # 5.0
print(math.ceil(3.2))     # 4
print(math.floor(3.8))    # 3
print(math.sin(math.pi))  # 0.0
print(math.log10(1000))   # 3.0
print(math.pi)            # 3.141592653589793



# sys モジュール
実行システムに関するモジュール
たとえば、次のコードで実行を強制終了することができる

import sys
sys.exit()
print("paiza")
→ 何も出力されない

## 🔹 主な機能一覧（sysモジュール）

| 関数・属性名 | 説明 | 使用例 |
|---------------|------|--------|
| `sys.argv` | コマンドライン引数をリストで取得 | `print(sys.argv)` |
| `sys.exit([code])` | プログラムを終了する（code は終了ステータス） | `sys.exit(0)` |
| `sys.version` | Python のバージョン情報を取得 | `print(sys.version)` |
| `sys.path` | モジュール探索パス（リスト） | `print(sys.path)` |
| `sys.platform` | 実行中の OS 名（例：`'win32'`, `'darwin'`, `'linux'`） | `print(sys.platform)` |
| `sys.getsizeof(obj)` | オブジェクトのメモリ使用量（バイト単位）を返す | `print(sys.getsizeof(1000))` |
| `sys.stdin` / `sys.stdout` / `sys.stderr` | 標準入出力ストリームを扱う | `sys.stdout.write("Hello")` |
| `sys.maxsize` | 整数の最大値（システム依存） | `print(sys.maxsize)` |
| `sys.modules` | 読み込まれているモジュール一覧（辞書型） | `print(sys.modules.keys())` |
