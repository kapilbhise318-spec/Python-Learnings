# WAP to print prime numbers 1 to 100 ....


# num = int (input('Enter a number to check wether a given number is Prime or Not: '))

# if num <=1 :
#     print(num,'is not prime...')
# else:
#     for i in range(2, int(num ** 0.5)+1):
#         if num % i == 0 :
#             print(num, 'is not prime... ')
#             break
#     else:
#         print(num, 'Is prime number...')


# print all prime numbers a 1 to 100


print('The Prime numbers from 1 to 100: ') 
for num in range(1,101):
    for i in range(2, int(num ** 0.5)+1):
        if num % i ==0:
            break
           
    else:
        print(num, end=" ")