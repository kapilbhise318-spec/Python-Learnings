list1=[1,2,3,4,2,5,6,8]
n=len(list1)
k=14

for i in range(n):
    for j in range(i+1, n):
        if list1[i] + list1[j]==k:
            print("Pair of number is :",list1[i],list1[j])