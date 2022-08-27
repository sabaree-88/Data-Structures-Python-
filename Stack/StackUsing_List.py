#Create an Stack using list
print("*********STACK*********")
stack = [] #empty stack
n= int (input("Enter the number of item in stack:"))

def insertElement():
    #insert the element in stack
    for i in range(n):
        stack.append(input())
    print("Stack elements are:", stack)

def removeElement():
    #remove the element in stack
    print("Before removing element in stack:", stack)
    print(stack.pop())
    print("After removed the element:", stack)

insertElement()
removeElement()