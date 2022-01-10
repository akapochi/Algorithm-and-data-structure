# -*- coding: utf-8 -*-
"""アルゴリズムとデータ構造_第8回.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xuvs3PKHp8mUDrhAVTahLE4efdrWncgW

# 二分探索木

（共有用）第07回アルゴリズムとデータ構造.ipynbの最後に学んだ二分探索木について見ていく．以下のコードは（共有用）第07回アルゴリズムとデータ構造.ipynbの最後の部分に更にコードを追加している．

※`class`を用いたコーディングについて不安がある人は，渡辺先生の「プログラミング基礎同演習」のテキスト　https://kaityo256.github.io/python_zero/class/index.html　を参考に勉強してください．
"""

class Node: #Nodeのクラスを用意．

  def __init__(self, value): # クラスの初期化のためのメソッド __init__  https://docs.python.org/ja/3/reference/datamodel.html#object.__init__ を参照．
    self.value = value
    self.left = None
    self.right = None

  def __str__(self): # オブジェクトを文字列にして返すメソッド __str__  https://docs.python.org/ja/3/reference/datamodel.html#object.__str__ を参照．
    left = f'[{self.left.value}]' if self.left else '[]'
    right = f'[{self.right.value}]' if self.right else '[]'
    return f'{left} <- {self.value} -> {right}'


class BinarySearchTree: #BinarySearchTreeのクラスを用意．
  def __init__(self): # クラスの初期化のためのメソッド __init__
    self.nodes = [] # 最初は空

  def add_node(self, value): # ノードを追加．
    node = Node(value)
    if self.nodes: # self.nodesがNoneでなければif文の中に入る．

      parent, direction = self.find_parent(value)
      print("value:", value)
      print("parent:", parent)
      print("direction:", direction)
      print("-----")

      if direction == 'left':
        parent.left = node
      else:
        parent.right = node

    self.nodes.append(node)

  def find_parent(self, value): # 親を見つける．
    node = self.nodes[0]

    while node: # nodeがNoneでないあいだじゅうずっと以下が実行される
      p = node  # 戻り値の候補（親かもしれない）としてとっておく．
      if p.value == value:
        raise ValueError('Cannot add the value that is the same as the values already added.')
      if p.value > value:
        direction = 'left'
        node = p.left
      else:
        direction = 'right'
        node = p.right
    return p, direction

  """
  以降，（共有用）第07回アルゴリズムとデータ構造.ipynb にはない新たな記述
  """
  def search_node(self, value):
    p = self.nodes[0] # 根を指す：self.nodes[0]
    while True:
      # print(p.value)
      if p is None:
        return False
      if value == p.value: # valueといま見ているノードpの値p.valueが等しければTrueとする．
        return True
      elif value < p.value: # valueがいま見ているノードpの値p.valueより小さければ，ノードp.leftを見る．
        p = p.left
      else: # valueがいま見ているノードpの値p.valueより小さくないかつ等しくない場合は，ノードp.rightを見る．
        p = p.right

  def find_min(self):

    if self.nodes[0] is None:
      return None

    p = self.nodes[0]
    while p.left is not None: # p.leftが空になるまで（つまりpが葉になるまで）回す
      p = p.left

    return p.value

  def find_max(self):
    if self.nodes[0] is None:
      return None

    p = self.nodes[0]
    while p.right is not None: # p.leftが空になるまで（つまりpが葉になるまで）回す
      p = p.right

    return p.value

#  def remove_node(self, value): ### 発展問題 ###

"""## 二分探索木を生成し，ノード探索，最小値探索を実行

例1
"""

btree1 = BinarySearchTree() # btree1をクラスBinarySearchTreeのオブジェクトとする．
for v in [10, 20, 49, 4, 3, 9, 30]:
  btree1.add_node(v)

for node in btree1.nodes:
  print(node)

print(btree1.search_node(20))
print(btree1.find_min())
print(btree1.find_max())

#print(btree1.remove_node(99))

#for node in btree1.nodes:
#  print(node)

#print(btree1.remove_node(20))

#for node in btree1.nodes:
#  print(node)

"""例2"""

btree2 = BinarySearchTree() # btree1をクラスBinarySearchTreeのオブジェクトとする．
for v in [32, 54, 39, 49, 70, 12, 34]:
  btree2.add_node(v)

for node in btree2.nodes:
  print(node)

print(btree2.search_node(20))
print(btree2.find_min())
#print(btree1.find_max())

"""# ヒープ構造とヒープソート"""

def heap_sort(array):

  def down_heap(array, left, right): # array中のarray[left]からarray[right]の要素をヒープ化する関数を定義
    tmp = array[left] # 根

    parent = left
    while parent < (right+1) // 2:
      child_left = 2*parent + 1 # 左の子
      child_right = child_left + 1 # 右の子
      if child_right <= right and array[child_right] > array[child_left]:
        child = child_right
      else:
        child = child_left

      if tmp >= array[child]:
        break
      array[parent] = array[child]
      parent = child

    array[parent] = tmp
    print("parent,array[parent]=",parent,array[parent])
    print("array=",array)
    print("-----")


  for i in range((len(array)-1) // 2, -1, -1): # array[i]からarray[len(array)-1]をヒープ化
    print(i)
    down_heap(array, i, len(array)-1)


  print("****")
  print("heap structure=",array)
  print("****")

  for i in range(len(array)-1, 0, -1):
    array[0], array[i] = array[i], array[0] # 最大要素(array[0])と未ソート部末尾要素を交換
    down_heap(array, 0, i-1) # array[0]からarray[i-1]をヒープ化

"""例1"""

test_list1 = [53, 24, 96, 12, 32, 86]
print(test_list1)

heap_sort(test_list1)
print(test_list1)

"""例2"""

test_list2 = [3, 3, 2, 1, 3, 4, 0]

print(test_list2)

heap_sort(test_list2)
print(test_list2)

"""## Pythonの標準モジュール `heapq` を使った方法

公式ドキュメント https://docs.python.org/ja/3/library/heapq.html を参照．
"""

import random
import heapq


def heap_sort_heapq(array):
  heap = []
  for v in array:
    heapq.heappush(heap, v) # 上記公式ドキュメントによれば 「heapq.heappush(heap, item)　は，item を heap に push します．ヒープ不変式を保ちます．」
  return [heapq.heappop(heap) for _ in range(len(heap))]

random.shuffle(test_list2)
print(test_list2)

print(heap_sort_heapq(test_list2))
