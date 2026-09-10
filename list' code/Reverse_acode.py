





# Method 1 slicing.
# list=[10,20,30,40,50]
# print(list[::-1])



# method 2 using (.reverse()) function.
# list1=[1,2,3]
# l=(list1)
# l.reverse()
# print(l)


# method 3 using for loop...
# l=[3,2,1,6,5,4]
# rl=[]
# for i in range(len(l)-1,-1,-1):
#     rl.append(l[i])
# print(rl)


# for loop 2.example..
empty_list=[]
create_list=int(input("Enter a size of the list: "))
for i in range(create_list):
    Add_Elements=int(input("Enter number to add in the List: "))
    empty_list.append(Add_Elements)

i=0
j=create_list-1

while(i<j):
    t=empty_list[i]
    empty_list[i]=empty_list[j]
    empty_list[j]= t
    i=i+1
    j=j-1
for i in range(create_list):
    print(empty_list[i])