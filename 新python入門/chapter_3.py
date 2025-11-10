# coding: utf-8
# for inによるループ処理
for カウンタ変数 in 繰り返す範囲:
    繰り返し処理

# 繰り返しの回数を指定するrange関数
range(10) 0から9まで、10回繰り返す
range(6, 11) 6から10まで繰り返す

# for inによるループ処理
for i in range(5):
    print("ハロー、paizaラーニング")
→
ハロー、paizaラーニング
ハロー、paizaラーニング
ハロー、paizaラーニング
ハロー、paizaラーニング
ハロー、paizaラーニング

# for inによるループ処理
for i in range(6):
    print(str(i))
→
0
1
2
3
4
5

# for inによるループ処理
for i in range(1, 13):
    print(str(i) + '月')
→
1月
2月
3月
4月
5月
6月
7月
8月
9月
10月
11月
12月

# coding: utf-8
# whileによるループ処理

カウンタ変数を初期化
while 条件式:
    繰り返し処理
    カウンタ変数を更新


# whileによるループ処理
i = 0
while i <= 4:
    print("ハロー、paizaラーニング")
    i = i + 1
→
ハロー、paizaラーニング
ハロー、paizaラーニング
ハロー、paizaラーニング
ハロー、paizaラーニング
ハロー、paizaラーニング


# whileによるループ処理
i = 0
while i <= 5:
    print(str(i))
    i = i + 1
→
0
1
2
3
4
5


# 代入演算子
演算子　使用例	意味　　　　　　　　　　	別の書き方
+=	　　a += 1	a変数の値を1増加させる。	a = a + 1と同じ
-=	　　a -= 1	a変数の値を1減少させる。	a = a - 1と同じ


# whileによるループ処理
i = 5
while i <= 15:
    print(str(i))
    i += 1
→
5
6
7
8
9
10
11
12
13
14
15

# whileによるループ処理
i = 5
while i >= 1:
    print(str(i))
    i -= 1
→
5
4
3
2
1

# html プルダウンリストの基本形
<select name='age'>
  <option>1才</option>
  <option>2才</option>
  <option>3才</option>
</select>

# html 箇条書きの基本形
<ul>
  <li>1才</li>
  <li>2才</li>
  <li>3才</li>
</ul>

# HTMLによる箇条書き
print("<ul>")
for i in range(100):
    print("<li>" + str(i + 1) + "</li>")
print("</ul>")
→
・1
・2
 :
・100


# 標準入力から1行読み込む
line = input()

# coding: utf-8
# 標準入力
line = input()
print(line)

# coding: utf-8
# 標準入力
number = int(input())
print(number * 100)

# 複数行読み込みの基本形
# coding: utf-8
# 標準入力とループ処理
count = int(input())
print("データ個数 " + str(count))
for i in range(count):
    line = input().rstrip()
    print("hello " + line)

# rsrtrip()
データの行末の改行を削除する。
改行が残っていると、その後の処理に悪影響を及ぼすことがあるので、ここで削除。
インプットの後に、ドットに続けて記述することで、インプットの戻り値の改行を削除することができる。
line = input().rstrip()


# coding: utf-8
# 標準入力とループ処理
count = int(input())
for i in range(count):
    print("スライムがあらわれた")
→（入力値 8)
スライムがあらわれた
スライムがあらわれた
スライムがあらわれた
スライムがあらわれた
スライムがあらわれた
スライムがあらわれた
スライムがあらわれた
スライムがあらわれた

# coding: utf-8
# 標準入力とループ処理
num1 = int(input())
num2 = int(input())
for i in range(num1, num2 + 1):
    print(i)
→（入力値 5, 12)
5
6
7
8
9
10
11
12

# coding: utf-8
# 西暦年と昭和年の対応表
# 1926年から1988年までをループで出力
# ループ内で、各西暦年を昭和年に変換

for seireki in range(1926, 1989):
    print("西暦" + str(seireki) + "年は", end = "")
    shouwa = seireki - 1925
    print("昭和" + str(shouwa) + "年です")
→
西暦1926年は昭和1年です
西暦1927年は昭和2年です
西暦1928年は昭和3年です
...
西暦1988年は昭和63年です
