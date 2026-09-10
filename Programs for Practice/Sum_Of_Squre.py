i=int(input("Enter a number: "))

sum=0
while (i>0):
    digit = i%10
    sum=sum+ digit * digit
    i=i//10
print(sum)













a=int(input("Enter a number: "))
sum=0
product=1

while(a>0):
    d=a%10
    if d%2 == 0:
        sum=sum + d
    else:
        product=product * d
    a=a//10
print(sum)
print(product)