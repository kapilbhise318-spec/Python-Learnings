# using for loop 

a=[1,2,3,4,5]
p=3
k=100
a.append(0)
for i in range(len(a)-2, p-2, -1):
    a[i+1]=a[i]
a[p-1]=k
print(a)





# using insert method
k=[5,5,5,5,5,5]
k.insert(2,100)
print(k)