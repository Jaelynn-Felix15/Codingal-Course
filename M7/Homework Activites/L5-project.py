1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10
a = 1
b = 1
print(a)
print(b)
for i in range(18):
    temp = a
    a = b 
    b = temp + a
    print(b)