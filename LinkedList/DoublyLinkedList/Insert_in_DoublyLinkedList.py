class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Doubly_linked_list:
    def __init__(self):
        self.data=None
    
    def insert_at_beigning(self,data):
        n_beg=Node(data)
        a=self.head
        a.prev=n_beg
        n_beg.next=a
        self.head=n_beg


    def insert_at_end(self,data):
        nend=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=nend
        nend.prev=a

    def insert_at_specified_node(self,position,data):
        ni=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        ni.prev=a
        ni.next=a.next
        a.next.prev=ni
        a.next=ni

    def forwardTraverse(self):
        print()
        if self.head is None:
            print("Doubly Linked List is Empty!")
        else:
            a=self.head
            while a is not None:
                print(a.data, end=" ")
                a=a.next

    def backwardTraversal(self):
        print()
       
        if self.head is None:
            print("Doubly Linked List is Empty!")

        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=" ")
                a=a.prev


n1=Node(5)
dll=Doubly_linked_list()
dll.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
n3=Node(15)
n3.prev=n2
n2.next=n3
n4=Node(20)
n4.prev=n3
n3.next=n4

dll.backwardTraversal()
dll.insert_at_beigning(2)
dll.forwardTraverse()
dll.insert_at_end(21)
dll.forwardTraverse()
dll.insert_at_specified_node(2,21)
dll.backwardTraversal()

