# Singly Linked List
# 
# A linked list is a list that is liknked to nodes.
# The first node is called the Head.
# The last node is called the Tail.
# The Null signifies it's the end of the list.
# The tail or last node points to Null.
# Each node points to the next node by means of a pointer.
# It is a data structure consisting of a group of nodes that together represent a sequence.
# Ex.
# 
class Node:
  def __init__(self, element):
      self.element = element
      self.next = None

# creating object from Node Class
# nodeImplement = Node(10) 