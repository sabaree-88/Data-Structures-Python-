stack=[]
def push():
    element=input("Enter the element:")
    stack.append(element)
    print(stack)

def pop_element():
    e=stack.pop()
    print("Poped element is:",e)
    print(stack)

while True:
    print("Enter the opertion: \n1.Push\n2.Pop\n3.Exit ")
    choices=int(input("Enter your choice:"))
    if choices==1:
        push()
    elif choices==2:
        pop_element()
    elif choices==3:
        break
    else:
        print("Enter the correct option:")