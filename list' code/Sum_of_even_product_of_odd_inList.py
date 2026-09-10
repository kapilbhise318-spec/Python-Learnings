num=[15,20,30,35]

even_sum=0
odd_prod=1

for i in num:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_prod *= i
        
print(even_sum)
print(odd_prod)
