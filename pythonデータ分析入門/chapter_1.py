# pandasにおけるデータの基本単位であるSeriesの作成方法

import pandas as pd
# 辞書によるseriesの作成
s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s)
→
a    3   #a,b,c: ラベル　という
b    1
c    2
dtype: int64

# 単一の値によるseriesの作成
ind = ["a", "b", "c"]
s2 = pd.Series(1, index=ind)
print(s2)
→
a    1
b    1
c    1
dtype: int64

# ラベルが重複したseriesの作成
s3 = pd.Series([3, 1, 2], index=["a", "a", "c"])
print(s3)
→
a    3
a    1
c    2
dtype: int64

⭐️ 値の参照
s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s["a"]) 
→ 3

print(s["b":"c"])
→
b    1
c    1　　← ラベルでスライシングした時は終点も含まれる！
dtype: int64

print(s[1:2])
→
b    1
dtype: int64

ind = ["a", "c"]
print(s[ind])
→
a    3
c    2
dtype: int64

⭐️更新、追加、削除
s = pd.Series({"a": 3, "b": 1, "c": 2})
s["a"] = 813　# 更新
s["d"] = 100  # 追加
del s["a"]  # del文による削除
print(s.pop("a"))  # 値の削除と削除された値の取得
print(s.drop("a"))  # 要素を削除した新しいSeriesを返す（元のシリーズは変更しない）


⭐️Series同士の演算
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
t = pd.Series({"b": 11, "c": 22, "a": 33})

print(s + t)
→
a    36
b    12
c    24
dtype: int64

# 欠損値がある場合
s = pd.Series({"a": 3, "b": 1, "c": 2})
t = pd.Series({"b": 11, "d": 22, "a": 33})
print(s + t)
→
a    36.0
b    12.0
c     NaN　←型はfloat
d     NaN
dtype: float64

# Seriesとスカラーの演算
s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s * 10)
→
a    30
b    10
c    20
dtype: int64


⭐️Seriesの属性

# index属性
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s.index)  # インデックスの取得
→
Index(['a', 'b', 'c'], dtype='object')

s.index = ["d", "e", "f"]  # インデックスの書き換え
→
d    3
e    1
f    2
dtype: int64

s = pd.Series([3, 1, 2]) 
print(s)
→ ラベルがない場合、0から順番に整数が振られる
0    3
1    1
2    2
dtype: int64

s = pd.Series([3, 1, 2]) 
print(s.index)  # RangeIndex
→
RangeIndex(start=0, stop=3, step=1)

# name属性
import pandas as pd

s = pd.Series([3, 1, 2], name="nums")
print(s.name)  # 名前の取得
→ nums

new_s = s.rename("values")  # 名前の付け替え
print(new_s)  # 名前の取得
→ values

s.rename("values", inplace=True)  # sそのものの名前の変更
print(s)
→
0    3
1    1
2    2
Name: values, dtype: int64

s.index.name = "chars"  # インデックスのname属性を指定
print(s)
→
chars
0    3
1    1
2    2
Name: nums, dtype: int64


# dtype属性

import pandas as pd

s = pd.Series([3, 1, 2], name="nums")
print(s.dtype)  # dtypeの取得
→
int64

print(s)
→
0    3
1    1
2    2
Name: nums, dtype: int64

s = pd.Series([3, 1, 2], name="nums", dtype="float64")  # dtypeを指定
print(s)
→
0    3.0
1    1.0
2    2.0
Name: nums, dtype: float64


⭐️フィルタリング
# Seriesとスカラーの比較演算
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s > 1)
→
a     True
b    False
c     True
dtype: bool

# bool値のSeriesによるフィルタリング
print(s[s > 1])
→
a    3
c    2
dtype: int64

# Series同士のビット演算
p = pd.Series([True, True, False])
q = pd.Series([True, False, False])

print(p & q)
→
0     True
1    False
2    False
dtype: bool

print(p | q) # or
→
0     True
1     True
2    False
dtype: bool

print(~p)　# not
→
0    False
1    False
2     True
dtype: bool

# 複数条件のフィルタリング
t = pd.Series([3, 5, 15])
print(t[(t % 3 == 0) & (t % 5 == 0)])
→
2    15
dtype: int64

s = pd.Series({"a": 1, "b": 4, "c": 7})
print(s[(s > 2) & (s < 7)])
→
b    4
dtype: int64


⭐️ソート
import pandas as pd

s = pd.Series({"b": 3, "c": 1, "a": 2})

# インデックスによるソート
print(s.sort_index())  # 昇順
→
a    2
b    3
c    1
dtype: int64

print(s.sort_index(ascending=False))  # 降順
→
c    1
b    3
a    2
dtype: int64

# 値によるソート
print(s.sort_values())  # 昇順
→
c    1
a    2
b    3
dtype: int64

print(s.sort_values(ascending=False))  # 降順
→
b    3
a    2
c    1
dtype: int64
