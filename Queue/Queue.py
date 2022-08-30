class Queue:
    #constructor
    def __init__(self):
        self.queue = []

    #insert the element in queue
    def enqueue(self,item):
        self.queue.append(item)

    #remove the element in queue    
    def dequeue(self):
        if len(self.queue)<1:
            return None
        return self.queue.pop(0)

    #display the element in the queue
    def display(self):
        print(self.queue)

    #size of the queue
    def size(self):
        return len(self.queue)
#intatiate the variable with the class
q=Queue()

#assigning the value
q.enqueue(3)
q.enqueue(7)
q.enqueue(8)
q.enqueue(6)
q.enqueue(2)
q.enqueue(1)
q.enqueue(4)

#display the element in the queue
q.display()

#remove the element in queue
q.dequeue()

print("After remove the element in queue")

q.display()

    