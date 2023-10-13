# Numba 3

rows = 5
for x in range(1, rows + 1):
    for y in range(1, x + 1):
        print(y, end=' ')
    print('')
    
# Numba 2

n=int(input("Enter a number: ")) 
    #IDK HOW TO PRINT A LOOP WITH SOLUTION :(
print("Sum:",n*(n+1)//2)

#Numba 3
rows = 5

for x in range(rows+1, 0, -1):
    for y in range(0, x-1):
        print(y+1, end=' ')
    print(" ")
