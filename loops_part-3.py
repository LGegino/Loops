#Numba 3
rows = int(input("Number:"))

for x in range(rows+1, 0, -1):
    for y in range(0, x-1):
        print(y+1, end=' ')
    print(" ")
