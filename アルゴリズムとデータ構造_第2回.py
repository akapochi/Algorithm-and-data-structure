# -*- coding: utf-8 -*-
"""第2回アルゴリズムとデータ構造.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Js0j7Ni4dRm6f_cu-lAkTr2VHBUxWKQX

# その1 : 関数の定義

Pythonでは，関数は以下のようにして定義される．
```
def 関数名(引数名1, 引数名2, ...):
    処理
    return 戻り値1, 戻り値2, ...
```
上の関数は`引数名1`，`引数名2`，... を入力し，`戻り値1`,`戻り値2`,...を出力する．
これについては，渡辺先生の「プログラミング基礎同演習」のテキスト

https://kaityo256.github.io/python_zero/scope/index.html

や，プログラミング言語 Python情報サイトのゼロからのPython入門講座にある

https://www.python.jp/train/function/index.html

を参考にすると良い．


2つの値`a`と`b`の加減乗除（算術演算）を行う関数を定義し，見ていこう．
"""

def arithmetic_operation(a, b):
  summation = a + b
  diff = a - b
  product = a * b
  ratio = a / b
  return summation, diff, product, ratio

"""これを実行する．"""

arithmetic_operation(12,8)

"""## エラーメッセージを見てみよう

入力数が不足していると，下記のようになる．
"""

arithmetic_operation(1)

"""入力数が多すぎると，下記のようになる．"""

arithmetic_operation(1,2,3)

"""## 複数の値の代入

代入演算子の両辺は複数の変数，値を取ることもできる．
```
a, b = 100, 200
```
と，
```
a = 100
b = 200
```
は同じことを行っている．これを応用して，下記のように書くことができる．
"""

ao1, ao2, ao3, ao4 = arithmetic_operation(12,8)
print(ao1, ao2, ao3, ao4)

"""## ローカル変数とグローバル変数

*   関数の中で代入した変数は，すべて**ローカル変数**となります．
*   もう一つの変数は**グローバル変数**です．ローカル変数以外の，関数の外部で代入された変数は，すべてグローバル変数になります．

これについては，渡辺先生の「プログラミング基礎同演習」のテキスト

https://kaityo256.github.io/python_zero/scope/index.html

や，
プログラミング言語 Python情報サイトのゼロからのPython入門講座にある

https://www.python.jp/train/function/local_var.html

を参考にすると良い．

ローカルスコープの外では，ローカル変数は未定義となっている．
"""

print(diff)

"""# その2 : リストの操作

渡辺先生の「プログラミング基礎同演習」のテキスト

https://kaityo256.github.io/python_zero/list/index.html

を参考にすると良い．

## リストに要素を追加する方法
リストに要素を追加あるいは結合する方法として，`append()`, `extend()`, `insert()`, `+`演算子やスライスについて見ていく．

### `append()`メソッド

リストに要素を追加する方法として，リストのメソッドである`append()`を見ていく．

第01回で見た`range()`関数を用いて初期リストを生成し，そのリストに要素を追加することを見ていく．

`range()`関数については，

https://docs.python.org/ja/3/tutorial/controlflow.html#the-range-function
https://docs.python.org/ja/3/library/stdtypes.html#range

を参照．
"""

my_list1 = list(range(5))
print(my_list1)

my_list1.append(512) # リスト末尾に数値512を追加
print(my_list1)

my_list1.append('new_str') # 文字列new_strをリスト末尾に追加
print(my_list1)

my_list1.append([128, 256, 512]) # リスト[128, 256, 512]をリスト末尾に追加
print(my_list1)

print(my_list1[7]) # appendメソッドはリストを追加することもできるが，結合はされない．

"""### `extend()`メソッド
リストにリストを結合する方法として，リストのメソッドである`extend()`を見ていく．
"""

my_list2 = list(range(4))
print(my_list2)

my_list2.extend([128, 256, 512]) # extendメソッドはリストを結合する．
print(my_list2)

print(my_list2[5]) # extendメソッドはリストにリストを結合することができる．

