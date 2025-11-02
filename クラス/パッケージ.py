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
