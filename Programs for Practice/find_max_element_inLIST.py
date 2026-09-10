#  find max and min element in the list 



list=[1,10,20,30,40,50,589,99]

max=list[0]
min=list[0]

for i in list:
    if i > max:
        max = i
    
    if i < min:
        min = i

print(max)
print(min)