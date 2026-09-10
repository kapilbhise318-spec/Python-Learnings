# l=[12,45,1,2,4,78]

# n=len(l)

# for i in range(n):
#     for j in range(i+1,n):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)





# Sort  list without using sort()

# list=[9,8,7,6,5,4,3,2,1]
# n=len(list)

# for i in range(n):
#     for j in range(i+1,n):
#         if list[i]>list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)


l1=[789,358,143]
m=len(l1)
for i in range(m):
    for j in range(i+1,m):
        if l1[i]>l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)