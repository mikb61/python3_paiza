# 🧩 Python 主要データ型メソッドまとめ

Pythonの主要データ型（リスト・タプル・辞書・集合）のメソッド一覧です。  
この表を押さえておくと、基本操作はすべてカバーできます。

---

## 📋 リスト（list）

| メソッド | 説明 | 例 |
|-----------|------|----|
| `append(x)` | 末尾に要素を追加 | `a = [1,2]; a.append(3)` → `[1,2,3]` |
| `extend(iterable)` | 他のリストを結合 | `a.extend([4,5])` → `[1,2,3,4,5]` |
| `insert(i, x)` | 指定位置に要素を挿入 | `a.insert(1, 99)` → `[1,99,2,3]` |
| `remove(x)` | 最初に見つかったxを削除 | `a.remove(2)` |
| `pop(i)` | i番目を取り出して削除 | `a.pop(0)` → `1` |
| `sort()` | 昇順に並べ替え | `a.sort()` |

	•	sort() → リスト限定・中身を直接変更（破壊的）
	•	sorted() → どんなイテラブルもOK・新しいリストを返す（非破壊的）

| `reverse()` | 要素を逆順に並べ替え | `a.reverse()` |
| `count(x)` | xの出現回数 | `[1,2,2,3].count(2)` → `2` |
| `index(x)` | 最初に出るxの位置 | `[10,20,30].index(20)` → `1` |
| `copy()` | リストのコピーを作成 | `b = a.copy()` |

---

## 🧱 タプル（tuple）

| メソッド | 説明 | 例 |
|-----------|------|----|
| `count(x)` | xの出現回数 | `(1,2,2,3).count(2)` → `2` |
| `index(x)` | 最初に出るxの位置 | `(10,20,30).index(30)` → `2` |

> 📝 タプルは「変更不可（immutable）」なので、  
> append・removeなどの操作はできません。

---

## 🗝️ 辞書（dict）

| メソッド | 説明 | 例 |
|-----------|------|----|
| `keys()` | すべてのキーを返す | `{"a":1,"b":2}.keys()` → `dict_keys(['a','b'])` |
| `values()` | すべての値を返す | `{"a":1,"b":2}.values()` → `dict_values([1,2])` |
| `items()` | (キー,値)のペアを返す | `{"a":1,"b":2}.items()` → `dict_items([('a',1),('b',2)])` |
| `get(key, default)` | keyの値を取得（存在しない時はdefault） | `d.get('x', 0)` → `0` |
| `update(dict)` | 他の辞書で更新 | `d.update({"c":3})` |
| `pop(key)` | 指定キーを削除し値を返す | `d.pop("a")` |
| `clear()` | 全要素削除 | `d.clear()` |
| `copy()` | 辞書のコピーを作成 | `new = d.copy()` |

---

## 🧮 集合（set）

| メソッド | 説明 | 例 |
|-----------|------|----|
| `add(x)` | 要素を追加 | `s.add(4)` |
| `remove(x)` | 要素を削除（存在しないとエラー） | `s.remove(2)` |
| `discard(x)` | 要素を削除（存在しなくてもOK） | `s.discard(10)` |
| `pop()` | 任意の要素を削除して返す | `s.pop()` |
| `clear()` | 全要素削除 | `s.clear()` |
| `union(t)` | 和集合を返す | `a.union(b)` |
| `intersection(t)` | 積集合を返す | `a.intersection(b)` |
| `difference(t)` | 差集合を返す | `a.difference(b)` |
| `symmetric_difference(t)` | 対称差を返す | `a.symmetric_difference(b)` |
| `issubset(t)` | 部分集合か判定 | `a.issubset(b)` |

---

## 🧠 覚え方のヒント

- **リストは「順番重視」**：`append`, `insert`, `pop`
- **辞書は「キー操作」**：`.keys()`, `.values()`, `.items()`
- **集合は「集合演算」**：`union`, `intersection`, `difference`
- **タプルは「読み取り専用」**：`count`, `index` しか使えない！

---

📘 **おすすめ練習法**
```python
# 例：dictの練習
student = {"name":"Taro","age":20,"city":"Tokyo"}

print(student.keys())     # dict_keys(['name','age','city'])
print(student.get("age")) # 20
print(list(student.items())) # [('name','Taro'),('age',20),('city','Tokyo')]