my_list2.extend('new_str') # 文字列の場合は1文字ずつ追加される．
print(my_list2)

"""### `+`演算子

リストにリストを結合する方法として，`+`演算子を見ていく．
"""

my_list3 = list(range(5))
print(my_list3)

my_list4 = my_list3 + [5, 6] # +でリストを結合
print(my_list4)

print(my_list3)
my_list3 += [5,6]
print(my_list3)

"""### `insert()`メソッド

指定した位置に要素を追加挿入する方法として，リストのメソッド`insert()`を見ていく．
"""

my_list5 = list(range(6))
print(my_list5)

my_list5.insert(0, 128) #要素0に数128を追加
print(my_list5)

my_list5.insert(2, 256) #要素2に数256を追加
print(my_list5)

my_list5.insert(-1, 512) #負の数の場合は-1が末尾の一つ前になる．
print(my_list5)

my_list5.insert(-2, 1024) #負の数の場合は-1が末尾の一つ前になる．
print(my_list5)

my_list5.insert(0, [-512, -256, -128]) #要素0にリスト[-512, -256, -128]を追加（結合はされない）
print(my_list5)

print(my_list5[0], my_list5[1]) # 結合はされていない

"""### スライス`:`

リストやタプルのすべての要素を追加挿入あるいは代入する方法として，スライス`:`を用いる方法を見ていく．
"""

my_list6 = list(range(3))
print(my_list6)

my_list6[1:1] = [128, 256, 512] #1番めの要素にリスト[128, 256, 512]を追加挿入する．
print(my_list6)
print(my_list6[2])

print(my_list6)
my_list6[1:3] = [-8192, -4096, -2048] #1番めから2番めの要素にリスト[-8192, -4096, -2048]を代入する．
print(my_list6)

"""## リストから要素を削除する方法
リストから要素を削除する方法として，`claer()`, `pop()`, `remove()`やインデックスやスライスで位置・範囲を指定した`del`文について学ぶ．

### `clear()`メソッド

すべての要素が削除され，空のリストにするリストのメソッド`clear()`
"""

my_list7 = list(range(0,32,3))
print(my_list7)

my_list7.clear() # リストのメソッドclear()によって空のリストが生成される．
print(my_list7)

"""### `pop()`メソッド

指定した位置の要素を削除し，その要素の値を取得するリストのメソッド`pop()`
"""

my_list8 = list(range(16))
print(my_list8)

print(my_list8.pop(0))
print(my_list8)

print(my_list8.pop(2))
print(my_list8)

print(my_list8.pop(-1))
print(my_list8)

print(my_list8.pop(-2))
print(my_list8)

print(my_list8.pop()) #引数なしの場合はリストの最後が選ばれる．
print(my_list8)

"""### `remove()`メソッド

指定された値と同じ要素を検索し，最初の要素を削除するリストのメソッド`remove()`を見ていく．
"""

my_list9 = [0, 1, 1, 2, 1, 3, 4, 2, 3, 5, -3]
print(my_list9)

my_list9.remove(4) #値が4である最初の要素を削除
print(my_list9)

my_list9.remove(2) #値が2である最初の要素を削除
print(my_list9)

"""### `del`文

インデックス・スライスで位置・範囲を指定して要素を削除する`del`文について見ていく．
"""

my_list10 = list(range(10))
print(my_list10)

del my_list10[0] #0番目の要素を削除
print(my_list10)

del my_list10[-1] #-1番目の要素（最後の要素）を削除
print(my_list10)

del my_list10[-3] #-3番目の要素（最後から3番めの要素）を削除
print(my_list10)

del my_list10[2] #2番目の要素を削除
print(my_list10)

my_list11 = list(range(10))
print(my_list11)

del my_list11[3:5] #3番目から4番目の要素を削除
print(my_list11)

del my_list11[:2] #0番目（最初）から1番目の要素を削除
print(my_list11)

del my_list11[4:] #4番目から最後の要素を削除
print(my_list11)

del my_list11[-2:] #最後から2番めから最後まで削除
print(my_list11)

