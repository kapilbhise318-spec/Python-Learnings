# a=[30,10,20,30]

# # find frequency of 30
# b=30
# c=0
# for i in a:
#     if i == b:
#         c=c+1
# print(c)





# 2nd Method
# Create an empty list
a=[]

# size of list
size=int(input("Enter a number to fix size of the list..."))
for i in range(size):
    value=int(input("Enter elements: "))      # add elements which add in list a
    a.append(value)
    
   
number=int(input("Enter a number to its frequency: "))     #Search frequent number..
frequency=0
for i in range(size):
    if a[i]==number:       # compare the numbers
        frequency=frequency+1
print("Frequency of the given number is",frequency)