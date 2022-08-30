<<<<<<< HEAD
#create the array
print("Enter the size of an array: ")
total=int(input())
arr = []

print("Enter ",total, "ELements:")
for i in range(total):
    arr.append(input())
print(arr)

#Delete an element in array
def delete_item():
    print("Enter the element to delete: ")
    val = input()
    if val in arr:
        arr.remove(val)

        print("The new array:", end=" ")
        for i in range(total-1):
            print(arr[i],end=" ")
    else:
        print("SORRY! , Element is not in the array")
#delete_item()

def sort_array():
    print("Elements of original Array:")
    for i in range(total):
        print(arr[i],end=" ")

    #Sort Opreation
    for i in range(total):
        for j in range(i+1, total):
            if (arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("Elements of Sorted array(Ascending:)")
    for i in range(total):
        print(arr[i],end=" ")
#sort_array()

#Searching an element in an array
def search():
    print("Elements of array:")
    for i in range(0, total):
        print(arr[i],end=" ")
    print("\n")
    print("Enter the value to Search:",end=" ")

    print("\n It Returns the Index Position:",arr.index(input()))

#search()


=======
#create the array
print("Enter the size of an array: ")
total=int(input())
arr = []

print("Enter ",total, "ELements:")
for i in range(total):
    arr.append(input())
print(arr)

#Delete an element in array
def delete_item():
    print("Enter the element to delete: ")
    val = input()
    if val in arr:
        arr.remove(val)

        print("The new array:", end=" ")
        for i in range(total-1):
            print(arr[i],end=" ")
    else:
        print("SORRY! , Element is not in the array")
#delete_item()

def sort_array():
    print("Elements of original Array:")
    for i in range(total):
        print(arr[i],end=" ")

    #Sort Opreation
    for i in range(total):
        for j in range(i+1, total):
            if (arr[i]>arr[j]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("Elements of Sorted array(Ascending:)")
    for i in range(total):
        print(arr[i],end=" ")
#sort_array()

#Searching an element in an array
def search():
    print("Elements of array:")
    for i in range(0, total):
        print(arr[i],end=" ")
    print("\n")
    print("Enter the value to Search:",end=" ")

    print("\n It Returns the Index Position:",arr.index(input()))

#search()


>>>>>>> b3862e7a6b713f893aaa97f3a2775b1681fbffd1
