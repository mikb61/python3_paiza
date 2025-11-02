1. パッケージとは？
	•	モジュールをまとめたもの
	•	モジュール = Python ファイル（*.py）
	•	パッケージ = モジュールを入れる「フォルダ」
	•	フォルダ内に __init__.py というファイルを置くことで Python はそのフォルダをパッケージとして認識する

mypackage/           ← パッケージ
    __init__.py      ← パッケージであることを示す
    module1.py       ← モジュール
    module2.py       ← モジュール


2. パッケージの使い方
(1) モジュールごとインポート
import mypackage.module1
mypackage.module1.func1()  # module1内の関数func1を呼ぶ

(2) モジュールから関数だけインポート
from mypackage.module1 import func1
func1()  # 直接呼べる

(3) パッケージ内のすべてをまとめて使う（__init__.py の設定次第）
from mypackage import module1
module1.func1()


3. サブパッケージも可能
パッケージの中にさらにフォルダを作ってサブパッケージにできる
mypackage/
    __init__.py
    module1.py
    subpackage/
        __init__.py
        module2.py

from mypackage.subpackage import module2
module2.func2()


4. ポイントまとめ
	1.	パッケージ = モジュールのフォルダ
	2.	モジュール = Python ファイル
	3.	__init__.py があるとパッケージとして認識される
	4.	import / from … import … で呼び出し方を選べる
	5.	サブパッケージで階層的に整理可能


💡 例えると：
	•	モジュール = 「本」
	•	パッケージ = 「本棚」
	•	サブパッケージ = 「本棚の引き出し」
	•	import は「本棚から本を取り出すこと」、from … import … は「本棚から本の特定の章だけ取り出すこと」



＿＿＿＿＿＿＿＿＿＿＿

1. サブモジュールとは？
	•	サブモジュール = パッケージの中にあるモジュール
	•	つまり、あるパッケージ内の Python ファイル (*.py) を指します
	•	サブモジュールは 親パッケージと同じ階層にある他のモジュールと同じ扱い です

例
mypackage/                ← パッケージ
    __init__.py
    module1.py            ← サブモジュール
    module2.py            ← サブモジュール
    subpackage/           ← サブパッケージ
        __init__.py
        module3.py        ← サブモジュール

	•	module1.py と module2.py は mypackage のサブモジュール
	•	module3.py は mypackage.subpackage のサブモジュール


2. 同じパッケージ内のモジュールを使う場合
相対インポートが可能

# module1.py から module2.py を使う場合
from . import module2    # module2は同じmypackage内
module2.func2()

	•	. は 同じパッケージ内 を指す
	•	サブパッケージ内なら .. で 1階層上のパッケージ を指すことも可能
