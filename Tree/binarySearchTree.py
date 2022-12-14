from tkinter import N


class BST:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    
    #insert function
    def insert(self,data):
        #tree is empty
        if self.key is None:
            self.key = data
            return
        #tree has the one or two node check the condition (decide which position to insert the new node (left or right))
        if self.key>data:
            if self.left:
                self.left.insert(data)
            else:
                self.left=BST(data)
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right=BST(data)
    #searching
    def search(self,data):
        if self.key == data:
            print("Node is FOUND!")
            return
        if data < self.key:
            if self.left:
                self.left.search(data)
            else:
                print("Node is not present in the Tree!")
        else:
            if self.right:
                self.right.search(data)
            else:
                print("Node is not present in the Node")

    #deletion
    def delete(self,data):
        if self.key is None:
            print("Tree is empty!")
            return
        if data < self.key:
            if self.left:
                self.left=self.left.delete(data)
            else:
                print("The given node is not present in the tree!")
        elif data > self.key:
            if self.right:
                self.right=self.right.delete(data)
            else:
                print("The given node is not present in the tree!")
        else:
            if self.left is None:
                temp=self.right
                self=None
                return temp
            if self.right is None:
                temp=self.left
                self=None
                return temp
            node = self.right
            while self.left:
                node=self.left
            self.key = node.key
            self.right = self.right.delete(node.key)
        return self
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key,end=" ")
        if self.right:
            self.right.inorder()
    
    def preorder(self):
        print(self.key,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.key,end=" ")
def count(node):
    if node is None:
        return 0
    return 1+count(node.left)+count(node.right)
    
root=BST(15) 
root.insert(31)
root.insert(23)
root.insert(76)
root.insert(90)
root.insert(12)
root.insert(10)
root.insert(8)
root.insert(3)    
print("inorder")
root.inorder()
print()
print("preorder")
root.preorder()
print()
print("postorder")
root.postorder()