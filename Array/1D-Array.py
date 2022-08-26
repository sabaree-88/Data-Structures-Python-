print("Enter the size of an Array:")
num = int(input())
arr = []

print("Enter ",num, "elements:",end=" ")

for i in range(num):
    element = input().split()
    arr.append(element)
print("Array elements are:",end=" ")
for i in range(num):
    print(arr[i],end="")
