# 🧩 pandas — Series と DataFrame の完全まとめ

pandas は Python のデータ解析ライブラリ。ここでは **Series（1次元）** と **DataFrame（2次元）** の違い、作り方、基本操作をまとめています。

---

## 概要

| 名前 | 概要 | 使いどころ |
|------|------|------------|
| **Series** | 1次元のラベル付き配列（値 + インデックス） | 1列分のデータ（例：身長だけ） |
| **DataFrame** | 2次元の表（行 × 列） | 複数列からなる表（例：名前・年齢・身長） |

---

## Series の作り方 & イメージ

    import pandas as pd

    s = pd.Series([100, 200, 300], index=["A", "B", "C"])
    print(s)

**出力イメージ**

    A    100
    B    200
    C    300
    dtype: int64

**ポイント**
- インデックス（`A`, `B`, `C`）を持つ。
- `s["A"]` のようにラベルでアクセスできる。
- numpy と親和性が高く、ベクトル演算が可能：`s * 2` など。

---

## DataFrame の作り方 & イメージ

    import pandas as pd

    df = pd.DataFrame({
        "名前": ["田中", "佐藤", "鈴木"],
        "年齢": [25, 30, 28],
        "身長": [170, 165, 180]
    })
    print(df)

**出力イメージ**

       名前  年齢   身長
    0  田中  25  170
    1  佐藤  30  165
    2  鈴木  28  180

**ポイント**
- 各列が `Series` になっている（例：`df["年齢"]` は Series）。
- 行ラベル（インデックス）と列ラベル（カラム名）を持つ。
- 表計算・結合・欠損値処理など多数の高機能メソッドあり。

---

## Series と DataFrame の関係（要点）

- `DataFrame` の 1 列が `Series`。
- `type(df["身長"])` → `pandas.Series`
- `df[["身長"]]`（二重ブラケット）は `DataFrame` を返す（列を DataFrame として抜きたいとき）。

---

## よく使う基本操作（コードはインデントで示す）

- 先頭・末尾確認

    df.head()      # 先頭5行（引数で数を指定可）
    df.tail()      # 末尾5行

- 統計量

    df.describe()  # 数値列の基本統計量（count、mean、std、min、max 等）

- 列アクセス / 新しい列の作成

    ages = df["年齢"]           # Series を返す
    df["BMI"] = df["体重"] / (df["身長"]/100) ** 2  # 列演算で新列追加

- 行・列の選択（主な方法）

    df.loc[0, "名前"]      # ラベル指定（行ラベル、列ラベル）
    df.loc[:, "年齢"]      # 全行の「年齢」列（Series）
    df.iloc[0, 1]          # 整数位置で指定（位置ベース）

- フィルタリング（条件抽出）

    df[df["年齢"] > 25]    # 年齢が25より大きい行を取得

- 列を複数選択（DataFrame を返す）

    df[["名前", "身長"]]

- ソート

    df.sort_values("身長", ascending=False)

- 欠損値処理

    df.isnull()            # 欠損値のブールマスク
    df.dropna()            # 欠損行を削除
    df.fillna(0)           # 欠損を指定値で埋める

- 結合（SQL 的な join）

    pd.merge(df1, df2, on="id", how="inner")  # 内部結合など

---

## Series / DataFrame の内部は NumPy ベース
- 高速なベクトル計算（なるべくループではなくベクトル演算を使う）
- 型は列ごとに統一されやすい（数値列は数値型にキャストされる）

---

## よくある間違い（Tips）
- `df["col1", "col2"]` はエラー。複数列は `df[["col1", "col2"]]`（二重ブラケット）。
- `df["col"].mean()` は `Series` の平均。`df.mean()` は DataFrame の列ごとの平均。
- 行を直接変更する際は `.loc` を使う（チェイン割当の警告を避ける）。

---

## ミニサンプル（実践フロー）

1. CSV 読み込み

    df = pd.read_csv("data.csv")

2. 基本確認

    df.head()
    df.info()
    df.describe()

3. 欠損確認・処理

    df.isnull().sum()
    df = df.dropna(subset=["重要列"])

4. 集計（グループ化）

    df.groupby("カテゴリ")["数値列"].mean()

5. 出力

    df.to_csv("out.csv", index=False)

