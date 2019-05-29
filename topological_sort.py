# -*- coding: utf-8 -*-
"""Graph (1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19smA3Q2q4FZpHuMLiN2CoH3Wz2BlAdg-
"""

class Node:
  def __init__(self, data):
    self.data = data
    self.neighbors = []
    self.visited = False
    
  def add_neighbor(self, neighbor):
    self.neighbors.append(neighbor)

  def set_visited(self, visited):
    self.visited = visited

  def get_data(self):
    return self.data

  def get_neighbors(self):
    return self.neighbors

  def get_visited(self):
    return self.visited


class Graph:
  def __init__(self):
    self.nodes = []

  def add_node(self, node):
    self.nodes.append(node)
  
  def topological_sort(self):
    stack = []
    if len(self.nodes) > 0:
      for node in self.nodes:
        node.set_visited(False)
        
    if len(self.nodes) > 0:
      for node in self.nodes:
        if node.get_visited() is False:
          node.set_visited(True)
          self.top_check(node, stack)
          
    for i in range(len(stack)):
      print(stack.pop(), end=" ")
    
  def top_check(self, new_node, stack):
    neighbors = new_node.get_neighbors()
    if neighbors is not None:
      for neighbor in neighbors:
        if neighbor.get_visited() is False:
          neighbor.set_visited(True)
          self.top_check(neighbor, stack)
    stack.append(new_node.get_data())
    
graph = Graph()

node_A = Node('A')
graph.add_node(node_A)
node_B = Node('B')
graph.add_node(node_B)
node_C = Node('C')
graph.add_node(node_C)
node_D = Node('D')
graph.add_node(node_D)
node_E = Node('E')
graph.add_node(node_E)
node_F = Node('F')
graph.add_node(node_F)
node_G = Node('G')
graph.add_node(node_G)
node_H = Node('H')
graph.add_node(node_H)
node_I = Node('I')
graph.add_node(node_I)
node_J = Node('J')
graph.add_node(node_J)

node_A.add_neighbor(node_B)
node_A.add_neighbor(node_F)

node_B.add_neighbor(node_H)

node_D.add_neighbor(node_C)
node_D.add_neighbor(node_E)
node_D.add_neighbor(node_I)

node_E.add_neighbor(node_I)

node_G.add_neighbor(node_A)
node_G.add_neighbor(node_B)
node_G.add_neighbor(node_C)

node_I.add_neighbor(node_C)

node_J.add_neighbor(node_E)

graph.topological_sort()