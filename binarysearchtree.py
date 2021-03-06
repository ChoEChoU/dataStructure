# -*- coding: utf-8 -*-
"""BinarySearchTree.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J7HJtzxJWvsSeOfHtZ2ufxRum4gwQbkJ
"""

class Node:
  
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    
  def set_left(self, left):
    self.left = left
    
  def set_right(self, right):
    self.right = right
    
  def get_left(self):
    return self.left
  
  def get_right(self):
    return self.right
  
  def get_key(self):
    return self.key
  
class Binary_search_tree:
  
  def __init__(self):
    self.root = None
  
  def get_root(self):
    return self.root
  
  def search(self, key):
    return self.check(self.root, key)
  
  def check(self, node, key):
    if node is None:
      return None
    
    if node.get_key() == key:
      return node
    elif node.get_key() > key:
      return self.check(node.get_left(), key)
    else:
      return self.check(node.get_right(), key)
    
  def insert(self, node):
    if self.root is None:
      self.root = node
    else:
      self.insert_node(self.root, node)
    
  def insert_node(self, parent, node):
    if parent.get_key() > node.get_key():
      if parent.get_left() is None:
        parent.set_left(node)
      else:
        return self.insert_node(parent.get_left(), node)
    else:
      if parent.get_right() is None:
        parent.set_right(node)
      else:
        return self.insert_node(parent.get_right(), node)
    
  def print_tree(self):
    self.print_node(self.root, 0)
      
  def print_node(self, node, depth):
    if node is not None:
      msg = ""
      for i in range(0, depth):
        msg += " "
      msg += str(node.get_key())
      print(msg)
      self.print_node(node.get_left(), depth + 1)
      self.print_node(node.get_right(), depth + 1)
    
bst = Binary_search_tree()      
    
node_40 = Node(40)
bst.insert(node_40)
node_15 = Node(15)
bst.insert(node_15)
node_69 = Node(69)
bst.insert(node_69)
node_8 = Node(8)
bst.insert(node_8)
node_25 = Node(25)
bst.insert(node_25)
node_54 = Node(54)
bst.insert(node_54)
node_86 = Node(86)
bst.insert(node_86)
node_5 = Node(5)
bst.insert(node_5)
node_10 = Node(10)
bst.insert(node_10)
node_20 = Node(20)
bst.insert(node_20)
node_30 = Node(30)
bst.insert(node_30)
node_50 = Node(50)
bst.insert(node_50)
node_66 = Node(66)
bst.insert(node_66)
node_83 = Node(83)
bst.insert(node_83)
node_90 = Node(90)
bst.insert(node_90)

result = bst.search(66)
if result is None:
  print("fail")
else:
  print("success")

result = bst.search(67)
if result is None:
  print("fail")
else:
  print("success")
  
print("---------------")
bst.print_tree()