list=[121,21,98]
sum=0
 
for i in list:
    if i==2:
        raise Exception ('Exception 2 is found')
    else:
        sum= sum + i
print(sum)

# def test_code():
#     mylist = [12, 2, 98]
#     sum_val = 0
#     for i in mylist:
#         if i == 2:
#             raise Exception('Exception 2 is found')
#         else:
#             sum_val = sum_val + 1

# try:
#     test_code()
# except Exception as e:
#     print(f"Raised: {e}")
