モジュール（module） は、Pythonのコードをまとめたファイルのこと。
他のファイルから読み込んで再利用することで、コードを整理・分割できる。

📄 モジュール = .py ファイル
例）mymodule.py というファイルを作ると、それが1つのモジュールになる。


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


