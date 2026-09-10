# i=int(input("Enter a number: "))

# original_number=i

# sum=0
 
# while(i>0):

#     dd= i%10
#     sum=sum+ dd * dd * dd
#     i=i//10

# if original_number==sum:


#     print("Armstrong number.")
# else:
#     print("Not Armstron number...")





# Wether a 531 number is Armstrong number or not

i= int(input("Enter a number: "))

original_number = i

sum = 0

while (i>0):
     
    dd= i%10
    
    sum= sum + dd * dd * dd
    
    i=i//10

if original_number==sum:
    print ("Armstrong number")
else:
    print("Not an Armstrong Number..")