r_num=int(input("Enter the number of Rows: "))
c_num=int(input("Enter the number of Columns: "))

twoD_arr = [[0 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        twoD_arr[row][col] = row*col
print(twoD_arr)