# Here's a simple Python program to calculate the HCF (Highest Common Factor)
#and LCM (Least Common Multiple) of two numbers.

# Method 1: Using a Loop (Beginner-Friendly)


# num1=int(input('Enter a first number: '))
# num2=int(input('Enter second number: '))

# # Find LCF
# small=min(num1, num2)

# for i in range(small, 0, -1):
#     if num1 % i ==0 and num2 % i == 0 :
#         hcf = i
#         break

# # Find LCM
# lcm = (num1 * num2) // hcf

# print('HCF=',hcf)
# print('LCM=',lcm)






# Calculate HCF of two numbers(separately)....


# num1=int(input('Enter first number: '))
# num2=int(input('Enter second number: '))

# small  = min(num1, num2)

# for i in range(small, 0, -1):
#     if num1 % i == 0 and num2 % i ==0:
#         hcf = i
#         break

# print('HCF=',hcf)



# Calculate LCM of two numbers(separately)....

# num1=int(input('Enter a  first number: '))
# num2=int(input('Enter a scend number: '))

# greater=max(num1, num2)

# while True:
#     if greater % num1 == 0 and greater % num2 == 0:
#         lcm=greater
#         break
#     greater = greater + 1

    
# print('LCM=',lcm)



# Euclidean Algorithm

# a=int(input('enter 1st number: '))
# b=int(input('enter 2nd number: '))

# while b!=0:
#     a,b=b, a%b
# print('GCD[HCF] =',a)


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD =", gcd(num1, num2))