n = int(input("Enter the number of rows"))

for i in range(0, n): # 0,1,2,3

    for j in range(0, i+1): #(i = 0, j = 0); (i = 1, j = 0,1); (i = 2, j = 0,1,2; (i = 3, j = 0,1,2,3)
        print("*", end = "")

    print("\n")