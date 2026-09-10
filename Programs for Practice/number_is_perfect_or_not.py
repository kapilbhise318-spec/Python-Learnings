# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).

# Example:

# 6 → Divisors: 1, 2, 3
# Sum = 1 + 2 + 3 = 6
# Therefore, 6 is a perfect number.





num=int(input('Enter a number to check wether entered number is Perfect or Not! '))

sum=0

for i in range(1,num):
    if num % i == 0:
        sum += i
if num == sum :
    print(num," is a Perfect Number...")
else:
    print(num," is a not Perfect Number...")