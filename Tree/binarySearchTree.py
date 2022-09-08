class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None

#Inorder Traversal
def inorder(root):
    if root is not None:
        inorder(root.left)

        print(str(root.key)+"->",end=" ")

        inorder(root.right)


#insert function
def insert(node,key):
    if node is None:
        return Node(key)

    if key<node.key:
        node.left=insert(node.left,key)
    
    else:
        node.right=insert(node.right,key)

    return node


#find inorder successor

def minValueNode(node):
    current=node
    while (current.left is not None):
        current=current.left

    return current

#deletion

def deleteNode(root,key):
    if root is None:
        return root

    if key<root.key:
        root.left=deleteNode(root.left,key)

    elif key>root.key:
        root.right=deleteNode(root.right,key)

    else:
        #node having only one child or no child
        if root.left is None:
            temp=root.right
            root=None
            return temp

        elif root.right is None:
            temp=root.left
            root=None
            return temp

        #if the node has two childern , place the inorder successor in position

        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=deleteNode(root.right,temp.key)
        temp=minValueNode(root.left)
        root.key=temp.key
        root.left=deleteNode(root.left,temp.key)


    return root


root=Node(5)
root=insert(root,10)
root=insert(root,3)
root=insert(root,4)
root=insert(root,2)
root=insert(root,7)
root=insert(root,8)

inorder(root)
print("\n")
root=deleteNode(root,7)
print("\n")
inorder(root)
