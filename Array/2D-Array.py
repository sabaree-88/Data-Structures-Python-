<<<<<<< HEAD
r_num=int(input("Enter the number of Rows: "))
c_num=int(input("Enter the number of Columns: "))

twoD_arr = [[0 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        twoD_arr[row][col] = row*col
=======
r_num=int(input("Enter the number of Rows: "))
c_num=int(input("Enter the number of Columns: "))

twoD_arr = [[0 for col in range(c_num)] for row in range(r_num)]

for row in range(r_num):
    for col in range(c_num):
        twoD_arr[row][col] = row*col
>>>>>>> b3862e7a6b713f893aaa97f3a2775b1681fbffd1
print(twoD_arr)