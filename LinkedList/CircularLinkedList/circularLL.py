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

n1=Node(8)
sll=SinglyLinkedList()
sll.head=n1
n2=Node(6)
n1.next=n2
n3=Node(7)
n2.next=n3
n4=Node(4)
n3.next=n4
n4.next=n1

sll.Traverse()