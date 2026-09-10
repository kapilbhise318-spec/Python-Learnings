# with open('data.txt','r') as file:
#     data=file.read()
#     print(data) 


# Without using with statement:

file=open('data.txt','r')
data=file.read()
print(data)
file.close()