#Create Node
class Node:
    #Constructor
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

#Create Doubly Linked List
class doubly_linkedList:
    #constructor
    def __inti__(self):
        self.data=None
    
    #forward Travarsal
    def f_traverse(self):
        a=self.head
        while a is not None:
            print(a.data,end=" ")
            a=a.next

    #backward traversal
    def b_traverse(self):
        #first traverse in forward
        a=self.head
        while a.next is not None:
            a=a.next

        #backward traverse
        while a is not None:
            print(a.data, end=" ")
            a=a.prev 

    #delete the first node in the list
    def deletion_at_begin(self):
        a=self.head
        self.head=a.next
        a.next=None
        self.head.prev=None
    
    #delete the last element in the list
    def deletion_at_end(self):
        a=self.head.next
        prev=self.head
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None
        a.prev=None

    #delete the specified node in list
    def deletion_at_specified_position(self,position):
        a=self.head.next
        prev=self.head
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next.prev=prev
        a.next=None
        a.prev=None



n1=Node(12)
dll=doubly_linkedList()
dll.head=n1
n2=Node(13)
n2.prev=n1
n1.next=n2
n3=Node(10)
n3.prev=n2
n2.next=n3
n4=Node(29)
n4.prev=n3
n3.next=n4

dll.f_traverse()
print()
dll.b_traverse()
#print()
#dll.deletion_at_begin()
#print()
#dll.f_traverse()
#print()
dll.deletion_at_specified_position(3)
print()
dll.f_traverse()
