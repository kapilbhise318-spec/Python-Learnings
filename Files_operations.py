# Reading Entire File


# file=open('Server.py', 'r')
# content=file.read()
# print(content)
# file.close()


# Reading 1 line at a time 

# file=open('explore.txt','r')

# lines=file.readlines()
# print(lines)

# file.close()



# 3)  Writing to a file


# file=open('explore.txt','w')
# file.write("Hello My name is Aka")
# file.close()



# with open statement file 

with open('explore.txt','r') as file:
    content=file.read()
    print(content)
