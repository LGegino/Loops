# Numba 1

rows = int(input("Number:"))

for x in range(1, rows + 1):
    for y in range(1, x + 1):
        print(y, end=' ')
    print('')
    