---

## まとめ（覚えておくこと）
- **Series = 1列 / 1次元**、**DataFrame = 表 / 2次元**  
- DataFrame の列は Series で扱える  
- ベクトル演算を使うと高速かつ簡潔に書ける  
- `loc`/`iloc`/`merge`/`groupby` は頻出API
---

### 参考
- pandas 公式ドキュメント: https://pandas.pydata.org/pandas-docs/stable/


⭐️
# DataFrameの作成(Seriesを値とする辞書)  
import pandas as pd

s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t})
print(df)
→
   num string
a  3.0  paiza
b  1.0    NaN
c  NaN  daiza

# index引数とculums引数による行名・列名の指定
import pandas as pd

s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t},
                  index=["c", "a", "b", "d"], columns=["string", "num", "new"])
print(df)
→
  string  num  new
c  daiza  NaN  NaN
a  paiza  3.0  NaN
b    NaN  1.0  NaN
d    NaN  NaN  NaN


# DataFrameの作成(辞書を値とする辞書)  
import pandas as pd

s = {"a": 3, "b": 1}
t = {"a": "paiza", "c": "daiza"}
df = pd.DataFrame({"num": s, "string": t})
print(df)
→
   num string
a  3.0  paiza
b  1.0    NaN
c  NaN  daiza


# DataFrameの作成(リストを値とする辞書)  
import pandas as pd

df = pd.DataFrame({"num": [3, 1], "string": ["paiza", "daiza"]}, index=["a", "b"])
print(df)
→
   num string
a    3  paiza
b    1  daiza


⭐️行・列・セルの参照

import pandas as pd

s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t})

# 列名による列の参照
print(df["num"])

# 属性による列の参照
print(df.num)
 属性参照によって列を参照する場合、列名はPythonの変数名として適切なものになっている必要がある。
 たとえば`"paiza.io"`を列名とした場合、属性参照を用いることはできない（ドットの手前で意図せず区切られてしまう）。
 この場合でも列名による参照は可能。
→
a    3.0
b    1.0
c    NaN
Name: num, dtype: float64

# loc属性による行の参照
print(df.loc["b"])


# iloc属性による行の参照
print(df.iloc[1])

→
num       1.0
string    NaN
Name: b, dtype: object


# at属性によるセルの参照
print(df.at["a", "string"])

# iat属性によるセルの参照
print(df.iat[0, 1])

→
paiza

# at属性によるセルの更新
df.at["a", "string"] = "pizza"

# iat属性によるセルの更新
df.iat[0, 1] = "pizza"

print(df)
→
   num string
a  3.0  pizza
b  1.0    NaN
c  NaN  daiza


⭐️スライシング

import pandas as pd

s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
u = pd.Series({"b": True})
df = pd.DataFrame({"num": s, "string": t, "bool": u})

   num string  bool
a  3.0  paiza   NaN
b  1.0    NaN  True
c  NaN  daiza   NaN

# 行に関するスライシング
print(df["b":"c"])
print(df[1:3])  # 整数インデックス
→
   num string  bool
b  1.0    NaN  True
c  NaN  daiza   NaN

# 列に関するスライシング
print(df.loc[:, "string":])
→
  string  bool
a  paiza   NaN
b    NaN  True
c  daiza   NaN

# 行と列を同時にスライシング
print(df.loc[:"b", "string":])
→
  string  bool
a  paiza   NaN
b    NaN  True


# locとilocによる個別の行・列指定
print(df.loc[["a", "c"], ["num", "bool"]])
print(df.iloc[[0, 2], [0, 2]])
→
   num bool
a  3.0  NaN
c  NaN  NaN


⭐️更新・追加・削除
import pandas as pd

s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t})

   num string
a  3.0  paiza
b  1.0    NaN
c  NaN  daiza


# 更新
df["num"] = pd.Series({"a": 300, "b": 100})
     num string
a  300.0  paiza
b  100.0    NaN
c    NaN  daiza

# シリーズで列の追加
df["bool"] = pd.Series({"b": True})
   num string  bool
a  3.0  paiza   NaN
b  1.0    NaN  True
c  NaN  daiza   NaN

# スカラーで列の追加
df["bool"] = False
   num string   bool
