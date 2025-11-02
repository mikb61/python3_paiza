# 例外
コードを実行すると、エラーが発生し、実行が終了する場合がある。このようなとき「例外が発生した」「例外が送出された」という。

a = float("abc")

上記コードを実行すると、ValueError という例外が発生する
今回は、文字列 abc を浮動小数点数に変換できなかったために発生した

## 🧩 よく出る例外と原因（Python）

| 例外名 | 発生する原因 |
|:--|:--|
| `ZeroDivisionError` | 0で割ったとき |
| `ValueError` | 型は正しいが値が不正なとき（例：`int("abc")`） |
| `TypeError` | 型が不適切なとき（例：`"a" + 3`） |
| `IndexError` | 範囲外のインデックスにアクセスしたとき |
| `KeyError` | 存在しない辞書キーを指定したとき |
| `NameError` | 定義されていない変数を使ったとき |
| `AttributeError` | オブジェクトに存在しない属性やメソッドを使ったとき |
| `FileNotFoundError` | 存在しないファイルを開こうとしたとき |
| `ImportError` | モジュールや関数のインポートに失敗したとき |
| `RuntimeError` | その他の実行時エラーが発生したとき |


# 例外処理
コード実行時に発生する例外に対しておこなう処理のこと
例外処理を用意すると、例外によって実行が途中で終了しないようにすることができる

# try文
try:
    例外が発生しうる処理
except 予期される例外名:
    例外が発生したときにおこなう処理

try:
    a = float(input())
except ValueError:
    print("入力値は数字でなければなりません。")


1 つの except 節で、複数の例外を受けるようにすることができる
コードでは、except 節の例外名を書くところに例外名のタプルを書く

try:
    a = float(input())
    b = float(input())
    print(a / b)
except (ValueError, ZeroDivisionError):　　←このタプルについては、かっこを省略することはできない！
    print("入力値が正しくありません。")


except 節は複数用意することができる
except 節を複数用意した場合、発生した例外にマッチする except 節が上から順番に探索され、最初にマッチした except 節に処理が移る
コードでは、普段 except 節を書くときと同じように書く

try:
    a = float(input())
    b = float(input())
    print(a / b)
except ValueError:
    print("入力値は数字でなければなりません。")
except ZeroDivisionError:
    print("0 で割ることはできません。")


except 節で受ける例外には、その例外クラスの子孫にあたるクラスのものも含まれる
そのため、except 節で受ける例外のクラスを Exception にすると、ほとんどすべての例外を受けることができる

try:
    a = float(input())
    b = float(input())
    print(a / b)
except Exception:
    print("例外が発生しました。")

でも、曖昧でバグにつながりやすいので、できるだけ細かく例外を分類して記述した方がいい


例外クラスのインスタンスを生成することができる
e = ValueError("test1", "test2")
print(e.args)
例外クラスのインスタンスのメンバ変数 args には、コンストラクタに渡した引数の分だけ要素をもつタプルが代入される


# raise 文
意図的に例外を発生させることができる

raise 文の書き方 1:
raise 例外クラスのインスタンス

例:
raise ValueError("0 ≦ x ≦ 10 の整数を指定してください。")

例外クラスに渡した引数の値（= 例外クラスのインスタンスのメンバ変数 args の値）は、エラーメッセージに使われる

raise 文の書き方 2:
raise 例外クラス名

例:
raise ValueError

この場合、メンバ変数 args の値を設定できないため、「なぜエラーが発生したか」を詳細に伝えることができない


# 独自の例外クラスを定義
Exception クラスを継承してクラスを定義すると、独自の例外クラスを定義することができる
class InputValueError(Exception):
    pass

raise InputValueError("入力値は整数値でなければなりません。")



try:
    # 例外が発生するかもしれない処理
    x = int(input("数字を入力してください: "))
    print(10 / x)
except ValueError:
    # ValueError が発生したときの処理
    print("数字を入力してください！")
except ZeroDivisionError:
    # 0で割ろうとしたときの処理
    print("0では割れません！")
else:
    # 例外が発生しなかった場合の処理
    print("計算成功！")
finally:
    # 例外の有無に関わらず必ず実行される処理
    print("処理終了")

	•	try：例外が発生する可能性のある処理
	•	except：例外が発生した場合の処理
	•	else：例外が発生しなかった場合の処理
	•	finally：必ず実行される処理（後片付けなどに使う）
