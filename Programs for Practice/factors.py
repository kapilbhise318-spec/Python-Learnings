n=int (input('Enter a number to calculate factors of a numbers: '))

for i in range(1, n+1):
    if n % i ==0:
        print(i, end=" ")
    