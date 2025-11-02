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


⭐️chatGPTの練習問題

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("残高不足")

    def transfer(self, amount, other_account):
        if self.balance >= amount:
            self.withdraw(amount)
            other_account.deposit(amount)
        else:
            print("残高不足")

    def show_balance(self):
        print(self.balance)




class Character:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    def attack(self, target, damage):
        target.hp -= damage
        if target.hp <= 0:
            target.hp = 0  # 倒れたら負の値を防ぐ
            print(f"{target.name}は倒れた")

    def heal(self, amount):
        self.hp += amount

    def use_magic(self, cost):
        if self.mp >= cost:
            self.mp -= cost
        else:
            print("魔力不足")

    def status(self):
        print(self.name, self.hp, self.mp)





class Hero:

    total_heroes = 0

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.inventory = []
        Hero.total_heroes += 1

    def attack(self, target, damage):
        target.hp -= damage
        if target.hp <= 0:
            target.hp = 0
            print(f"{target.name}は倒れた")

    def heal(self, amount):
        self.hp += amount

    def use_magic(self, cost):
        if self.mp >= cost:
            self.mp -= cost
        else:
            print("魔力不足")

    def pick_item(self, item):
        self.inventory.append(item)

    def show_status(self):
        print(self.name, self.hp, self.mp, self.inventory)

    @classmethod
    def show_total_heroes(cls):
        print(cls.total_heroes)



1. クラスメソッドとは？
	•	通常のメソッドは インスタンスを操作 → self が最初の引数
	•	クラスメソッド は クラス自体を操作 → cls が最初の引数
	•	デコレーター @classmethod をつける

class MyClass:
    count = 0  # クラス変数

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def show_count(cls):
        print(cls.count)

 なぜ便利？
	1.	インスタンスを作らなくても呼べる → クラス全体の情報を扱える
	2.	継承時に便利 → サブクラスでも cls は自分のクラスを指す



class Hero:

    total_heroes = 0

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        Hero.total_heroes += 1

    def attack(self, target, damage):
        target.hp -= damage
        if target.hp <= 0:
            target.hp = 0
            print(f"{target.name}は倒れた")

    def show_status(self):
        print(self.name, self.hp, self.mp)

    @classmethod
    def show_total_heroes(cls):
        print(cls.total_heroes)


class Mage(Hero):

    def attack(self, target, damage):
        print(f"{self.name}は魔法で攻撃！")
	    super().attack(target, damage)  # 元の Hero.attack() を呼ぶ
          もしくは、
		target.hp -= damage
        if target.hp <= 0:
            target.hp = 0
            print(f"{target.name}は倒れた")

    def use_magic(self, cost):
        if self.mp >= cost:
            self.mp -= cost
            print(f"{self.name}は魔力を{cost}消費した")
        else:
            print("魔力不足")