my_list12 = list(range(32))
print(my_list12)

del my_list12[:] #リスト全要素を削除
print(my_list12)

my_list13 = list(range(16))
print(my_list13)

del my_list13[2:12:2]
#スライスは最初 : 最後 : ステップの記法であるから，2番目の要素から11番めの要素まで2ステップずつ削除（2, 4, 6, 8, 10のインデックスの要素を削除）
print(my_list13)

del my_list13[::4] #最初の要素（0番目の要素）から最後の要素まで4ステップずつ削除（0, 4, 8, ...のインデックスの要素を削除）
print(my_list13)

"""### リスト内包表記

条件を満たす要素を削除する（条件を満たさない要素を残す）ことを行うリスト内包表記
"""

my_list14 = list(range(16))
print(my_list14)

my_list15 = ([i for i in my_list14 if i % 2 == 0]) #iが2で割り切れる場合のみ残す
print(my_list15)
print(my_list14)

"""## その他

### `len()`関数

リストのサイズを取得する方法として，`len()`を見ていく．
"""

my_list16 = [0, 2, 4, 6, 8, 10]
print(len(my_list16))

"""### リストの「複製」

渡辺先生の「プログラミング基礎同演習」のテキスト

https://kaityo256.github.io/python_zero/list/index.html

の「メモリ上でのリストの表現」を参照するとよい．

なお，下記のコードで使われている`id()`はPythonの組み込み関数であり，オブジェクトの**識別値**を返す．

https://docs.python.org/ja/3/library/functions.html#id

を参照すると良い．

#### メモリ上のリストの表現
"""

my_list17 = [1,2,3]
my_list17_copy = my_list17
print("my_list17=",my_list17,", id of my_list17=",id(my_list17))
print("my_list17_copy=",my_list17_copy,", id of my_list17_copy=",id(my_list17_copy))

my_list17_copy[1] = 4
print("my_list17=",my_list17,", id of my_list17=",id(my_list17))
print("my_list17_copy=",my_list17_copy,", id of my_list17_copy=",id(my_list17_copy))

my_list17_copy.append(10)
print("my_list17=",my_list17,", id of my_list17=",id(my_list17))
print("my_list17_copy=",my_list17_copy,", id of my_list17_copy=",id(my_list17_copy))

my_list17_copy = [3,2,4,8]
print("my_list17=",my_list17,", id of my_list17=",id(my_list17))
print("my_list17_copy=",my_list17_copy,", id of my_list17_copy=",id(my_list17_copy))

my_list17_copy[1] = 100
print("my_list17=",my_list17,", id of my_list17=",id(my_list17))
print("my_list17_copy=",my_list17_copy,", id of my_list17_copy=",id(my_list17_copy))

my_list17_copy.append(200)
print("my_list17=",my_list17,", id of my_list17=",id(my_list17))
print("my_list17_copy=",my_list17_copy,", id of my_list17_copy=",id(my_list17_copy))

"""### `copy.copy()`や`copy.deepcopy()`

Pythonの標準ライブラリ`copy`を用いてリストの「複製」を行う．詳細は，

https://docs.python.org/ja/3/library/copy.html

を参照すると良い．

#### 浅いコピー`copy.copy()`
"""

import copy
my_list18 = [[1,2],[3,4]]
my_list18_copy = copy.copy(my_list18)
print("my_list18=",my_list18,", id of my_list18=",id(my_list18))
print("my_list18_copy=",my_list18_copy,", id of my_list18_copy=",id(my_list18_copy))

my_list18_copy[1][1] = 8
print("my_list18=",my_list18,", id of my_list18=",id(my_list18))
print("my_list18_copy=",my_list18_copy,", id of my_list18_copy=",id(my_list18_copy))

"""`id(my_list18)`と`id(my_list18_copy)`は異なるIDなのに，`my_list[1][1]`の値も変わっている．二次元配列の要素のリストのidを見てみる．"""

