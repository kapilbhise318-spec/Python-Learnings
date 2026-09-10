i=int(input("Enter a number to findout wether a given number is palindrome or not: "))
x=i
rev=0

while(i>0):
    rev=(rev*10) + (i%10)
    i=i//10
if (x==rev):
    print("Given number is palindrom.")
else:
    print("Given number is not palindrome number:")