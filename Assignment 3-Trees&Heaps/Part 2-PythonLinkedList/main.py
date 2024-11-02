# A Linked List Node

class Node:
  def __init__(self, data=None):
    self.data = data
    self.left = None
    self.right = None


class Bst:
  def __init__(self, root=None):
    self.root = root

  def add(self, data):
    if self.root is None:
      self.root = Node(data)
    else:
      current = self.root
      while current is not None:
        if (current.data > data):
          if (current.left is None):
            current.left = Node(data)
            return
          else:
            current = current.left
        else:
          if (data > current.data):
            if (current.right is None):
              current.right = Node(data)
              return
            else:
              current = current.right



binaryTree = Bst()
binaryTree.add(10)
binaryTree.add(5)
binaryTree.add(8)
binaryTree.add(4)
binaryTree.add(15)
print(binaryTree.root.data)
print(binaryTree.root.left.data)
print(binaryTree.root.right.data)
print(binaryTree.root.left.left.data)
print(binaryTree.root.left.right.data)