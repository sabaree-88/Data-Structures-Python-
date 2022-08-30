from tkinter.messagebox import NO


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
    
    def insert_at_specified_position(self,position,data):
        print()
        
        nodePosition=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nodePosition.next=a.next
        a.next=nodePosition

n1=Node(31)
sll=SinglyLinkedList()
sll.head=n1
n2=Node(32)
n1.next=n2
n3=Node(34)
n2.next=n3
n4=Node(37)
n3.next=n4

sll.Traverse()

sll.insert_at_specified_position(3,35)

sll.Traverse()