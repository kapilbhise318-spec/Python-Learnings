# using listComprehensive/

# easy=[x ** 3 for x in  range(10) if x % 2==0]
# print(easy)


# Using Simple List method


list=[]
for x in range (10):
    if  x%2==0:
        list.append(x**3)

print(list)