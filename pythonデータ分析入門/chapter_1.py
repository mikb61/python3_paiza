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
import pandas as pd

s = pd.Series({"a": 3, "b": 1, "c": 2})
print(s.index)  # インデックスの取得
s.index = ["d", "e", "f"]  # インデックスの書き換え

s = pd.Series([3, 1, 2]) 
print(s.index)  # RangeIndex
