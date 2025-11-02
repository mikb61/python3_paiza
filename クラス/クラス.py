# クラス
共通の特徴をもったデータの分類のこと
型と呼ばれることもある
例: int, str, list など...

# オブジェクト
「クラス」に属する個々の実体のこと
「クラス」にしたがって生成される
例: 1, "abc", [1, 2, 3] など...

# インスタンス
「クラス」に属する個々の実体のこと
「クラス」にしたがって生成される
例: 1, "abc", [1, 2, 3] など...

#「オブジェクト」と「インスタンス」の使い分け
オブジェクト: 広く「クラス」から生成された実体を指すときに、よく使われる
インスタンス: 実体が、どの「クラス」から生成されたか、を強調したいときに、よく使われる


class クラス名:
    処理

class Person:
age = 1000
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def add_age(self, year):
        self.age += year

    def add_and_print_age(self, year):
        self.add_age(year)
        print(self.age)
  
kirishima = Person("Kirishima", 15)
print(kirishima.name, kirishima.age) → Kirishima, 15

kirishima.age = 26
print(kirishima.age) → Kirishima, 26

kirishima.add_age(2)
print(kirishima.age)  → 28

kirishima.add_and_print_age(4) → 32

print(kirishima.age) → 32

print(Person.age) → 1000

# コンストラクタ
クラスを定義するときに定義する __init__ 関数（ダンダーイニット関数）をコンストラクタと呼ぶ
コンストラクタとは、インスタンスが生成されるときに呼び出されるメソッドのこと
インスタンスが生成されるときに、1 度だけ呼び出される
コンストラクタの役割は主にメンバ変数を用意すること
Python でコンストラクタの名前は __init__ と決まっている
コンストラクタの仮引数のうち、第 2 引数以降の仮引数には、インスタンスを生成するときに指定した実引数が渡される

# クラス変数
そのクラスから生成されるすべてのインスタンスで共通して使うことができる変数のこと
クラス変数とメンバ変数の変数名が重複した場合は、メンバ変数が優先される



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, year):
        self.age += year

    def add_and_print_age(self, year):
        self.add_age(year)
        print(self.age)


people = [Person("Kirishima", 15), Person("Rokumura", 14), Person("Midori", 13)]
for person in people:
    print(person.name, person.age)

→
kirishima 15
Rokumura 14
MIdori 13


# プライベート変数
アクセス制限がかかった変数で、クラスの外側からメンバ変数を自由に使うことができない変数のこと
他のプログラミング言語では用意できるものが多いが、Python において完全なプライベート変数を用意することはできない


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def print_profile(self):
        print(f"名前: {self.name}, 年齢: {self.__age}")


kirishima = Person("Kirishima", 15)

kirishima.__age += 1000  →エラー
print(kirishima.__age)　→エラー

kirishima._Person__age += 1000　　→_Person（_クラス名）をつけるとエラーが解消される
print(kirishima._Person__age)　→_Person（_クラス名）をつけるとエラーが解消される

kirishima.print_profile()


# 継承
すでに定義したクラスからさらに細かい分類のクラスを作ること
継承されるクラス : スーパークラス, 親クラス
継承したクラス : サブクラス, 子クラス
サブクラスでは、スーパークラスのメンバ変数やメソッドを使える

サブクラス名のうしろの括弧のなかでスーパークラスにしたいクラスの名前を書く

class サブクラス名(クラス名1, ..., クラス名2):
    処理

「処理」のところは、普段クラスを定義するときと同様に、メソッドなどを書く
サブクラスで定義するメソッドの名前は、スーパークラスで定義してあるメソッドの名前と同じでもよい
