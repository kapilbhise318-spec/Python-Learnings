# ***USING FOR LOOP***

# string="nohtyP"

# reverse=" "

# for _ in string:
#     reverse=_+reverse
# print(reverse)





# *** USING SLICE OPERATOR ***


# string="nohtyP"
# print(string[::-1])



# 3)... USING REVERSE STRING



def reverse_string(s):
    if len(s)==0:
        return s
    else:
        return reverse_string(s[1:])+(s[0])
text=''
print(reverse_string(text))