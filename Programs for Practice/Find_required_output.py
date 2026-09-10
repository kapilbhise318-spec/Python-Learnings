# input= "The sky is blue"
# output="blue is sky The"

s="The sky is blue"


l=s.split()

l=l[::-1]
l=' '.join(l)
print(l)