print("id(my_list18[0])=",id(my_list18[0]),",id(my_list18[1])=",id(my_list18[1]),",id(my_list18_copy[0])=",id(my_list18_copy[0]),",id(my_list18_copy[1])=",id(my_list18_copy[1]))

"""#### 深いコピー`copy.deepcopy()`"""

my_list19 = [[1,2],[3,4]]
my_list19_deepcopy = copy.deepcopy(my_list19)
print("my_list19=",my_list19,", id of my_list19=",id(my_list19))
print("my_list19_deepcopy=",my_list19_deepcopy,", id of my_list19_deepcopy=",id(my_list19_deepcopy))

my_list19_deepcopy[1][1] = 8
print("my_list19=",my_list19,", id of my_list19=",id(my_list19))
print("my_list19_deepcopy=",my_list19_deepcopy,", id of my_list19_deepcopy=",id(my_list19_deepcopy))

"""念の為，先程と同様に二次元配列の要素のリストのidを見てみる．"""

print("id(my_list19[0])=",id(my_list19[0]),",id(my_list19[1])=",id(my_list19[1]),",id(my_list19_deepcopy[0])=",id(my_list19_deepcopy[0]),",id(my_list19_deepcopy[1])=",id(my_list19_deepcopy[1]))

"""### 要素の値がランダムなリストを作成する．"""

import random
#randomについては， https://docs.python.org/ja/3/library/random.html を参照のこと
random.seed(2) #random.seed()についてはこのページのrandom.seedの項を参照のこと．引数は乱数の種(seed)と呼ばれる．
my_list20 = [random.randint(1,6) for _ in range(12)] #random.randint(a, b)はa<=N<=bであるようなランダムな整数Nを返す．for _ in range(12)で12回それを繰り返している．
print(my_list20)

"""練習 : 0から9までのランダムな整数からなる要素数10のリストmy_list_aと100から109までのランダムな整数からなる要素数15のリストmy_list_bを作成し，その後，リストmy_list_aの後ろにリストmy_list_bを**結合**したリストmy_list_cを作成する．（「追加」ではなく「結合」であることに注意）"""

import random
random.seed(3)
my_list_a = [random.randint(0,9) for _ in range(10)]
print(my_list_a)
my_list_b = [random.randint(100,109) for _ in range(15)]
print(my_list_b)
my_list_c = my_list_a + my_list_b
print(my_list_c)

"""# その3 : 数の表現方法とビット演算

## 数の表現方法

### 2進数表現

非負整数を2進数で表現してみる．
"""

a = 27
bin(a) #0bは2進数(binary number)であることを表すプレフィックス

a = 54
bin(a) #0bは2進数(binary number)であることを表すプレフィックス

"""### 16進数表現

非負整数を16進数で表現してみる．
"""

a = 27
hex(a) #0xは16進数(hexadecimal)であることを表すプレフィックス

a = 54
hex(a) #0xは16進数(hexadecimal)であることを表すプレフィックス

"""### 8進数表現

非負整数を8進数で表現してみる．
"""

a = 27
oct(a) #0oは8進数(octal)であることを表すプレフィックス

a = 54
oct(a) #0oは8進数(octal)であることを表すプレフィックス

"""プレフィックス`0b`, `0o`, `0x`をつけることで，整数型`int`の数値を記述できる．　"""

bin_int = 0b101 #0bは2進数(binary number)であることを表すプレフィックス
oct_int = 0o101 #0oは8進数(octal)であることを表すプレフィックス
hex_int = 0x101 #0xは16進数(hexadecimal)であることを表すプレフィックス
print(bin_int)
print(oct_int)
print(hex_int)

"""### 32ビット

32ビットに格納できる符号なし整数／符号付き整数の範囲
"""

0b11111111111111111111111111111111 # 32個の1が並んでいる，0bは2進数(binary number)であることを表すプレフィックス

0b1111111111111111111111111111111 # 31個の1が並んでいる，0bは2進数(binary number)であることを表すプレフィックス

"""### 64ビット

64ビットに格納できる符号なし整数／符号付き整数の範囲
"""