a  3.0  paiza  False
b  1.0    NaN  False
c  NaN  daiza  False

# loc属性で行の追加
df.loc["d"] = pd.Series({"num": 813, "string": "pizza"})
     num string
a    3.0  paiza
b    1.0    NaN
c    NaN  daiza
d  813.0  pizza


# concatメソッドで行・列の追加
print(pd.concat([df, pd.DataFrame({"num": 813, "string": "paiza", "bool": True}, index = ["d"])]))
     num string  bool
a    3.0  paiza   NaN
b    1.0    NaN   NaN
c    NaN  daiza   NaN
d  813.0  paiza  True


# 列の削除
del df["string"]　 # delメソッド

print(df.pop("string"))  # popメソッド
a    paiza
b      NaN
c    daiza
Name: string, dtype: object

print(df)
   num  bool
a  3.0   NaN
b  1.0  True
c  NaN   NaN

# 列の削除(dropメソッド）
print(df.drop("string", axis=1))

   num  bool
a  3.0   NaN
b  1.0  True
c  NaN   NaN


# 行の削除(dropメソッド）
print(df.drop("a"))
   num string  bool
b  1.0    NaN  True
c  NaN  daiza   NaN


・pandas.DataFrameのdropメソッドは引数でinplace=TrueとすることでもとのDataFrameに変更を加えるようになる（この際、メソッドの返り値はNoneになる）
・inplace引数とaxis引数を組み合わせれば行・列の削除に関する操作をdropメソッドで統一的におこなうことができる


⭐️DataFrame同士の演算
import pandas as pd


df1 = pd.DataFrame({"num": {"a": 1, "b": 2, "d": 4},
                    "string": {"a": "paiza", "d": "daiza"}})
   num string
a    1  paiza
b    2    NaN
d    4  daiza

df2 = pd.DataFrame({"num": {"a": 10, "c": 30, "d": 40},
                    "name": {"c": "pizza", "d": ".io"}})
   num   name
a   10    NaN
c   30  pizza
d   40    .io

print(df1 + df2)
   name   num  string
a   NaN  11.0     NaN
b   NaN   NaN     NaN
c   NaN   NaN     NaN
d   NaN  44.0     NaN

print(df1 * 2)
   num      string
a    2  paizapaiza
b    4         NaN
d    8  daizadaiza


⭐️フィルタリング
import pandas as pd

s = pd.Series({"a": 3, "b": 1})
t = pd.Series({"a": "paiza", "c": "daiza"})
df = pd.DataFrame({"num": s, "string": t})
   num string
a  3.0  paiza
b  1.0    NaN
c  NaN  daiza

# ブール値のSeriesによるフィルタリング
print(df[df["num"] > 2])

# queryメソッドによるフィルタリング
print(df.query("num > 2"))

   num string
a  3.0  paiza

🧩 クエリとは？
	•	定義：データベースやデータセットに対して「こういう条件でデータを取り出したい」と命令すること
	•	目的：必要な情報だけを取り出したり、集計したり、更新したりする

print(df.query("num > 2 or string == 'daiza'"))

s = "daiza"
print(df.query("num > 2 or string == @s"))

num string
a  3.0  paiza
c  NaN  daiza


⭐️ソート
import pandas as pd

s = [3, 1, 2]
t = ["paiza", "daiza", "pizza"]
df = pd.DataFrame({"string": t, "num": s}, index=["c", "a", "b"])
  string  num
c  paiza    3
a  daiza    1
b  pizza    2

print(df.sort_index())  # 行の昇順
  string  num
a  daiza    1
b  pizza    2
c  paiza    3

print(df.sort_index(ascending=False))  # 行の降順
  string  num
c  paiza    3
b  pizza    2
a  daiza    1

print(df.sort_index())  # 列の昇順
   num string
c    3  paiza
a    1  daiza
b    2  pizza

print(df.sort_index(ascending=False))  # 列の降順
  string  num
c  paiza    3
a  daiza    1
b  pizza    2

print(df.sort_values(by="num"))  # 値の昇順
  string  num
a  daiza    1
b  pizza    2
c  paiza    3

print(df.sort_values(by="num", ascending=False))  # 値の降順
  string  num
c  paiza    3
b  pizza    2
a  daiza    1
