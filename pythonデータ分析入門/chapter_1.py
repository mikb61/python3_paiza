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

# 値の参照
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
