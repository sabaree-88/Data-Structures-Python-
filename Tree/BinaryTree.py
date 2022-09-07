class Tree:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key

    def inorderTra(self):
        
        if self.left:
            self.left.inorderTra()
        print(self.key,end=" ")
        if self.right:
            self.right.inorderTra()

    def preOrderTra(self):
       
        print(self.key,end=" ")
        if self.left:
            self.left.preOrderTra()
        if self.right:
            self.right.preOrderTra()
    
    def postOrderTra(self):
        
        if self.left:
            self.left.postOrderTra()
        if self.right:
            self.right.postOrderTra()
        print(self.key,end=" ")


root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.left.right=Tree(5)
root.right.left=Tree(6)
root.right.right=Tree(7)
root.right.left=Tree(18)

print("\nInorder Traversal: ")
root.inorderTra()
print("\nPreorder Traversal: ")
root.preOrderTra()
print("\nPostorder Traversal:")
root.postOrderTra()