0b1111111111111111111111111111111111111111111111111111111111111111 # 64個の1が並んでいる，0bは2進数(binary number)であることを表すプレフィックス

0b111111111111111111111111111111111111111111111111111111111111111 # 63個の1が並んでいる，0bは2進数(binary number)であることを表すプレフィックス

"""### 小数の表現"""

1 + 1 + 1 == 3 # 整数値なのでピッタリ合う

0.1 + 0.1 + 0.1 == 0.3 # 浮動小数点なのでピッタリ合わない

from decimal import Decimal
# decimal については　https://docs.python.org/ja/3/library/decimal.html　を参照のこと

print(Decimal.from_float(0.1)) # from_float の説明は上記ページの from_float(f) の部分を参照のこと．
print(Decimal.from_float(0.1 + 0.1 + 0.1))
print(Decimal.from_float(0.3))

"""float型の最大値，最小値"""

import sys
# sys については https://docs.python.org/ja/3/library/sys.html?highlight=sys#module-sys を参照のこと．
print(sys.float_info.max) # float_info.max については上記ページの float_info の部分の max を参照のこと．
print(sys.float_info.min) # float_info.max については上記ページの float_info の部分の min を参照のこと．

"""## ビット演算

### ビットシフト演算

ビットシフト演算は`<<`, `>>`で表される．前者は左ビットシフト，右ビットシフトである．
"""

x = 27
print(bin(x))
print(x << 1) # x << 1　はxについて，1ビット分左ビットシフトを行う．
print(bin(x << 1)) # x << 1　はxについて，1ビット分左ビットシフトを行う．

x = 27
print(bin(x))
print(x << 2) # x << 2　はxについて，2ビット分左ビットシフトを行う．
print(bin(x << 2)) # x << 2　はxについて，2ビット分左ビットシフトを行う．

x = 54
print(bin(x))
print(x >> 1) # x >> 1　はxについて，1ビット分右ビットシフトを行う．
print(bin(x >> 1)) # x >> 1　はxについて，1ビット分右ビットシフトを行う．

x = 54
print(bin(x))
print(x >> 2) # x >> 2　はxについて，2ビット分右ビットシフトを行う．
print(bin(x >> 2)) # x >> 2　はxについて，2ビット分右ビットシフトを行う．

"""### 論理演算

論理演算`AND`,`OR`,`XOR`に対応する演算子は`&`,`|`,`^`である．
"""

x = 9
y = 10
print(bin(x))
print(bin(y))
print(x & y, bin(x & y)) # x と y の論理積(AND)
print(x | y, bin(x | y)) # x と y の論理和(OR)
print(x ^ y, bin(x ^ y)) # x と y の排他的論理和(XOR)

"""練習 : 値xを2進数表示（ビット表示）した時，一つのビットだけ反転した値zをすべて書き出す．

例）x=5とすると，5の2進数表示（ビット表示）は101であるから，2進数表示で100, 111, 001なるz，すなわち，4, 7, 1を書き出す．

x = 235 について見ていこう．
"""

x = 235
binLength = len(bin(x)) - 2
for n in range(binLength):
  y = 2 ** n
  z = x - y if bin(x)[-n-1] == "1" else x + y
  print(x, z, bin(x), format(z, '08b'), bin(x)[-n-1] == "1")

"""### その他（負の整数の取り扱い）"""

x = -1
print(bin(x))

x = -1
print(bin(x & 0xff)) # 8ビット表現での補数表現

x = -2
print(bin(x & 0xff)) # 8ビット表現での補数表現

x = -3
print(bin(x & 0xff)) # 8ビット表現での補数表現

"""ビット反転は`~`演算子で表される．ただし，ビット反転は，単純に各ビットを反転した値ではなく，`~x`は`-(x+1)`となる値を返す．

参考 : https://docs.python.org/ja/3/reference/expressions.html#unary-arithmetic-and-bitwise-operations
"""

x = 10
print(bin(x))
print(~x)
print(bin(~x))
print(bin(~x & 0xff)) # 8ビット表現での補数表現