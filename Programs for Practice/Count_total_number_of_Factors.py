i= int  (input("Enter a number: "))
count=0


for j in range(1,i+1):
    if i%j ==0:

        count +=1
       

print("Total number of factor's of given number is",count)
