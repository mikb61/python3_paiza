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
