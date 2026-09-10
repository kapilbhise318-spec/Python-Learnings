a=[]
list=int(input("Enter a number to create a list: "))
for i in range(list):
    value=int(input("Enter list' elements: "))
    a.append(value)

even=0
odd=0

for i in range(list):
    if(a[i]%2 ==0):
        even=even+1
    else:
        odd=odd+1
print("Even elements in the list =",even,"Odd elements in the list =",odd)