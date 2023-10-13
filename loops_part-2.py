# Numba 2
sum=0
f=""

n=int(input("Enter a number: ")) 

for x in range(1, n+1):
    f=f+str(x)
    if x != n:
        f=f+"+"
    
print("Formula", f)

print("Sum:",n*(n+1)//2)