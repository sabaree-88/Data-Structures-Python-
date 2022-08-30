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

    def delete_at_begin(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None

n1=Node(31)
sll=SinglyLinkedList()
sll.head=n1
n2=Node(32)
n1.next=n2
n3=Node(33)
n2.next=n3
n4=Node(34)
n3.next=n4

sll.Traverse()

sll.delete_at_begin()

sll.Traverse()