class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def Traverse(self):
        if self.head is None:
            print("Singly Linked List is Empty!")
        else:
            a=self.head
            while a is not None:
                print(a.data, end="->")
                a=a.next 
    def insert_at_begin(self,data):
        print()
        nb=Node(data)
        nb.next=self.head
        self.head=nb

n1=Node(12)
sll=SinglyLinkedList()
sll.head=n1
n2=Node(33)
n1.next=n2
n3=Node(78)
n2.next=n3
n4=Node(23)
n3.next=n4

sll.Traverse()

sll.insert_at_begin(56)

sll.Traverse()

