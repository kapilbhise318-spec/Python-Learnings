# for i in range(5):
#     for j in range(2,4):
#         print(j)



# i=1
# while i<4:
#     for j in range(1,4):
#         print(j)
#     i+=1



# Interview qUESTION:...



for num in range(2,10):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
 