num=int(input('Enter a number to findout wether a number is prime or not: '))

if num <= 1:
    print(num, 'not prime number...')
else:
    for i in range(2, num):
        if num % i ==0:
            print(num,"Not prime number...")
            break

    else:
        print(num, 'Number is Prime...')