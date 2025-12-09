class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder (root):#LDR
      if root is not None:
       inorder(root.left)
       print(str(root.key),end="-> ")
       inorder(root.right)
def preorder (root):#DLR
      if root is not None:
       print(str(root.key),end="-> ")
       preorder(root.left)
       
       preorder(root.right)

def postorder (root):#LRD
      if root is not None:
       postorder(root.left)
       postorder(root.right)
       print(str(root.key),end="-> ")

nodes=[10,20,30,40,50]
print("\n nodes in the binary tree : ",nodes)
root=Node(nodes[0])
root.left=Node(nodes[1])
root.right=Node(nodes[2])
root.left.left=Node(nodes[3])
root.left.right=Node(nodes[4])
print("\n inorder traversal: ",end=" ")
inorder(root)
print("\npreorder traversal: ",end=" ")
preorder(root)
print("\npostorder traversal: ",end=" ")

postorder(root)
