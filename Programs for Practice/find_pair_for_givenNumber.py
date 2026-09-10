list1=[1,2,3,1,4,5,6,444,777,888,999,1001]


n=len(list1)
k=1778

for i in range(n):
    for j in range(i+1, n):

        if (list1[i]+list1[j])==k:
            print(list1[i],",",list1[j])