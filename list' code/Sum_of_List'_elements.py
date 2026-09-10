# a=[]
# list=int(input("Enter a number to create a list: "))
# for i in range(list):
#     value=int(input("Enter a list's elements: "))
#     a.append(value)
# sum=0

# for i in range(list):
#     sum=sum+a[i]
# print("The size of list is",list,"and","sum of its elements is: ",sum)



R=[]

list=int(input("Enter a number to create list: "))
for  i in range(list):
    addition=int(input("Enter the element of the list: "))
    R.append(addition)
sum=0
for i in range(list):
    sum=sum+R[i]
print("The sum of list elements is", sum)