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


    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.key,end=" ")
        if self.right:
            self.right.inorder()

root=BST(None)
root.insert(20)
root.insert(5)
root.insert(25)
root.inorder()
root.search(6)